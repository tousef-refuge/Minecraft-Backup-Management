from PySide6 import QtCore, QtWidgets

from app.logic import ZipExtractor

class AutoExtractConfirm(QtWidgets.QDialog):
    def __init__(self, zip_path, track_numbers):
        super().__init__()
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
        self.timer.start(1000) #add configurer later

        self.thread = None
        self.extractor = None
        self.is_extracting = False

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
        self.extractor = ZipExtractor(self.zip_path, self.track_numbers)
        self.extractor.moveToThread(self.thread)

        self.thread.started.connect(self.extractor.run)
        self.extractor.status.connect(self.status_label.setText)
        self.extractor.finished.connect(self.cleanup_extract)

        self.thread.start()

    def cleanup_extract(self):
        self.is_extracting = False

        self.thread.quit()
        self.thread.wait()

        self.extractor.deleteLater()
        self.thread.deleteLater()

    #camelcase jumpscare
    def closeEvent(self, event):
        self.timer.stop()

        if self.extractor:
            self.extractor.stop()

        super().closeEvent(event)
