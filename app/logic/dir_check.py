import zipfile
import os

def is_valid_mc_dir(folder):
    needed_subdirs = ["assets", "versions", "libraries", "saves"]
    return (os.path.basename(folder) == ".minecraft" and
                all(os.path.isdir(os.path.join(folder, subdir)) for subdir in needed_subdirs))

def is_valid_world_folder(folder):
    return True

def find_zip(zip_dir, world_name):
    for zip_path in zip_dir.glob("*.zip"):
        try:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                top_level = set()
                for name in zip_ref.namelist():
                    if not name:
                        continue

                    parts = name.split('/')
                    if len(parts) > 1:
                        top_level.add(parts[0])

                world_dir ,= top_level
                if is_valid_world_folder(world_dir) and world_dir == world_name:
                    return zip_path

        except zipfile.BadZipFile | ValueError:
            continue
    return None
