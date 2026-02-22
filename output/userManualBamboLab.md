Bambu Lab H2C

3D Printing User Manual

V1.0  2026.01

Bambu Lab H2C 3D Printing User Manual

Copyright Notice

This manual and its contents are intended solely to guide users in operating and using this prod-

uct. The intellectual property rights are owned by Shenzhen Tuozhu Technology Co., Ltd. (here-

inafter referred to as "Bambu Lab"). Without the written authorization of Bambu Lab, no pa of

this manual may be reproduced, distributed, modified, or provided to any third party in any form.

Manual Scope Description

This manual focuses primarily on the and H2C 3D printers. Some accessories or features men-

tioned in certain chapters are optional or upgrade items and may not be included in your prod-

uct package. Please select the appropriate content for learning and operation according to your

product model and configuration.

Version and Update

After rmware upgrades, information related to new features will be displayed on the printer's

touchscreen. You can click the link below or visit the Bambu Lab Wiki page, then select or H2

Series > H2C > Printer Features > H2C Firmware Release History to view detailed information.

If there is any discrepancy between this manual and the rmware release history, the rmware re-

lease history shall prevail.

wiki.bambulab.com/h2c/manual/h2c-rmware-release-history

Image and Parameter

Images shown in this manual are for illustrative reference only. The actual display and features

may va depending on the software or rmware version.

1

Bambu Lab H2C 3D Printing User Manual

Thank you for choosing the Bambu Lab H2C 3D Printer!

This manual provides you with comprehensive information for using 3D printing functions, includ-

ing device setup, operation, and routine maintenance. To ensure safe, correct, and efficient use of

this product, please carefully read and fully understand this manual before use.

Use Guide

 Use the table of contents for quick navigation.

 Search for keywords in this PDF.

 Visit Bambu Lab Wiki (wiki.bambulab.com/h2) to search for keywords and access detailed

steps and videos.

Quick Sta Guide

1. Read the instructions in Read before Use.

2. Sta your rst print.

3. Get 3D model resources.

4. Adjust slicing parameters.

5. Check print quality issues and solutions, as well as other common problems and fixes.

Additional Resources

• Unboxing and Installation: View the unboxing guide (wiki.bambulab.com/general/unbox-

ing-guide) for instructions on unpacking and setting up the printer.

• Customized Courses: Visit the Bambu Lab Academy (bambulab.com/support/academy) to learn

systematic courses on the printer and software.

Feedback Survey

If you have any questions or suggestions regarding this user manual, please click the following

link or scan the QR code to provide feedback.

bambulab.com/support/documentation/feedback

2

Bambu Lab H2C 3D Printing User Manual

Symbol Guide

NOTE

Supplementary explanations for the main content.

TIPS

Suggestions to optimize operations, improve efficiency, or enhance portability, helping you

use the printer more effectively.

CAUTION

Operations that may affect print quality or device performance. Please operate carefully to

avoid potential issues.

DANGER

Potential risks present. Ignoring this may cause equipment damage or personal injury. Please

always follow the relevant guidelines.

Technical Support

If you encounter problems during use, it is recommended to rst consult this manual. You can al-

so visit Bambu Lab Wiki to obtain detailed troubleshooting solutions by searching with keywords,

or consult Bambu Al (support.bambulab.com) for maintenance tips, diagnostic methods, and solu-

tions.

If your issue is not addressed or the troubleshooting steps do not resolve it, submit a service tick-

et or contact online technical support via the Service & Support website (bambulab.com/support)

to get professional assistance.

3

Bambu Lab H2C 3D Printing User Manual

Table of Contents

Read  before  Use.............................................................................................................. 10

Chapter 1 Introduction...................................................................................................12

1.1  Product  Introduction.................................................................................................................................12

1.2  H2C..................................................................................................................................................................13

1.2.1  3D  Printer........................................................................................................................................13

1.2.2  Toolhead..........................................................................................................................................16

1.2.3 Induction Hotend Rack.............................................................................................................. 18

1.2.4 Printer Touchscreen.................................................................................................................... 19

1.3  AMS  2  Pro.....................................................................................................................................................22

1.4 Printer and AMS Status........................................................................................................................... 23

1.4.1 Printer Status Indicator..............................................................................................................23

1.4.2 Induction Hotend Status Light................................................................................................24

1.4.3  Hotend  Indicator.......................................................................................................................... 24

1.4.4 AMS 2 Pro Status Indicator......................................................................................................25

1.4.5  HMS  Messages..............................................................................................................................26

Chapter  2  First  Print.......................................................................................................28

2.1  Preparation................................................................................................................................................... 28

2.1.1  Printer  Placement.........................................................................................................................28

2.1.2  Initial  Installation.......................................................................................................................... 28

2.1.3  Initial  Calibration.......................................................................................................................... 30

2.2 Induction Hotend Setup.......................................................................................................................... 31

2.3 Install Induction Hotend.......................................................................................................................... 31

2.4  Load  Filament..............................................................................................................................................31

2.4.1  AMS  2  Pro.......................................................................................................................................32

2.4.2 External Spool Holder................................................................................................................ 32

2.5 Initiate a Print from Printer Touchscreen.......................................................................................... 33

2.6 Remove the Model after Printing.........................................................................................................34

2.7  Unload  Filament..........................................................................................................................................35

4

Bambu Lab H2C 3D Printing User Manual

2.7.1  AMS  2  Pro.......................................................................................................................................35

2.7.2 External Spool Holder................................................................................................................ 35

2.8  Waste  Disposal............................................................................................................................................ 35

2.9 Connect Multiple AMS units...................................................................................................................36

2.9.1 Placement Recommendations................................................................................................. 36

2.9.2  Connection  Steps......................................................................................................................... 38

Chapter 3 Access 3D Model Resources.......................................................................40

3.1 MakerWorld Model Community............................................................................................................ 40

3.2 MakerLab Creative Tools......................................................................................................................... 41

Chapter 4 Initiate a Print from Bambu Handy.......................................................... 43

4.1 Install and Bind Bambu Handy............................................................................................................. 43

4.2  Initiate  a  Print..............................................................................................................................................44

Chapter 5 Initiate a Print from Bambu Studio.......................................................... 48

5.1 Install and Bind Bambu Studio............................................................................................................. 48

5.2 Introduction to Bambu Studio Interface............................................................................................50

5.3 Download and Import Model.................................................................................................................54

5.3.1 MakerWorld Models.................................................................................................................... 54

5.3.2  Other  Models.................................................................................................................................54

5.4  Initiate  a  Print..............................................................................................................................................56

5.5 Adjust Slicing Parameters....................................................................................................................... 57

5.5.1  Model  Size...................................................................................................................................... 57

5.5.2  Quality  Settings............................................................................................................................ 58

5.5.3  Strength  Settings......................................................................................................................... 62

5.5.4  Support  Settings.......................................................................................................................... 67

5.5.5  Speed  Settings..............................................................................................................................74

Chapter 6 Key Features Introduction......................................................................... 77

6.1 Voek Hotend Change System.............................................................................................................77

6.1.1  Workflow......................................................................................................................................... 77

6.1.2 Nozzle and Filament Mapping................................................................................................ 78

6.1.3 Multi-Material Printing with Hard Filament........................................................................79

5

Bambu Lab H2C 3D Printing User Manual

6.1.4 Induction Hotend Rack Setup................................................................................................. 81

6.2 Dual Hotends Printing..............................................................................................................................82

6.2.1 Select Filament Grouping Mode............................................................................................. 82

6.2.2 Slicing Mode Selection...............................................................................................................86

6.2.3 Multi-Material Printing with Soft and Hard Filament......................................................87

6.3 Large Volume Printing..............................................................................................................................89

6.3.1 Horizontal Printing Area............................................................................................................ 90

6.3.2 Vertical Printing Area................................................................................................................. 91

6.3.3 Check the Model Placement Area..........................................................................................91

6.4 High Precision Printing Mode................................................................................................................92

6.4.1  Sta  Calibration........................................................................................................................... 92

6.4.2  Print  Calibration............................................................................................................................95

6.4.3 High-Precision Nozzle Offset Calibration............................................................................96

6.4.4 Motion Accuracy Calibration....................................................................................................98

6.5  Intelligent  Detection..................................................................................................................................99

6.5.1 AI Print Monitoring......................................................................................................................99

6.5.2 Build Plate Detection............................................................................................................... 100

6.5.3 Hotend Type Detection........................................................................................................... 100

6.5.4 Live View Camera Calibration...............................................................................................101

6.6 Air Condition System..............................................................................................................................101

6.6.1  Select  Mode.................................................................................................................................101

6.6.2 Custom Chamber Temperature............................................................................................ 102

Chapter 7 Basic Controls and Functions.................................................................. 103

7.1 Control from Printer Touchscreen..................................................................................................... 103

7.1.1  Speed  Settings........................................................................................................................... 103

7.1.2 XYZ Axis Movement................................................................................................................. 104

7.1.3 Nozzle and Extruder.................................................................................................................104

7.1.4 Hotend and Rack.......................................................................................................................105

7.1.5 Heatbed and Chamber Temperature................................................................................. 107

7.1.6 Chamber Light Mode............................................................................................................... 107

6

Bambu Lab H2C 3D Printing User Manual

7.1.7  Status  Indicator.......................................................................................................................... 108

7.1.8 Low Power Mode.......................................................................................................................108

7.1.9  Sound............................................................................................................................................. 109

7.2  Photo  and  Video...................................................................................................................................... 109

7.2.1  Video  Recording........................................................................................................................ 110

7.2.2  Photo..............................................................................................................................................110

7.2.3  Timelapse......................................................................................................................................111

7.3  Connect  to  Network............................................................................................................................... 112

7.3.1  LAN  Only  Mode..........................................................................................................................112

7.3.2  Developer  Mode.........................................................................................................................113

7.4 Connect USB Flash Drive......................................................................................................................114

7.4.1  Specification................................................................................................................................ 114

7.4.2 Connect and Format................................................................................................................ 114

7.4.3  Ejection..........................................................................................................................................115

7.5  Update  and  Restore............................................................................................................................... 115

7.5.1  Update  Firmware....................................................................................................................... 115

7.5.2  Initialization..................................................................................................................................116

Chapter  8  Filament....................................................................................................... 117

8.1 Select the appropriate filament..........................................................................................................117

8.1.1 Filament Types by Function...................................................................................................117

8.1.2 Filament Types by Temperature...........................................................................................119

8.2 Filament Compatibility and Parameter Settings........................................................................... 120

8.3  Filament  Drying........................................................................................................................................ 122

8.3.1 Filament Drying with the Printer......................................................................................... 122

8.3.2 Filament Drying with AMS 2 Pro/AMS HT........................................................................ 123

8.4  TPU  Printing  Guide..................................................................................................................................124

8.4.1  TPU  85A........................................................................................................................................ 125

8.4.2  TPU  90A........................................................................................................................................ 127

8.5 High-Temperature Filament Printing Guide...................................................................................129

Chapter 9 Print Quality Issues and Solutions..........................................................131

7

Bambu Lab H2C 3D Printing User Manual

9.1 First Layer Not Sticking.........................................................................................................................131

9.2 First Layer Too High/Too Low.............................................................................................................132

9.3 Poor Overhang Quality.......................................................................................................................... 132

9.4 Model Warping, Falling O, or Collapse..........................................................................................133

9.5 Filament Sticking to the Nozzle......................................................................................................... 134

9.6  Under-Extrusion....................................................................................................................................... 135

9.7 Stringing and Oozing............................................................................................................................. 136

9.8  Gloss  Difference....................................................................................................................................... 137

9.9  Interlayer  Cracking.................................................................................................................................. 138

9.10  Seam...........................................................................................................................................................139

9.11  Belt  Pattern............................................................................................................................................. 139

9.12  Top  Layer  Gaps...................................................................................................................................... 140

Chapter 10 Other Common Issues and Solutions................................................... 142

10.1 Printable Area Error..............................................................................................................................142

10.2 Nozzle Offset Calibration Failure.....................................................................................................142

10.3 Motion Accuracy Calibration Failure.............................................................................................. 143

10.4 Clogging Troubleshooting..................................................................................................................144

10.5 Nozzle/Hotend Unclogging Guide.................................................................................................. 148

10.5.1 Manual Extrusion.....................................................................................................................149

10.5.2 Unclogging Pin Cleaning...................................................................................................... 149

10.5.3  Cold  Pull..................................................................................................................................... 150

10.5.4 Hot Allen Key Cleaning (Left Hotend).............................................................................151

10.5.5 Hot Allen Key Cleaning (Right Hotend/Induction Hotend)...................................... 153

Chapter 11 Regular Maintenance.............................................................................. 156

11.1 Maintenance Frequency and Operation Requirements........................................................... 156

11.2  Print  Calibration..................................................................................................................................... 158

11.3 Clean the exterior and interior surfaces....................................................................................... 158

11.3.1  Printer  Exterior.........................................................................................................................158

11.3.2  Printer  Interior..........................................................................................................................158

11.4 Clean the Chamber Exhaust Grille and Fan................................................................................. 160

8

Bambu Lab H2C 3D Printing User Manual

11.5  Clean  the  Air  Filter................................................................................................................................161

11.6 Clean and Lubricate the XYZ Axes................................................................................................. 162

11.6.1 X-Axis Linear Rails.................................................................................................................. 162

11.6.2 Y-Axis Linear Rods................................................................................................................. 163

11.6.3 Z-Axis Linear Rods and Lead Screws...............................................................................163

11.7 Clean and Lubricate the Induction Hotend Rack.......................................................................164

11.8  Toolhead................................................................................................................................................... 165

11.8.1 Clean the Hotends..................................................................................................................165

11.8.2 Clean the Toolhead Surface................................................................................................166

11.8.3 Clean and Lubricate the Nozzle Lifting Assembly.......................................................166

11.9  Clean  the  Cameras................................................................................................................................167

11.10 Clean the Heatbed............................................................................................................................. 168

11.11 Clean the Build Plate.........................................................................................................................169

11.12 Replace Accessories...........................................................................................................................169

11.12.1  Hotend  -  Left.........................................................................................................................169

11.12.2 Hotend - Right (Induction Hotend)............................................................................... 170

11.12.3 Induction Hotend Silicone Sleeve................................................................................... 172

11.12.4 Induction Hotend Latch..................................................................................................... 173

11.12.5  Flow  Blocker........................................................................................................................... 174

11.12.6 Filament Cutter Blade......................................................................................................... 176

11.12.7  PTFE  Tube............................................................................................................................... 178

11.12.8 Nozzle Wiping Pad............................................................................................................... 180

11.12.9 4-in-1 PTFE Adapter II....................................................................................................... 181

11.12.10 Filament Cleaning Pad......................................................................................................182

9

Bambu Lab H2C 3D Printing User Manual

Read before Use

To ensure safe operation and optimal performance of the printer, carefully review the following

precautions before use:

Basic Safety and Electrical Requirements

• The actual operating voltage of the printer must match the voltage specified in the product

specifications to avoid equipment damage and safety hazards. You can check the label next to

the power socket for the specific voltage requirements.

• The printer is a high-temperature, high-speed device. Keep children and unauthorized person-

nel away to prevent burns, pinching, or other accidents.

• Do not touch the toolhead, heatbed, or moving pas during printing to prevent injuries.

Operation and Maintenance Recommendations

• To ensure proper functioning of the printer’s internal precision mechanisms, regular mainte-

nance is recommended (see Regular Maintenance).

• Use the right hotend to print specific types of TPU and the left hotend to print PPS/PPA-CF/

PET-CF. Other filament types have no restrictions (see Filament Compatibility and Parameter

Settings).

• The printer automatically switches between different hotends during printing. Do not manually

force switching to avoid damaging the device.

• For optimal print results, we recommend using official Bambu filaments. Bambu filaments have

undergone rigorous compatibility, safety, and stability testing based on the product’s charac-

teristics to ensure the best printing performance.

• Unless otherwise specified, always unplug the power cord before performing any operation,

maintenance, or modification to prevent electric shock or equipment damage.

• Unless otherwise specified, allow the printer to completely cool down before performing any

operation, maintenance, or modification.

Safety Instructions for AMS 2 Pro

• To prevent filament jams, do not load flexible materials such as TPU with a hardness of 95A

or lower, or moisture-absorbed PVA into the AMS 2 Pro.

• The AMS 2 Pro supports filament spool widths from 50 mm to 68 mm and diameters from 197

mm to 202 mm. Plastic spools are recommended.

10

Bambu Lab H2C 3D Printing User Manual

• Use a 6-pin cable to connect the H2 series 3D printer with a single AMS 2 Pro and enable the

AMS 2 Pro’s drying function. To d filament in multiple AMS 2 Pro units simultaneously, use the

official Bambu Lab power adapters to supply power to the additional AMS 2 Pro units.

• During filament drying, the AMS 2 Pro removes moisture from the interior through an external

circulation system. Ensure that the air inlet and outlet are not obstructed by other objects to

achieve optimal drying performance.

11

Bambu Lab H2C 3D Printing User Manual

Chapter 1 Introduction

Chapter 1 Introduction

1.1 Product Introduction

The H2C is an intelligent 3D printer based on Fused Deposition Modeling (FDM) technology,

deeply optimized for multi-color and multi-material printing applications. The H2C features the

innovative Voek Hotend Change System, supporting up to six Voek Induction Hotends. By di-

rectly switching hotends, it achieves a nearly "no purging" color change process, preventing col-

or mixing and material waste caused by traditional purging. This greatly enhances the efficien-

cy, stability, and final quality of multi-color and multi-material printing. Together with the left ho-

tend, the printer can use up to seven different filaments in a single print without purging waste

filament. Changing hotends greatly reduces filament waste from purging. The H2C also offers the

following features to provide a smaer printing experience, making your creativity more efficient

and diverse.

•

•

Increases color changing efficiency while supporting larger build volume.

Intelligent Detection increases print success.

• The refined enclosed design combined with chamber temperature control, supports printing

with high-performance filaments.

Recommend using the Automatic Material System (AMS) for fully automated filament changing

and management to maximize the H2C’s advantages and enhance printing intelligence and con-

venience:

• AMS 2 Pro: Supports RFID filament sync, automatic multi-color/multi-material changing, and

sma drying. Enhances multi-material printing and filament management for a smaer, more

convenient, and improved 3D printing experience.

• AMS HT: Specialized for high-temperature filaments, the AMS HT supports RFID filament sync,

automatic multi-color/multi-material changing, and sma drying, meeting the demands of en-

gineering-grade and professional printing.

NOTE

The printer can use up to seven different filaments in a single print without waste purging.

This requires configuring six induction hotends and one left hotend of the same diameter,

along with the corresponding number of AMS units.

12

Bambu Lab H2C 3D Printing User Manual

Chapter 1 Introduction

NOTE

The “no purging” concept does not include the initial purge required when loading a brand-

new filament into a hotend.

NOTE

The 8-second heating time for the induction hotend is measured based on Induction Hotend

printing temperature.

1.2 H2C

1.2.1 3D Printer

1. Automatic Top Vent: The top vent and rear chamber exhaust open automatically to bring in

external cool air and expel internal hot air, balancing the chamber temperature.

2. USB Po: Inse a USB drive to sta print jobs offline and to store timelapse video les.

3. Touchscreen: Displays printing parameters and controls the printer.

4. Filament Buer & Filament Tangle Detector: Detects filaments loading status and adjusts

speed dynamically. Monitors whether the filament is tangled.

5. Toolhead: Consists of two PTFE tube connectors at the top, the extruder, and the dual-hotend

assembly.

6. Sta/Pause button: Controls the sta, resume and pausing of laser and cutting tasks.

13

Bambu Lab H2C 3D Printing User Manual

Chapter 1 Introduction

NOTE

To pause or sta 3D printing, operate via the screen or software.

7. Air Filter: Filters the chamber’s internal airflow to remove ne particles and reduce odors dur-

ing printing.

1. Top Glass Cover: Made of tempered glass, it allows you to easily monitor print progress and

provides good sealing and safety.

2. Live View Camera: Monitors print progress in real time, used for timelapse recording and AI

detections.

3. Heatbed: Heats the print surface to ensure stable adhesion of printed layers to the build

plate, preventing warping or detachment.

4. Auxiliary Pa Cooling Fan: A high-powered 12W cooling fan that provides additional airflow

for high-speed printing.

5. Side Glass - Right: Made of tempered glass, it allows you to easily monitor print progress and

provides good sealing and safety.

6.

Induction Hotend Rack: Stores and automatically changes induction hotends. Supports fully

automatic replacement of up to 6 induction hotends. Monitors hotend temperature, position,

and operating status in real time. Supports fast preheating and cooling of induction hotends

to improve printing efficiency.

7. Status Indicator: Indicates the printer’s operating status through color and blinking patterns.

(See Status Indicator Light Meanings for detailed definitions).

14

Bambu Lab H2C 3D Printing User Manual

Chapter 1 Introduction

1. TPU Filament Inlet: Used to manually load TPU filament that is not supported by the AMS.

2. Purge Chute: Installed at the rear of the printer to discharge purged or waste filament from

the printer.

3. Active Chamber Exhaust & Chamber Exhaust Fan: Expels air from the chamber to maintain

stable temperature. In cooling mode, fan speed increases as the chamber temperature rises.

4. Safety Key: The printer can only be powered on after inserting the safety key or engaging the

emergency stop button.

5. Power Socket: Connects the power cable and turns on the power.

6. Bambu Bus Po 6-pin: Connects to the AMS.

7. Chamber Filament Inlet (Hotend - Right): Upper filament inlet that connects to the right ex-

truder and uses the right hotends for printing.

8. Chamber Filament Inlet (Hotend - Left): Lower filament inlet that connects to the left ex-

truder and uses the left hotend for printing.

9. Belt Tensioner: Adjusts and monitors belt tension, and feeds data back to the system to en-

sure printing accuracy and motion stability.

10. Bambu Bus Po 4-pin: Connects to expansion accessories.

15

Bambu Lab H2C 3D Printing User Manual

Chapter 1 Introduction

1.2.2 Toolhead

1. Toolhead Filament Inlet - Left: Feeds filament into the extruder and the left hotend for heat-

ing and printing.

2. Hotend Indicator: Displays the status of the extrusion channel, the active wheel operation,

and whether the printer is operating or idle (see Hotend Indicator).

3. Toolhead Enhanced Cooling Fan: Reduces heat from the extruder and hotend heat sink.

Combined with sma temperature control, it lowers the risk of clogging and extrusion block-

ages.

4. Hotend - Left: Heats and melts the filament through contact heat conduction. Uses a quick-

locking clip structure to support fast installation and removal. Features lifting function with

coordinated ow blocker to enable automatic nozzle switching and prevent hotend oozing.

5. Toolhead Filament Inlet - Right: Feeds filament into the extruder and the right hotend for

heating and printing.

6. Filament Cutter Lever - Right: Drives the filament cutter blade to cut the filament in the right

hotend during the automatic filament unload process.

7.

Induction Hotend Latch: Used to secure the induction hotend onto the induction heating as-

sembly, ensuring a stable installation.

8. Hotend - Right: Ensures precise temperature control through a contactless solution to heat

and melt the filament. Records and transmits hotend data, including real-time temperature

and filament type.

9. Toolhead camera: Used for motion accuracy calibration, high-precision nozzle offset calibra-

tion, and build plate identification code recognition.

10. Induction Heating Assembly: Used for precise heating and temperature monitoring, support-

ing a maximum heating temperature of 350 °C. Heating the nozzle through non-contact in-

duction heating technology.

16

Bambu Lab H2C 3D Printing User Manual

Chapter 1 Introduction

11. Pa Cooling Fan: Directs cooling airflow through the air duct to the left and right nozzles,

providing efficient cooling during printing.

12. Pa Cooling Fan Duct: Directs cool airflow to the left and right hotends.

13. Nozzle Camera: Located behind the nozzle, used for detecting hotend clumping, air print,

spaghetti, and similar anomalies; also used for calibrating purge chute position.

14. Flow Blocker: A small black ap located beneath the nozzle that moves laterally with nozzle

switching. It covers inactive nozzles to prevent molten filament from dripping onto the model

or printing area.

15. Filament Cutter Lever - Left: Drives the filament cutter blade to cut the filament in the left

hotend during the automatic filament unload process.

NOTE

The left hotend comes with a built-in 0.4 mm hardened steel nozzle and is compatible with

high ow and tungsten carbide nozzle versions.

NOTE

The right hotend is equipped by default with a standard induction hotend, including 1 × 0.2

mm, 1 × 0.4 mm, and 1 × 0.6 mm induction hotends inside the accessory box, and is compati-

ble with high ow versions.

NOTE

For other hotend types, please purchase them separately.

17

Bambu Lab H2C 3D Printing User Manual

Chapter 1 Introduction

1.2.3 Induction Hotend Rack

1.

Induction Hotend Latch Actuator: Unlocks and locks the latch to enable fully automated

changing of the induction hotends.

2.

Induction Hotend: Ensures precise temperature control through a contactless solution to heat

and melt the filament. Records and transmits induction hotend data, including real-time tem-

perature and filament type. The induction hotends can be automatically placed by the hotend

rack on the right hotend for printing.

3.

Induction Hotend Dock Assembly: Holds the induction hotend in place and uses sensors to

detect if the Induction hotend is docked.

4.

Induction Hotend Status Light: Visually indicates the installation status of the induction ho-

tend in the docking assembly and the status of the induction hotend rack through blinking

status (see Induction Hotend Status Light).

5.

Induction Hotend Rack Belt Assembly: Transmits power from the rack motor to move the in-

duction hotend rack up and down, achieving precise lifting and lowering of the induction ho-

tends.

6.

Induction Hotend Rack Motor: Drives the induction hotend rack to lift and lower.

18

Bambu Lab H2C 3D Printing User Manual

Chapter 1 Introduction

1.2.4 Printer Touchscreen

Homepage

1. Screen menu bar, for switch screens.

2. Select internal models or USB stored models.

3. View and set Nozzle & Extruder parameters.

4. Quick access to the Filament screen.

5. Quickly configure network settings.

6. Quick access to the HMS screen.

Control Screen

1. Select the appropriate air condition based on the filament type.

2. Set printing speed mode.

3. Control the movement of the toolhead and the heatbed.

4. Control the extruders and the movements of the hotends & rack; also supports setting the pa-

rameters.

19

Bambu Lab H2C 3D Printing User Manual

Chapter 1 Introduction

5. Set the chamber temperature.

6. Set heatbed temperature.

7. Control LED light.

Filament Screen

1. Switch between AMS or external spool.

2. Tap any filament spool icon to edit filaments, load/unload filament, and re-read filament RFID.

3. View humidity and temperature inside the AMS; perform drying.

4. Tap the external spool icon to edit filament and load/unload filament.

5. Select auto refill and AMS setup functions.

6. View filament loading operation guide.

Settings Screen

1. Log in and view account.

2. Configure printer network.

20

Bambu Lab H2C 3D Printing User Manual

Chapter 1 Introduction

3. Configure USB storage.

4. View and update rmware.

5. Configure calibration functions.

6. Use toolbox to maintain the printer.

7. Other function settings.

HMS Page

When the printer requires maintenance or encounters a fault, related prompt messages will be

displayed here (see HMS messages).

21

Bambu Lab H2C 3D Printing User Manual

Chapter 1 Introduction

1.3 AMS 2 Pro

1. Filament Inlet: Inse the filament tip into this inlet. Once engaged, the system will automati-

cally feed the filament.

2. Desiccant: Keeps the internal AMS chamber environment d.

3. Air IntakeIntroduces external d air.

4. PTFE Tube Release Button: Press this button on the back of the AMS to release and remove

the PTFE tube.

5. Filament Outlet: Connects the AMS to the printer’s filament inlet po.

6. Bambu Bus Po 6-pin: Connects the AMS to the printer or another AMS via a Bambu bus ca-

ble 6-pin.

7. Power Connector: Plug the power adapter into this po to supply power for the drying func-

tion.

8. Active Support Shaft: Actively supports and drives the rotation of the filament spool.

9. Air Vent: Expels moisture from inside the AMS.

22

Bambu Lab H2C 3D Printing User Manual

Chapter 1 Introduction

1.4 Printer and AMS Status

1.4.1 Printer Status Indicator

Indicator Light Modes

Meaning

White light breathing slowly
(when the touchscreen is on)

The light turns o (when the
screen sleeps)

Orange light ows

The printer is idle and not executing any print jobs

The printer is idle and not executing any print jobs

The printer is preparing for a print job (such as uploading, filament
changing, leveling, or heating).

The white light stays on and
shows a progress bar

Printing in progress. The light synchronously displays print
progress for convenient viewing of printing status.

Red light double ash

A print error has occurred. The light flashes as a warning until the
user closes the error prompt

Green light stays on

Print completed. The light remains green until the user closes the
"Print Completed" prompt or opens/closes the printer's door, top
cover, or side panels.

23

Bambu Lab H2C 3D Printing User Manual

Chapter 1 Introduction

1.4.2 Induction Hotend Status Light

Indicator Light Modes

Meaning

steady

O

Breathing

Blinking

Hotend in place

Hotend not in place

The induction hotend rack is performing a changing action

Induction hotend rack changing error

1.4.3 Hotend Indicator

Indicator Light
Modes

Meaning

One LED on the left
stays on

One LED on the
right stays on

One LED on the left
is blinking

The extruder is using the left extrusion path

The extruder is using the right extrusion path

Left extrusion path is extruding

24

Bambu Lab H2C 3D Printing User Manual

Chapter 1 Introduction

Indicator Light
Modes

One LED on the
right is blinking

All LEDs o

Meaning

Right extrusion path is extruding

Sleep mode. After switching the extrusion path, the LEDs stay on for about
10 seconds, then automatically turn o and enter sleep mode.

LEDs ow sequen-
tially

Operating normally. Appears when the printer powers on, the fan is proper-
ly connected and installed, or when printing stas

1.4.4 AMS 2 Pro Status Indicator

The AMS indicator light shows the current status: white means normal operation; red means error

or fault.

Normal Status LED
Blink Patterns

Meaning

Four slots with white
lights flashing in se-
quence

Four slots breathing
white

AMS is powering on and setting up; after setup completes, the white
light turns solid

Normal drying status

Four slots with solid
white lights

Indicates that all four slots have filament inserted after setup completes.
Only slots with filament light up when waking up

Solid white light stays
on

This slot is performing preloading, reading, or printing operations (in-
cluding loading and unloading)

25

Bambu Lab H2C 3D Printing User Manual

Chapter 1 Introduction

Normal Status LED
Blink Patterns

White light o

Meaning

Case 1: No feeding, reading, or printing within 15 minutes after the
screen turns o

Case 2: 10 seconds after preloading or reading is finished

Case 3: No operation within 20 minutes after setup.

Error Status Blinking

Meaning

Patterns

Four slots flashing red

Printer cannot detect AMS; communication error

- double ash

Red light breathing

After printing stas, the filament inlet does not detect any filament; in-

sert filament to resume normal operation.

Red light solid

Filament may be broken inside the AMS internal hub

Red light single ash

Generally indicates feeding failure; please check whether the filament

inlet is functioning properly

Red light double ash Case 1: Abnormality occurred during drying process

Case 2: When idle, drying module NTC disconnects, or abnormal air duct

temperature is detected; check all connections are secure

1.4.5 HMS Messages

HMS (Health Management System) is the built-in fault diagnosis and status monitoring system for

Bambu Lab printers and AMS (Automatic Material System).

When a device experiences hardware failure, print failure, or needs maintenance, HMS will provide

on-screen or app notifications and offer recommended solutions.

If an HMS message appears, you can use one of the following methods to locate and address the

fault:

• Scan the QR code with your phone to directly access the diagnostic and troubleshooting page.

• Visit the Bambu Lab Wiki and search the HMS code to view detailed causes and troubleshoot-

ing steps for the fault.

26

Bambu Lab H2C 3D Printing User Manual

Chapter 1 Introduction

TIPS

The printer evaluates the pollution level based on the task type and duration, provides tar-

geted cleaning and maintenance reminders. This feature requires the rmware to be upgrad-

ed to the latest version. It is recommended to update the rmware before rst use to enable

cleaning reminders.

When an HMS ale appears, a notification icon

 will display at the bottom right of the Home-

page, and a message ale

 will appear on the left menu bar. Tap any notification icon to enter

the HMS page and view detailed information.

27

Bambu Lab H2C 3D Printing User Manual

Chapter 2 First Print

Chapter 2 First Print

Before starting the rst print, please ensure that the printer is correctly positioned, the initial set-

up and automatic calibration are completed.

This chapter will guide you step by step to ensure the printer stas the rst print in optimal con-

ditions.

2.1 Preparation

2.1.1 Printer Placement

To ensure print quality and the safe operation of the printer, please keep your workspace clean

and organized. Place the printer on a stable and sturdy surface.

CAUTION

The printer is equipped with anti-vibration feet to absorb minor vibrations during printing.

Ensure the surface is stable to prevent the printer from shifting or falling during operation.

CAUTION

Calibration should be performed after the printer is properly placed. Moving the printer after

calibration may affect print quality.

2.1.2 Initial Installation

Please follow the steps below to complete the initial installation of the printer:

1. Remove Packaging Materials

Follow the "Quick Sta Guide" to remove the outer box, foam, moisture-proof bag, and inter-

nal fasteners, ensuring that there is no packaging materials left on or inside the printer.

2.

Inspect the Printer Components

a. Confirm that all included accessories are present (accessory box, power cord, quick sta

guide, spool holder, PTFE tubes, etc.).

b. Ensure the printer's standard textured PEI plate is correctly installed on the heatbed.

3.

Install Filament Components

Ensure the external spool and AMS 2 Pro are installed correctly.

28

Bambu Lab H2C 3D Printing User Manual

Chapter 2 First Print

If not yet installed, follow the steps below to connect the external spool to the left hotend and

AMS 2 Pro to the right hotend.

Scan the QR code or click the link to watch the installation video and jump to the relevant sec-

tions as needed.

https://wiki.bambulab.com/h2c/manual/unboxing-h2c

TIPS

If connecting multiple AMS units, refer to Connecting Multiple AMS Units for instructions.

4. Check Power-On Status

• Ensure the power cord is properly connected.

• Confirm the power switch on the back of the printer is turned on and the indicator light is

lit.

• The safety key is inserted into the rear po of the printer.

29

Bambu Lab H2C 3D Printing User Manual

Chapter 2 First Print

•

If an emergency stop button is installed, ensure it is not pressed down (i.e., it is in the re-

leased position).

• The touchscreen should light up normally and display the initial setup interface.

2.1.3 Initial Calibration

Upon rst startup, the printer will automatically enter the setup process. Please follow the on-

screen instructions to complete the following steps:

1. Language, region, and network settings

Select the appropriate language and time zone; choose an available Wi-Fi network, or skip

network selection if not required.

2. Account login

Open Bambu Handy and scan the QR code displayed on the touchscreen to bind the printer

(see Install and Bind Bambu Handy). You may skip binding if not needed.

3. Automatic calibration

The printer will automatically perform a series of operations, including motor noise cancella-

tion, vibration compensation, automatic bed leveling, and nozzle offset calibration.

4. Remove the foam under the heatbed

After calibration, the heatbed will rise. Remove the remaining foam.

5. Calibration completes

The touchscreen will display "Calibration Completed!" indicating you can sta your rst print.

CAUTION

When installing the printer, do not touch the build plate surface with your hands to prevent

oils and sweat from contamination, which can reduce adhesion and cause bad print quality. If

you accidentally touch it, we recommend cleaning the build plate with hot water and deter-

gent to ensure optimal adhesion.

TIPS

Connect a USB ash drive to the printer's USB po. This allows you to import sliced les and

sta printing directly from the touchscreen, and save print videos, print history, and print

cache.

30

Bambu Lab H2C 3D Printing User Manual

Chapter 2 First Print

2.2 Induction Hotend Setup

Step 1. On the printer touchscreen, tap

 > Calibrate > Induction Hotend Rack Setup.

Step 2. Follow the instructions to ensure no induction hotend is installed on the hotend rack,

then tap Sta to begin the setup.

2.3 Install Induction Hotend

Step 1. Take the induction hotends out of the accessory box.

Step 2. On the touchscreen, tap

 > Nozzle & Extruder > Hotends & Rack > Row A to raise the

row A.

Step 3.

Install induction hotends on the raised row. Pinch the heat sink of the hotend, align the

two holes with the dock assembly, and install it magnetically. After installing an induction

hotend, the status light next to it will stay on, indicating proper installation.

Step 4. On the Hotends & Rack interface, tap Row B to raise it, and install the remaining induc-

tion hotends following the same steps.

Step 5. After all hotends are installed, tap Read All. The printer will automatically detect infor-

mation for all induction hotends.

DANGER

The toolhead will read the induction hotends one by one. Do not put your hands in-

side the printer at this time to avoid injury.

2.4 Load Filament

31

Bambu Lab H2C 3D Printing User Manual

Chapter 2 First Print

2.4.1 AMS 2 Pro

When the printer detects a new AMS 2 Pro connection, the touchscreen will prompt to perform

AMS Setup. This step determines which side of the extruder the AMS 2 Pro is connected to. There

are two AMS 2 Pro setup modes:

• Auto Mode: Load a spool of filament into the AMS 2 Pro, then tap Detect to sta the setup

process. The AMS 2 Pro will complete the setup automatically.

TIPS

Inse a roll of filament into each AMS 2 Pro. If filament is already loaded, please unload it

rst. Ensure that no filament remains in the filament buer to prevent it from breaking or

jamming.

• Manual Mode: If no filament is available for automatic setup, tap Manual Setup on the touch-

screen to configure the connected AMS 2 Pro to the left or right hotend.

TIPS

The upper filament inlet on the printer corresponds to the right hotend, and the lower fila-

ment inlet corresponds to the left hotend.

TIPS

Connect the AMS 2 Pro to the upper filament inlet to fully leverage the advantages of the

voek hotend change system in multi-color and multi-material printing.

Step 1. Place the required filament into the AMS 2 Pro slot, then gently push it into the filament

inlet. After placing filament, close the top cover and the locking tab.

Step 2. On the touchscreen, tap

 >

 > AMS Setup, then select a setup mode.

Step 3. On the touchscreen filament page, select a filament type and tap Load. You can also load

filament by selecting it in Bambu Studio's device interface.

2.4.2 External Spool Holder

Step 1. Confirm the filament type and color for subsequent setup. Then, place the spool on the

spool holder according to the filament's winding direction.

32

Bambu Lab H2C 3D Printing User Manual

Chapter 2 First Print

Step 2. On the touchscreen, tap

  > External Spool > Edit, select the filament type and color,

then tap Confirm.

Step 3.

Inse the filament into the PTFE tube and push it into the toolhead until it cannot move

forward. At this time, a small green dot will appear at the toolhead on the touchscreen,

indicating that filament has been detected.

Step 4. On the touchscreen, tap Load. Wait for the hotend to heat up. Manually push the fila-

ment again to keep it inside the extruder. Then follow the on-screen instructions to com-

plete the process.

2.5 Initiate a Print from Printer Touchscreen
The printer includes built-in model les that allow you to initiate your rst print directly from the
touchscreen.

CAUTION

These models and those stored on USB are pre-sliced les. Therefore, the relationship be-

tween filament and hotends cannot be changed. If the required filament is not found on the

interface, please adjust the location of the filament in the AMS or external spool holder, so

that the filament corresponds to the designated hotend.

Step 1. On the touchscreen, tap

  > Print Files and select the model you want to print.

TIPS

To adjust calibration items, tap Advanced to set manually; all calibration items de-

fault to automatic.

Step 2. Select the matching filament and tap Print.

33

Bambu Lab H2C 3D Printing User Manual

Chapter 2 First Print

TIPS

You can also sta printing from Bambu Handy or Bambu Studio. See Initiate a Print

from Bambu Handy or Initiate a Print from Bambu Studio.

2.6 Remove the Model after Printing

Step 1. After printing finishes, wait until the heatbed and model have cooled down to room tem-

perature. Then, gently remove the model from the build plate to prevent deformation or

damage to the model or build plate.

Step 2.

If the model is difficult to remove, gently bend the build plate or use a scraper to help

detach the model.

Step 3. Remove the prime tower (if present), then carefully use a scraper to clear the pre-ex-

trude line.

Step 4. Put back the build plate and make sure it aligns with the heatbed's stoppers.

CAUTION

Do not touch the surface of the build plate with your hands to prevent oils or sweat

contamination, which can reduce adhesion and cause bad print quality. If you acci-

dentally touch it, we recommend cleaning the build plate with hot water and deter-

gent to ensure optimal adhesion.

34

Bambu Lab H2C 3D Printing User Manual

Chapter 2 First Print

2.7 Unload Filament

2.7.1 AMS 2 Pro

After the print job completes, the filament will automatically retract into the AMS 2 Pro.

If the print job is canceled or interrupted, tap

  > filament in the AMS > Unload on the touch-

screen to retract the filament gripped by the extruder into the AMS 2 Pro.

2.7.2 External Spool Holder

Step 1. Tap

  > External Spool > Unload on the touchscreen.

Step 2. Follow the instructions to pull back the filament after it exits the toolhead and rotate the

spool at the same time.

Step 3. When the filament nears the pneumatic connector, catch the filament by hand and insert

it into the hole of the spool. Then tap Resume (problem solved).

2.8 Waste Disposal

Waste refers to the excess filament extruded to clear residual filament inside the nozzle at the be-

ginning or during multi-color, multi-material printing, to ensure print quality. This waste is dis-

charged through the purge chute located on the back of the printer.

We recommend following the steps below to collect and dispose of the waste:

• Use a container to catch the waste during printing. A larger container allows you to empty it

less frequently.

• Make sure waste can pass successfully through the purge chute and enter the container.

• Before printing, make sure there is no waste left inside the purge chute.

• Regularly clean the waste container to avoid blocking the purge chute.

• During multi-color printing, the AMS frequently changes filaments; the longer the print job, the

more waste is generated. Please empty the container periodically during printing if necessary.

• Avoid installing covers or pipes on the back of the printer that might block the purge chute to

prevent clogging or print failure.

• Dispose of waste in accordance with the regulations of your country or region.

35

Bambu Lab H2C 3D Printing User Manual

Chapter 2 First Print

2.9 Connect Multiple AMS units

To connect multiple AMS units, attach them to the right hotend. Switching between multiple in-

duction hotends reduces filament purging during material changes and improves printing effi-

ciency.

The H2C supports using up to 6 right hotends for multi-material printing.We recommend con-

necting 2 AMS units to the right hotend, 1 AMS to the left hotend for optimal multi-color print-

ing experience.

To connect multiple AMS units, refer to the image below and use the 4-in-1 PTFE adapter for con-

nection. Unlike old adapters, this 4-In-1 PTFE adapter includes a cleaning pad near the outlet. It

can prevent debris on filament from entering the toolhead to reduce the risk of clogging.

NOTE

The green line indicates the PTFE Tube, the red line indicates the 6-pin cable, and the gray

line indicates the power adapter.

NOTE

The rst-generation AMS is plug-and-play with the H2C and supports multi-color printing

but does not support the drying. Due to differences in the loading mechanism and buer

structure, the H2C is not compatible with AMS Lite.

2.9.1 Placement Recommendations

The following examples use 2 AMS units connected to the right hotend and 1 AMS unit connected

to the left hotend.

• Method 1: Place one AMS 2 Pro and one AMS HT on top of the printer, and place another AMS

2 Pro on the oor. This method requires about 900 × 1020 × 1100 mm³ of space.

36

Bambu Lab H2C 3D Printing User Manual

Chapter 2 First Print

CAUTION

To adapt to different placements, the included PTFE Tube is 900 mm. If you place the AMS

2 Pro or AMS HT on top of the printer, you can shorten the PTFE Tube as needed (mini-

mum 600 mm) to reduce material change time and improve printing speed.

• Method 2: Use a double-layer bracket to place two AMS 2 Pro units on the top of the printer

and the AMS HT on the oor. This method requires about 650 × 1020 × 1300 mm³ of space.

NOTE

You can search for a suitable bracket in MakerWorld, or prepare or custom-make brackets

based on your actual needs.

37

Bambu Lab H2C 3D Printing User Manual

Chapter 2 First Print

CAUTION

When placing the devices, ensure that there is enough space to open the AMS cover and

the printer's front door.

2.9.2 Connection Steps

Please ensure that the AMS units are placed as described by method 1 in the previous chapter.

Then, follow the steps below.

Connect the PTFE Tube

Connect the 6-pin cable

NOTE

The green line is a PTFE tube connecting to the upper coupler. The blue line is a PTFE tube

connecting to the lower coupler. The red line is a 6-pin cable.

Step 1. Connect the 4-in-1 PTFE adapter to the printer's upper coupler.

a) Take out the shortest PTFE tube (185 mm) from the accessory box.

b)

Inse it into the printer's upper coupler, and push it forward until it cannot move fur-

ther.

c)

Inse the other end of the PTFE Tube into the 4-in-1 PTFE adapter.

Step 2. Connect the 4-in-1 PTFE adapter to the AMS 2 Pro.

a) Use the long PTFE Tube (900 mm) that comes with the AMS 2 Pro to connect the 4-

in-1 PTFE adapter to the AMS 2 Pro's filament outlet on the printer.

38

Bambu Lab H2C 3D Printing User Manual

Chapter 2 First Print

b) Use another long PTFE Tube to connect the 4-in-1 PTFE adapter to the AMS 2 Pro on

the oor.

Step 3. Use the PTFE tube that comes with the AMS HT to connect the printer’s lower coupler

and the AMS HT filament outlet. Push the tube forward until it cannot move further.

Step 4. Connect the 6-pin cable and the power cable.

a) Use a 6-pin cable to connect the printer and the AMS 2 Pro on the printer.

b) Use a 6-pin cable to connect the AMS 2 Pro on the printer and the AMS HT.

c) Use a long 6-pin cable to connect the AMS HT and the AMS 2 Pro on the oor.

d) Connect power cords to AMS 2 Pro and AMS HT as needed.

NOTE

• To use the AMS 2 Pro drying function, only the AMS 2 Pro directly connected

to the printer does not require external power. Other AMS 2 Pro units must

use the official external power adapter.

• To use the AMS HT drying function, it must be powered by an external AC

power cord.

Step 5. After connection, access the filament interface on the printer touchscreen. Check if the

AMS connection information displays normally. If AMS information is displayed correctly,

the connection is successful.

TIPS

To connect multiple AMS units, follow the same steps. H2C supports up to 4 AMS 2

Pro units and 8 AMS HT units operating simultaneously.

39

Bambu Lab H2C 3D Printing User Manual

Chapter 3 Access 3D Model Resources

Chapter 3 Access 3D Model Resources

3.1 MakerWorld Model Community

MakerWorld (makerworld.com) is Bambu Lab’s official 3D model sharing platform, bringing to-

gether a vast community of talented creators who upload high-quality models spanning every-

thing from a, design, function, and engineering. Whether you are a creative aist or an engineer

solving real-world problems, you can nd models that meet your needs here. Additionally, users

can exchange experiences, share ideas, and learn from each other.

Through MakerWorld, you can:

• Browse curated models and popular community recommendations.

• Download model les in STL, CAD, or 3MF formats.

• Send models directly to Bambu Studio for slicing and printing.

• Upload and share your creative designs, and engage with the community.

MakerWorld is available on the web and directly integrated into Bambu Handy and Bambu Studio

for seamless model browsing and printing.

NOTE

• 3MF les: Contain all print parameters and color information, enabling you to sta print-

ing directly in Bambu Studio.

• STL and CAD les： only contain 3D geometry. Print parameters or color information are

not included; you must set these in your slicer or printer software.

40

Bambu Lab H2C 3D Printing User Manual

Chapter 3 Access 3D Model Resources

3.2 MakerLab Creative Tools

MakerLab provides a range of creative tools that help turn your ideas into printable models with

ease. No modeling experience required, easily create personalized models in minutes.

Creative tools include generators for light boxes, exi toys, relief sculptures, vases, and more,

alongside AI-generated and parametric model tools that are accessible via the web.

MakerLab is integrated into both Bambu Studio and Bambu Handy, enabling seamless model

generation and printing.

NOTE

Bambu Handy supports only some of the tools. For full feature access, use a desktop brows-

er or Bambu Studio.

Each creative tool comes with detailed instructions. Please follow the instructions. The following

example demonstrates the usage process on the web using the Make My Statue (statue genera-

tor):

41

Bambu Lab H2C 3D Printing User Manual

Chapter 3 Access 3D Model Resources

Step 1. On the MakerWorld homepage top bar, click MakerLab > Make My Statue > New

Project.

Step 2. Upload an image as prompted, click confirm, and wait for the model to be generated.

Step 3.

If you are satisfied with the result, click Confirm to download the model. If not satisfied,

click Ret to regenerate.

Step 4. Open Bambu Studio, click File > Import, and select the model le. After importing into

Bambu Studio, you can slice and sta printing.

42

Bambu Lab H2C 3D Printing User Manual

Chapter 4 Initiate a Print from Bambu Handy

Chapter 4 Initiate a Print from Bambu Handy

4.1 Install and Bind Bambu Handy

Bambu Handy is an integrated mobile application designed specifically for Bambu Lab 3D print-

ers. With this app, you can search and print models with one tap, remotely monitor and manage

print jobs, quickly reuse past projects, and adjust settings flexibly during printing.

Before installing Bambu Handy, please ensure the following:

• The printer and your phone are connected to the same network.

• The selected region for the printer matches the region of the Bambu Handy app version.

Step 1. Visit bambulab.com/download or search for Bambu Handy in your mobile app store to

download and install the app.

Step 2. Open Bambu Handy, read and agree to the Privacy Policy and User Agreement, then en-

ter the home page.

Step 3. On the Me page, tap Sign In / Sign Up, enter your email address and verification code to

complete registration.

Step 4. On the printer touchscreen, tap

 > Log in and a QR code will appear on the screen.

Step 5. On the Bambu Handy Devices page, tap + Bind Printer, then scan the QR code dis-

played on the printer touchscreen.

43

Bambu Lab H2C 3D Printing User Manual

Chapter 4 Initiate a Print from Bambu Handy

Step 6. Review and accept the Terms and Conditions and Privacy Policy, then tap Confirm to

Bind.

Step 7. Name the printer, then tap Confirm to complete the binding process.

4.2 Initiate a Print

Step 1. On the Models page, select the model to print and tap Prepare to Print.

Step 2. Select your printer model and print profile, then tap Next to enter the preparation page.

44

Bambu Lab H2C 3D Printing User Manual

Chapter 4 Initiate a Print from Bambu Handy

Model Details

Print Profiles

Step 3. Confirm the printer and build plate models are correct. Select the nozzle diameter and

filament grouping strategy. Check the matching between filaments and hotends. Set the

number of copies and print options, then tap Sta Print.

TIPS

To manually set the matching between filaments and hotends, tap the targeted fila-

ment or hotend icon to enter the hotend selection page and make adjustments.

45

Bambu Lab H2C 3D Printing User Manual

Chapter 4 Initiate a Print from Bambu Handy

Confirm printer model and build plate type

Set filament grouping and print options

NOTE

Bambu Handy automatically assigns filaments based on Filament-Saving Mode. To

adjust this, see Select Filament Grouping Mode.

Step 4. Monitor or adjust the print job on the Devices page.

46

Bambu Lab H2C 3D Printing User Manual

Chapter 4 Initiate a Print from Bambu Handy

a. Camera View: Remotely view live feed of the printer to monitor print status.

b. Progress Bar: Displays current print layer and estimated remaining time to track print

progress.

c. Task Controls: Pause or stop the print in real-time.

d. Pas Skip: When printing multiple pas, if a model collapses or fails to print correct-

ly, use this feature to skip the current model pa and continue printing the remaining

models.

e. Printer Settings:

• Print Speed: Choose from Silent, Standard, Spo, and Ludicrous.

• Heatbed Temperature: Monitor and adjust the heatbed temperature.

• Light: Turn the printer chamber light on or o.

• Pa Cooling Fan: Adjust the cooling fan speed based on the filament characteris-

tics and model structure.

47

Bambu Lab H2C 3D Printing User Manual

Chapter 5 Initiate a Print from Bambu Studio

Chapter 5 Initiate a Print from Bambu Studio

5.1 Install and Bind Bambu Studio

Bambu Studio is the official slicing software developed by Bambu Lab, featuring customized func-

tions designed specifically for Bambu 3D printers. It offers a project-based workflow, optimized

slicing algorithms, and an intuitive graphical interface to deliver a smooth printing experience. Be-

fore 3D printing, the model must be sliced, which means converting the 3D model into instruc-

tions recognizable by the printer. This is a critical step in turning your creative design into a physi-

cal printed product.

To smoothly install and run Bambu Studio, please ensure your computer meets the following re-

quirements:

• Operating system: Windows 10, Mac OS X 10.15, Ubuntu 20.02, Fedora 36, or later.

• Processor: Intel® Core 2 or AMD Athlon® 64; 2 GHz or higher.

• Memory: Minimum 4 GB RAM; 8 GB RAM or higher recommended.

• Storage: At least 2 GB of available space.

• Graphics support: OpenGL 2.0 compatible.

Step 1. Download Bambu Studio.

• Windows and MacOS versions: bambulab.com/download

• Linux version: github.com/bambulab/BambuStudio/releases

Step 2. Double-click the downloaded .exe le and follow the instructions to complete the instal-

lation and open the software.

Step 3. Select your region and click Next.

Step 4. Read and choose whether to join the Customer Experience Improvement Program.

Step 5. Select the printer model and nozzle size preset you will use, then click Next. The selected

preset will be used later to generate suitable print paths during slicing.

48

Bambu Lab H2C 3D Printing User Manual

Chapter 5 Initiate a Print from Bambu Studio

Step 6. Choose the filament preset, then click Next.

Filament presets include parameters such as print temperature. Once a filament is se-

lected for future prints, all printing parameters will be applied without the need for man-

ual adjustments.

Step 7. Check Install Bambu Network Plug-in, then click Finish to sta the installation.

This plugin supports printing over local networks or the internet and enables remote

control and user data synchronization.

49

Bambu Lab H2C 3D Printing User Manual

Chapter 5 Initiate a Print from Bambu Studio

Step 8. After logging in, printer information will be automatically synchronized across all your

devices.

5.2 Introduction to Bambu Studio Interface

Home

The Home interface integrates model management, resources, and learning content. This is the

default page when opening Bambu Studio.

1. Account information: View the current account or log out.

2. Page navigation: Quickly access recently opened les, online models (MakerWorld), MakerLab,

Maker's Supply, print history, and user manuals.

50

Bambu Lab H2C 3D Printing User Manual

Chapter 5 Initiate a Print from Bambu Studio

3. Search bar: Enter keywords to search online models inside MakerWorld.

4. Project operations: Open local projects or create new ones.

Prepare

This interface is used to select the printer model, filament type, print settings, and to slice models

and send print jobs.

1. Printer settings: Bambu Studio slices and generates suitable print parameters based on these

settings.

2. Filament settings: Select the filament type and color used for printing. Preset parameters are

loaded automatically.

3. Print presets: Provides multiple quality-level presets (such as Standard, Fine, etc.) ready to

use.

4. Print parameter details: Models downloaded from MakerWorld usually include all print para-

meters recommended by the creator. Simply select the printer model to slice. Parameters can

be manually adjusted to fulfill custom applications, such as lowering layer height to reduce

layer lines (see Adjust Slicing Parameters).

5. Top toolbar: Provides multiple options for viewing and modifying the model.

6. Slice button: After selecting the slicing mode and filament grouping mode, click Slice Plate to

generate a preview of the printed pas and their G-code. (see Dual Hotend Printing).

7. Print and export: Initiate printing or export les. Click

 to choose from the following options.

• Print plate: To print the currently selected plate.

• Print all: To print all plates.

• Export plate/all sliced le: Export sliced les of the currently selected plate/all plates to

printer storage.

51

Bambu Lab H2C 3D Printing User Manual

Chapter 5 Initiate a Print from Bambu Studio

• Send/Send all: Send sliced les of the currently selected plate/all plates to the printer's USB

drive. The print job can then be initiated from the printer screen.

NOTE

This operation requires the Bambu Network Plugin installed, and Bambu Studio and

the printer must be on the same network.

8. Print plate: Designated location for placing and editing models.

Preview

This interface displays detailed information about the sliced models, such as line types, filament,

print speed, and print paths. At the same time, custom actions can be added at specific layers, in-

cluding custom G-code, print pauses, and filament changes.

Device

This interface shows the status and operation options of the currently connected printer.

52

Bambu Lab H2C 3D Printing User Manual

Chapter 5 Initiate a Print from Bambu Studio

1. Connected device information. If you have multiple printers, click the printer name to switch

between devices.

2. View various printer information, including device status, storage media, rmware updates,

and Health Management System (HMS). This section enables real-time monitoring, device

control, USB drive le access, and rmware updates.

3. Play/pause live video and view playback status.

4. Display information about the current print job, including job thumbnail and print progress.

You can skip objects, pause, sta, or stop the job.

5. Adjust the air condition and control temperatures of the hotends, heatbed, and chamber. The

left value indicates the current temperature, while the right value indicates the target temper-

ature.

6. Control toolhead and heatbed movement when the printer is idle.

7. Displays the loading status of the left and right extruders. A green dot indicates the filament is

loaded. Control the extruders by clicking the up/down arrows to manually extrude or retract 1

cm of filament.

8. Toggle display between and Filament and Hotends.

9. Display and manage filament information, supporting filament editing, loading, and unload-

ing operations, and allows control of the Auto Refill feature. If connected to AMS, you can also

manage functions such as filament insertion update, update on startup, and update remaining

capacity.

53

Bambu Lab H2C 3D Printing User Manual

Chapter 5 Initiate a Print from Bambu Studio

10. Display and manage hotend and induction hotend rack information, supporting hotend infor-

mation access and control of the rack's lifting and homing.

5.3 Download and Import Model

MakerWorld hosts a wide variety of high-quality models uploaded by creators, including both

model les and complete print configurations. The creators predefine the print parameters, en-

abling you to download and send the le directly to the printer with a single click, eliminating the

need for further tuning.

5.3.1 MakerWorld Models

Step 1. Select the model you want to print on the MakerWorld website or within Bambu Studio's

online models, then go to the model details page.

Step 2. Choose a print profile that matches your printer model and printing requirements.

Step 3.

If you are using MakerWorld on a browser, click Open in Bambu Studio; if you are using

Bambu Studio, click Download and open.

Step 4. Bambu Studio will automatically download the model and open it in the Prepare inter-

face.

5.3.2 Other Models

Step 1. Prepare the model le.

NOTE

Bambu Studio supports the following le formats: .3mf, .stl, .stp, .step, .amf, .obj.

Step 2.

Import the model using your preferred method.

a. Select File > Import > Import 3MF/STL/STEP/SVG/OBJ/AMF

54

Bambu Lab H2C 3D Printing User Manual

Chapter 5 Initiate a Print from Bambu Studio

b.

In the Prepare interface, click

 in the top toolbar, select the le, then click Open.

c. Drag and drop the model le directly into the Prepare interface.

Step 3. After successful import, the model will automatically load onto the plate, ready for pre-

viewing, editing, or slicing.

55

Bambu Lab H2C 3D Printing User Manual

Chapter 5 Initiate a Print from Bambu Studio

5.4 Initiate a Print

Step 1. Select the correct printer model.

Step 2. Click Sync info and select a nozzle for printing. The system will automatically sync the

nozzle data from the toolhead and Induction hotend rack, including nozzle diameter, ow

settings, and nozzle configuration. Then, slicing will be generated according to the se-

lected nozzle type.

NOTE

Bambu Studio does not currently support mixed slicing with hotends of different di-

ameters.

When induction hotends with the same diameter but different ows are installed,

the system automatically sets the nozzle ow to "Hybrid". It will prioritize the stan-

dard-ow nozzle and assign the high-ow nozzle only when it does not introduce

additional purging.

Step 3. Click

 in the Project Filaments list to sync AMS filament information, and select the

purge mode (Standard or Purge Saving).

• Standard Mode: The purge volume for the prime tower strictly follows the parameters

specified in the Project Filaments >

 > Filament > Filament prime volume, ensuring

stable and reliable print quality.

• Purge Saving Mode: The prime tower purge volume is xed at 15 mm³ to reduce fila-

ment consumption and improve overall print speed.

56

Bambu Lab H2C 3D Printing User Manual

Chapter 5 Initiate a Print from Bambu Studio

Step 4. Select the desired preset from the Process drop-down list. Smaller layer height results in

longer print time. For most models printed with a 0.4 mm nozzle, a 0.2 mm layer height

provides a good balance between print quality and efficiency.

Step 5. Adjust slicing parameters as needed.

NOTE

Process presets include appropriate default parameters suitable for most print

tasks. You can adjust them based on your actual needs or desired results.

Step 6. After completing all settings, select the filament grouping mode, perform model slicing,

and review information such as color scheme, filament usage, and print time (see Dual

Hotend Printing).

Step 7. Send the print job. Confirm the filaments used by the left and right extruders, configure

advanced options if needed, then click Send.

NOTE

Timelapse recording is o by default, while other print calibrations are set to auto.

To use high-precision nozzle offset calibration data, please disable the nozzle offset

calibration when sending the print job.

5.5 Adjust Slicing Parameters

5.5.1 Model Size

You can adjust the model size according to your printing requirements.

Step 1. Click the model you want to resize to activate the top toolbar.

Step 2. Click the Scale tool.

57

Bambu Lab H2C 3D Printing User Manual

Chapter 5 Initiate a Print from Bambu Studio

Step 3. Adjust the model size.

• Enter a percentage or an exact value for the X, Y, and Z axes. When Uniform Scale

is checked, modifying any value automatically adjusts the other two proportionally.

When it is unchecked, each axis can be adjusted independently.

• Drag the control points on the model. Dragging the control points at the four bottom

corners scales the model uniformly; dragging other control points stretches the model

along a single direction.

Modify values

Drag control points

5.5.2 Quality Settings

Print quality parameters directly affect the model’s level of detail and overall appearance. Proper-

ly configuring these parameters helps achieve an optimal balance between printing precision and

efficiency.

58

Bambu Lab H2C 3D Printing User Manual

Chapter 5 Initiate a Print from Bambu Studio

Layer Height

Layer height refers to the vertical stacking height of each printed layer (unit: mm) and is a key pa-

rameter determining print resolution and efficiency.

For example, with a 0.4 mm nozzle, a smaller layer height (such as 0.12 mm) achieves finer layers,

resulting in smoother surfaces and richer details, but significantly increases print time. In compari-

son, a larger layer height (such as 0.28 mm) decreases print time but may produce noticeable lay-

er lines affecting surface quality.

59

Bambu Lab H2C 3D Printing User Manual

Chapter 5 Initiate a Print from Bambu Studio

Recommended settings:

• Layer height is typically 50% of the nozzle diameter, with a recommended range of 30% to

70% of the nozzle diameter. For instance, when using a 0.4 mm nozzle, the recommended lay-

er height range is 0.12 mm – 0.28 mm.

• When optimizing layer height, consider model complexity, required strength, and nozzle diame-

ter to balance surface quality and printing efficiency.

Initial Layer Height

The height of the rst printed layer of the model. Increasing the initial layer height enhances ad-

hesion between the model and the build plate, reducing the risk of warping or detachment.

For more details on layer height settings, please visit the Bambu Lab Wiki (wiki.bambula-

b.com/home) for relevant guidance.

Seam

A seam is a small gap formed where the sta and end points of wall paths meet on the model sur-

face, usually appearing as a vertical line. This phenomenon is an inherent structural characteristic

that cannot be completely avoided in FDM 3D printing.

On models with edges or protrusions, seams can be naturally concealed. However, on smooth

cued or continuous surfaces like cylinders, seams are more noticeable and can affect the exter-

nal appearance.

60

Bambu Lab H2C 3D Printing User Manual

Chapter 5 Initiate a Print from Bambu Studio

To achieve better print results, you can set the seam position in Quality parameters. There are four

types of seam positions to choose from:

• Nearest: Prioritizes concave or convex non-overhang vertices to hide seams, especially suitable

for models with sharp corners. If no suitable vertices are found, it selects positions close to the

end of the previous path to reduce travel distance and oozing.

• Aligned: Aligns seam across layers, making them more concentrated and easier to post-

process.

• Random: Distributes seams randomly on each layer to avoid visible lines, but may cause irregu-

lar surface patterns.

• Back: Fixes seams on the back side of the model, suitable for display models.

61

Bambu Lab H2C 3D Printing User Manual

Chapter 5 Initiate a Print from Bambu Studio

For more details on seam settings, please visit the Bambu Lab Wiki (wiki.bambulab.com/home) for

relevant guidance.

Only One Wall on Top Surfaces

When enabled, the top surface of the model is printed as a single wall, helping achieve clean and

neat surfaces. For models with at top structures (such as cubes), this results in a smooth and

neat finish. However, for models with cued top surfaces (such as spheres), it may cause notice-

able layer lines that affect surface detail.

When printing cued top surfaces, it is recommended to select Not Applied to obtain better sur-

face quality and smoothness.

5.5.3 Strength Settings

Strength-related parameters directly affect the model's structural integrity and durability.

62

Bambu Lab H2C 3D Printing User Manual

Chapter 5 Initiate a Print from Bambu Studio

Wall Loops

This parameter determines the thickness of the model’s outer walls, directly impacting overall

structural strength and surface quality. Outer and inner walls are typically differentiated by color

(in Bambu Studio preview) as shown below, orange represents the outer wall and yellow repre-

sents the inner wall.

Recommended settings:

• Functional pas: Set to 3–4 walls to improve structural strength and durability.

63

Bambu Lab H2C 3D Printing User Manual

Chapter 5 Initiate a Print from Bambu Studio

• Decorative models: Set to 2 layers to save material and improve efficiency.

Top Shell Layers and Thickness

Top shell layers determines the number of solid layers at the top of the model, typically including

the outermost top surface, internal solid infill, and bridge layers.

The top shell thickness is calculated as follows:

Top shell thickness = Top shell layers × Layer height

For example, the default setting is 5 layers × 0.2 mm = 1.0 mm.

Setting the appropriate top shell thickness helps achieve a smooth, solid top surface and

strengthens the model.

NOTE

•

•

If the manually set thickness is less than the calculated value, Bambu Studio will auto-

matically increase the top shell layers to match the calculated thickness.

If the thickness is set to 0, the system will automatically calculate the thickness based on

the top shell layers and layer height.

Recommended settings:

•

It is recommended to set the top shell layers to 4–6 to ensure a smooth, solid top surface and

effectively cover the underlying infill.

• When using larger layer heights or low sparse infill density, increasing the top shell layers is

suggested to improve print quality.

64

Bambu Lab H2C 3D Printing User Manual

Chapter 5 Initiate a Print from Bambu Studio

Bottom Shell Layers and Thickness

Bottom shell layers determine the solid thickness of the model's base, consisting of the bottom

surface and solid infill above it.

The bottom shell thickness is calculated as follows:

Bottom shell thickness = Bottom shell layers × Layer height

Increasing the bottom shell layers appropriately enhances bottom strength and stability, and im-

proves adhesion to the build plate.

NOTE

•

•

If the manually set thickness is less than the calculated value, Bambu Studio will auto-

matically increase the bottom shell layers to match the calculated thickness.

If the thickness is set to 0, the system will automatically calculate the thickness based on

the bottom shell layers and layer height.

Recommended settings:

• Setting the bottom shell thickness to 0 means it is fully determined by layer height and bottom

shell layers.

•

In most cases, 3 or more bottom shell layers are recommended to ensure a solid and reliable

base.

Sparse Infill

Sparse infill density determines how compact the model's internal structure is.

• Low density (10% – 20%): Suitable for non-load-bearing display models, significantly saving fil-

ament and print time.

65

Bambu Lab H2C 3D Printing User Manual

Chapter 5 Initiate a Print from Bambu Studio

• High density (above 30%): Enhances structural strength, suitable for functional pas.

• Recommended settings: 15%, suitable for most daily prints, balancing strength and efficiency.

Sparse Infill Patterns

Different sparse infill patterns suit various needs and can be categorized as follows:

• Strength-focused patterns: Such as Honeycomb, Cubic, Gyroid. These patterns provide uni-

form load distribution and high strength, making them ideal for functional pas.

• Speed-focused patterns: Such as Grid, Support Cubic, Lightning. These patterns have simple

paths and allow fast infill, making them ideal for test prints or efficiency focused tasks.

• Aesthetic-focused patterns: Such as Hilbe Cue, Octagram Spiral, Archimedean Chords.

These patterns offer unique textures or smoother internal structures, improving the overall ap-

pearance of models with visible infill.

66

Bambu Lab H2C 3D Printing User Manual

Chapter 5 Initiate a Print from Bambu Studio

For more details on sparse infill patterns or advanced strength settings, please visit the Bambu

Lab Wiki (wiki.bambulab.com/home) for relevant guidance.

5.5.4 Support Settings

In FDM 3D printing, support structures are critical in complex models with overhangs, bridges, and

other challenging geometries. Proper support configuration can significantly improve print suc-

cess rates and simplify post-processing.

Introduction to Common Parameters

• Type

Normal Supports are generated using a standard linear structure, providing a stable, evenly

distributed layout, fast generation, and easy removal from the model surface. This type is suit-

able for mechanical pas and geometric models dominated by at or linear surfaces.

67

Bambu Lab H2C 3D Printing User Manual

Chapter 5 Initiate a Print from Bambu Studio

Tree supports employ a "trunk + branches" branching structure built layer by layer, making

contact only at critical stress points. They are ideal for complex cued surfaces and detailed

characters or a models, greatly reducing support material usage and avoiding leaving obvious

marks on ne surfaces.

Auto means Bambu Studio generates support automatically based on the set threshold angle.

Manual indicates that supports are generated only in the areas you specify, using the Supports

Painting tool. For detailed steps on support painting, please visit the Bambu Lab Wiki (wik-

i.bambulab.com/home) for relevant guidance.

• Threshold Angle

Threshold angle defines the steepest surface angle (relative to the horizontal plane) that can

be printed without supports. When the surface angle is smaller than this threshold and the sup-

port type is set to Auto, supports will be generated. Adjusting this value is a quick way to con-

68

Bambu Lab H2C 3D Printing User Manual

Chapter 5 Initiate a Print from Bambu Studio

trol the amount of support generated. Lower values produce fewer supports, higher values

produce more. The default value is 30°, suitable for most models.

• On Build Plate Only

Enabling this option ensures that all supports originate only from the build plate and do not at-

tach to the model itself. This helps reduce support marks on the model surface, improving ap-

pearance quality and simplifying post-processing. However, for structures far from the build

plate or completely suspended, this setting may not offer adequate support. It should be used

carefully based on the model geometry.

• Filament for Supports

Supports consist of two pas: support base and support interface.The support interface is

the contact layer with the model, and the rest forms the support body. These two pas can

use different types of filaments. If unspecified, the current layer’s filament is used by default to

minimize filament change time. Typically, dedicated support materials (such as Bambu Support

W and Support G) are chosen for printing the support interface to improve removability and

surface quality.

Introduction to Advanced Parameters

• Normal Support Style

69

Bambu Lab H2C 3D Printing User Manual

Chapter 5 Initiate a Print from Bambu Studio

◦ Grid: Projects overhang areas vertically onto the build plate and expand outward to cre-

ate regular, grid-like support columns. The supports are stable and strong, suitable for large

horizontal overhangs.

◦ Snug: Grows precisely along the model contour, saving material and providing flexible sup-

port shapes. It is well suited for complex or detailed areas.

• Tree Support Style

◦ Tree Slim : Features thin branches and an optimized overall structure. Suitable for small,

lightweight overhangs. Its aggressive merging strategy reduces material consumption and

minimizes removal marks.

70

Bambu Lab H2C 3D Printing User Manual

Chapter 5 Initiate a Print from Bambu Studio

◦ Tree Strong: Characterized by a thicker trunk and branches, offering a more robust struc-

ture with strong load-bearing capacity. Recommended for large or heavy overhangs where

stronger support is required.

◦ Tree Hybrid: Combines the advantages of tree and normal supports. The software automat-

ically determines the most suitable structure and applies it in different areas. This style of-

fers a flexible automated strategy aimed at optimizing support structures for different model

pas.

71

Bambu Lab H2C 3D Printing User Manual

Chapter 5 Initiate a Print from Bambu Studio

◦ Tree Organic: Generated using biomimetic algorithms, producing natural, smooth, and

cued branches. It intelligently routes support to reach overhangs while minimizing material

usage and easing removal. Suitable for most models that require tree supports.

• Raft

A raft is a base layer located beneath the model and support structures. It is used to enhance

adhesion during printing, especially with warp-prone filaments such as ABS. Rafts effectively

prevent support detachment and lift the entire model o the build plate, isolating it from po-

tential surface unevenness.

72

Bambu Lab H2C 3D Printing User Manual

Chapter 5 Initiate a Print from Bambu Studio

• Top Z Distance

The vertical distance between the top of the support interface and the underside of the mod-

el’s overhang.

When using dedicated support interface filaments such as Bambu Support for PLA, Bambu

Support for PLA/PETG, or Bambu Support for PA/PET, this value can be set to 0, allowing direct

contact between support and model. When the support interface uses the same filament as the

model, a value of around 0.2 mm is recommended to prevent supports from becoming difficult

to remove. The table below shows how the Top Z Distance affects support removal and support

surface quality:

Top Z Distance

Ease of Support Removal

Support Surface Quality

Increase

Easier

73

Lower

Bambu Lab H2C 3D Printing User Manual

Chapter 5 Initiate a Print from Bambu Studio

Top Z Distance

Ease of Support Removal

Support Surface Quality

Decrease

Harder

Higher

• Support/Object XY Distance

This parameter controls the horizontal distance between supports and the model, with a de-

fault value of 0.35 mm. The greater the distance, the easier it is to remove the support, and

it also reduces the risk of scratching the model’s surface. If the support is difficult to remove,

consider increasing this value appropriately.

CAUTION

◦ The top Z distance and the support/object XY distance should be adjusted together.

Their combination directly impacts model surface quality and ease of support removal.

Finding the optimal balance is key to achieving efficient and high-quality printing.

◦ It is recommended to remove supports within 2 hours after printing. Prolonged expo-

sure may cause moisture absorption, making supports softer and harder to remove—

especially when printing moisture-sensitive filaments such as PA-CF, PA6-CF, or when

using water-absorbing support filaments like PVA or Support for PA/PET. If supports are

hard to remove, drying the model or cooling it before removal may help.

For more advanced support settings, please visit the Bambu Lab Wiki (wiki.bambulab.com/home)

for relevant guidance.

5.5.5 Speed Settings

Selecting the appropriate print speed helps improve print quality and accuracy. Bambu Studio

provides optimized default speed presets that work well for most print jobs. You may also ne-

tune the print speed according to custom needs.

TIPS

Process presets already include all required settings for specific printing scenarios and are

recommended for beginners. If you need to adjust the print speed, please enable advanced

mode in the process tab.

74

Bambu Lab H2C 3D Printing User Manual

Chapter 5 Initiate a Print from Bambu Studio

Print speed

•

Initial Layer Speed

The print speed for solid infill and other pas of the rst layer. This setting directly affects bed

adhesion.

• Overhang Speed

When Slow down for overhangs is enabled, Bambu Studio automatically reduces inner and out-

er wall print speeds in overhang areas to improve overhang surface performance. This feature

is enabled by default and can be disabled if needed.

• Other Layers Speed

Print speeds for inner and outer walls, infill, bridge, and supports. If the default parameters do

not meet expectations, custom adjustments can be made.

75

Bambu Lab H2C 3D Printing User Manual

Chapter 5 Initiate a Print from Bambu Studio

• Travel Speed

The movement speed when no filament is extruded. This mainly affects overall printing efficien-

cy.

• Acceleration

Print acceleration for travel, rst layer, inner and outer walls, top surface, and sparse infill. This

parameter can affect motion smoothness and speed transition during printing.

76

Bambu Lab H2C 3D Printing User Manual

Chapter 6 Key Features Introduction

Chapter 6 Key Features Introduction

6.1 Voek Hotend Change System

The Voek Hotend Change System is the core technology module enabling multi-material and

multi-color printing on this printer. It supports storage and automatic switching of up to 6 induc-

tion hotends. The system achieves fully automatic material changes through automatic hotend

changing combined with the AMS (Automatic Material System). This significantly reduces color

mixing risks and enables nearly "no purging" material changes during 7-color printing.

NOTE

Up to 7 different filaments can be used in a single print without purge waste. This requires 6

induction hotends and one left hotend of the same diameter, along with the corresponding

numbers of AMS units.

NOTE

The "no purging" concept does not include the initial purge when filament enters the hotend

for the rst time.

6.1.1 Workflow

The Voek Hotend Change System automatically coordinates hotend storage, fetching, heating,

and cleaning during printing without manual intervention. During the induction hotend switching

process, the printer will automatically perform the following steps:

Step 1. The toolhead moves to the right, unlocks the current right hotend, and places it in an

empty dock on the induction hotend rack.

Step 2. According to the slicing settings, fetch the next induction hotend from the rack and lock

it onto the right hotend.

Step 3. The induction heating assembly heats the hotend to the target temperature quickly and

extrudes a small amount of filament onto the prime tower to balance extrusion pressure.

Step 4. After completing these steps, the printer stas printing with the switched hotend.

CAUTION

To ensure correct storage of the induction hotend on the right hotend during switching,

please confirm there is an available empty dock on the induction hotend rack.

77

Bambu Lab H2C 3D Printing User Manual

Chapter 6 Key Features Introduction

6.1.2 Nozzle and Filament Mapping

When sending a multi-color print job, Bambu Studio automatically searches for and matches fila-

ment in the AMS with the same material type (such as PLA, ABS, etc.) and the closest color based

on the slicing project settings. It also considers the filament record last used on the induction ho-

tend to match the most suitable induction hotend.

•

•

If the material type and color are exactly the same, the mapping will complete automatically.

If the material type matches but the color does not exactly match, the closest color will be se-

lected for mapping.

Before starting a print, click "Sync info" in Bambu Studio to synchronize nozzle information, then

click

 to synchronize filament information to ensure accurate mapping.

CAUTION

Bambu Studio bases nozzle mapping on the filament settings in the sliced le. Please com-

plete filament information synchronization before slicing.

When starting a print, the printer automatically calculates and generates the mapping between

filament and nozzle based on the printing parameters and the current nozzle status on the ma-

chine.

CAUTION

This calculation is performed on the printer. If the printer's network connection is poor, auto-

matic mapping may fail.

1. Filament type and color.

2. Filament storage location: The display on the external spool shows "Ext"; inside the AMS, posi-

tions are labeled with letters and numbers. The same letter indicates positions within the same

AMS unit.

78

Bambu Lab H2C 3D Printing User Manual

Chapter 6 Key Features Introduction

3. Assigned induction hotend location: Installed on the right hotend is marked as R; positions on

the rack are numbered 1 through 6.

If you are not satisfied with the automatic mapping results, you can manually adjust the nozzle

mapping on the Send print job page.

Because the required nozzle type (including nozzle diameter and ow rate) is preset for each fila-

ment during slicing, nozzles that do not meet these requirements will be shown in gray and can-

not be selected during remapping. You can only select nozzles that meet the slicing requirements.

After completing remapping, if the new configuration increases filament consumption, the soft-

ware will display an estimated increase to help you assess the impact of the adjustment.

6.1.3 Multi-Material Printing with Hard Filament

Hard filament multi-material printing optimizes performance and functionality based on pa re-

quirements. It achieves lightweight structures, enhanced durability, and improves design freedom

and integration. To ensure a secure connection between different materials, use beam interlock-

ing. Create small bridge-like or beam-like structures on one material, into which another material

is interlocked. This forms an additional bonding layer between different materials to enhance their

connection.

79

Bambu Lab H2C 3D Printing User Manual

Chapter 6 Key Features Introduction

CAUTION

High-temperature and low-temperature filaments must not be mixed for printing, as this

may cause extruder or nozzle clogging and damage. Bambu Studio will automatically restrict

the mixing of high and low temperature filaments during slicing.

When printing high-temperature and medium-temperature filaments together, mid-temper-

ature filaments may soften, increasing the risk of extruder or nozzle clogging. Carefully ad-

just the chamber temperature during printing.

How to use beam interlocking

1. Check the model to ensure it contains two or more objects with intersecting areas where beam

interlocking is required.

2.

In Bambu Studio's slicing settings, select two objects that need to use beam interlocking,

right-click it and click Merge.

3. Click Global in the process menu, select Others > Advanced, check Use beam interlocking to

enable it.

4. Adjust beam interlocking parameters such as width, direction, layers, depth, and boundary

avoidance according to the model and material requirements.

Parameter Introduction

•

•

Interlocking beam width: Determines the thickness or width of each interlocking beam (de-

fault 0.8 mm). A larger width increases contact area and mechanical lock strength but occupies

more space. Excessive width may interfere with pa design.

Interlocking direction: Determines the direction or angle in which the interlocking beams are

generated. The default angle is 22.5°, which means the beams are slightly inclined rather than

fully vertical or horizontal. This affects bonding stability and the material’s bending behavior

under stress.

80

Bambu Lab H2C 3D Printing User Manual

Chapter 6 Key Features Introduction

•

•

•

Interlocking beam layers: Determines the height of each beam, i.e., the number of printed lay-

ers for each beam. It is generally recommended to keep the default value of 2. This influences

bonding strength.

Interlocking Depth: Defines the depth of the interlocking beam in the material, with a default

value of 2. Increasing depth (such as to 6) allows beams to extend further into the material,

forming more layers and creating a stronger bond. Note that adjusting depth may affect the

number of filament changes during slicing.

Interlocking boundary avoidance: Controls the distance between the interlocking beam and

the outer wall, affecting the surface quality and edge strength of the outer wall. For exam-

ple, when set to 1, the beams are positioned close to the outer walls, providing high structur-

al strength while maintaining good surface quality. For example, when set to 10, the beams are

offset significantly inward, resulting in smoother outer surfaces but reduced edge strength.

CAUTION

Please check the wall thickness and internal space to ensure that interlocking beams can be

generated and that the outer wall thickness is sufficient to maintain structural strength. For

thin walls or high-detail areas, adjust beam layer count and depth as needed to avoid affect-

ing key features.

TIPS

Optimize beam interlocking direction based on pa orientation to achieve more reliable

bonding.

TIPS

Before printing, it is recommended to verify that the parameter settings are appropriate us-

ing a small test piece.

6.1.4 Induction Hotend Rack Setup

Induction hotend rack setup ensures the toolhead can accurately locate the hotend rack when

switching induction hotends, enabling smooth fetch and uninstall of induction hotends. On the

printer touchscreen, tap

 > Calibration > Induction Hotend Rack Setup. Follow the on-screen

instructions to ensure no induction hotends are installed on the induction hotend rack, then tap

Sta to perform the setup.

81

Bambu Lab H2C 3D Printing User Manual

Chapter 6 Key Features Introduction

When is induction hotend rack setup needed?

• Before the rst print on a new printer.

• After restoring to factory settings.

• After replacing the MC board.

• After replacing or disassembling the induction hotend rack.

• After long-distance transportation of the printer.

6.2 Dual Hotends Printing

This printer is equipped with dual hotends on the left and right, allowing for quick switching be-

tween two materials or colors to enhance model expression and functionality. For example, com-

bining hard and soft materials can meet the manufacturing requirements of complex pas (see

Soft and Hard Filament Multi-Material Printing ).

The dual hotends design supports flexible switching of materials or colors within the same task,

eliminating frequent filament changes and significantly reducing print preparation time.

6.2.1 Select Filament Grouping Mode

This printer's filament grouping considers both the distribution of filaments between the left and

right hotends and the number of available induction hotends, automatically assigning multiple fil-

aments reasonably to the corresponding hotends for printing. During slicing, the number of avail-

able induction hotends directly affects the final filament grouping plan and the amount of fila-

ment used for purging.

82

Bambu Lab H2C 3D Printing User Manual

Chapter 6 Key Features Introduction

Bambu Studio intelligently assigns suitable hotends and print sequences for filaments based on

the number of filaments required by the model, the purge amounts for different print orders, and

the physical characteristics of the hotends.

Bambu Studio provides 3 filament grouping modes: Filament-Saving Mode, Convenience Mode,

and Custom Mode. The system defaults to Filament-Saving Mode, which is enabled automatically

without manual activation.

If you need to switch grouping modes, follow the steps below.

1. Hover the mouse cursor over the Slicing button on the interface to display a pop-up window

containing 3 modes.

2. Click to select the desired filament grouping mode.

3. Click the slicing button to perform the slicing operation.

Filament-Saving Mode

Filament-Saving Mode aims to minimize filament waste caused by purging during filament

changes by assigning filaments that appear together in more layers (meaning frequent switching)

and those with large purge volumes to different hotends, following these rules:

•

filament quantity ≥ 2 types: The algorithm will allocate one type of consumable to the left ho-

tend. Switching between the left and right hotends is most efficient, reducing both purge vol-

ume and switching time. In contrast, switching between induction hotends also reduces purg-

ing but takes longer overall due to loading and unloading reliance on the AMS.

• When the number of filament types exceeds the total number of hotends: The algorithm

prioritizes assigning the two filaments with the lowest purge requirement to the same hotend,

maximizing material savings.

Before using this mode, it is recommended to manually set or synchronize the pairing relationship

between the AMS and left/right hotends so the filament grouping in Bambu Studio reflects the

83

Bambu Lab H2C 3D Printing User Manual

Chapter 6 Key Features Introduction

physical layout. If the printer is not connected to the AMS, it is assumed by default that each ho-

tend is connected to one external spool.

After slicing, filaments are bound to their assigned hotends. When sending a print job, switching

to the other hotend is not allowed, even if it contains a filament with a closer color match. To save

filament while improving color matching, manually adjust the filament placement based on the

grouping results.

NOTE

This printer supports up to 4 AMS 2 Pro units and 8 AMS HT units simultaneously, providing

a total of 24 filament slots. In extreme cases, if all AMS units are connected to the same ho-

tend, that hotend supports a maximum of 24 filament spools.

TIPS

Filament-Saving Mode prioritizes reducing purge filament consumption. The filaments au-

tomatically assigned after slicing may differ from the ones initially required by the model. If

model color accuracy is critical, it is recommended to manually adjust filament positions ac-

cording to the grouping.

84

Bambu Lab H2C 3D Printing User Manual

Chapter 6 Key Features Introduction

Convenience Mode

Convenience mode groups filaments based on the actual filament's placement in the AMS, typical-

ly without requiring additional adjustments. It is suitable for scenarios such as remote printer op-

eration, where frequent manual AMS adjustments are impractical.

Please ensure the printer is connected before using this mode. For more accurate filament match-

ing, it is recommended to synchronize AMS information from the filament list before slicing, en-

suring the software obtains data consistent with the actual filament placement.

NOTE

This mode is easy to operate but may consume more filament than the filament-saving

mode.

Custom Mode

If the grouping from Filament-Saving Mode or Convenience Mode does not fully meet your needs

but you wish to adjust based on them, you can follow the steps below.

1.

2.

In the slicing results display panel, click Regroup filament.

In the filament grouping pop-up window, select Custom Mode.

3. Drag the filaments you want to move to the target hotend positions.

4. Click OK, and Bambu Studio will recalculate the slicing results based on your adjustments.

85

Bambu Lab H2C 3D Printing User Manual

Chapter 6 Key Features Introduction

If you want to fully customize how filaments are assigned, follow these steps.

1. Hover the mouse cursor over the Slicing button on the interface to display a pop-up window

containing 3 modes.

2. SelectCustommode, click the slicing button to open the filament grouping pop-up window.

3. Drag the filaments you want to move to the target hotend positions.

4. Click OK, and Bambu Studio will recalculate the slicing results according to your custom set-

tings.

After slicing, the system will display how much filament could be saved by using the (Fila-

ment-Saving Mode) compared to your manual grouping. This helps you evaluate whether opti-

mization is worthwhile.

NOTE

Material-Saving Mode considers only the amount of filament saved from reduced purging.

In some cases, it may result in more filament changes than Convenience Mode or Custom

Mode, which is normal.

6.2.2 Slicing Mode Selection

To apply a uniform filament grouping mode across all build plates, select your desired grouping

mode, then click Slice all. At this point, all build plates will use the same grouping mode, and any

existing plate-specific grouping modes will be overwritten.

To set filament grouping modes individually for each build plate, configure the filament grouping

for a single plate, then click Slice plate.

86

Bambu Lab H2C 3D Printing User Manual

Chapter 6 Key Features Introduction

6.2.3 Multi-Material Printing with Soft and Hard Filament

Multi-material printing of soft and hard filaments allows both soft and hard materials to be inte-

grated within the same model, creating a unified rigid-ex structure that achieves both function-

al and performance requirements. This process reduces assembly steps, improves overall print-

ing efficiency, and expands creative and engineering design freedom. It is particularly suitable for

products requiring both strength and flexibility, such as helmets, bicycle saddles, and functional

prototypes.

TIPS

It is the same for both H2C and H2D for how to print with soft and hard filament at the same

time. Please see Soft and Hard Filament Multi-Material Printing Guide on our Wiki (wiki.bam-

bulab.com/h2/manual/soft-and-hard-filament-multi-material-printing-guide) for detailed

instructions.

CAUTION

It is strongly recommended to use Bambu filaments to ensure optimal print quality and de-

vice safety.

CAUTION

Due to softening of flexible filaments at high temperatures during printing, this feature cur-

rently only supports mixed printing of Bambu TPU 95A HF with high-temperature engineer-

ing filaments.

87

Bambu Lab H2C 3D Printing User Manual

Chapter 6 Key Features Introduction

The following uses PETG-CF combined with TPU 95A HF as an example to briey outline the main

operational steps.

Step 1. Prepare the filaments and d the TPU filament (see Drying Filament).

• Recommended drying equipment: AMS HT

• Temperature: 75 °C

• Drying duration: 18 hours

Step 2. Load the engineering filament (PETG-CF) into the left hotend, and load TPU 95A HF into

the right hotend.

CAUTION

Certain types of flexible filament (TPU) can only be printed with the right hotend.

Step 3. Choose the appropriate chamber temperature mode based on the model.

Model Type

Recom-

Key Operation Tips

mended Air

Condition

Mode

TPU as Base Layer or

Cooling

Keep the TPU bed temperature stable; set the

Main Structure

Mode

engineering filament bed temperature lower

than 70 °C

Engineering material as

Heating

TPU must use an external spool, and it is rec-

base, for strength

Mode

ommended to use a dedicated hotend for TPU

printing

Step 4. Enable Interlocking Beams. In Bambu Studio's go to Prepare interface, select Others

>  >Check "Use beam interlocking" to enhance bonding between these two filament

types.

88

Bambu Lab H2C 3D Printing User Manual

Chapter 6 Key Features Introduction

Step 5. Set slicing parameters or download preset profiles according to the chosen air condi-

tioning mode.

TIPS

Please visit the wiki (wiki.bambulab.com/home) to obtain preset slicing profiles and

parameter setup methods, search for the Soft and Hard Filament Multi-Material

Printing Guide.

Step 6. Preparation before printing. If selecting cooling mode, remove the top cover glass to

prevent the chamber temperature from rising.

CAUTION

Except when using the textured PEI build plate, always apply a full layer of glue-

stick to non-textured print sheets to avoid damage.

Step 7. After printing is complete, wait until the chamber temperature drops below 45 °C before

unloading the filament.

TIPS

If the model adheres too tightly to the build plate, apply alcohol at the junction be-

tween the model and the build plate, then gently remove the model.

6.3 Large Volume Printing

This printer supports large volume printing, enabling the completion of large models or entire

structures in a single print without segmenting, improving both efficiency and final pa strength.

The large printing volume expands possibilities for applications such as prototyping, functional

89

Bambu Lab H2C 3D Printing User Manual

Chapter 6 Key Features Introduction

pas, artwork, and architectural models, offering greater design freedom while minimizing post-

assembly work and cumulative errors.

6.3.1 Horizontal Printing Area

The printer's total horizontal print area is 330×320 mm². The left hotend's print area is 325×320

mm², and the right hotend's print area is 305×320 mm². Using the lower-left corner of the build

plate's printable area as the coordinate origin (0, 0), the specific print ranges for the two hotends

are as follows:

• Left hotend: printable area coordinates from (0, 0) to (325, 320)

• Right hotend: printable area coordinates from (25, 0) to (330, 320)

• Shared printable area for both hotends: coordinates from (25, 0) to (325, 320)

Left hotend's printable area

Right hotend's printable area

On both sides of the build plate preview interface in Bambu Studio, there are light gray areas. The

left side is labeled “Left hotend only area.” The right side's “Right hotend only area” is not labeled

due to its smaller size. This means that when the model is placed within this light gray area, print-

ing is allowed only with the left hotend or right hotend, respectively.

90

Bambu Lab H2C 3D Printing User Manual

Chapter 6 Key Features Introduction

1. Left hotend only area

2. Right hotend only area

6.3.2 Vertical Printing Area

The printer's maximum overall print height is 325 mm, but the maximum printable heights differ

between the left and right hotends. The details are as follows:

• Left hotend: Maximum print height 320 mm

• Right hotend: Maximum print height 325 mm

When the model is placed within the “Left hotend only area,” its maximum height must be ≤ 320

mm and must not exceed the left hotend's maximum print height.

If the model height exceeds 320 mm (for example, 324 mm), even if it is placed in the central

shared area covered by both hotends instead of the “Right hotend only area,” printing can only be

completed using the right hotend.

6.3.3 Check the Model Placement Area

When the model is placed in the non-printable area of either the left or right hotend, all filaments

used by the model can only be printed with the hotend that covers that specific print area.

NOTE

All filaments include the main filament set in the system, the filaments applied to specific

surface areas using the color painting function, and the filaments applied to local regions of

the model using the modifier function.

91

Bambu Lab H2C 3D Printing User Manual

Chapter 6 Key Features Introduction

If Bambu Studio detects a conflict between model placement and printable area, an error mes-

sage will be displayed. Model placement or filament assignment must be adjusted before slicing

and printing can proceed. The following are common conditions that trigger error prompts:

• Same filament cross area conflict: The same filament is used in both the "left hotend only area"

and "right hotend only area" (a single filament cannot be used across both areas simultaneous-

ly).

• Model height exceeds: The overall model height exceeds the maximum printable height of the

printer (i.e., > 325 mm).

• Manual hotend and filament position conflict: When using custom mode, manually assigned

hotends and filaments must correspond to the printer's defined printable area for each hotend;

otherwise, a position-filament-nozzle mismatch error will occur.

• Manual hotend assignment and height limit conflict: Using custom mode to manually assign

hotends to filaments where the model height exceeds the maximum printable height of the as-

signed hotend.

• Partial filament exceeds assigned hotend printable area: After color painting or modifier

functions, some filament paths extend beyond the printable area of the assigned hotend.

• Flush path extends beyond assigned hotend’s printable area: When the “Flush into Objects'

infill/support” function is enabled, slicing may generate ush paths that extend outside the as-

signed hotend’s printable area.

6.4 High Precision Printing Mode

6.4.1 Sta Calibration

Method 1: Sta calibration from the printer touchscreen

Tap

 > Calibration on the printer touchscreen to enter the calibration page, then select the de-

sired calibration routine.

92

Bambu Lab H2C 3D Printing User Manual

Chapter 6 Key Features Introduction

Method 2: Sta calibration from Bambu Handy

At the bottom of the Bambu Handy interface, select Devices, tap the icon in the top-right corner

 to enter the settings menu, then choose Calibration and select the calibration task as needed.

93

Bambu Lab H2C 3D Printing User Manual

Chapter 6 Key Features Introduction

Tap Devices

Tap Calibration

Sta Calibration

NOTE

Bambu Handy only supports initiating certain calibration tasks. If the calibration you need is

not available, please initiate it directly from the printer touchscreen.

Method 3: Sta calibration from Bambu Studio

At the top of the Bambu Studio interface, select Device, tap Calibration in the top-right corner,

and choose the calibration task as needed.

NOTE

Bambu Studio only supports initiating certain calibration tasks. If the calibration you need is

not available, please initiate it directly from the printer touchscreen.

94

Bambu Lab H2C 3D Printing User Manual

Chapter 6 Key Features Introduction

6.4.2 Print Calibration

Print Calibration automatically adjusts key printer parameters through built-in sensors, ensuring

optimal print conditions without manual intervention.

• Motor Noise Cancellation: Reduces motor noise during printing, especially during long-dura-

tion or high-speed prints. By optimizing motor motion algorithms and control strategies, noise

is reduced and print surfaces become smoother, enhancing the overall print quality.

• Vibration Compensation: Measures the printer’s mechanical resonance model to compensate

for vibrations. During printing, any detected vibrations trigger automatic toolhead adjustments

to maintain print accuracy. Reduces acceleration-related artifacts while significantly improving

print speed.

• Auto Bed Leveling: Detects the flatness of the heatbed by having the nozzle contact the build

plate, ensuring more consistent extrusion height.

• High-temperature Bed Leveling: Measures the flatness of the heatbed at 100 °C to improve

the rst-layer print quality for high-temperature filaments such as ABS, ASA, PC, and PA.

• Nozzle Offset Calibration: Measures and corrects dual-nozzle positional deviation across the

XYZ axes to ensure accurate switching and prevent misalignment. Measures the offset between

the two nozzles using the eddy current sensor in the toolhead and the nozzle offset calibration

sensor located at the back of the heatbed, enabling compensation during printing.

How to use nozzle offset calibration data?

Method 1: Enable nozzle offset calibration on the Send Print Job page in Bambu Studio.

Method 2: On the Bambu Handy Send Print Job page, enable nozzle offset calibration from Ad-

vanced Options.

95

Bambu Lab H2C 3D Printing User Manual

Chapter 6 Key Features Introduction

Bambu Studio Nozzle Offset Calibration

Bambu Handy Nozzle Offset Calibration

When is nozzle offset calibration required?

• Before the rst print on a new printer.

• After a severe collision, relocation, or disassembly and reassembly of the printer.

• After adjusting the belt tensioner.

• When print quality issues occur.

• During routine maintenance.

6.4.3 High-Precision Nozzle Offset Calibration

Used to accurately calibrate the positional differences between the dual nozzles in the XY direc-

tion, ensuring precise alignment of the printing path when switching nozzles, thereby improving

the surface quality and layer alignment.

Using AI visual recognition, it detects the actual print line positions of the two nozzles in the XY

directions, calculates the XY offset between nozzles, and obtains a high-precision nozzle position

calibration offset, which is automatically applied during printing.

Compared with standard nozzle offset calibrations, high-precision nozzle offset calibration is

based on the actual printed lines, theoretically providing higher positioning accuracy and avoiding

potential errors associated with sensor-based calibration methods.

96

Bambu Lab H2C 3D Printing User Manual

Chapter 6 Key Features Introduction

How to use high-precision nozzle offset calibration data?

Method 1: On the Send Print Job page in Bambu Studio, turn o nozzle offset calibration.

Method 2: On the Send Print Job page in Bambu Handy, turn o nozzle offset calibration from

Advanced Options.

Bambu Studio Nozzle Offset Calibration

Bambu Handy Nozzle Offset Calibration

When is nozzle offset calibration needed?

When printing with dual nozzles and visible layer misalignment occurs on your model, you can se-

lect either nozzle offset calibration or high-precision nozzle offset calibration as needed.

97

Bambu Lab H2C 3D Printing User Manual

Chapter 6 Key Features Introduction

6.4.4 Motion Accuracy Calibration

Used to improve the printer's positioning accuracy, suitable for large volume or high precision

printing scenarios. This calibration effectively reduces motion lag and distortion, enhancing model

dimensional accuracy and assembly quality.

During the calibration process, the toolhead camera scans each unique QR code square on the vi-

sion encoder to obtain the absolute position of the toolhead. The system compares the actual co-

ordinates with the software coordinates. It calculates the motion error at each point, allowing the

machine to compensate accordingly, resulting in a corrected and precise position of the toolhead.

Calibration results can be maintained for weeks, unaffected by filaments or nozzles, making the

operation simple and time-efficient. Although assembly changes or maintenance intervention will

require a new calibration procedure.

NOTE

This function is an additional feature and requires the separate purchase of the vision en-

coder.

CAUTION

Do not place the vision encoder on the heatbed when it is hot. Otherwise, the high tempera-

tures may cause the vision encoder to expand and deform, resulting in calibration errors.

98

Bambu Lab H2C 3D Printing User Manual

Chapter 6 Key Features Introduction

How to use motion accuracy calibration data?

On the printer touchscreen, tap

  > Settings >  Print Options and check Motion Accuracy En-

hancement (enabled by default). After enabled, the printer applies the motion accuracy calibra-

tion data during 3D printing, cutting, and laser engraving.

When is motion accuracy calibration needed?

• When the motion accuracy enhancement feature is enabled for the rst time on a new printer.

• After the printer experiences a severe collision, relocation, or disassembly and reassembly.

• After adjusting the belt tension.

• For routine maintenance, it is recommended to perform once eve two weeks.

6.5 Intelligent Detection

This printer is equipped with multiple intelligent detection features that automatically identify ab-

normalities during printing and promptly ale users, significantly improving print success rates.

The system accurately detects issues such as nozzle clogging, air printing, or material pile-up

through visual inspection, filament feed tracking, and torque monitoring, reducing material waste

and the risk of equipment damage. Intelligent detection operates fully automatically without user

intervention, making printing more reliable and effortless.

6.5.1 AI Print Monitoring

On the printer screen, tap

 > Settings > Print Options, then check the boxes to enable the cor-

responding AI detection features as needed, and adjust the detection sensitivity accordingly. De-

tection sensitivity can be set to High, Medium, or Low according to your requirements. For exam-

ple, to prevent frequent pauses caused by minor defects, set the detection sensitivity to Low.

Spaghetti Detection: The nozzle camera and live view camera capture images at xed inter-

vals, while an AI algorithm analyzes consecutive frames. Once filament tangling or stable filament

clumps are detected below the nozzle, this feature is triggered.

Material Pile-up Detection: The live view camera monitors the filament purge location to identify

any accumulation of waste material, preventing excessive scraps from causing toolhead collisions

or skipped steps.

Clumping Detection: The nozzle camera identifies when the nozzle is completely covered by fila-

ment. The system then issues a warning and guides the required corrective actions.

99

Bambu Lab H2C 3D Printing User Manual

Chapter 6 Key Features Introduction

Air Printing Detection: The nozzle camera monitors the distance between the nozzle and the

model as well as the extrusion status, and identifies cases of no extrusion or minimal leakage.

The following conditions may prevent proper operation of the nozzle camera’s sma detection.

Please troubleshoot accordingly:

• Confirm that the nozzle camera is correctly installed and functioning properly.

• Check that the nozzle camera lens is clean and that its light is operational to ensure clear image

capture.

• When printing high-temperature materials, if the temperature near the nozzle exceeds 85 °C,

the system will automatically pause sma detection to protect the camera.

• Ensure AI detection features are enabled in Print Options. Using third-party slicing software or

G-code intended for other printer models may cause the detection feature to malfunction.

CAUTION

AI detection relies on good lighting conditions. Please ensure the printer’s internal LED light

is turned on. By default, the printer automatically turns on the LED light when printing the

rst layer. If you manually turn o the light, the system will not turn it on automatically again.

CAUTION

Spaghetti Detection cannot completely guarantee the prevention of print failures. This fea-

ture may occasionally produce false positives. Detection performance may be reduced when

using black or dark-colored materials.

6.5.2 Build Plate Detection

On the printer touchscreen, tap

 > Settings > Print Options to enable the build plate detection

feature. The live view camera will detect the presence and type of the build plate on the heatbed.

If the actual build plate used does not match the settings in the slicer le, the system will pause

the print to prevent failure.

6.5.3 Hotend Type Detection

The hotend type can be detected using the following methods:

• On the printer touchscreen, select

 > Nozzle & Extruder, then tap Read Nozzle Info.

• Each time a print job is sent to the printer, the system automatically verifies the hotend on the

current toolhead against the hotend type specified in the sliced le.

100

Bambu Lab H2C 3D Printing User Manual

Chapter 6 Key Features Introduction

The live view camera captures images of the toolhead hotend to perform in-place and type de-

tection, displaying the results on the screen to prevent print failures caused by a mismatch be-

tween the installed hotend and the sliced le.

6.5.4 Live View Camera Calibration

After replacing or disassembling the live view camera, to ensure the accuracy of functions such as

spaghetti detection and material pile-up detection, as well as reliable Intelligent detection during

the printing process, it is necessary to perform live view camera calibration. On the printer touch-

screen, go to

 > Calibration > Live View Camera Calibration, then tap Sta to begin calibra-

tion.

NOTE

The printer is calibrated at the factory before shipment, so routine calibration of the live view

camera is generally not required during normal operation.

6.6 Air Condition System

The air conditioning system automatically adjusts the temperature and airflow inside the cham-

ber, providing the optimal printing environment for different materials. The system automatical-

ly switches between heating and cooling modes based on filament type, preventing warping of

high-temperature filaments and clogging of low-temperature ones. It also dynamically adjusts fan

speed and heating power to maintain stable temperatures, save energy, and reduce noise, ensur-

ing print quality and efficiency across various printing scenarios.

6.6.1 Select Mode

This printer automatically selects the appropriate chamber condition mode for each filament type.

You do not need to set it manually, as Bambu Studio automatically configures it during slicing

based on the filament type.

You can also switch modes from the printer screen by selecting

 > Air Condition.

Cooling Mode

Suitable for printing filaments with low heat resistance, such as PLA and TPU. When the printer is

idle or printing without chamber heating enabled, it operates in cooling mode. In this mode, the

chamber heat circulation fan remains o.

101

Bambu Lab H2C 3D Printing User Manual

Chapter 6 Key Features Introduction

Heating Mode

Suitable for printing filaments with high heat resistance, such as ABS, ASA, PC, and PA. When the

chamber temperature is set and heating begins, the system switches to Heating Mode.

In this mode, the chamber heat circulation fan turns on automatically, while the auxiliary pa cool

fan remains o.

6.6.2 Custom Chamber Temperature

You can set the chamber temperature via the printer screen, Bambu Studio, or Bambu Handy. The

system will automatically switch to heating mode.

102

Bambu Lab H2C 3D Printing User Manual

Chapter 7 Basic Controls and Functions

Chapter 7 Basic Controls and Functions

This chapter introduces the main control methods and basic functions of the printer, including

touchscreen operation, basic settings, print status monitoring, and common functions. By un-

derstanding these operations, you can quickly get started with daily use and maintenance of the

printer.

7.1 Control from Printer Touchscreen

The printer is equipped with a full-color touchscreen that displays device status and provides an

interactive control interface, allowing you to configure multiple printer settings.

7.1.1 Speed Settings

You can adjust the print speed during printing, which affects both the print time and the surface

quality of the model. Generally, increasing the speed will shorten the print time, but may result in

poorer surface quality. Reducing the speed can improve surface quality, but will require more time

to print. On the touchscreen, select

 > Speed to adjust the speed by 4 modes:

• Ludicrous: 166% of normal print speed and acceleration.

• Spo: 124% of normal print speed and acceleration.

• Standard: normal print speed and acceleration.

• Silent: 50% of normal print speed and acceleration.

You can flexibly adjust the print speed based on actual needs during printing. For example, when

encountering intricate details or overhanging structures, lowering the speed improves surface

quality and printing success rate.

103

Bambu Lab H2C 3D Printing User Manual

Chapter 7 Basic Controls and Functions

7.1.2 XYZ Axis Movement

Control the movement of the toolhead and heatbed when the printer is idle. For example, when

you need to clean or maintain the printer, you can use the touchscreen to move the toolhead and

heatbed for more space.

On the touchscreen, select

 > Motion and move the toolhead and heatbed.

• Toolhead: Tap the +X/-X and +Y/-Y buttons to move the toolhead. Tap the 1 or 10 button to

move the toolhead along the X-axis and Y-axis.

• Heatbed: Tap the 1 or 10 button to raise or lower the heatbed.

7.1.3 Nozzle and Extruder

Used to switch between left and right nozzles and set the temperature, type, material, and diam-

eter for each. You can also manually extrude or retract filament while checking filament extrusion

at the nozzle. These can be used in routine maintenance, filament replacement, nozzle cleaning,

and print preparation. On the touchscreen, select Settings

 > Nozzle & Extruder to set the noz-

zle and extruder parameters.

104

Bambu Lab H2C 3D Printing User Manual

Chapter 7 Basic Controls and Functions

1. Switch nozzle: Select the left/right nozzle to switch between the nozzles. The hotend and the

ow blocker operate in a linked mechanism: When one hotend is lowered, the ow blocker

shifts to the other hotend.

2. Set nozzle temperature: Tap to enter a value and set the temperature for the corresponding

hotend.

3. Setleft nozzle information: Tap Read Left Nozzle Info, and the printer will read the nozzle

type, material, and diameter; or tap the

 to manually set the information.

4. Extruder indicator light: When the extruder’s green light is on, it means the Hall sensor has

detected filament.

5. Control the extruder: Use the up and down buttons to extrude or retract 1 cm of filament.

CAUTION

• Clear the build plate before reading the left hotend information and do not put your

hands inside the printer during the reading process.

• The information for the right hotend nozzle is automatically read and cannot be edited

manually.

NOTE

The ow blocker is mounted on the ow blocker lever to seal the inactive nozzle to prevent

oozing. When the printer is powered on, you can select the left or right hotend on the touch-

screen to switch between the nozzles and the ow blocker; in maintenance mode (powered

o), manually toggle the ow blocker lever to switch nozzles for easier operation.

7.1.4 Hotend and Rack

105

Bambu Lab H2C 3D Printing User Manual

Chapter 7 Basic Controls and Functions

Fetches and nests the right hotend (induction hotend). Automatically reads the induction ho-

tend's type, material, diameter, and filament mapping information so that the correct hotend will

be used before printing.

On the touchscreen, select

 > Nozzle & Extruder > Hotends & Rack to manage the hotends on

the rack and toolhead.

NOTE

Because induction hotends went through factory testings, new hotends will also display the

filament color during the tests. Clearing the filament color information here is currently not

supported.

DANGER

The touchscreen displays a warning when the rack is raised, lowered, or homed. Do not put

your hand inside the printer to avoid injury.

1. Manage induction hotend on toolhead: Tap the right hotend icon > Nest to place the hotend

on the toolhead to an empty dock on the slot. If it displays Empty, tap any hotend on the rack

and select Fetch to install it on the hotend.

2. Manage induction hotend on hotend rack: Tap any hotend to Read, Fetch, or nest it. Tap the

hotend shown as Empty to Nest the toolhead's right hotend or Install to manually install a

new hotend.

3. Raise a row: Tap Row A or Row B to raise it automatically, allowing you to manually Install or

Uninstall hotends.

4. Rack rough homing: Tap the Homing icon to pre-home the rack. Before moving the toolhead

on the touchscreen, the rack will automatically home roughly to avoid collision.

106

Bambu Lab H2C 3D Printing User Manual

Chapter 7 Basic Controls and Functions

5. Hotend history information: Tap Hotends Info to view specifications, serial numbers, and

version numbers of all induction hotends previously read.

6. Read All: Tap Read All; the printer will fetch hotends on the rack, read them, and update their

information one by one.

7. Operation Guide: View detailed steps for installing Induction Hotends and refreshing hotend

information.

7.1.5 Heatbed and Chamber Temperature

On the printer touchscreen, select

 > Heatbed or

 > Chamber, then enter the desired heatbed

or chamber temperature.

7.1.6 Chamber Light Mode

Turning on the chamber light allows you to monitor the printing process and chamber in real time.

Additionally, AI detection relies on adequate lighting, so enabling the chamber light improves de-

tection accuracy.

On the touchscreen, select

 > Settings > Chamber Light Mode.

107

Bambu Lab H2C 3D Printing User Manual

Chapter 7 Basic Controls and Functions

• Manual Mode: The chamber light turns on automatically only when AI detection is required.

You can also manually turn the light on or o via the touchscreen when checking the print or

performing maintenance.

• Energy-Saving Mode: The light automatically turns o when the printer is idle and only turns

on when needed to save energy, such as during printing.

7.1.7 Status Indicator

Used to indicate the printer's health status and print job status. On the touchscreen, tap

 >  Set-

tings > Status Indicator. Then turn it on or o (see Printer and AMS Status).

7.1.8 Low Power Mode

Low power mode allows the printer to work low-carrying electrical environment. After enabled,

the printer limits the maximum power of the AC heating module (heating component for heatbed

and chamber) to approximately 860 W. This reduces the instantaneous load on home power sys-

tems, ensuring a stable and reliable printing process.

108

Bambu Lab H2C 3D Printing User Manual

Chapter 7 Basic Controls and Functions

The low power mode only limits the maximum power output. It does not reduce total power

consumption. Also, the heatbed and chamber may need more time to reach the desired tempera-

ture.

On the touchscreen, select

 > Settings > Low Power Mode to enable or disable low power

mode.

7.1.9 Sound

Enable the sound option so that the printer will emit a sound when it is turned on, when printing

begins, and when printing is complete. On the touchscreen, select

 > Settings > Sound to turn it

on or o.

7.2 Photo and Video

The printer is equipped with a 1920x1080 HD live view camera mounted at the upper left of the

printer’s front panel. This camera is primarily used for real-time monitoring, time-lapse photog-

109

Bambu Lab H2C 3D Printing User Manual

Chapter 7 Basic Controls and Functions

raphy, photo and video recording, and intelligent detection. This chapter focuses on the printer's

photo and video recording functions.

7.2.1 Video Recording

The printer is able to record the print process. This makes it easy to check the overall print status

and sees as a valuable reference for troubleshooting and after-sales support. The printer has an

USB po to connect a USB ash drive to save videos. Please insert a USB ash drive before en-

abling this feature. You can enable or disable video recording using the following methods:

Method 1: On the touchscreen, select

 > Settings > Video. Turn the function on or o or adjust

the resolution.

Method 2: In Bambu Studio, select Device > Camera >

 > Auto-record Monitoring to enable

the video recording function.

7.2.2 Photo

110

Bambu Lab H2C 3D Printing User Manual

Chapter 7 Basic Controls and Functions

You can capture photos to record the model printing process. Using the printer’s live view camera,

you can remotely monitor printer operations and easily capture photos inside the printer to record

the printing progress.

Step 1: Go to Device in Bambu Handy.

Step 2: Tap

 to sta viewing.

Step 3: Tap

 to capture a photo.

7.2.3 Timelapse

The time-lapse function automatically takes a photo after each layer is printed and combines all

photos into an accelerated video. There are two time-lapse modes:

1. Traditional mode (default): After each layer is printed, the printer takes a photo at the cur-

rent position, and the toolhead stays at the end of the layer. As a result, you can see the tool-

head moving in the video.

2. Smooth mode: After each layer is printed, the toolhead moves to the prime tower or a safe

position before taking a photo so the toolhead remains stationary in the video. This mode au-

tomatically generates a prime tower.

111

Bambu Lab H2C 3D Printing User Manual

Chapter 7 Basic Controls and Functions

In Bambu Studio, go to Prepare to select a time-lapse mode. Navigate to Process > Global >

Others >  Special Mode > Timelapse.

TIPS

If you select the smooth mode, please ensure prime tower is enabled (enabled by default).

Based on the heatbed height changing by 5 mm with each nozzle switch, the printer will take a

photo at the correct time to create a smooth video. The heatbed will not be "jumping" in the video.

How to Enable

When starting a print job, you can manually enable or disable the time-lapse function on the

touchscreen, Bambu Studio, or Bambu Handy.

• On the printer touchscreen: Tap the print preview and nd Timelapse in the bottom right of

the interface to turn it on.

• Bambu Studio: After slicing finishes, click Print plate/print all in the upper-right corner. In the

pop-up window, click Open of Timelapse.

• Bambu Handy: Go to Prepare to Print, navigate to Options > Timelapse at the bottom, and

then Enable it.

7.3 Connect to Network

This printer supports Wi-Fi and LAN-only mode. When LAN-only mode is enabled, you can fur-

ther configure parameters in the developer mode.

7.3.1 LAN Only Mode

112

Bambu Lab H2C 3D Printing User Manual

Chapter 7 Basic Controls and Functions

When enabled, the printer can only be accessed and controlled within the local area network. It

cannot be accessed remotely via the internet, nor can it use cloud features such as Bambu Handy

and print history. This mode is suitable for high demands on data security.

On the touchscreen, you can select

 > Settings > LAN Only and enable LAN-only mode.

7.3.2 Developer Mode

When enabled, the printer allows third-party software or devices to directly control and manage

print tasks and process data. This offers greater flexibility and interactivity, but may pose safety

risks.

After enabling LAN-only mode, you can enable developer mode in the following settings:

 >

Settings > LAN Only > Developer Mode (only for 3D printing).

113

Bambu Lab H2C 3D Printing User Manual

Chapter 7 Basic Controls and Functions

7.4 Connect USB Flash Drive

The printer has a USB po to connect a USB ash drive with sliced les. Then, you can sta print-

ing directly from the touchscreen. In addition, you can also save print logs, time-lapse videos, and

cache data to the USB drive.

7.4.1 Specification

1. USB 2.0 or higher (with a minimum write speed of over 10 MB/s) is required; supported le

systems are FAT32 and exFAT.

2. The printer does not limit the USB ash drive's capacity. The maximum supported capacity

depends on the le system:

File System

Operating System

Maximum Capacity

Maximum Size

Used for Formatting

for Single File

FAT32

Linux or macOS

Windows

2 TB

32 GB

exFAT

Any operating system

128 PB

4 GB

4 GB

16 EB

NOTE

• Video les can use up to 65% of the USB ash drive’s capacity, with a maximum of 500

les.

• 15% of the drive’s capacity is reserved as free space. If data on the drive (including hidden

les) exceeds 85% of capacity, recording will be disabled.

• When available space is above 15%, the printer can record normally. When the drive is

85% full, the printer will automatically delete the oldest video les to free up space.

7.4.2 Connect and Format

Step 1: Inse a compatible USB ash drive into the printer's USB po.

Step 2: Format the USB drive (if needed). On the touchscreen, tap

 > USB Storage > Format

External Storage to format the drive as FAT32 directly on the printer (suitable for USB ash dri-

ves with up to 2 TB).

114

Bambu Lab H2C 3D Printing User Manual

Chapter 7 Basic Controls and Functions

7.4.3 Ejection

To eject the USB ash drive, select

 > USB Storage > Eject to safely remove the drive and pre-

vent data corruption.

NOTE

The printer only supports one USB ash drive at the same time. You cannot connect multiple

drives via a USB hub.

7.5 Update and Restore

7.5.1 Update Firmware

The printer rmware will be continuously updated for new features. When a new rmware version

is available, you can update it using the following methods:

115

Bambu Lab H2C 3D Printing User Manual

Chapter 7 Basic Controls and Functions

Online Update

When the printer is connected via Wi-Fi, it will check for new rmware updates. You can update

the rmware online through the printer’s touchscreen.

Step 1: When new rmware is available, a prompt will appear on the touchscreen asking if you

want to update. Tap Yes and follow the instructions to complete the update.

Method 2: You can also select

 > Firmware > Update on the screen to manually update.

7.5.2 Initialization

Initialization can restore the printer to its factory settings, clearing all custom configurations and

user data. Please note that this action is irreversible. Ensure there is no important data before

proceeding.

On the touchscreen, select

 > Settings > Restore to Factory Settings to complete setup.

116

Bambu Lab H2C 3D Printing User Manual

Chapter 8 Filament

Chapter 8 Filament

8.1 Select the appropriate filament

Different 3D printing filaments have unique physical properties, making them suitable for differ-

ent applications. Choosing filaments based on printing needs helps improve print quality and final

product performance. Below is a brief introduction to several common filament types. For detailed

characteristics and parameters, please refer to the Bambu Lab Filament Guide (bambulab.com/fil-

ament-guide).

8.1.1 Filament Types by Function

Basic Materials

• PLA

The most common entry-level 3D printing material, offering good printing stability and ease of

use. It supports low-temperature printing with minimal warping and excellent detail resolution,

but has poor toughness and limited strength.

Recommended use: eve day prototyping, home printing, and low-load applications.

• PETG HF

Features good toughness, water resistance, heat resistance, and chemical resistance. However, it

is prone to moisture absorption and can be easily scratched.

Recommended use: containers, durable pas, and functional components.

Engineering Materials

• ABS

Features good heat resistance and toughness. However, it is ve prone to warping while printing.

Recommended use: mechanical housings, functional pas.

• ASA

Similar to ABS but with superior UV resistance.

Recommended use: outdoor constructions, automotive pas.

• PC

117

Bambu Lab H2C 3D Printing User Manual

Chapter 8 Filament

Offers excellent heat resistance, impact resistance, and rigidity. However, it requires strict envi-

ronmental control during printing.

Recommended use: high-strength structural pas, high-temperature applications, and mechani-

cal components.

Flexible Materials

• TPU

TPU is a highly elastic and wear-resistant material, but it prints relatively slowly. Its hardness is

defined by the Shore A scale: the lower the value, the softer the filament. For example, TPU 85A is

softer than TPU 90A. Common hardness levels include 75A, 80A, 83A, 85A, 90A, 95A, etc.

Recommended use: flexible models such as shoe sole prototypes, seals, cushions, etc.

TIPS

It is recommended to print with TPU of 80A hardness and above. Higher hardness improves

printing stability and reduces the risk of print failure.

Glass/Carbon Fiber Reinforced Materials

• -CF (Carbon ber reinforced composites)

Carbon ber is added to standard base materials (such as PLA, PETG, PA) to significantly enhance

rigidity and strength while maintaining lightweight properties.

Recommended use: load-bearing structural pas and lightweight structural designs.

• -GF (Glass ber reinforced composites)

Glass ber is added to improve the toughness and wear resistance of the material.

Recommended use: industrial mechanical pas, structural frame components.

Support Materials

Support materials are specially optimized for easy removal and good stability. They are intend-

ed only for printing support structures; using them as the main material may decrease model

strength and surface quality.

• PVA (Water-soluble support material)

A flexible, biodegradable polymer with strong moisture absorption. It absorbs water from the air

and dissolves in water. PVA is commonly used as a water-soluble support material in 3D printing.

118

Bambu Lab H2C 3D Printing User Manual

Chapter 8 Filament

Recommended use: serving as a support material when printing complex structures or models

with supports that are difficult to remove manually.

8.1.2 Filament Types by Temperature

Based on extensive real-world data from Bambu Lab official materials, filaments can be classified

as follows to ensure stable performance on the printer and to avoid softening or deformation dur-

ing printing:

• High-Temperature Filaments

These filaments need to be printed at a higher chamber temperature to achieve strong layer

adhesion and to effectively control shrinkage and other key print-quality parameters.

Common high-temperature filaments include: ABS, ASA, ASA-CF, PC, PA, PA-CF, PA-GF, PA6-CF,

PET-CF, PPS, PPS-CF, PPA-CF, PPA-GF, ABS-GF, ASA-Aero.

• Mid-Temperature Filaments

This category offers excellent temperature resistance and can achieve high-quality printing re-

sults without chamber heating.

Common mid-temperature filaments include: HIPS, PE, PP, EVA, PE-CF, PP-CF, PP-GF, PHA.

• Low-Temperature Filaments

Due to their low heat deflection temperature, these filaments may soften and deform inside the

extruder or hotend when the chamber temperature exceeds 45 °C, increasing the risk of clog-

ging. Therefore, they must not be used in a high-temperature chamber environment.

Common low-temperature filaments include: PLA, PETG, PETG-CF, TPU, TPU-AMS, PLA-CF,

PLA-AERO, PVA, BVOH, PCTG.

NOTE

Non-official filaments may have different heat deflection temperatures for the same mate-

rial type due to formula differences. It is recommended to refer to ISO 75 (under a 1.8 MPa

load) when determining material classification. If the heat deflection temperature is below 80

°C, treat the filament as low-temperature filament. Alternatively, consult the filament supplier

directly for official classification advice to ensure optimal print compatibility.

119

Bambu Lab H2C 3D Printing User Manual

Chapter 8 Filament

CAUTION

Currently, only TPU 95A HF can be co-printed with high-temperature engineering materials.

Other high and low temperature filaments must not be mixed for printing, as this may

cause extruder or nozzle clogging and damage. Bambu Studio will automatically restrict the

mixing of high and low temperature filaments during slicing.

CAUTION

High-temperature and low-temperature filaments must not be mixed for printing, as this

may cause extruder or nozzle clogging and damage. Bambu Studio will automatically restrict

the mixing of high and low temperature filaments during slicing.

When printing high-temperature and medium-temperature filaments together, mid-temper-

ature filaments may soften, increasing the risk of extruder or nozzle clogging. Carefully ad-

just the chamber temperature during printing.

8.2 Filament Compatibility and Parameter Settings

The printer features a fully enclosed structure. The left hotend is equipped with a hardened steel

0.4 mm nozzle. The right hotend uses an induction hotend, supplied with three nozzle sizes: 0.2

mm, 0.4 mm, and 0.6 mm. It supports printing with various filaments, ranging from basic mate-

rials to high-performance engineering materials. Both hotends can reach up to 350 °C, and the

heatbed can reach up to 120 °C, enabling stable printing of high-temperature filaments such as

ABS, PC, and PA-CF.

Filament

Compatible
Nozzle Sizes

Hotend
Restric-
tions

Nozzle Temp
(°C) (±10 °C)

Hardened
Steel Ho-
tend Re-
quired

AMS Com-
patible

D Be-
fore Use

PLA*

All sizes

None

190 - 240

PETG HF

All sizes

None

230 - 260

ABS

ASA

PC

All sizes

None

240 - 280

All sizes

None

240 - 280

All sizes

None

260 - 290

No

No

No

No

No

Yes

Yes

Yes

Yes

Yes

Recom-
mended

Yes

Recom-
mended

Recom-
mended

Yes

120

Bambu Lab H2C 3D Printing User Manual

Chapter 8 Filament

Filament

Compatible
Nozzle Sizes

TPU 95A HF

PLA-CF

PETG-CF

PET-CF

PAHT-CF

ABS-GF

PA6-GF

PPA-CF

PPS-CF

PVA

0.2 mm not
supported

0.2 mm not
supported

0.2 mm not
supported

0.4 mm rec-

ommended

0.2 mm not
supported

0.6 mm rec-

ommended

0.2 mm not
supported

0.6 mm rec-

ommended

0.2 mm not
supported

0.2 mm not
supported

0.6 mm rec-

ommended

0.2 mm not
supported

0.6 mm rec-

ommended

0.2 mm not
supported

0.6 mm rec-

ommended

0.2 mm not
supported

AMS Com-
patible

D Be-
fore Use

Hotend
Restric-
tions

Use right
hotend
only

Nozzle Temp
(°C) (±10 °C)

Hardened
Steel Ho-
tend Re-
quired

220 - 240

No

None

210 - 240

Yes

No

Yes

None

240 - 270

Yes

Yes

Yes

Recom-
mended

Recom-
mended

Use left
hotend
only

260 - 300

Yes

No

Yes

None

260 - 300

Yes

Yes

Yes

None

240 - 280

Yes

Yes

Recom-
mended

None

260 - 300

Yes

Yes

Yes

Use left
hotend
only

Use left
hotend
only

285 - 320

Yes

No

Yes

310 - 340

Yes

No

Yes

None

190 - 240

No

Yes

Yes

121

Bambu Lab H2C 3D Printing User Manual

Chapter 8 Filament

NOTE

The nozzle sizes listed in this table include 0.2 mm, 0.4 mm, 0.6 mm, and 0.8 mm.

NOTE

Here, PLA* refers to the standard type of PLA without carbon ber (-CF), glass ber (-GF),

or other hard particles such as metallic or inorganic non-metallic llers.

Included materials: PLA Basic, PLA Matte, PLA Tough, PLA Metal, PLA Silk, PLA Aero, and

others.

Excluded materials: PLA Wood, PLA-CF, PLA-GF, PLA Sparkle, PLA Marble, PLA Glow, and

other lled materials.

CAUTION

The right induction hotend does not support PET-CF, PPS-CF, PPA-CF. When printing with

the right hotend, the bending of the PTFE tube during homing may cause filament breakage.

During X-Axis homing, the toolhead rst moves to the rear of the heatbed, then moves left

and right to detect limits. When reaching the right limit, the PTFE tube bends more sharply,

especially noticeable for right hotend, increasing the risk of filament breakage. Therefore, it

is recommended to print such filaments using the left hotend.

CAUTION

TPU 85A is not supported on the left hotend, which increases the risk of clogging. It is cur-

rently recommended to use the right hotend only.

8.3 Filament Drying

8.3.1 Filament Drying with the Printer
You can d filament directly using the printer. The following steps walk you through the process.

Step 1. Prepare the filament drying container. You can use the original filament box or download

and print the dedicated PC drying box from MakerWorld.

Step 2. Remove any debris from the heatbed and the bottom of the printer chamber.

Step 3. On the printer screen, select

 > Toolbox > D Filament.

Step 4. Tap Prepare, the printer will automatically move the toolhead and heatbed to the desig-

nated position.

122

Bambu Lab H2C 3D Printing User Manual

Chapter 8 Filament

Step 5. Place the filament to be dried on the heatbed, then cover it with the cardboard box or PC

box.

Step 6. Select the filament type. The printer will automatically set the heatbed temperature and

drying duration.

Step 7. Tap Sta to begin the drying process.

TIPS

It is recommended to manually ip the filament halfway through drying for more even drying.

8.3.2 Filament Drying with AMS 2 Pro/AMS HT
The AMS 2 Pro and AMS HT are equipped with built-in drying modules that heat and d the fila-
ment inside the chamber. The following section details the specific operation methods.

NOTE

The maximum drying temperature supported by AMS 2 Pro is 65 °C. For materials requiring

higher drying temperatures, it is recommended to use AMS HT.

NOTE

The printer can power only one AMS 2 Pro at a time. To d multiple AMS 2 Pro units simulta-

neously, additional AMS units must be connected to dedicated power adapters.

CAUTION

Flexible and engineering materials must be dried before printing to avoid print failures or

equipment damage.

CAUTION

To prevent the filament from being deformed by the gears due to softening during drying,

the system automatically disables drying for AMS units involved in current printing or those

in an auto-refill relationship with them.

Step 1. Properly connect the printer with AMS 2 Pro/AMS HT following the quick sta guide and

complete AMS Setup (see Load Filament from AMS 2 Pro).

Step 2. Place the filament to be dried into the AMS slot, retract any loaded filament, and close

the lid.

Step 3. On the printer touchscreen, select

 >

.

123

Bambu Lab H2C 3D Printing User Manual

Chapter 8 Filament

Step 4. Choose the filament type, and the printer will automatically adjust the default drying

temperature and duration. Tap Sta to begin drying.

TIPS

If multiple AMS units are connected, you can sta drying for each device individually from

the filament page or switch between AMS units from the top-left corner of the drying page.

8.4 TPU Printing Guide

NOTE

When printing certain types of TPU, the H2C uses the same loading method as the H2D. The

following instructions are illustrated using the H2D and do not affect actual operation.

Pre-print Preparation

TPU 85A and TPU 90A are two flexible materials with different hardness levels; 85A is softer than

90A. To ensure smooth TPU printing, complete the following preparations before printing.

NOTE

To prevent filament jams, do not load flexible materials such as TPU with a hardness of 95A

or lower, or moisture-absorbed PVA and BVOH into the AMS.

• Store filaments in a storage box with desiccants to maintain ambient humidity below 20% RH.

• Thoroughly d the filament before printing. For details, please refer to Filament Drying.

124

Bambu Lab H2C 3D Printing User Manual

Chapter 8 Filament

•

•

It is strongly recommended to use the top filament rack for feeding assistance. You can down-

load the corresponding model from MakerWorld (makerworld.com) by searching for "H2D Flex-

ible Filament Top-feed Rack".

It is recommended to use a new hotend or a dedicated TPU hotend.

• Clean the textured PEI build plate. In most cases, glue is not required. If TPU adheres too

strongly, glue can be used as a release layer for easier model removal.

• Ensure key components such as the extruder, cutter, and hotend are in good condition. Clean

or replace them if necessary. For details, please refer to Replace Accessories.

Scan the QR code or click the link to watch the TPU printing video guide.

wiki.bambulab.com/h2/h2d-tpu-printing-guide

8.4.1 TPU 85A

CAUTION

• TPU 85A cannot be fed through the PTFE tube, as excessive resistance may prevent

smooth extrusion. Please feed the filament directly into the toolhead.

• TPU 85A requires a 0.6 mm hotend for printing. Please replace with a 0.6 mm hotend be-

fore printing and set the hotend diameter to 0.6 mm on the screen.

Step 1. Prepare for filament loading.

a. Press the pneumatic connector and remove the PTFE tube connected to the right

toolhead filament inlet.

b. Press the pneumatic connector and remove the PTFE tube connected to the upper

pa of the filament buer, then pull the tube out from the cable chain clip.

c. Prepare a 5 cm PTFE tube, slightly bend it, and insert it into the filament outlet of the

AMS HT/sealed box. Place the filament inside and close the top cover.

d. Adjust the height of the AMS HT/sealed box so that the filament outlet is slightly

higher than the printer body.

125

Bambu Lab H2C 3D Printing User Manual

Chapter 8 Filament

Step 2. Load the filament.

a. On the screen, select

 > Nozzle & Extruder to set the right hotend temperature to

250 °C.

b. After the hotend heats up to 250 °C, manually push the filament into the extruder,

then tap

 on the screen to extrude the filament.

NOTE

Do not tap rapidly and continuously to avoid TPU being caught in the extruder

gear and causing a clog.

Step 3. Adjust slicing parameters.

• Print temperature: 225 °C (recommended)

• Bed temperature: 30 – 35°C

• Air condition: Cooling mode

• Volume speed: Keep default

• Flow dynamics calibration: Auto or O

Step 4. Adjust model position.

Place the model toward the front center area of the build plate to reduce resistance

along the filament loading path and improve printing stability.

126

Bambu Lab H2C 3D Printing User Manual

Chapter 8 Filament

Step 5. Choose either of the following methods to unload TPU after the print is complete.

• Method 1: On the printer touchscreen, select

 > TPU Filament > Unload.

• Method 2: Manual filament unload (recommended). Heat the right hotend to 250 °C,

tap Unload, and gently pull out the filament by hand as the extruder gears rotate.

8.4.2 TPU 90A

Step 1. Prepare filament for loading.

a. Press the pneumatic connector, pull out the PTFE tube connected to the upper pa

of the filament buer, and insert it into the dedicated TPU filament inlet. Adjust the

toolhead position so that an appropriate length of PTFE tube extends from the TPU

filament inlet.

b. Press the pneumatic connector and remove the PTFE tube connected to the right

toolhead filament inlet.

c. Prepare a 5 cm PTFE tube, slightly bend it, and insert it into the filament outlet of the

AMS HT/sealed box. Then place the filament and insert it into the PTFE tube. Finally,

close the top cover.

d. Adjust the height of the AMS HT/sealed box so that its filament outlet is level with the

TPU filament inlet.

127

Bambu Lab H2C 3D Printing User Manual

Chapter 8 Filament

TIPS

If using a top rack to assist loading, please visit the Makerworld model page for de-

tailed instructions and installation guidance.

Step 2. Load the filament.

a. Pull the filament from the filament outlet of AMS HT or sealed box and manually push

it into the printer's TPU filament inlet until the filament comes out of the other end of

the PTFE tube.

b. On the printer screen, tap

 > Nozzle & Extruder, and set the right hotend tempera-

ture to 250 °C.

c. After the hotend heats up to 250 °C, manually push the filament into the extruder,

then tap

 on the screen to extrude the filament.

CAUTION

Do not tap rapidly and continuously to avoid TPU being caught in the extruder

gear and causing a clog.

d. Observe the right hotend. Once the filament is continuously extruded, reinsert the

PTFE tube into the right toolhead filament inlet.

128

Bambu Lab H2C 3D Printing User Manual

Chapter 8 Filament

Step 3. Adjust slicing parameters.

• Print temperature: 225 °C (recommended)

• Bed temperature: 30 – 35 °C

• Air condition: Cooling mode

• Volume speed: Keep default

• Flow dynamics calibration: Auto or O

Step 4. Adjust model position.

Place the model toward the front center area of the build plate to reduce resistance

along the filament loading path and improve printing stability.

Step 5. Choose either of the following methods to unload TPU after the print is complete.

• Method 1: On the printer touchscreen, select

 > TPU Filament > Unload.

• Method 2: Manual filament unload (recommended). Heat the right hotend to 250 °C,

tap Unload, and gently pull out the filament by hand as the extruder gears rotate.

8.5 High-Temperature Filament Printing Guide

The printer features an enclosed design, equipped with hotends up to 350 °C and active cham-

ber heating up to 65 °C, ensuring stable printing conditions and reducing warping risks.

Supported high-temperature filaments include ABS, ASA, PC, Nylon, and others. These filaments

offer excellent performance and durability but require specific printing conditions. The following

steps will assist you in achieving optimal printing results.

129

Bambu Lab H2C 3D Printing User Manual

Chapter 8 Filament

CAUTION

• Do not use a 0.2 mm nozzle. A 0.6 mm nozzle is recommended, followed by a 0.4 mm noz-

zle.

•

It is recommended to use a new nozzle or set the nozzle temperature to 280 °C and clean

its interior before printing to ensure it is free of clogs.

Step 1. D the filament. For detailed steps, see Filament Drying.

TIPS

Certain filaments require higher drying temperatures, which the AMS 2 Pro cannot

provide. For better drying results, it is recommended to purchase the AMS HT.

Step 2. Apply a layer of solid or liquid glue on the build plate surface.

NOTE

You can purchase official heatbed solid glue on the Bambu Lab official platform.

Step 3. Preheat the printer.

Before starting the print, set the chamber temperature to the desired value (such as 65

°C) on the printer screen, Bambu Studio, or Bambu Handy. The printer will automatically

switch to heating mode.

To heat up faster, set the heatbed temperature to 100 °C to assist in raising the chamber

temperature and simultaneously preheat the heatbed.

Step 4. Recommended model slicing settings.

• Set the layer height between 0.15 and 0.3 mm, with a maximum print speed of 100

mm/s.

• When printing multiple pas, set the print sequence to By object.

• For large models, choose the Strength preset (6 walls, 25% sparse infill density).

Step 5. After printing, allow the model to cool down to room temperature gradually within the

chamber before removal.

TIPS

If printing carbon-ber (CF) or glass-ber (GF) reinforced engineering materials, post-print

annealing is recommended. Visit the Bambu Lab Wiki (wiki.bambulab.com/home) and search

for "annealing" to nd related guidance.

130

Bambu Lab H2C 3D Printing User Manual

Chapter 9 Print Quality Issues and Solutions

Chapter 9 Print Quality Issues and Solutions

9.1 First Layer Not Sticking

Possible Causes and Solutions

1. Mismatched build plate

Ensure the build plate type matches the filament used, and select the correct build plate in

Bambu Studio.

2. Diy build plate surface

Clean the build plate surface with warm water and a neutral detergent to remove any contam-

inants without damaging the build plate coat.

3. Bed leveling not performed

On the printer screen: select

 > Calibration > Print Calibration > Auto bed Leveling/High-

temperature Bed Leveling to perform bed leveling.

In Bambu Studio, go to the device page, select Calibration > Bed Leveling to perform bed

leveling.

131

Bambu Lab H2C 3D Printing User Manual

Chapter 9 Print Quality Issues and Solutions

9.2 First Layer Too High/Too Low

Full-plate rst layer too low

Partial rst layer too low

Full-plate rst layer too high

Possible Causes

• The rst layer being too low (partial area or full-plate) may cause print failure or damage to the

nozzle or build plate.

• The rst layer being too high can result in poor adhesion, poor surface quality, or reduced

structural strength, and in severe cases, model collapse or shifting, leading to a print failure.

Solutions

• On the printer screen, go to

 > Calibration > Print Calibration, and run Auto Bed Leveling

and High-temperature Bed Leveling.

•

If the issue persists after bed leveling, visit the Bambu Lab Wiki (wiki.bambulab.com/home) and

search for "H2C First Layer" to obtain a detailed tutorial.

9.3 Poor Overhang Quality

When printing overhang structures, if the extruded filament does not cool and solidify quickly, it

tends to sag, affecting both appearance and structural integrity.

132

Bambu Lab H2C 3D Printing User Manual

Chapter 9 Print Quality Issues and Solutions

Possible Causes and Solutions

1.

Insufficient support

Check the overhang angle. If it exceeds 45°, support structures should be added.

2. Print speed too high

Reduce the printing speed appropriately or enable the Slow down for overhangs function.

3.

Insufficient cooling

Lower the nozzle temperature as appropriate, increase the fan speed for the auxiliary pa

cooling fan and the pa cooling fan, and lastly open the front door and top glass cover to help

reduce the chamber temperature.

9.4 Model Warping, Falling O, or Collapse

During printing, localized shrinkage or poor bed adhesion may cause the model to warp, detach,

or collapse. Warped areas often exhibit a noticeable horizontal bulge, caused by the nozzle being

too close to the warped surface. This results in flattening of the extruded material and subsequent

extrusion overflow.

Possible Causes and Solutions

133

Bambu Lab H2C 3D Printing User Manual

Chapter 9 Print Quality Issues and Solutions

1. Tall model with unstable center of gravity

Add supports, reduce print speed and acceleration. Lay the model at whenever possible, split

the model for printing if necessary.

2. Nozzle collision with the model

Clean the nozzle and slightly increase the nozzle temperature. Reduce print and infill speeds.

Choose sparse infill patterns like Gyroid or Concentric to avoid crossing paths.

3. High material shrinkage rate

For large prints, select filaments less prone to warping, such as PLA.

4.

Improper printing environment or settings

Raise the heatbed temperature appropriately, close the printer's front door and top glass cov-

er, reduce fan speed, lower sparse infill density, and select non-crossing infill patterns like Gy-

roid.

5.

Insufficient bed adhesion

Verify that the build plate information in Bambu Studio matches the actual build plate. Clean

the build plate and nozzle. Enable Brim and increase the brim width. Apply glue to the build

plate surface if needed to enhance bonding and raise the heatbed temperature slightly.

9.5 Filament Sticking to the Nozzle

During printing, small amounts of molten filament may stick to the nozzle surface. This can cause

local under-extrusion, rough surfaces, and—in severe cases—nozzle clog or clumping. This issue is

common with high-viscosity filaments such as PETG.

Sticky nozzle

Clean nozzle

Possible Causes and Solutions

134

Bambu Lab H2C 3D Printing User Manual

Chapter 9 Print Quality Issues and Solutions

1. Moist filament

D the filament. For detailed steps, see Filament Drying.

2. Excessive ow rate or worn nozzle

Adjust the ow rate to reduce over-extrusion, and replace the nozzle if necessary.

3. Print speed too slow or temperature too high

Match print speed with nozzle temperature: increase nozzle temperature when printing at

higher speed or higher volumetric speed; lower nozzle temperature when printing slowly.

4. Worn, loose, misaligned, or damaged nozzle wiping pa

Identify issues by visually inspecting, manually moving the wiping pa, or pushing the tool-

head against it after powering o. Repair or replace it if abnormalities are found.

5. Too many travel paths in the model

Optimize the print layout to avoid excessive travel paths between model sections.

9.6 Under-Extrusion

Under-extrusion occurs when the printer does not extrude enough filament, causing incomplete

infill or surface discontinuities. It can present as overall under-extrusion or partial under-extru-

sion.

Full-plate under-extrusion

Partial under-extrusion

Possible Causes and Solutions

1. Excessive extrusion resistance

135

Bambu Lab H2C 3D Printing User Manual

Chapter 9 Print Quality Issues and Solutions

Check whether the spool rotates freely or if the filament is tangled. Clean or replace the PTFE

tube, clean or replace the extruder gears, and unclog or replace the nozzle.

2.

Insufficient extrusion

Slightly increase the nozzle temperature or reduce the print speed. Unclog or replace the noz-

zle, and adjust the ow ratio in Bambu Studio accordingly.

3. Under-extrusion at corners

This may be due to an incorrect pressure advance value, requiring a recalibration of the ow

rate.

9.7 Stringing and Oozing

Stringing and oozing typically appear as thin filament strands or small blobs on the surface. It is

commonly caused by excessive extrusion, moist filament, or abnormal melting and ow behavior

of the filament.

Stringing model

Normal model

Possible Causes and Solutions

1. Moist filament

D the filament. For detailed steps, see Filament Drying.

2. Long travel distance with small retraction length

Increase the retraction length or speed appropriately to prevent molten filament from leaking

during travel moves.

3. Special model structure or improper placement

136

Bambu Lab H2C 3D Printing User Manual

Chapter 9 Print Quality Issues and Solutions

Reduce the spacing between models and enable Avoid crossing walls feature in Bambu Studio.

4. Nozzle temperature too high

Lower the nozzle temperature moderately to increase filament melt viscosity, making it less

"liquid" and reducing oozing.

5. Using low-density filaments (such as PLA Aero) without reducing temperature or ow

rate

Lower the print temperature appropriately and adjust the ow rate to the range of 0.5 – 0.7.

6. Worn or oversized nozzle

Ensure the actual nozzle matches the slicing settings. Check the nozzle condition and replace

it if worn.

9.8 Gloss Difference

At the same temperature, a slower print speed produces a smoother surface. At the same print

speed, a higher temperature results in a glossier surface finish. If uneven surface gloss appears

during printing, it is usually caused by differences in material melting behavior or cooling rates,

which lead to variations in ow leveling and surface roughness. This phenomenon is more notice-

able with highly reflective materials.

Possible Causes and Solutions

1. Significant differences in print speed across different areas of the model (such as over-

hang areas)

137

Bambu Lab H2C 3D Printing User Manual

Chapter 9 Print Quality Issues and Solutions

For large models, slightly reduce outer wall speed; for small models, slightly reduce overall

print speed. If necessary, disable Slow down for overhangs.

2. High print speed when using a low layer height (such as 0.08 mm)

This may cause a sh-scale effect on the model surface. Consider increasing the layer height,

lowering print speed, or raising print temperature accordingly.

9.9 Interlayer Cracking

Interlayer cracking occurs due to insufficient bonding between layers, resulting in visible cracks on

the model surface. This issue is commonly seen when printing ABS, ASA, PC, PET-CF, PA-CF, and

high-shrinkage filaments.

Possible Causes and Solutions

1. Under-extrusion leading to gaps between lines

Clean and unclog the nozzle, appropriately increase the nozzle temperature, or reduce the

print speed.

2. Weak interlayer adhesion or thin structural sections

Increase the number of model wall loops or raise the sparse infill density to enhance strength.

3. Excessive cooling

Reduce fan speed appropriately, increase the bed temperature, and close the printer's front

door and top glass cover.

138

Bambu Lab H2C 3D Printing User Manual

Chapter 9 Print Quality Issues and Solutions

9.10 Seam

In FDM 3D printing, the transition point where each layer stas and ends naturally forms a seam.

The following methods can be used to optimize the seam appearance and improve surface quali-

ty.

Optimization Methods

1. Set the number of wall loops to 3.

2. Print the model individually to avoid seam accumulation from multi-model prints.

3. Appropriately increase the nozzle temperature and reduce the outer wall speed.

4. For ring-shaped or rotationally symmetric models, t enabling Spiral vase mode.

9.11 Belt Pattern

During printing, contact between the belt and idler pulley may leave stripes on the model surface,

matching the belt tooth pitch (2 mm). This is a common occurrence when using CoreXY 3D print-

ers.

139

Bambu Lab H2C 3D Printing User Manual

Chapter 9 Print Quality Issues and Solutions

Solutions

1.

2.

Increase the outer wall print speed to 200 mm/s.

If the filament's default speed is low, t reducing the layer height or slightly increasing the

temperature and the maximum volumetric speed.

9.12 Top Layer Gaps

Due to incorrect ow ratio settings, nozzle issues, or unstable extrusion, noticeable gaps may ap-

pear on the model's top layer.

Possible Causes and Solutions

1.

Incorrect nozzle size

Verify that the nozzle diameter set in the slicing software matches the actual nozzle.

2. Extrusion blockage

Clean and maintain the extruder, PTFE tube, and nozzle.

3.

Improper ow rate (too high or too low)

140

Bambu Lab H2C 3D Printing User Manual

Chapter 9 Print Quality Issues and Solutions

Recalibrate the ow rate on the Calibration page of Bambu Studio.

141

Bambu Lab H2C 3D Printing User Manual

Chapter 10 Other Common Issues and Solutions

Chapter 10 Other Common Issues and Solutions

10.1 Printable Area Error

When Bambu Studio detects that the placement of a model conflicts with the printable area, a

warning or error message will be triggered and displayed. For more information about the print

area, see Check the Model Placement Area.

Possible Causes and Solutions

1. The model’s default filament is in the non-printable area of the corresponding nozzle.

Adjust the model position to ensure it is within the printable area of the assigned nozzle.

2. The embedded pa of a model's printed area is in the non-printable area of a certain noz-

zle.

After slicing, check the internal layer position and adjust the model so that its internal layers

are within the corresponding printable area of the corresponding nozzle.

3. Flush to object's support/infill is enabled, causing the G-code path to exceed the printable

area of a certain nozzle.

Adjust the position of the support or infill so that it is fully within the printable area of the as-

signed nozzle.

4. The support filament is in the non-printable area of the corresponding nozzle.

Adjust the model position to ensure all supports are within the printable area of the assigned

nozzle.

10.2 Nozzle Offset Calibration Failure

The causes of nozzle offset calibration failure and high-precision nozzle offset calibration failure

are different. Please troubleshoot according to the following common causes and corresponding

solutions.

Possible Causes and Solutions for Nozzle Offset Calibration Failure

1. Calibration sensor is not detected or large positioning deviation

Check for related HMS error messages displayed by the printer.

2. Non-official hotend installed

Replace with an official hotend.

142

Bambu Lab H2C 3D Printing User Manual

Chapter 10 Other Common Issues and Solutions

3. Hotend not properly installed

Check if the hotend clip is securely fastened.

Possible Causes and Solutions for High-Precision Nozzle Offset Calibration Failure

1. Poor print quality of the calibration model

Remove existing calibration prints, clean the build plate, and rerun bed leveling. Check the

nozzle for clogging or oozing, and clean or replace it if necessary.

2. Low color contrast between the two calibration filaments

Use two filaments with a higher color contrast for calibration.

3. LED lights were not enabled during calibration

Turn on both LED lights and keep them on throughout the calibration process.

4. Toolhead camera lens is diy

Clean the lens with alcohol wipes.

5. Abnormal toolhead camera installation (tilted or damaged)

Reinstall or replace the toolhead camera.

10.3 Motion Accuracy Calibration Failure

If the motion accuracy calibration fails, the printer will display an error message and disable the

motion accuracy enhancement feature.

Possible Causes and Solutions

1. Toolhead camera is diy or not functioning

Check if the toolhead camera lens is clean or has any di or smudges. If so, gently wipe with

lens tissue and also check for related HMS errors.

2.

Incorrect build plate type or vision encoder not placed correctly

Use the official vision encoder and ensure it is correctly placed on the heatbed.

3. Vision encoder pattern is diy or damaged

Wipe the top layer of the vision encoder with alcohol and inspect for obvious damage or de-

formation. If any is found, replace the vision encoder.

4. "Calibration Failed" shown after calibration completes

This indicates the post-calibration motion accuracy does not meet expectations and requires

recalibration.

143

Bambu Lab H2C 3D Printing User Manual

Chapter 10 Other Common Issues and Solutions

5. Chamber LEDs or external lights enabled during calibration, causing camera overexposure

Turn o the chamber LEDs and any external light sources, then ret the calibration.

10.4 Clogging Troubleshooting

If you experience the following issues during printing, please follow the troubleshooting steps to

diagnose the problem.

• No filament or ve little extrusion: The extruder gear rotates normally, but no filament comes

out of the nozzle, or the extruded filament is extremely thin.

• Clicking noises from the extruder: This sound occurs when the extruder servo motor slips be-

cause it cannot push filament into the hotend.

• Under-extrusion or layer gaps in the print: Layers do not bond properly, leaving visible gaps

or holes.

• Print fails immediately: The toolhead moves, but no filament is extruded from the nozzle.

Possible Causes

1. Excessive resistance inside the PTFE Tube, preventing smooth filament loading.

2. Clogging inside the extruder, including the dual extruder idlers, extruder gear, the gap be-

tween them, and the extruder filament guide.

3. Clogged nozzle or hotend throat, preventing proper melting or extrusion.

Solutions

Please see H2C Clog Inspection (wiki.bambulab.com/h2c/troubleshooting/clogging) for detailed

troubleshooting steps and solutions. Below is an oveiew of the procedures.

NOTE

The following instructions use the right hotend as an example. The left hotend uses the same

procedure; simply switch to the corresponding left-side components.

Step 1. Remove the toolhead enhanced cooling fan

Open the printer's front door and remove the top glass cover. Unplug the toolhead en-

hanced cooling fan connector, pinch the top of the fan, and lift it up to remove it.

144

Bambu Lab H2C 3D Printing User Manual

Chapter 10 Other Common Issues and Solutions

Step 2. Remove the induction hotend

On the printer touchscreen, go to

 > Motion: XYZ, tap

 to lower the heatbed, then

tap -Y to move the toolhead forward for easy access.

On the printer touchscreen, tap

 > Nozzle & Extruder, confirm the nozzle temperature

has cooled to room temperature, then press the Filament cutter lever to cut the filament.

Tap Right to move the ow blocker and expose the right hotend.

Pull the induction hotend latch to the right to unlock it, and gently remove the Voek in-

duction hotend by holding the nozzle tip and pulling diagonally.

NOTE

To remove the left hotend, rst cut the left-side filament, remove the silicone sock,

unlock the one-clip mechanism, then remove the left hotend.

145

Bambu Lab H2C 3D Printing User Manual

Chapter 10 Other Common Issues and Solutions

CAUTION

Ensure the nozzle is at room temperature before cutting filament to avoid sec-

ondary clogs.

Step 3. Manually unload the filament

Press the black outer ring and remove the PTFE Tube from the toolhead.

Push the right idler arm forcefully to the right and hold it in place, then gently pull the fil-

ament up with the other hand.

•

•

If filament can be smoothly removed, proceed to Step 4.

If you feel strong resistance, do not force it. Skip to Step 6 for extruder clog trou-

bleshooting and cleaning.

CAUTION

Forcing filament out when there is resistance may jam it in the dual extruder idlers,

making later cleaning more difficult.

Step 4. Manual extrusion

Inse a new filament into the right toolhead filament inlet and t manual extrusion.

On the printer touchscreen, tap

 > Nozzle & Extruder > Extruder, select Right, then

tap

 to extrude filament. If a prompt appears stating “Please heat the nozzle to above

170 °C”, you may select “Don't remind me”.

•

If filament extrudes smoothly, clogging may be in the nozzle. Proceed to Step 5 for

clog cleaning.

146

Bambu Lab H2C 3D Printing User Manual

Chapter 10 Other Common Issues and Solutions

•

If filament cannot be extruded or retracted, the extruder may be jammed. Skip to Step

6 for extruder clog troubleshooting and cleaning.

Step 5. Clear hotend/nozzle clogs

Pinch the induction nozzle end and place it onto the right hotend. Push the induction ho-

tend latch to the left until it cannot move further, and gently shake to confirm secure in-

stallation.

On the touchscreen home interface, go to

 > Nozzle & Extruder.

Select Right (for right hotend), then set the hotend temperature slightly above the fila-

ment's normal print temperature (such as PLA: 220 °C).

Once heated, slowly insert the unclogging pin into the nozzle and move it up and down

several times to clear the clog.

DANGER

Filament may unexpectedly eject due to internal pressure release. Always wear

heat-resistant gloves during cleaning, and keep your head and body away from the

printer chamber to avoid burns.

TIPS

For more clearing methods, refer to Nozzle/Hotend Unclogging Guide.

Step 6. Clear extruder clogs

If manual filament unloading or extrusion fails, clogs may be:

• Filament stuck in the gap between the extruder gear and the dual extruder idlers.

147

Bambu Lab H2C 3D Printing User Manual

Chapter 10 Other Common Issues and Solutions

• Filament stuck at the extruder filament guide entrance or inside the guide.

• For the right hotend, filament stuck at or inside the idler arm exit.

For the above cases, disassemble the filament cutter, extruder filament guide, and ex-

truder dual idlers as needed, then remove any stuck filament.

NOTE

Extruder cleaning is complicated. Please see H2C Clog Inspection (wiki.bambula-

b.com/h2c/troubleshooting/clogging) for detailed instructions.

10.5 Nozzle/Hotend Unclogging Guide

Hotend clogging is relatively common in FDM 3D printing and can present in the following ways.

• Under-extrusion: Insufficient filament extrusion, leading to gaps or layer breaks on the model

surface.

• No extrusion: The printer operates normally, but no filament is extruded from the nozzle.

Possible Causes

1. Heat creep softening: When printing low-temperature materials (such as PLA) in an enclosed

environment, the filament may soften before entering the hotend.

2. Abnormal filament diameter: The filament diameter is uneven or exceeds 1.75 mm, causing

jams at the hotend entrance.

3. Foreign object clogging: Extruder debris or filament fragments can enter the hotend, causing

partial or complete nozzle blockage.

4. Particle-lled filaments: Filaments containing particles (such as carbon ber–reinforced,

glow-in-the-dark, or glitter filaments) may accumulate at the nozzle tip and cause clogs.

5. Material residue from mixed filaments: When switching between filament types (such as PLA

to PC, ASA to TPU), leftover filament may not be fully purged, leading to mixing and clogging.

Solutions

There are 4 common methods for unclogging a nozzle. Choose the one that best suits your situa-

tion.

1. Manual extrusion: Heat the nozzle and manually push the filament to extrude the clogged

portion.

2. Unclogging pin cleaning: Use the unclogging pin to clear the nozzle tip.

148

Bambu Lab H2C 3D Printing User Manual

Chapter 10 Other Common Issues and Solutions

3. Cold pull: Heat the nozzle, then cool it to room temperature and quickly pull out the filament

to remove the blockage.

4. Hot Allen key cleaning: Heat the nozzle and insert an Allen key into it to clear residual fila-

ment. This is suitable for cold-end clogs.

10.5.1 Manual Extrusion

Step 1. Heat the hotend. On the printer screen, tap

  > Nozzle & Extruder, then select the left

or right hotend that needs cleaning. Set the hotend temperature slightly above the rec-

ommended printing temperature for your filament (such as set PLA to 220 °C), then tap

Confirm to sta heating.

Step 2. Manually extrude. When the temperature reaches the set value, on the printer touch-

screen navigate to

  > Nozzle & Extruder, then tap

 at the corresponding nozzle to

extrude filament and check if the nozzle extrudes properly.

If the filament cannot be extruded or does not form a continuous strand, proceed to Un-

clogging Pin Cleaning (see step 2).

TIPS

When using TPU, tap the load button no more than three times. Do not rapidly or

repeatedly tap the load/unload button, as this may cause clogging or filament en-

tanglement.

10.5.2 Unclogging Pin Cleaning

CAUTION

This method does not apply to nozzles smaller than 0.4 mm.

149

Bambu Lab H2C 3D Printing User Manual

Chapter 10 Other Common Issues and Solutions

Step 1. Heat the hotend. On the printer screen, select

  > Nozzle & Extruder, then choose the

left or right hotend that needs cleaning. Set the hotend temperature slightly above the

recommended printing temperature for your filament (such as set PLA to 220 °C), then

tap Confirm to sta heating.

Step 2. Once the hotend reaches the set temperature, insert the unclogging pin into the nozzle

and move it up and down several times.

DANGER

Sudden pressure release inside the nozzle may cause the hot filament to eject un-

expectedly. Always wear protective gloves during this process, and keep your hands

and body away from the hotend assembly.

10.5.3 Cold Pull

"Cold pull" is a 3D printer maintenance technique used to remove debris, clogs, or residual fila-

ment from inside the nozzle.

On the printer screen, go to

  > Toolbox > Nozzle Cold Pull Maintenance, then follow the on-

screen instructions to complete the process.

150

Bambu Lab H2C 3D Printing User Manual

Chapter 10 Other Common Issues and Solutions

You will be guided through the following steps:

Step 1. Select the hotend and filament that need cleaning.

Step 2. Remove the PTFE tube from the toolhead.

Step 3.

Inse the previously used filament. The printer will automatically heat the nozzle, purge

residual filament, and cool it to the proper temperature.

Step 4. Remove the filament and reinstall the PTFE tube.

10.5.4 Hot Allen Key Cleaning (Left Hotend)

CAUTION

This method only applies to Allen key H1.5.

DANGER

Wear protective gloves while operating to prevent burns from dripping or molten filament.

Step 1. On the printer touchscreen, tap

 > Nozzle & Extruder > Extruder, select Left, then re-

move the silicone sock, unlock the nozzle clip, and remove the left hotend.

Step 2. Use pliers to hold the Allen key securely and heat it for approximately 10 seconds.

151

Bambu Lab H2C 3D Printing User Manual

Chapter 10 Other Common Issues and Solutions

Step 3. While the tip of the Allen key is still hot, quickly insert it into the hotend through the

heatsink, pushing until it passes through the filament inside. Then wait about 30 seconds

for the Allen key to cool slightly.

Step 4. Now the Allen key is in the hotend, surrounded by filament. Use a standard gas lighter to

heat the nozzle tip for about 20 seconds.

DANGER

• Do not overheat the nozzle or use high-power butane torches. Only use a stan-

dard gas lighter.

• The nozzle tip just needs to be hot enough that you can remove the Allen key

along with the filament inside.

• Overheating the nozzle may cause filament to drip or splatter. Always keep the

nozzle tip pointed away from yourself.

152

Bambu Lab H2C 3D Printing User Manual

Chapter 10 Other Common Issues and Solutions

Step 5. After heating, gently pull out the Allen key. The filament and clog material should come

out in one piece with the key.

Step 6. Once finished, reinstall the hotend.

10.5.5 Hot Allen Key Cleaning (Right Hotend/Induction Ho-
tend)

DANGER

Always wear protective gloves while operating to prevent burns from dripping or molten fila-

ment.

CAUTION

This method only applies to Allen key H1.5.

153

Bambu Lab H2C 3D Printing User Manual

Chapter 10 Other Common Issues and Solutions

CAUTION

Avoid exposing the induction hotend magnet to high temperatures, strong magnetic elds,

or severe impacts, as this may cause demagnetization and affect proper function.

Step 1. On the printer touchscreen, select

 > Nozzle & Extruder > Extruder. Choose Right and

set the right hotend temperature slightly above the filament’s normal print temperature

(such as 220 °C for PLA).

Step 2. Then, on the printer touchscreen, select Hotends & Rack. Tap the induction hotend on

the toolhead, then choose Nest. The printer will automatically nest the right hotend into

an available dock on the induction hotend rack.

DANGER

If the Nest operation is not performed from the printer screen, the induction ho-

tend must be removed by gripping the nozzle tip. Since the nozzle has already been

heated in Step 1, this poses a severe burn risk. Do not use this method.

Step 3. On the printer touchscreen, tap

 > Motion: XYZ. Move the toolhead to a suitable posi-

tion to enable easy removal of the induction hotend.

Step 4. Remove the induction hotend from its corresponding dock. Hold only the heatsink sec-

tion and avoid touching the nozzle tip.

DANGER

Do not touch the nozzle tip of a heated induction hotend to avoid burns.

Step 5. Use pliers to hold the Allen key securely and heat it for approximately 10 seconds.

Step 6. While the Allen key tip is still hot, quickly insert it vertically through the top of the

heatsink into the hotend, pushing it into the clogged filament as shown below. Then wait

154

Bambu Lab H2C 3D Printing User Manual

Chapter 10 Other Common Issues and Solutions

about 30 seconds for the Allen key to cool slightly and grip firmly onto the surrounding

filament.

Step 7. After cooling, slowly and steadily pull the Allen key out. The clogged filament should be

extracted with the key, clearing the blockage inside the nozzle.

155

Bambu Lab H2C 3D Printing User Manual

Chapter 11 Regular Maintenance

Chapter 11 Regular Maintenance

11.1 Maintenance Frequency and Operation Require-
ments

The printer evaluates the pollution level based on task type and duration, provides targeted

cleaning and maintenance reminders. This feature requires the rmware to be upgraded to the

latest version. It is recommended to update the rmware before rst use to enable cleaning re-

minders.

If the printer is only used for 3D printing, the cleaning and maintenance frequencies should be the

following:

Component

Type

Frequency

Operating Steps

The printer

Printer system

Calibration

After trans-
port or main-
tenance

Perform print calibration

Exterior surface

Active cham-
ber exhaust

Chamber ex-
haust fan

Air filter

Flame sensor

Auxiliary pa
cooling fan

Live view camera

BirdsEye camera

(laser version only)

Left and right
inner lining

Rack unit

Induction hotend
dock assembly

External area

Interior
surface

Induction
hotend rack

Clean

3 months

Wipe with a non-
woven cloth damp-
ened with alcohol.

Clean

3 months

Wipe with a non-
woven cloth damp-
ened with alcohol.

Clean

1 month

Wipe with a non-
woven cloth damp-
ened with alcohol.

Wipe with a non-woven
cloth dampened with al-
cohol, then apply lubri-
cant oil after cleaning.

Linear rods

Clean and
lubricate

156

Bambu Lab H2C 3D Printing User Manual

Chapter 11 Regular Maintenance

Component

Type

Frequency

Operating Steps

X-axis linear rails

Y-axis linear rods

Z-axis linear rods
and lead screws

XYZ axes

Clean and
lubricate

1 month

Nozzle lifting rail

Clean and
Lubricate

1 month

Toolhead

Toolhead camera

Nozzle camera

Clean

3 months

Left and right
hot end nozzles

Clean

When Con-
taminated

Wipe with a non-woven
cloth dampened with al-
cohol, then apply lubri-
cant oil after cleaning.

Wipe with a non-woven
cloth dampened with alco-
hol, then apply lubricant
grease to the lead screws
and lubricant oil to the
linear rods after cleaning

Use a non-woven cloth
dampened with alcohol
to wipe, then apply lu-
bricant after cleaning

Wipe with a non-
woven cloth damp-
ened with alcohol.

Increase the nozzle tem-
perature, then wipe it with
the nozzle cleaning sponge
dampened with water.

NOTE

Some images below may use other H2 series models for demonstration; this does not affect

actual operation.

CAUTION

For sustained printing with high-temperature or engineering materials, it is recommended to

increase maintenance frequency to once per month.

CAUTION

• Before starting a laser task, remove all induction hotends from the hotend rack to prevent

dust or debris from attaching during processing.

• After frequent use of the laser module, clean and maintain the printer to ensure long-term

stable operation.

157

Bambu Lab H2C 3D Printing User Manual

Chapter 11 Regular Maintenance

DANGER

Ensure regular cleaning and maintenance of the printer as required, failure to do so may

cause equipment damage and safety risks.

11.2 Print Calibration

To ensure printing accuracy and stable operation, perform a full calibration after moving the

printer or maintaining key components such as the XYZ axes and toolhead.

On the printer screen, tap

 > Calibration > Print Calibration, then select the calibration task as

needed.

NOTE

You can also sta print calibration tasks via Bambu Handy and Bambu Studio. See Initiate

Calibration.

11.3 Clean the exterior and interior surfaces

11.3.1 Printer Exterior

Prepare alcohol and a non-woven cloth.

Use a non-woven cloth dampened with alcohol to wipe the exterior surfaces, touchscreen, auto-
matic top vent, and other areas.

11.3.2 Printer Interior

Tools: Non-woven cloth, alcohol.

Step 1. Open the front door. Use a non-woven cloth dampened with alcohol to wipe the frame

and the inner surface of the front door.

Step 2. Wipe the auxiliary pa cooling fan on the left side.

158

Bambu Lab H2C 3D Printing User Manual

Chapter 11 Regular Maintenance

Step 3. Wipe the surface of the left and right inner linings and the upper side of the inner lining,

and at the same time wipe the purge wiper to clean up any remaining filament.

Step 4. Wipe the four ame sensors located at the four corners inside the printer and the LED

strips on both sides.

159

Bambu Lab H2C 3D Printing User Manual

Chapter 11 Regular Maintenance

11.4 Clean the Chamber Exhaust Grille and Fan

Tools: Non-woven cloth, alcohol, dust brush.

Step 1. Remove the chamber exhaust. Use the dust brush to sweep o surface dust, then wipe

with a non-woven cloth dampened with alcohol. If the grille is heavily soiled, rinse it with

water and clean it with a brush.

Pull the grille outward

Rotate 90° clock-

Lift the latch up-

wise to remove

ward to remove it

Step 2. Use the dust brush to clear dust from the outside of the chamber exhaust fan.

Step 3.

Install the exhaust grille back into the printer from bottom to top.

160

Bambu Lab H2C 3D Printing User Manual

Chapter 11 Regular Maintenance

Inse the left latch into the slot

Snap the right position-

ing block into the slot

CAUTION

If you rinse the exhaust grille with water, d it thoroughly before reinstalling. Moisture can

affect the normal operation of other electronic components.

11.5 Clean the Air Filter

Tools: Non-woven cloth, alcohol, dust brush, new activated carbon filter.

Step 1. Hold the top of the air filter cover and pull outward to remove it.

161

Bambu Lab H2C 3D Printing User Manual

Chapter 11 Regular Maintenance

CAUTION

If there's too much dust on the surface, place a piece of paper under the filter to

prevent dust from falling into the printer.

Step 2. Use the dust brush to remove dust from both sides of the filter cover, then wipe with a

non-woven cloth dampened with alcohol. If the filter cover is heavily soiled, rinse it with

water and clean it with a brush.

CAUTION

If you rinse the filter cover with water, d it thoroughly before reinstalling. Moisture

can affect the normal operation of other electronic components.

Step 3.

If the filter surface shows obvious stains, blockage, or saturation, replace it with a new

activated carbon filter. Hold the filter handle and pull outward to remove the old filter.

11.6 Clean and Lubricate the XYZ Axes

11.6.1 X-Axis Linear Rails

Tools: Non-woven cloth, alcohol, lubricant oil.

Step 1. Use a non-woven cloth dampened with alcohol to wipe the X-axis linear rails and belts.

Step 2. Manually move the toolhead to the other side and clean the remaining areas.

Step 3. Apply lubricant oil to the upper and lower sides of the linear rails. Move the toolhead left

and right 4 – 6 times to spread it evenly.

162

Bambu Lab H2C 3D Printing User Manual

Chapter 11 Regular Maintenance

Lubricate the upper side

of the X-axis linear rail

Lubricate the lower side

of the X-axis linear rail

11.6.2 Y-Axis Linear Rods

Tools: Non-woven cloth, alcohol, lubricant oil.

Step 1. Use a non-woven cloth dampened with alcohol to wipe the Y-axis linear rods on both

sides.

Step 2. Manually move the toolhead to clean the remaining areas.

Step 3. Apply lubricant oil to the rods, then move the toolhead back and foh 4 – 6 times to

spread it evenly.

Wipe the left Y-axis rod

Lubricate the left Y-axis rod

11.6.3 Z-Axis Linear Rods and Lead Screws

Tools: Non-woven cloth, alcohol, lubricant oil.

The Z-axis consists of lead screws and linear rods arranged in three groups located at the left

front, right front, and center rear of the printer.

163

Bambu Lab H2C 3D Printing User Manual

Chapter 11 Regular Maintenance

NOTE

When cleaning, slightly raise the heatbed to ensure the bottom of the lead screws and linear

rods are also thoroughly cleaned.

CAUTION

Use different lubricants for the linear rods and lead screws. Do not mix them up.

Step 1. Use a non-woven cloth dampened with alcohol to wipe the lead screws and linear rods.

Step 2. Apply lubricant oil on the linear rods (dashed area) and grease on the lead screws (solid

line area).

Step 3. Complete cleaning and lubrication for all three groups.

Step 4. Connect the power supply. On the printer screen, move the heatbed up and down 3 – 4

times to ensure the lubricants spread evenly.

Wipe the Z-axis lead screws and linear rods

Lubricate the Z-axis lead

screws and linear rods

11.7 Clean and Lubricate the Induction Hotend Rack

Tools: Non-woven cloth, alcohol, lubricant oil.

Step 1. Use a non-woven cloth dampened with alcohol to wipe the hotend rack body, induction

hotend dock assembly, and the four linear rods.

Step 2. Apply lubricant oil on the linear rods and slide the rack up and down to ensure the lubri-

cant spreads evenly.

Step 3. Use a tissue or non-woven cloth to remove excess lubricant oil from the rods.

164

Bambu Lab H2C 3D Printing User Manual

Chapter 11 Regular Maintenance

Wipe the induction hotend rack

Lubricate the linear rods

11.8 Toolhead

NOTE

When cleaning the internal components of the toolhead, please visit the official Wiki (wik-

i.bambulab.com/home) and search for "Dual Extruder Filament Guide Replacement Guide for

the H2C" to nd detailed disassembly and assembly instructions.

CAUTION

The bottom of the toolhead has a magnet with protective high-temperature tape. Do not re-

move this tape during cleaning.

DANGER

If you need to operate at high temperatures, please wear heat-resistant gloves to prevent

burns.

11.8.1 Clean the Hotends

Tools: Heat-resistant gloves, nozzle cleaning sponge (included in the toolbox), 3D brush handle.

NOTE

On the printer screen, tap

 > Print Files > Internal, select the brush handle model le

brush.3mf, and sta printing as prompted.

Regularly clean the left and right hotends. If clogging or damage occurs and regular cleaning

steps do not resolve the issue, see "Replace the hotend - left" and "Replace the hotend - right".

165

Bambu Lab H2C 3D Printing User Manual

Chapter 11 Regular Maintenance

Step 1. Attach the included nozzle cleaning sponge to the 3D brush handle.

Step 2. On the printer screen, tap

 > Nozzle & Extruder > Extruder, select the correspond-

ing nozzle, set the nozzle temperature ( within the melting range of the current filament),

and wait for it to heat up.

Step 3. Moisten the sponge with a small amount of water and wipe the hotend silicone sock and

sleeves, as well as surrounding areas until all di is removed.

11.8.2 Clean the Toolhead Surface

Tools: Non-woven cloth, alcohol.

Step 1. Use a non-woven cloth dampened with alcohol to wipe the pa cooling fan air duct and

the hotend silicone sock and sleeves.

Step 2. Continue wiping the extruder front cover, extruder filament guide, and both filament

cutters.

11.8.3 Clean and Lubricate the Nozzle Lifting Assembly

Tools: cotton swabs, alcohol, lubricant oil.

166

Bambu Lab H2C 3D Printing User Manual

Chapter 11 Regular Maintenance

Step 1. Remove the left hotend and the extruder filament guide assembly.

Step 2. Use a cotton swab dampened with alcohol to wipe the linear rail of the lifting assembly.

Step 3. Apply a small amount of lubricant oil on the linear rail.

Step 4. On the printer screen, tap

 > Nozzle & Extruder > Extruder, then switch the left and

right hotends 3 – 5 times to ensure the lubricant spreads evenly.

11.9 Clean the Cameras

Tools: Non-woven cloth, alcohol.

Step 1: Use a non-woven cloth dampened with alcohol to clean the toolhead camera, nozzle cam-

era, live view camera, and birdseye camera.

Clean the toolhead camera and nozzle camera

Clean the live view camera

NOTE

The H2C standard version does not include the birdseye camera by default. Only the H2CL

or H2C upgraded with the laser module kit includes the birdseye camera.

167

Bambu Lab H2C 3D Printing User Manual

Chapter 11 Regular Maintenance

CAUTION

When cleaning cameras, use a non-woven cloth dampened with a small amount of alcohol

and wring it out before wiping to prevent alcohol from seeping into the plastic cover.

11.10 Clean the Heatbed

Tools: Non-woven cloth, alcohol.

Step 1. On the printer screen, tap

 > Motion > Heatbed >

 to raise the heatbed. Clean any

leftover filament underneath.

Step 2. Spray alcohol evenly on the bottom of the printer, then wipe clean with a non-woven

cloth.

Step 3. Lower the heatbed on the printer screen, then remove the build plate. Wipe the surface

of the heatbed with a non-woven cloth dampened with a small amount of alcohol.

Step 4. Clean the rear of the heatbed, the nozzle offset calibration sensor, the nozzle steel sheet,

and the calibration sticker areas. Ensure the sensor surface is free of di or obstructions.

Step 5. After the alcohol has fully evaporated, place the build plate back properly.

CAUTION

Please check and clean the heatbed surface. Ensure no debris remains before placing the

build plate back. Otherwise, foreign objects may cause irreversible damage to the surface

during heating.

168

Bambu Lab H2C 3D Printing User Manual

Chapter 11 Regular Maintenance

11.11 Clean the Build Plate

Tools: Non-woven cloth, dish detergent, sponge (or brush).

Step 1: Use warm water and dish detergent to clean the build plate with a sponge or brush, then

wipe the build plate d with a non-woven cloth.

11.12 Replace Accessories

11.12.1 Hotend - Left

Regularly clean the hotends. If clogging or damage occurs and regular cleaning steps do not re-

solve the issue, follow the steps below to replace the hotend.

DANGER

Before replacing the hotend, ensure the nozzle temperature has cooled down to room tem-

perature to prevent burns.

Step 1. On the printer screen, tap

 > Motion > heatbed >

 to lower the heatbed to the bot-

tom.

Step 2. On the printer screen, tap

 > Nozzle & Extruder > Extruder, then tap Left to move the

ow blocker to the other side for easier removal.

CAUTION

Do not directly p the ow blocker with your hands. The ow blocker is fragile, ex-

cessive force may break it.

169

Bambu Lab H2C 3D Printing User Manual

Chapter 11 Regular Maintenance

Step 3. Turn o the printer, ensure that the nozzle has cooled down to room temperature, and

remove the printer's top glass cover.

Step 4. Pinch the two corners at the top of the toolhead front cover, lift upward, and remove the

toolhead front cover.

Step 5.

If filament remains inside the hotend, press down the left filament cutter lever to cut the

filament.

Step 6. Make sure the hotend to be removed is not obstructed by the ow blocker. Remove the

silicone sock, unlock the locking tab, and remove the hotend.

Step 7.

Install the new hotend, lock the locking tab (push the left latch then fasten the right clip),

t the silicone sock, then reinstall the toolhead front cover and the printer's top glass

cover.

11.12.2 Hotend - Right (Induction Hotend)

Regularly clean the induction hotend. If clogging or damage occurs and regular cleaning steps do

not resolve the issue, follow the steps below to replace the induction hotend.

DANGER

Before replacing the induction hotend, ensure the nozzle temperature has cooled down to

room temperature to prevent burns.

11.12.2.1 Auto Replacement on the Toolhead

Step 1. On the printer screen, tap

 > Nozzle & Extruder > Hotends & Rack.

Step 2. Select the hotend rack showing Empty, tap Nest, then wait for the toolhead to return

the induction hotend to the empty rack automatically.

Step 3. Select the number of the induction hotend to install, tap Fetch, then wait for the tool-

head to install automatically.

11.12.2.2 Auto Replacement on the Hotend Rack

Step 1. On the printer screen, tap

 > Nozzle & Extruder > Hotends & Rack.

Step 2. Select the number of the induction hotend to replace, then tap Uninstall. The rack will lift

automatically.

Step 3. Manually remove the induction hotend to be replaced, and put on the new one.

Step 4. On the printer screen, select the number of the new induction hotend, then tap Read to

update the hotend diameter and material information.

170

Bambu Lab H2C 3D Printing User Manual

Chapter 11 Regular Maintenance

11.12.2.3 Manual Replacement on the Toolhead

To replace the induction hotend while the printer is powered o, please follow the steps below.

Step 1. Lower the heatbed. On the printer screen, select

 > Motion, tap

 to lower the

heatbed.

Step 2. Move the ow blocker. On the printer screen, select

 > Nozzle & Extruder > Extruder.

Tap Right to move the ow blocker aside for easier removal.

Step 3. Power o the printer. Press the power switch on the back of the printer.

Step 4. Remove the toolhead front cover. Unplug the toolhead enhanced cooling fan. Hold the

top of the front cover and lift it upward to remove it.

Step 5. Remove the induction hotend. Pull the induction hotend latch to the right to unlock it.

Pinch the nozzle tip and pull the hotend diagonally to remove it.

Step 6.

Install the induction hotend. Pinch the nozzle tip and nest it onto the toolhead's right

hotend. Push the induction hotend latch to the left until it stops moving. Gently shake to

confirm it is securely installed.

171

Bambu Lab H2C 3D Printing User Manual

Chapter 11 Regular Maintenance

11.12.3 Induction Hotend Silicone Sleeve

When the induction hotend silicone sleeve is damaged, cracked, or deformed due to aging, re-

place it with a new sleeve following the steps below.

Step 1. Lift along the notch on the induction hotend silicone sleeve to remove the sleeve.

Step 2. Align the protruding pa of the silicone sleeve with the positioning groove on the hotend

and press it in.

Step 3. Firmly pull the other side of the silicone sleeve outward until it covers the nozzle. Then

slowly rotate it back and foh while pressing inward.

Step 4. Ensure the silicone sleeve ts tightly against the induction hotend. If there's any raised

pa, press continuously until it ts into the hotend groove.

172

Bambu Lab H2C 3D Printing User Manual

Chapter 11 Regular Maintenance

11.12.4 Induction Hotend Latch

Regularly check the lubrication of the induction hotend latch. When the latch is worn or damaged,

replace it following the steps below.

NOTE

To maintain the latch, the extruder filament guide assembly must be removed rst. Please

visit the official Wiki (wiki.bambulab.com/home) and search for "Dual Extruder Filament

Guide Replacement Guide for the H2C" to nd detailed disassembly and assembly instruc-

tions.

Step 1. Remove the left and right hotend assemblies and the extruder filament guide assembly.

Step 2. Pull the induction hotend latch to the right until it is removed.

Step 3. Apply lubricant oil to the slide groove of the new induction hotend latch, fully lubricating

both sides.

173

Bambu Lab H2C 3D Printing User Manual

Chapter 11 Regular Maintenance

Step 4. Face the latch top side (with two small squares) up, then insert the latch into the tool-

head slide groove.

Step 5.

Install the extruder filament guide assembly and the left and right hotends.

Step 6. Gently wiggle the right hotend to confirm that the latch securely locks the right hotend

in place.

11.12.5 Flow Blocker

Tools: H2.0 and H1.5 allen keys, ow blocker (included in the toolbox).

When the ow blocker is deformed, rst check its condition and t to manually adjust it. If it can-

not be restored, replace it with a new one. Deformation of the ow blocker directly affects its abil-

ity to accurately cover the nozzle, reducing its effectiveness and degrading print quality.

CAUTION

Ensure the nozzle temperature is at room temperature before operation to prevent burns.

174

Bambu Lab H2C 3D Printing User Manual

Chapter 11 Regular Maintenance

NOTE

The disassembly and assembly steps for the ow blocker are the same on H2 series printers.

The following uses the H2D model as an example without affecting the actual operation.

Step 1. Check the position of the ow blocker.

• Flow blocker too low: The blocker is located below the nozzle, but there is a noticeable

gap between it and the nozzle.

• Flow blocker too high: When toggling the ow blocker lever to move the blocker, it

hits the nozzle midway and cannot correctly move below the nozzle.

Step 2. Adjust the ow blocker.

•

•

If the ow blocker is too low, move the blocker lever to the middle position, then gen-

tly lift the blocker upward. Repeat as needed until it ts snugly beneath the nozzle.

If the ow blocker is too high, move the blocker lever to the middle position, then gen-

tly push the blocker downward. Repeat as needed until it can smoothly move under

the nozzle without hitting it midway.

• With prolonged use, the ow blocker may become worn or damaged. If manual ad-

justments are insufficient to repair it, proceed to Step 3 to replace the ow blocker.

Step 3. Move the ow blocker lever to the middle position, remove screw A (M2.5×8×3), and re-

move the ow blocker assembly.

Step 4. Use an allen key to remove screw A (M2.5×8×3), then remove screw B (M1.6×2) to re-

move the ow blocker.

175

Bambu Lab H2C 3D Printing User Manual

Chapter 11 Regular Maintenance

Step 5. Align the screw holes of the new ow blocker with those of the base, tighten screw B

(M1.6×2), then reinstall screw A (M2.5×8×3).

Step 6. Push the screw A slightly to the right to avoid blocking the blocker path, then tighten the

screw. Manually move the ow blocker lever to confirm that it can properly cover both

nozzles.

11.12.6 Filament Cutter Blade

Tools: H2.0 allen key, new filament cutter blade (included in the toolbox).

NOTE

The disassembly and assembly steps for the filament cutter blade are the same on H2 series

printers. The following uses the H2D model as an example without affecting the actual oper-

ation.

176

Bambu Lab H2C 3D Printing User Manual

Chapter 11 Regular Maintenance

CAUTION

Before replacing the left filament cutter, tap

 > Nozzle & Extruder > Extruder on the

printer touchscreen to switch to the left nozzle.

DANGER

The blade edge is sharp and poses a risk of cuts while being handled. Please operate with

caution.

Regularly inspect the blade for wear. Replace it if the blade becomes dull or chipped. The replace-

ment steps for the left and right filament cutters are basically the same. The following instructions

use the right filament cutter as an example:

Step 1. Use an H2.0 allen key to remove the fixing screw for the right cutter. Remove the cutter

and torsion spring from the extruder together.

Step 2. Remove the filament cutter slot and replace it with a new blade. Install the filament cut-

ter slot back into the cutter lever with the notch facing upwards.

Step 3. Place the torsion spring over the cylinder and insert one end of the spring into the small

hole.

177

Bambu Lab H2C 3D Printing User Manual

Chapter 11 Regular Maintenance

Step 4.

Inse the right cutter lever and blade together into the extruder slot. Hold the cutter

lever to prevent it from loosening, and tighten the screw using the H2.0 hex wrench. En-

sure that the cutter lever won't spring open.

11.12.7 PTFE Tube

Tools: White PTFE tube (610 mm), black PTFE tube (590 mm).

The PTFE tubes inside the printer connect the filament buer and the toolhead, delivering fila-

ment from the buer to the toolhead. Regularly check the condition of the PTFE tubes inside the

printer. If wear occurs, replace them by following the steps below.

178

Bambu Lab H2C 3D Printing User Manual

Chapter 11 Regular Maintenance

NOTE

The disassembly and assembly steps for the PTFE tubes are the same on H2 series printers.

The following uses the H2D model as an example without affecting the actual operation.

Step 1. Turn o the printer and disconnect the power cord. Press the black outer rings of the

pneumatic connectors (at the PTFE tube couplers on the rear of the printer) and unplug

the external PTFE tubes.

Step 2. Press the black outer rings of the pneumatic connectors (at the toolhead filament inlets),

then unplug the PTFE tubes.

Step 3. Push the yellow sliders to the right. Press the black outer rings of the pneumatic connec-

tors (at the upper and lower ends of the filament buer), then unplug both PTFE tubes.

Step 4. Pass two new PTFE tubes through the hole on the side of the cable chain clip, then insert

them into the two pneumatic connectors of the filament buer.

179

Bambu Lab H2C 3D Printing User Manual

Chapter 11 Regular Maintenance

Step 5. Finally, insert the other ends of the PTFE tubes into the toolhead filament inlets.

11.12.8 Nozzle Wiping Pad

Tool: Nozzle wiping pad (included in toolbox).

The nozzle wiping pad is installed on the purge wiper and is used to remove residual waste on the

nozzle. It is made of soft silicone material to ensure good contact with the nozzle during wiping.

Replace the nozzle wiping pad by following these steps if it is damaged or detached.

NOTE

The disassembly and assembly steps for the nozzle wiping pad are the same on H2 series

printers. The following uses the H2D model as an example without affecting the actual oper-

ation.

Step 1. Remove the old nozzle wiping pad from the purge wiper.

180

Bambu Lab H2C 3D Printing User Manual

Chapter 11 Regular Maintenance

Step 2.

Install the new nozzle wiping pad in the correct orientation. Ensure both rubber clips

face inward and the at surface faces outward. Align the two clips of the nozzle wiping

pad with the grooves on the purge wiper, then press down to snap it into place.

11.12.9 4-in-1 PTFE Adapter II

When the PTFE tubes connected to the 4-in-1 PTFE adapter II are worn, cannot be locked proper-

ly, or when the adapter is damaged, replace it following the steps below.

Step 1. Press the black outer rings on the 4-in-1 PTFE adapter II and pull out the PTFE tubes to

remove the adapter.

181

Bambu Lab H2C 3D Printing User Manual

Chapter 11 Regular Maintenance

Step 2. Connect the PTFE tubes to the new 4-in-1 PTFE adapter II to complete the installation.

Step 3. After installation, gently pull the PTFE tube to confirm it is properly locked. Ensure the

adapter is connected in the correct direction and that the filament loads smoothly with-

out jamming or blockage.

NOTE

The inlet side (four holes) can connect to AMS units or external filament spools.

The outlet side (one hole) must connect to the printer.

11.12.10 Filament Cleaning Pad

Tools: Tweezer, non-woven cloth, alcohol, new filament cleaning pad (included in toolbox).

The main function of the filament cleaning pad is to block filament debris on the pad side, pre-

venting debris from entering the toolhead and causing clogs. Regularly clean the filament clean-

ing pad following the steps below. Replace the pad if there's significant wear.

182

Bambu Lab H2C 3D Printing User Manual

Chapter 11 Regular Maintenance

Step 1. Press the black outer rings on the 4-in-1 PTFE adapter II and pull out the PTFE tubes to

remove the adapter.

Step 2. Use tweezer to grip the filament cleaning scraper and lift it out.

Step 3. Wipe o the di on the cleaning pad using a non-woven cloth dampened with alcohol.

Step 4.

If the pad shows significant wear, replace the pad with a new one. Press the cleaning pad

down with the small tab facing the outlet side of the 4-in-1 PTFE adapter II, ensure it sits

ush with the adapter body.

183

Enjoy!

The manual is subject to change without notice.
Visit the Bambu Lab website for a latest version.

bambulab.com/support/documentation

