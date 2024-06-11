# osu-cleaner-python #

# [Imports] #
import os, time
from dict import *

# [Stuff] #
user = os.path.expanduser("~")
path = f"{user}/AppData/Local/osu!/Songs/"
deletion_names = [
    f"{base_name}{extension}" for base_name in base_deletion_names for extension in ext
]
deletion_files = []

# [Main Loop] #


def main():
    kb_size = 0
    mb_size = 0
    count = 0

    folder_scan = os.scandir(path)

    start = time.time()
    for entry in folder_scan:
        if entry.is_dir():
            song_scan = os.scandir(os.path.join(path, entry.name))
            for sub_entry in song_scan:
                if sub_entry.is_file():
                    for deletion_name in deletion_names:
                        deletion_path = os.path.join(path, entry, deletion_name)
                        if os.path.exists(deletion_path):
                            count += 1
                            size = os.path.getsize(deletion_path)
                            deletion_files.append(deletion_path)
                            print(
                                f"{deletion_name} has BEEN found in {entry.name} | {size/1024}: KB"
                            )
                            kb_size += size / 1024
                            mb_size += size / 1048576
                        else:
                            pass
                    break
    end = time.time()

    if count > 1:
        confirmed = input(
            str(
                f"Do you wish to delete {count} files and save {int(mb_size)} MB? (Yes/No): "
            )
        ).lower()
        if confirmed == "yes":
            start = time.time()
            for deletion_path in deletion_files:
                os.remove(deletion_path)
                print(f"Removing {deletion_name} in {deletion_path}")
            end = time.time()
            print(
                f"File(s) Found | Total: {count}\nTotal Size    | KB: {int(kb_size)} MB: {int(mb_size)}\nElapsed       | {round(end - start, 3)}s\nExiting..."
            )
        else:
            print("error, exiting")
            exit
    elif count < 1:
        print(f"{count} Files found to cleanup!\nExiting...")
        exit


# [Script Start]
confirm = input(
    str(
        "Do you wish to search for all the bloat files associated within osu songs folder(s)? (Yes/No): "
    )
).lower()

if confirm == "yes":
    main()
else:
    exit
