from PySide6 import QtCore, QtWidgets

from app.logic import ZipExtractor, get_top_level, get_end_num, remove_end_num

from pathlib import Path

class StatusDialog(QtWidgets.QDialog):
    # noinspection PyTypeChecker
    def __init__(self, zip_path, track_numbers):
        super().__init__()
        self.settings = QtCore.QSettings()
        self.zip_path = zip_path
        self.track_numbers = track_numbers
        self.setWindowTitle("Success")

        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.main_layout)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(10)

        self._build_labels()

        self.adjustSize()
        self.setFixedSize(self.size())

        #giga magic
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.start_extract)
        self.timer.start(int(self.settings.value("refresh_time", 1000)))

        self.thread = None
        self.extractor = None
        self.is_extracting = False

        #number tracker logic thing
        world_name ,= get_top_level(self.zip_path)
        save_dir = Path(self.settings.value("minecraft_dir")) / "saves"

        #prioritize current save first if it exists
        self.world_num = get_end_num(next(
            (p.name for p in save_dir.iterdir() if p.is_dir()
             and remove_end_num(p.name) == remove_end_num(world_name)),
            ''
        ))
        #if its zero we change that
        #it also needs to actually track numbers
        if (not self.world_num) and self.track_numbers:
            self.world_num = get_end_num(world_name)

        if not self.track_numbers:
            self.world_num = 0
        else:
            self.world_num += 1 #increment by 1

    def _build_labels(self):
        info_label = QtWidgets.QLabel("The world will remain extracted for\nas long as this window is open.")

        frame = QtWidgets.QFrame(frameShape=QtWidgets.QFrame.Shape.StyledPanel)
        frame_layout = QtWidgets.QVBoxLayout(frame)
        frame_layout.setSpacing(4)

        self.status_label = QtWidgets.QLabel("Idle")
        frame_layout.addWidget(self.status_label, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)

        self.main_layout.addWidget(info_label)
        self.main_layout.addWidget(frame)

    def start_extract(self):
        if self.is_extracting:
            return
        self.is_extracting = True

        self.thread = QtCore.QThread()
        self.extractor = ZipExtractor(self.zip_path, self.world_num)
        self.extractor.moveToThread(self.thread)

        self.thread.started.connect(self.extractor.run)
        self.extractor.status.connect(self._status_connect)
        self.extractor.finished.connect(self.cleanup_extract)

        self.thread.start()

    def cleanup_extract(self):
        self.is_extracting = False

        self.thread.quit()
        self.thread.wait()

        self.extractor.deleteLater()
        self.thread.deleteLater()

    def _status_connect(self, message):
        self.status_label.setText(message)
        if message == "Extracting..." and self.track_numbers:
            self.world_num += 1

    #camelcase jumpscare
    def closeEvent(self, event):
        self.timer.stop()

        if self.extractor:
            self.extractor.stop()

        super().closeEvent(event)
