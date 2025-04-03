from PySide6.QtWidgets import QMainWindow

from .ui_form import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.configure_connections()

    def configure_connections(self):
        pass
