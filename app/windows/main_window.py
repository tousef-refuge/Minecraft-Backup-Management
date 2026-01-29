from PySide6 import QtCore, QtWidgets

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Minecraft Backup Management")
        self.settings = QtCore.QSettings()

        self.main_layout = QtWidgets.QGridLayout(self)
        self.setLayout(self.main_layout)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setVerticalSpacing(10)

        self.adjustSize()
        self.setFixedSize(self.size())
