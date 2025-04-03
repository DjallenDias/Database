import os.path
from os import getenv
from dotenv import load_dotenv

load_dotenv()

DB_URL = f"postgresql://{getenv("PGUSER")}:{getenv("PGPASSWORD")}@{getenv("PGHOST")}/{getenv("PGDATABASE")}?sslmode=require"

APP_NAME = "Vendas"
MAINWINDOW_SIZE = (600, 400)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UI_FILE = os.path.join(BASE_DIR, "gui", "form.ui")
FORM_PY_FILE = os.path.join(BASE_DIR, "gui", "ui_form.py")