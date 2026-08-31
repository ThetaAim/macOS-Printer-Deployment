import tkinter as tk


def install_pkgs(pkgs, text_widget, event):
    """Display package installation commands without executing them."""
    if not pkgs:
        text_widget.insert(tk.END, "\n[DEMO] No packages configured.\n")
        event.set()
        return False

    for pkg_path, file_name in pkgs:
        text_widget.insert(
            tk.END,
            f"[DEMO] Would install {file_name}:\n"
            f"       installer -pkg '{pkg_path}' -target /\n",
        )

    text_widget.insert(
        tk.END,
        "[DEMO] Package installation simulation complete.\n\n",
    )
    event.set()
    return True
