from PySide6 import QtCore, QtWidgets

from app.windows.window_build import info_layout
from app.logic import find_zip
from .status import StatusDialog
from .config import ConfigDialog

from pathlib import Path

class Dialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Backup Auto Extract")
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
            info_layout(self.track_numbers, "Extracted worlds will be called <name>#<num> where\n<num> is increased by 1 everytime the world is restored\nThe world name you type above should NOT end\nwith #<num> otherwise the program won't detect it")
        )

        self.scan_save = QtWidgets.QCheckBox()
        frame_layout.addRow(
            "Scan Save Folder:",
            info_layout(self.scan_save, "On top of the backups/ folder, the saves/ folder will\nadditionally be scanned\nThe program will use the first correct .zip file it detects\nstarting with backups/ and then moving to saves/")
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
        world_name = self.world_name.text().strip()
        track_numbers = self.track_numbers.isChecked()

        zip_path = find_zip(Path(self.settings.value("minecraft_dir")) / "backups", world_name, track_numbers)
        if self.scan_save.isChecked():
            zip_path = zip_path or find_zip(Path(self.settings.value("minecraft_dir")) / "saves",
                                            world_name, track_numbers)

        if zip_path:
            status_dialog = StatusDialog(zip_path, track_numbers)
            status_dialog.exec()
        else:
            QtWidgets.QMessageBox.warning(
                self,
                "Error",
                "No backup with this world name has been found.\nKeep in mind the name of the folder inside the backup\nis checked, not the zip itself."
            )

    @staticmethod
    def _on_config():
        config_dialog = ConfigDialog()
        config_dialog.exec()
