# KG Construction

Pipeline per costruire un **Knowledge Graph (KG)** a partire da manuali tecnici PDF, con un approccio ad agenti.

## Obiettivo Del Progetto

Convertire manuali tecnici non strutturati in una rappresentazione strutturata (triplette/relazioni) utile per:
- troubleshooting guidato
- analisi difetti e cause ricorrenti
- integrazione futura con NetworkX/Neo4j

La pipeline è progettata in fasi:
1. Router Agent: isola le pagine utili dal PDF completo
2. Extractor Agent: estrae entità/relazioni dal contenuto tagliato
3. Resolver Agent: normalizza e deduplica le entità
4. KG Builder: converte il risultato in formato grafo

## Stato Attuale (Implementato)

Attualmente è implementata la **Fase 1 - Router Agent** in `agents/router_agent.py`.

### Cosa Fa Oggi Il Router Agent

La funzione principale è `process_pdf(filename: str, page_offset: int = PAGE_OFFSET)`.

Flusso implementato:
1. Carica variabili ambiente con `python-dotenv`
2. Legge il PDF da `sourceRaw/<filename>`
3. Estrae testo dalle prime 15 pagine (TOC/index)
4. Chiama LLM (`ChatOpenAI`) con prompt di sistema dedicato
5. Usa output strutturato Pydantic (`with_structured_output`) con:
   - `RelevantSection`
   - `TOCAnalysis`
6. Applica conversione pagine stampate -> indici PDF reali usando:
   - `absolute = printed_page + PAGE_OFFSET - 1`
7. Crea un PDF preview in memoria (`fitz.open()` + `insert_pdf`)
8. Salva anteprima in `temp_preview.pdf`
9. Apre automaticamente il PDF nel viewer di sistema:
   - macOS: `open`
   - Windows: `os.startfile`
   - Linux: `xdg-open`
10. Chiede conferma CLI:
   - `y`: salva in `sourceOptimized/<nome>_optimized.pdf`
   - `n`: elimina `temp_preview.pdf`
11. Esegue cleanup con chiusura documenti

### Note Funzionali Importanti

- Supporta sezioni **non consecutive**: se sono rilevanti capitolo 2 e capitolo 6, li unisce nello stesso PDF preview/finale.
- Se i range restituiti dall’LLM si sovrappongono, possono comparire pagine duplicate.
- L’ordine delle sezioni nel PDF ottimizzato segue l’ordine restituito dall’LLM.

## Struttura Codebase Attuale

```text
.
├── agents/
│   ├── extractor_agent.py
│   ├── resolver_agent.py
│   └── router_agent.py
├── tools/
│   ├── kg_builder.py
│   └── pdf_parser.py
├── sourceRaw/
│   └── userManualBamboLab.pdf
├── sourceOptimized/
│   └── userManualBamboLab_optimized.pdf
├── output/
│   └── userManualBamboLab.md
├── state.py
├── workflow.py
├── main.py
├── requirements.txt
└── .env
```

## Requisiti Tecnici

Dipendenze in `requirements.txt`:
- `openai`
- `python-dotenv`
- `markitdown[pdf]`
- `PyMuPDF`
- `langchain-openai`
- `langchain-core`
- `pydantic`

## Setup

1. Crea/attiva virtual environment (consigliato)
2. Installa dipendenze:

```bash
python3 -m pip install -r requirements.txt
```

3. Inserisci API key in `.env`:

```env
OPENAI_API_KEY=your_key_here
```

## Come Testare Agente 1

Assicurati che il PDF sia in `sourceRaw/`.

Esegui:

```bash
python3 -c "from agents.router_agent import process_pdf; process_pdf('userManualBamboLab.pdf')"
```

Durante il test:
1. Lo script genera `temp_preview.pdf`
2. Si apre il viewer PDF di sistema
3. Confermi con `y` oppure annulli con `n`

Output atteso con `y`:
- `sourceOptimized/userManualBamboLab_optimized.pdf`

## Configurazioni Chiave

In `agents/router_agent.py`:
- `TOC_PAGES_TO_READ = 15`: quante pagine iniziali analizzare per TOC
- `PAGE_OFFSET = 0`: offset manuale tra numerazione stampata e indice PDF reale
- `MODEL_NAME = "gpt-4o-mini"`: modello LLM usato

## Limiti Attuali

- Router dipende dalla qualità del TOC e dal testo estraibile (PDF scansiti senza OCR sono critici).
- `main.py`, `workflow.py`, `state.py`, `tools/*`, `extractor_agent.py`, `resolver_agent.py` sono ancora skeleton/minimali.
- Non c’è ancora deduplica automatica dei range pagina.
- Non c’è ancora una pipeline end-to-end completa fino al KG finale.

## Roadmap Prossime Fasi

1. Implementare Extractor Agent (triplette sintomo-problema-procedura)
2. Implementare Resolver Agent (normalizzazione, merge sinonimi, deduplica)
3. Implementare `tools/kg_builder.py` verso NetworkX/Neo4j
4. Collegare tutto in `workflow.py` e aggiungere entrypoint operativo in `main.py`
5. Aggiungere test automatici su PDF campione
