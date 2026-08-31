from Tools.tools import to_absolute

# ─────────────────────────────────────────────────────────────
# CONFIGURATION LAYER — edit this file to adapt to your environment.
#
# packages: maps each .pkg file to its display name.
#           File names and folder names must match exactly.
#
# printer_configs: defines each printer to register via lpadmin.
#           Fields: (display_name, ip_address, queue_name, ppd_path, location, options)
#           PPD paths are relative to /Library/Printers/PPDs/Contents/Resources/
#           Options are model-specific — check your printer's PPD for valid keys.
# ─────────────────────────────────────────────────────────────

packages = [
    (to_absolute('../pkgs/Client/client.pkg'), 'Print Management Client'),
    (to_absolute('../pkgs/PrinterA/driver.pkg'), 'Printer A Driver'),
    (to_absolute('../pkgs/PrinterB/driver.pkg'), 'Printer B Driver'),
    (to_absolute('../pkgs/PrinterC/driver.pkg'), 'Printer C Driver'),
    (to_absolute('../pkgs/PrinterD/driver.pkg'), 'Printer D Driver')
]
# Replace these placeholders with values for the target environment.
print_server_address = "PRINT_SERVER_ADDRESS"

printer_configs = [
    (
        "Printer A", print_server_address, "QUEUE_NAME_A",
        "/Library/Printers/PPDs/Contents/Resources/PRINTER_A.ppd", "LOCATION",
        {"OPTION_KEY": "OPTION_VALUE"}
    ),
    (
        "Printer B", print_server_address, "QUEUE_NAME_B",
        "/Library/Printers/PPDs/Contents/Resources/PRINTER_B.ppd", "LOCATION",
        {}
    ),
    (
        "Printer C", print_server_address, "QUEUE_NAME_C",
        "/Library/Printers/PPDs/Contents/Resources/PRINTER_C.ppd", "LOCATION",
        {}
    ),
    (
        "Printer D", print_server_address, "QUEUE_NAME_D",
        "/Library/Printers/PPDs/Contents/Resources/PRINTER_D.ppd", "LOCATION",
        {}
    )
]
