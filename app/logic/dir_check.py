import os

def is_valid_mc_dir(folder):
    needed_subdirs = ["assets", "versions", "libraries", "saves"]
    return (os.path.basename(folder) == ".minecraft" and
                all(os.path.isdir(os.path.join(folder, subdir)) for subdir in needed_subdirs))

def is_valid_world_folder(folder):
    pass