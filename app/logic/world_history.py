from app.settings import SettingsList

def append_path(path):
    remove_path(path)
    history = SettingsList("world_history")
    history.append(path)

    if len(history) > 6: #only the 5 most recent worlds are considered
        remove_path(history[0])

def remove_path(path):
    #deja vu
    history = SettingsList("world_history")
    if path in history:
        history.remove(path)