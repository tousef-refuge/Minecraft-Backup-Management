from PySide6 import QtCore, QtWidgets

from app.logic import find_zip
from .auto_extract_confirm import AutoExtractConfirm

from pathlib import Path

class AutoExtractDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Backup Auto Extract")
        self.settings = QtCore.QSettings()

        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.main_layout)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(10)

        self._build_options()
        self._build_run_button()

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
            info_layout(self.track_numbers, "Extracted worlds will be called <name>#<num> where\n<num> is increased by 1 everytime the world is restored")
        )

        self.scan_save = QtWidgets.QCheckBox()
        frame_layout.addRow(
            "Scan Save Folder:",
            info_layout(self.scan_save, "On top of the backups/ folder, the saves/ folder will\nadditionally be scanned")
        )

        self.main_layout.addWidget(frame)

    def _build_run_button(self):
        self.run_button = QtWidgets.QPushButton("Run")
        self.run_button.clicked.connect(self._on_run)
        self.main_layout.addWidget(self.run_button)

    def _on_run(self):
        world_name = self.world_name.text().strip()
        zip_path = find_zip(Path(self.settings.value("minecraft_dir")) / "backups", world_name)
        if self.scan_save.isChecked():
            zip_path = zip_path or find_zip(Path(self.settings.value("minecraft_dir")) / "saves", world_name)

        if zip_path:
            auto_extract_confirm = AutoExtractConfirm(zip_path, self.track_numbers.isChecked())
            auto_extract_confirm.exec()
        else:
            QtWidgets.QMessageBox.warning(
                self,
                "Error",
                "No backup with this world name has been found.\nKeep in mind the name of the folder inside the backup\nis checked, not the zip itself."
            )

def info_layout(widget, text):
    sublayout = QtWidgets.QHBoxLayout()
    info = QtWidgets.QLabel('ⓘ')
    info.setToolTip(text)
    sublayout.addWidget(widget, alignment=QtCore.Qt.AlignmentFlag.AlignRight)
    sublayout.addWidget(info, alignment=QtCore.Qt.AlignmentFlag.AlignLeft)
    return sublayout