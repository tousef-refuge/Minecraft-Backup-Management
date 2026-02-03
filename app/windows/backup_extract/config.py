from PySide6 import QtCore, QtWidgets

from app.windows.window_build import info_layout

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

        self.refresh_time = QtWidgets.QSpinBox()
        self.refresh_time.setMinimum(1)
        self.refresh_time.setMaximum(1000000)
        self.refresh_time.setValue(int(self.settings.value("refresh_time", 1000)))
        frame_layout.addRow(
            "Refresh Time:",
            info_layout(self.refresh_time, "The amount of time between each extraction attempt\nin milliseconds. 1 second is recommended")
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
        self.settings.setValue("refresh_time", self.refresh_time.value())
        self.close()