from PySide6 import QtCore, QtWidgets

class AutoExtractDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Backup Auto Extract")
        self.settings = QtCore.QSettings()

        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.main_layout)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(10)

        self.adjustSize()
        self.setFixedSize(self.size())