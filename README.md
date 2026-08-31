# Pistol — Printer Installer

> A one-click macOS utility that silently installs, configures, and presets an entire print fleet for end users.

> **Portfolio Demo Notice**  
> This public repository is a non-operational demonstration of the original production tool.  
> The original project performs the full printer deployment workflow described below, including package installation, printer creation, preset deployment, and privileged macOS automation.  
> In this public version, all system-changing actions have been replaced with simulated output, and all production-specific configuration, credentials, installers, and environment details have been removed.

---

## What It Does

The original Pistol project automates the full printer deployment workflow on macOS:

1. **Installs all driver packages** (`.pkg`) using AppleScript with elevated privileges.
2. **Creates and registers printers** via `lpadmin`, applying model-specific PPDs, queue definitions, and printer options.
3. **Copies print presets** directly into the user's macOS preferences, so printers are ready with the correct paper, tray, and finishing defaults out of the box.
4. Presents the full deployment process through a simple **Tkinter GUI** with visible progress output.

The public portfolio version preserves this workflow and project structure, but displays the actions that would be executed instead of modifying the system.

---

## Deployment Workflow

The production version follows this sequence:

```text
Launch application
        |
        v
Read printer and package configuration
        |
        v
Install required packages
        |
        v
Register network printers with CUPS / lpadmin
        |
        v
Apply PPD and hardware-specific options
        |
        v
Deploy macOS print presets
        |
        v
Installation complete
```

In the public demo, the same sequence is simulated and displayed in the application log.

---

## Architecture

```text
Pistol/
├── main.py                  # Entry point and Tkinter UI
├── Data/
│   └── Data.py              # Generic package and printer configuration
├── Scripts/
│   ├── Installer/
│   │   └── tk_installer.py  # Package-installation workflow
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

## How It Works

### 1. Launch

The application opens directly to the deployment interface.

In the original version, macOS requests administrator approval when privileged package installation begins.

In the public demo, no administrator privileges are requested.

### 2. Package Installation

The original application processes the required installation packages through a shared workflow using AppleScript and macOS administrator privileges.

Package execution output is written to the application log so the user can follow the deployment process.

The public demo builds and displays the commands that would normally be executed, but does not run them.

### 3. Printer Creation

After the required packages are installed, the original project creates each configured printer using CUPS / `lpadmin`.

For every printer, the workflow applies:

- A display name
- A network queue
- A print-server address
- A PPD file
- A location
- Optional model-specific settings such as trays, drawers, finishers, or other PPD options

The public demo generates and displays the equivalent commands without registering any printers.

### 4. Preset Deployment

The original project deploys macOS print preset files into the user's preferences so predefined print settings are immediately available.

The public demo displays the source and destination paths that would be used, but does not copy or modify any files.

---

## Generic Configuration

`Data/Data.py` contains placeholders only.

Examples include:

- `PRINT_SERVER_ADDRESS`
- Generic printer names
- Generic queue names
- Generic PPD paths
- Generic location values
- Example option keys and values
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
| Preset deployment | macOS preference files |
| Automation model | Configuration-driven deployment |

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

The demo displays the actions and commands that would be executed by the original production version, but does not perform any system changes.

---

## Safety

This public portfolio version does **not**:

- Install packages
- Execute `osascript`
- Execute `lpadmin`
- Register printers
- Copy presets
- Change file ownership or permissions
- Request administrator privileges
- Modify the host system

Files placed under `pkgs/` are ignored by Git except for placeholder `.gitkeep` files.

---

## Why This Repository Is Non-Operational

The original project was built for use in a real managed macOS environment.

This public repository intentionally preserves the project structure, configuration model, GUI, workflow, and technical design while removing the operational code paths and production-specific data that would make the tool directly deployable.

The goal is to demonstrate the engineering approach and macOS automation workflow without distributing the complete production implementation.
