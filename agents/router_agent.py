"""Agent 0 (Router): identify and crop troubleshooting sections from raw PDFs."""

from __future__ import annotations

import os
import platform
import subprocess
import sys
from pathlib import Path

import fitz
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

try:
    from state import WorkflowState
except ModuleNotFoundError:
    sys.path.append(str(Path(__file__).resolve().parents[1]))
    from state import WorkflowState

SOURCE_RAW_DIR = Path("sourceRaw")
SOURCE_OPTIMIZED_DIR = Path("sourceOptimized")
TEMP_PREVIEW_FILE = Path("temp_preview.pdf")
TOC_PAGES_TO_READ = 15
PAGE_OFFSET = 0
MODEL_NAME = "gpt-4o-mini"

SYSTEM_PROMPT = (
    "You are an expert analyst in industrial technical documentation. "
    "Your task is to analyze text extracted from the first pages "
    "(Table of Contents/Index) of a technical manual and identify ONLY "
    "the chapters or sections dedicated to: troubleshooting, problem "
    "resolution, error codes, quality defects, and corrective maintenance.\n"
    "MANDATORY RULES:\n"
    "1. Extract the exact title of each relevant section.\n"
    "2. Identify the 'start_page' (the page where the section starts as shown in the TOC).\n"
    "3. Calculate the 'end_page' by looking at the next chapter start page in the TOC and subtracting 1. "
    "If it is the last chapter in the manual, estimate a logical length (e.g., start_page + 20).\n"
    "4. Ignore introductions, unboxing, installation, warranty, or technical specifications.\n\n"
    "Return data strictly adhering to the required JSON schema."
)


class RelevantSection(BaseModel):
    title: str = Field(
        description="The exact chapter or section title identified as relevant"
    )
    start_page: int = Field(
        description="The printed page number where the relevant section starts"
    )
    end_page: int = Field(
        description="The printed page number where the relevant section ends"
    )


class TOCAnalysis(BaseModel):
    sections: list[RelevantSection] = Field(
        description="List of relevant sections found in the table of contents"
    )


def _extract_toc_text(doc: fitz.Document) -> str:
    max_pages = min(TOC_PAGES_TO_READ, len(doc))
    chunks: list[str] = []
    for page_index in range(max_pages):
        page_text = doc[page_index].get_text("text")
        chunks.append(f"=== PDF page index {page_index} ===\n{page_text}")
    return "\n\n".join(chunks)


def _analyze_toc_with_llm(toc_text: str, model_name: str) -> TOCAnalysis:
    llm = ChatOpenAI(model=model_name, temperature=0)
    structured_llm = llm.with_structured_output(TOCAnalysis)
    return structured_llm.invoke(
        [
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(content=toc_text),
        ]
    )


def _clamp_page_index(page_index: int, total_pages: int) -> int:
    return max(0, min(page_index, total_pages - 1))


def _open_in_default_viewer(pdf_path: Path) -> None:
    system = platform.system()
    if system == "Darwin":
        subprocess.run(["open", str(pdf_path)], check=False)
    elif system == "Windows":
        os.startfile(str(pdf_path))  # type: ignore[attr-defined]
    else:
        subprocess.run(["xdg-open", str(pdf_path)], check=False)


def process_pdf(filename: str, page_offset: int = PAGE_OFFSET) -> Path | None:
    """Process one PDF from sourceRaw and optionally save optimized preview."""

    load_dotenv()
    SOURCE_RAW_DIR.mkdir(parents=True, exist_ok=True)
    input_pdf_path = SOURCE_RAW_DIR / filename

    if not input_pdf_path.exists():
        raise FileNotFoundError(f"Missing input PDF: {input_pdf_path}")

    doc = fitz.open(input_pdf_path)
    preview_doc = fitz.open()

    try:
        toc_text = _extract_toc_text(doc)
        analysis = _analyze_toc_with_llm(toc_text, model_name=MODEL_NAME)

        if not analysis.sections:
            print("Nessuna sezione rilevante trovata nell'indice.")
            return None

        print("\nSezioni rilevanti trovate:")
        selected_indices: list[int] = []
        for section in analysis.sections:
            absolute_start = section.start_page + page_offset - 1
            absolute_end = section.end_page + page_offset - 1
            absolute_start = _clamp_page_index(absolute_start, len(doc))
            absolute_end = _clamp_page_index(absolute_end, len(doc))
            if absolute_end < absolute_start:
                absolute_end = absolute_start

            print(
                f"- {section.title}: printed {section.start_page}-{section.end_page} | "
                f"pdf_index {absolute_start}-{absolute_end}"
            )
            preview_doc.insert_pdf(doc, from_page=absolute_start, to_page=absolute_end)
            selected_indices.extend(range(absolute_start, absolute_end + 1))

        preview_doc.save(TEMP_PREVIEW_FILE)
        _open_in_default_viewer(TEMP_PREVIEW_FILE)

        confirm = input("\nConfermi il taglio? (y/n): ").strip().lower()
        if confirm != "y":
            if TEMP_PREVIEW_FILE.exists():
                TEMP_PREVIEW_FILE.unlink()
            print("Operazione annullata")
            return None

        SOURCE_OPTIMIZED_DIR.mkdir(parents=True, exist_ok=True)
        output_name = f"{Path(filename).stem}_optimized.pdf"
        optimized_path = SOURCE_OPTIMIZED_DIR / output_name
        TEMP_PREVIEW_FILE.replace(optimized_path)
        print(f"PDF ottimizzato salvato in: {optimized_path}")
        return optimized_path
    finally:
        preview_doc.close()
        doc.close()


def process_all_raw_pdfs(page_offset: int = PAGE_OFFSET) -> list[Path]:
    """Process all PDFs found in sourceRaw, one by one."""

    load_dotenv()
    SOURCE_RAW_DIR.mkdir(parents=True, exist_ok=True)
    pdf_files = sorted(SOURCE_RAW_DIR.glob("*.pdf"))

    if not pdf_files:
        print(f"Nessun PDF trovato in: {SOURCE_RAW_DIR}")
        return []

    print(f"Trovati {len(pdf_files)} PDF in {SOURCE_RAW_DIR}.")
    optimized_outputs: list[Path] = []
    for index, pdf_path in enumerate(pdf_files, start=1):
        print(f"\n[{index}/{len(pdf_files)}] Processing: {pdf_path.name}")
        try:
            optimized_path = process_pdf(pdf_path.name, page_offset=page_offset)
            if optimized_path is not None:
                optimized_outputs.append(optimized_path)
        except Exception as exc:
            print(f"Errore durante il processing di {pdf_path.name}: {exc}")

    print(
        f"\nCompletato. PDF approvati e salvati: {len(optimized_outputs)}/{len(pdf_files)}"
    )
    return optimized_outputs


def router_agent(state: WorkflowState) -> WorkflowState:
    """Compatibility node: run PDF routing when source_pdf is provided in state."""

    if not state.source_pdf:
        return state

    optimized_path = process_pdf(state.source_pdf, page_offset=PAGE_OFFSET)
    if optimized_path is None:
        state.selected_pages = []
    return state


if __name__ == "__main__":
    process_all_raw_pdfs()
