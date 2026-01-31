from PySide6 import QtCore, QtWidgets

class AutoExtractConfirm(QtWidgets.QDialog):
    def __init__(self, zip_dir, track_numbers):
        self.zip_dir = zip_dir
        self.track_numbers = track_numbers
        super().__init__()