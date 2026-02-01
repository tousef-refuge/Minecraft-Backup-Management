from PySide6 import QtCore

from pathlib import Path
import zipfile

class ZipExtractor(QtCore.QObject):
    status = QtCore.Signal(str)
    finished = QtCore.Signal()

    def __init__(self, zip_path, track_numbers):
        super().__init__()
        self.settings = QtCore.QSettings()

        self.zip_path = zip_path
        self.track_numbers = track_numbers
        self.extract_dir = Path(self.settings.value("minecraft_dir")) / "saves"
        self._running = True

    def run(self):
        if not self.zip_path.exists():
            self.status.emit("Zip not found")
            self.finished.emit()
            return

        needs_extract = not self.extract_dir.exists()
        with zipfile.ZipFile(self.zip_path) as zip_ref:
            for name in zip_ref.namelist():
                if not (self.extract_dir / name).exists():
                    needs_extract = True
                    break

        if needs_extract:
            self.status.emit("Extracting...")
            self.extract_dir.mkdir(parents=True, exist_ok=True)

            with zipfile.ZipFile(self.zip_path) as zip_ref:
                zip_ref.extractall(self.extract_dir)

        self.status.emit("Up to date")
        self.finished.emit()

    def stop(self):
        self._running = False