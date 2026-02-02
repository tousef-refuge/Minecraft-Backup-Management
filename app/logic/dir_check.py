from .regex_funcs import remove_end_num

import zipfile
import os

def is_valid_mc_dir(folder):
    needed_subdirs = ["assets", "versions", "libraries", "saves"]
    return (os.path.basename(folder) == ".minecraft" and
                all(os.path.isdir(os.path.join(folder, subdir)) for subdir in needed_subdirs))

def is_valid_world_folder(folder):
    return True

def find_zip(zip_dir, world_name, track_numbers):
    for zip_path in zip_dir.glob("*.zip"):
        try:
            world_dir ,= get_top_level(zip_path)
            if track_numbers:
                world_dir = remove_end_num(world_dir)

            if is_valid_world_folder(world_dir) and world_dir == world_name:
                return zip_path

        except ValueError:
            continue
    return None

def get_top_level(zip_path):
    top_level = set()
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            for name in zip_ref.namelist():
                if not name:
                    continue

                parts = name.split('/')
                if len(parts) > 1:
                    top_level.add(parts[0])

        return top_level

    except zipfile.BadZipFile:
        return set()
