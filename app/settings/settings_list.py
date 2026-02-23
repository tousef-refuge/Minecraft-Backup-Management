from PySide6 import QtCore

# noinspection PyTypeChecker
class SettingsList:
    def __init__(self, key):
        self._settings = QtCore.QSettings()
        self.key = key

    #actually gets the list
    def get(self):
        return self._settings.value(self.key, [], list)

    def append(self, val):
        lst = self.get()
        lst.append(val)
        self._settings.setValue(self.key, lst)

    def remove(self, val):
        lst = self.get()
        lst.remove(val)
        self._settings.setValue(self.key, lst)

    def __contains__(self, val):
        lst = self.get()
        return val in lst

    def __getitem__(self, idx):
        lst = self.get()
        return lst[idx]

    def __iter__(self):
        lst = self.get()
        return iter(lst)

    def __len__(self):
        lst = self.get()
        return len(lst)
