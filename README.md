# Pistol — Printer Installer

> **One click from a clean Mac to a ready-to-print workstation.**

Pistol is a macOS printer-deployment utility built to automate the complete workstation printing setup in one workflow.

The original production version:

- installs all required printer drivers;
- creates and registers the printers in macOS;
- points each printer to the correct network print-server queue;
- applies model-specific PPD and hardware settings to match the physical printer configuration, including trays, paper sizes, media types, paper weights, finishers, and other options;
- installs the Gespage Popup client automatically using the appropriate 32-bit or 64-bit package;
- deploys the required print presets;
- leaves the Mac ready for printing when the process completes.

All of this is handled through a single Tkinter-based workflow with visible progress output.

> **Portfolio Demo Notice**  
> This public repository is a non-operational demonstration of the original production tool.  
> The original project performs the full deployment workflow described above.  
> In this public version, all system-changing actions have been replaced with simulated output, and all production-specific configuration, credentials, installers, vendor packages, and environment details have been removed.

---

## What It Does

The production version follows this sequence:

```text
Launch application
        |
        v
Read package and printer configuration
        |
        v
Install printer drivers
        |
        v
Install Gespage Popup (32-bit or 64-bit)
        |
        v
Create printers in macOS
        |
        v
Connect printers to print-server queues
        |
        v
Apply PPD / physical printer configuration
        |
        v
Deploy print presets
        |
        v
Ready to print
```

The public portfolio version preserves the same workflow and project structure, but displays the actions that would be executed instead of modifying the system.

---

## Architecture

```text
Pistol/
├── main.py                  # Entry point and Tkinter UI
├── Data/
│   └── Data.py              # Generic package and printer configuration
├── Scripts/
│   ├── Installer/
│   │   └── tk_installer.py  # Driver / client installation workflow
│   ├── Printers/
│   │   └── Create_printer_with_settings.py
│   │                         # CUPS / lpadmin printer configuration
│   └── Presets/
│       └── Copy_Prst.py     # Print-preset deployment workflow
├── pkgs/
│   ├── Client/
│   ├── PrinterA/
│   ├── PrinterB/
│   ├── PrinterC/
│   ├── PrinterD/
│   └── Presets/
└── Tools/
    └── tools.py             # Path-resolution utilities
```

---

## How the Production Version Works

### 1. Driver Installation

The application installs the required printer driver packages on macOS using AppleScript and administrator privileges.

The workflow is designed so the required drivers are installed as part of the same deployment process rather than manually installing each package.

### 2. Gespage Popup Installation

The production version installs the Gespage Popup client automatically.

The required package version can be selected according to the target environment, allowing deployment of either the 32-bit or 64-bit package as part of the same one-click workflow.

### 3. Printer Creation and Print-Server Routing

After the required packages are installed, the project creates each configured printer using CUPS / `lpadmin`.

For every printer, the workflow defines:

- printer display name;
- network print-server address;
- queue name;
- PPD file;
- location;
- printer-specific hardware options.

This allows the Mac to communicate with the correct print-server queue rather than requiring each printer to be configured manually.

### 4. Physical Printer Configuration

The production version applies model-specific PPD settings so the macOS printer definition matches the actual physical device.

Depending on the printer, these settings can include:

- paper trays;
- paper sizes;
- media types;
- paper weights;
- drawers;
- finishers;
- binders;
- other model-specific hardware options.

The goal is for the printer to appear correctly configured to the user immediately after deployment.

### 5. Preset Deployment

Required macOS print presets are deployed automatically so commonly used print configurations are available without additional manual setup.

### 6. Ready to Use

After the workflow completes, the Mac has:

- required printer drivers;
- configured printer queues;
- print-server routing;
- physical printer options;
- Gespage Popup;
- print presets.

The workstation is ready for printing without requiring the user to manually configure each component.

---

## Portfolio Demo Behavior

The public version demonstrates the same flow without executing privileged or system-changing commands.

It:

1. Reads generic package and printer definitions from `Data/Data.py`.
2. Displays the package installation actions that would normally be performed.
3. Builds and displays the CUPS / `lpadmin` commands for each printer.
4. Displays the printer configuration and print-server routing.
5. Displays the source and destination of preset deployment.
6. Shows the complete simulated workflow in the Tkinter interface.

---

## Generic Configuration

`Data/Data.py` contains placeholders only.

Examples include:

- `PRINT_SERVER_ADDRESS`
- Generic printer names
- Generic queue names
- Generic PPD paths
- Generic locations
- Example PPD option keys and values
- Generic local package paths

No production IP addresses, hostnames, queue names, credentials, vendor installers, organization names, or environment-specific configuration are included.

---

## Tech Stack

| Layer | Technology |
| --- | --- |
| Language | Python 3 |
| UI | Tkinter |
| macOS automation | AppleScript / `osascript` |
| Printer management | CUPS / `lpadmin` |
| Printer configuration | PPD options |
| Deployment model | Configuration-driven automation |
| Preset deployment | macOS preference files |

---

## Running the Portfolio Demo

Requirements:

- Python 3
- Tkinter
- A graphical environment

Run:

```bash
python3 main.py
```

Click **Start Installation** to view the simulated deployment workflow.

The displayed actions and commands are informational only and are never executed.

---

## Safety

This public portfolio version does **not**:

- install packages;
- execute `osascript`;
- execute `lpadmin`;
- register printers;
- copy presets;
- change ownership or permissions;
- request administrator privileges;
- modify the host system.

Files placed under `pkgs/` are ignored by Git except for placeholder `.gitkeep` files.

---

## Why This Repository Is Non-Operational

The original utility was built for a real managed macOS environment.

This public repository intentionally preserves the project structure, configuration model, GUI, workflow, and technical design while removing the operational code paths and production-specific data that would make the tool directly deployable.

Its purpose is to demonstrate the engineering approach, macOS administration knowledge, printer-deployment workflow, and automation design without distributing the complete production implementation.
