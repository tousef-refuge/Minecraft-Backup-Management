from PySide6 import QtCore, QtGui, QtWidgets
from pathlib import Path
import sys
import os
sys.path.append(str(Path(__file__).resolve().parent))

from app.logic import is_valid_mc_dir
from backup_extract import Dialog as BackupExtractDialog

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Minecraft Backup Management")
        self.settings = QtCore.QSettings()

        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.main_layout)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(10)

        self._build_title()
        self._build_dir_select()
        self._build_buttons()

        self.adjustSize()
        self.setFixedSize(self.size())

    #window builders
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

    def _build_dir_select(self):
        frame = QtWidgets.QFrame(frameShape=QtWidgets.QFrame.Shape.StyledPanel)
        frame_layout = QtWidgets.QVBoxLayout(frame)

        text = QtWidgets.QLabel("Minecraft directory")
        frame_layout.addWidget(text)

        dir_layout = QtWidgets.QHBoxLayout()

        self.dir_select = QtWidgets.QLineEdit()
        self.dir_select.setFixedWidth(300)
        self.dir_select.setReadOnly(True)

        #find the default value for the .minecraft
        #directory if a directory hasnt been chosen already

        roaming = Path(os.environ["APPDATA"])
        default = roaming / ".minecraft"
        default.mkdir(parents=True, exist_ok=True)

        prev_dir = self.settings.value("minecraft_dir", None, str)
        final_dir = str(prev_dir if prev_dir else default)
        if is_valid_mc_dir(final_dir):
            self.dir_select.setText(final_dir)
            self.settings.setValue("minecraft_dir", self.dir_select.text())

            #generate backups folder automatically since it doesnt exist normally
            backups_dir = Path(final_dir) / "backups"
            backups_dir.mkdir(parents=True, exist_ok=True)
        else:
            self.dir_select.setText("No directory selected.")
            self.settings.setValue("minecraft_dir", None)

        dir_layout.addWidget(self.dir_select)

        browse_button = QtWidgets.QPushButton("Browse...")
        browse_button.clicked.connect(self._on_browse)
        dir_layout.addWidget(browse_button)

        frame_layout.addLayout(dir_layout)
        self.main_layout.addWidget(frame)

    def _build_buttons(self):
        layout = QtWidgets.QHBoxLayout()

        backup_extract_button = QtWidgets.QPushButton("Set up backup auto-extract")
        backup_extract_button.clicked.connect(self._on_backup_extract)
        layout.addWidget(backup_extract_button)

        self.main_layout.addLayout(layout)

    #button binds
    def _on_browse(self):
        start_dir = self.dir_select.text()

        folder = QtWidgets.QFileDialog.getExistingDirectory(
            self,
            "Select .minecraft Folder",
            start_dir
        )

        #check for valid .minecraft folder
        if folder:
            if is_valid_mc_dir(folder):
                self.dir_select.setText(folder)
                self.settings.setValue("minecraft_dir", folder)
            else:
                QtWidgets.QMessageBox.warning(
                    self,
                    "Error",
                    "Invalid .minecraft folder."
                )

    def _on_backup_extract(self):
        if self.settings.value("minecraft_dir"):
            backup_extract_dialog = BackupExtractDialog()
            backup_extract_dialog.exec()
        else:
            QtWidgets.QMessageBox.warning(
                self,
                "Error",
                "Invalid .minecraft folder."
            )