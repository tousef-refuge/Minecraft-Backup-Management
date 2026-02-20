from PySide6 import QtCore, QtWidgets
from .config import sort_method_dict

class StatusDialog(QtWidgets.QDialog):
    def __init__(self, zip_paths, track_numbers):
        super().__init__()
        self.settings = QtCore.QSettings()
        self.zip_paths = zip_paths
        self.track_numbers = track_numbers
        self.setWindowTitle("Success")

        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.main_layout)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(10)

        self._build_labels()
        self._run()

        self.adjustSize()
        self.setFixedSize(self.size())

    def _build_labels(self):
        info_label = QtWidgets.QLabel("The respective folders will now\nbe cleaned up.")

        frame = QtWidgets.QFrame(frameShape=QtWidgets.QFrame.Shape.StyledPanel)
        frame_layout = QtWidgets.QVBoxLayout(frame)
        frame_layout.setSpacing(4)

        self.status_label = QtWidgets.QLabel("Cleaning...")
        frame_layout.addWidget(self.status_label, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)

        self.main_layout.addWidget(info_label)
        self.main_layout.addWidget(frame)

    #genuinely praying to allah i didnt delete a super important backup here lmao
    # noinspection PyTypeChecker
    def _run(self):
        sort_method = sort_method_dict[self.settings.value("sort_method", "newest")]
        self.zip_paths.sort(key=sort_method)

        for idx, zip_path in enumerate(self.zip_paths):
            if idx >= int(self.settings.value("backup_count", 1)):
                zip_path.unlink()

        self.status_label.setText("Finished cleanup")