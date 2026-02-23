from app.settings import SettingsList

def append_world(world):
    remove_world(world)
    history = SettingsList("world_history")
    history.append(world)

    if len(history) > 6: #only the 5 most recent worlds are considered
        remove_world(history[0])

def remove_world(world):
    #deja vu
    history = SettingsList("world_history")
    if world in history:
        history.remove(world)