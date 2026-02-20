from PySide6 import QtCore, QtWidgets

from app.windows.window_build import info_layout

sort_method_dict = {
    "newest": lambda p: -p.stat().st_mtime,
    "oldest": lambda p: p.stat().st_mtime
}

class ConfigDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Configuration")
        self.settings = QtCore.QSettings()

        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.main_layout)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(10)

        self._build_config()
        self._build_buttons()

        self.adjustSize()
        self.setFixedSize(self.size())

    # noinspection PyTypeChecker
    def _build_config(self):
        frame = QtWidgets.QFrame(frameShape=QtWidgets.QFrame.Shape.StyledPanel)
        frame_layout = QtWidgets.QFormLayout(frame)
        frame_layout.setSpacing(4)

        self.backup_count = QtWidgets.QSpinBox()
        self.backup_count.setMinimum(1)
        self.backup_count.setMaximum(1000000)
        self.backup_count.setValue(int(self.settings.value("backup_count", 1)))
        frame_layout.addRow(
            "Backup Count:",
            info_layout(self.backup_count,
                        "The number of backups that will remain after the\ncleanup is complete")
        )

        sort_methods = sort_method_dict.keys()
        self.sort_method = QtWidgets.QComboBox()
        self.sort_method.addItems(sort_methods)
        self.sort_method.setCurrentText(self.settings.value("sort_method", "newest"))
        frame_layout.addRow(
            "Sorting Method:",
            info_layout(self.sort_method,
                        "The sorting method that will decide what backups get deleted\nFor example, setting the sorting method to 'newest' keeps the newest\nbackups and discards the rest")
        )

        self.main_layout.addWidget(frame)

    def _build_buttons(self):
        button_layout = QtWidgets.QVBoxLayout()
        button_layout.setSpacing(4)

        self.confirm_button = QtWidgets.QPushButton("Confirm")
        self.confirm_button.clicked.connect(self._on_confirm)
        button_layout.addWidget(self.confirm_button)

        self.main_layout.addLayout(button_layout)

    def _on_confirm(self):
        self.settings.setValue("backup_count", self.backup_count.value())
        self.settings.setValue("sort_method", self.sort_method.currentText())
        self.close()