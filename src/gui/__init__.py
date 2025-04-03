from os.path import exists, getmtime
from subprocess import run
from config import UI_FILE, FORM_PY_FILE

def update_ui():
    """Recompile the .ui file if it is newer than .py or if .py doesnt exists."""
    if not exists(FORM_PY_FILE) or getmtime(UI_FILE) > getmtime(FORM_PY_FILE):
        print("Updating UI...")
        run(["pyside6-uic", UI_FILE, "-o", FORM_PY_FILE], check=True)

update_ui()