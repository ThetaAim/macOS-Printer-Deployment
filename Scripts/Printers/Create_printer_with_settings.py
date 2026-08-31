def create_printer(printer_name, ip_address, queue, ppd_path, location="", **settings):
    """Return the CUPS commands that a real deployment would execute."""
    command = (
        f"lpadmin -p '{printer_name}' "
        f"-v 'sqport://{ip_address}/{queue}' "
        f"-L '{location}' "
        f"-P '{ppd_path}' "
        f"-E -o printer-is-shared=false"
    )
    commands = [command]

    for key, value in settings.items():
        commands.append(f"lpadmin -p {printer_name} -o {key}={value}")

    return commands
