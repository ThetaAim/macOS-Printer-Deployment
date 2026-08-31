# Pistol — Printer Installer

> **One click from a clean Mac to a ready-to-print workstation.**

Pistol is a macOS printer-deployment utility built to automate the complete printing setup in one workflow.

The original production version:

- installs all required printer drivers;
- creates and registers the printers in macOS;
- connects each printer to the correct network print-server queue;
- applies model-specific PPD and hardware settings such as trays, paper sizes, media types, paper weights, finishers, and other options;
- installs the Gespage Popup client automatically using the appropriate 32-bit or 64-bit package;
- deploys preconfigured macOS print presets for common printing workflows;
- leaves the Mac ready for printing when the process completes.

> **Portfolio Demo Notice**  
> This public repository is a non-operational demonstration of the original production tool.  
> All system-changing actions have been replaced with simulated output, and all production-specific configuration, credentials, installers, vendor packages, and environment details have been removed.

---

## Preview

![Pistol Printer Installer](images/pistol-demo.png)

---

## Workflow

```text
Launch application
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
Deploy ready-made print presets
        |
        v
Ready to print
```

The public portfolio version preserves the same workflow and project structure, but displays the actions that would be executed instead of modifying the system.

---

## How the Production Version Works

### Driver and Client Installation

The application installs the required printer drivers and Gespage Popup client as part of the same deployment process. The appropriate 32-bit or 64-bit Gespage package can be selected for the target environment.

### Printer Creation and Network Routing

Printers are created using CUPS / `lpadmin` and configured with the correct:

- printer name;
- print-server address;
- queue name;
- PPD file;
- location;
- model-specific options.

### Physical Printer Configuration

PPD settings are applied so the macOS printer definition matches the actual physical device, including trays, paper sizes, media types, paper weights, drawers, finishers, binders, and other supported hardware options.

### Ready-Made Print Presets

The production version deploys preconfigured macOS print presets for common printing workflows. These presets can include predefined paper, tray, media, quality, and finishing settings, allowing users to select ready-made configurations without rebuilding the settings for each job.

### Ready to Use

When the workflow completes, the workstation has the required drivers, printer queues, print-server routing, physical printer settings, Gespage Popup, and print presets already configured.

---

## Architecture

```text
Pistol/
├── main.py
├── Data/
│   └── Data.py
├── Scripts/
│   ├── Installer/
│   │   └── tk_installer.py
│   ├── Printers/
│   │   └── Create_printer_with_settings.py
│   └── Presets/
│       └── Copy_Prst.py
├── pkgs/
└── Tools/
    └── tools.py
```

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

## Public Demo Safety

The public version does **not** install packages, execute privileged commands, register printers, copy presets, request administrator privileges, or modify the host system.

It keeps the architecture, configuration model, GUI, and workflow visible while excluding production-specific data and operational deployment logic.
