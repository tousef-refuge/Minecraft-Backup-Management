from PySide6 import QtCore, QtGui, QtWidgets

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Minecraft Backup Management")
        self.settings = QtCore.QSettings()

        self.main_layout = QtWidgets.QHBoxLayout(self)
        self.setLayout(self.main_layout)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(10)

        self._build_title()

        self.adjustSize()
        self.setFixedSize(self.size())

    def _build_title(self):
        layout = QtWidgets.QHBoxLayout()
        layout.setSpacing(10)

        logo_pixmap = QtGui.QPixmap("textures/logo.svg").scaled(
            75, 75,
            QtCore.Qt.AspectRatioMode.KeepAspectRatio,
            QtCore.Qt.TransformationMode.SmoothTransformation
        )
        logo = QtWidgets.QLabel()
        logo.setPixmap(logo_pixmap)
        layout.addWidget(logo)

        title = QtWidgets.QLabel("Backup Management")
        title.setFont(QtGui.QFont("Courier", 25))
        layout.addWidget(title)

        self.main_layout.addLayout(layout)