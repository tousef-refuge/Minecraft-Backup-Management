from PySide6 import QtCore, QtWidgets

from app.windows.window_build import info_layout

class Dialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Backup Folder Cleanup")
        self.settings = QtCore.QSettings()

        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.main_layout)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(10)

        self._build_options()
        self._build_buttons()

        self.adjustSize()
        self.setFixedSize(self.size())

    def _build_options(self):
        frame = QtWidgets.QFrame(frameShape=QtWidgets.QFrame.Shape.StyledPanel)
        frame_layout = QtWidgets.QFormLayout(frame)
        frame_layout.setSpacing(4)

        self.world_name = QtWidgets.QLineEdit()
        frame_layout.addRow("World Name:", self.world_name)

        self.track_numbers = QtWidgets.QCheckBox()
        frame_layout.addRow(
            "Track World Numbers:",
            info_layout(self.track_numbers, "The program will additionally check for backups with the\nnaming scheme <name>#<num>\nThe world name you type above should NOT end\nwith #<num> otherwise the program won't detect it")
        )

        self.scan_save = QtWidgets.QCheckBox()
        frame_layout.addRow(
            "Scan Save Folder:",
            info_layout(self.scan_save, "On top of the backups/ folder, the saves/ folder will\nadditionally be scanned")
        )

        self.main_layout.addWidget(frame)

    def _build_buttons(self):
        button_layout = QtWidgets.QVBoxLayout()
        button_layout.setSpacing(4)

        self.run_button = QtWidgets.QPushButton("Run")
        self.run_button.clicked.connect(self._on_run)
        button_layout.addWidget(self.run_button)

        self.config_button = QtWidgets.QPushButton("Configure")
        self.config_button.clicked.connect(self._on_config)
        button_layout.addWidget(self.config_button)

        self.main_layout.addLayout(button_layout)

    def _on_run(self):
        pass

    def _on_config(self):
        pass