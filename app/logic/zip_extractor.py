from PySide6 import QtCore, QtMultimedia

from app.logic import remove_end_num, get_top_level
from app import PROJECT_DIR

from pathlib import Path
import zipfile

class ZipExtractor(QtCore.QObject):
    status = QtCore.Signal(str)
    finished = QtCore.Signal()

    def __init__(self, zip_path, world_num, play_sound):
        super().__init__()
        self.settings = QtCore.QSettings()

        self.zip_path = zip_path
        self.world_num = world_num
        self.extract_dir = Path(self.settings.value("minecraft_dir")) / "saves"
        self._running = True

        self.confirm_sound = None
        if play_sound:
            sound_path = str(PROJECT_DIR / "audio" / "confirm.wav")
            self.confirm_sound = QtMultimedia.QSoundEffect()
            self.confirm_sound.setSource(QtCore.QUrl.fromLocalFile(sound_path))
            self.confirm_sound.setVolume(0.5)

    def run(self):
        if not self.zip_path.exists():
            self.status.emit("Zip not found")
            self.finished.emit()
            return

        world_name ,= get_top_level(self.zip_path)
        needs_extract = not any(
            remove_end_num(p.name) == remove_end_num(world_name)
            for p in self.extract_dir.iterdir() if p.is_dir()
        )

        if needs_extract:
            self.status.emit("Extracting...")
            self.extract_dir.mkdir(parents=True, exist_ok=True)

            before = {p for p in self.extract_dir.iterdir() if p.is_dir()}
            with zipfile.ZipFile(self.zip_path) as zip_ref:
                zip_ref.extractall(self.extract_dir)
            after = {p for p in self.extract_dir.iterdir() if p.is_dir()}

            if self.world_num:
                new_dir = (after - before).pop()
                base_name = remove_end_num(new_dir.name)
                new_name = new_dir.with_name(f"{base_name}#{self.world_num}")
                new_dir.rename(new_name)
            if self.confirm_sound:
                self.confirm_sound.play()

        self.status.emit("Up to date")
        self.finished.emit()

    def stop(self):
        self._running = False