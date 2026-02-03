from PySide6 import QtCore, QtWidgets

class ConfigDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Configuration")
        self.settings = QtCore.QSettings()