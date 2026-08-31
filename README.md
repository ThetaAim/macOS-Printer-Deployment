# Printer Deployment Utility — Portfolio Demo

This repository is a non-operational portfolio demonstration of a macOS printer-deployment workflow. It preserves the original GUI, project structure, generic configuration model, and installation sequence while replacing every system-changing operation with visible demo output.

Running this project does not install packages, register printers, execute `osascript` or `lpadmin`, copy presets, request administrator privileges, or modify the system.

## Demonstrated Workflow

1. Read package and printer definitions from `Data/Data.py`.
2. Display the package installation commands that would be executed.
3. Build and display the CUPS commands for each configured printer.
4. Display the source and destination for print-preset deployment.
5. Complete the simulated workflow in the Tkinter log window.

## Project Structure

```text
.
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
├── Tools/
│   └── tools.py
└── pkgs/
    ├── Client/
    ├── PrinterA/
    ├── PrinterB/
    ├── PrinterC/
    ├── PrinterD/
    └── Presets/
```

## Generic Configuration

`Data/Data.py` contains placeholders only:

- `PRINT_SERVER_ADDRESS`
- `QUEUE_NAME_A` through `QUEUE_NAME_D`
- Generic printer names and PPD paths
- `LOCATION`
- Example option keys and values
- Generic local package paths

No production addresses, queues, hostnames, credentials, vendor packages, or organization-specific configuration are included.

## Running the Demo

Requirements:

- Python 3 with Tkinter
- macOS, Linux, or Windows with a graphical environment

Run:

```bash
python3 main.py
```

Click **Start Installation** to view the simulated workflow. The displayed commands are plain text and are never executed.

## Safety

The demo contains no calls that install packages, create printers, copy files, change ownership or permissions, or invoke privileged system commands. Files placed under `pkgs/` are ignored by Git except for `.gitkeep` placeholders.
