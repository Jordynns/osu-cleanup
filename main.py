# osu-cleaner-python #

# [Imports] #
import os, time

# [Stuff] #
user = os.path.expanduser("~")
path = f"{user}/AppData/Local/osu!/Songs/"
ext = [".mp3", ".wav", ".ogg", ".avi", ".png"]

base_deletion_names = [
    "comboburst",
    "combobreak",
    "failsound",
    "sectionpass",
    "sectionfail",
    "applause",
    "drum-hitnormal",
    "drum-hitnormal2",
    "drum-hitclap",
    "drum-hitclap2",
    "drum-hitfinish",
    "drum-hitfinish2",
    "drum-hitwhistle",
    "drum-hitwhistle2",
    "drum-slidertick",
    "drum-slidertick2",
    "drum-sliderslide",
    "drum-sliderslide2",
    "drum-sliderwhistle",
    "drum-sliderwhistle2",
    "normal-hitnormal",
    "normal-hitnormal2",
    "normal-hitclap",
    "normal-hitclap2",
    "normal-hitfinish",
    "normal-hitfinish2",
    "normal-slidertick",
    "normal-slidertick2",
    "normal-sliderslide",
    "normal-sliderslide2",
    "normal-sliderwhistle",
    "normal-sliderwhistle2",
    "soft-hitnormal",
    "soft-hitnormal2",
    "soft-hitclap",
    "soft-hitclap2",
    "soft-hitfinish",
    "soft-hitfinish2",
    "soft-hitwhistle",
    "soft-hitwhistle2",
    "soft-slidertick",
    "soft-slidertick2",
    "soft-sliderslide",
    "soft-sliderslide2",
    "soft-sliderwhistle",
    "soft-sliderwhistle2",
    "spinnerspin",
    "spinnerbonus",
    "taiko-normal-hitnormal",
    "taiko-normal-hitnormal2",
    "taiko-normal-hitclap",
    "taiko-normal-hitclap2",
    "taiko-normal-hitfinish",
    "taiko-normal-hitfinish2",
    "taiko-normal-hitwhistle",
    "taiko-normal-hitwhistle2",
    "taiko-soft-hitnormal",
    "taiko-soft-hitnormal2",
    "taiko-soft-hitclap",
    "taiko-soft-hitclap2",
    "taiko-soft-hitfinish",
    "taiko-soft-hitfinish2",
    "taiko-soft-hitwhistle",
    "taiko-soft-hitwhistle2",
    "taiko-drum-hitnormal",
    "taiko-drum-hitnormal2",
    "taiko-drum-hitclap",
    "taiko-drum-hitclap2",
    "taiko-drum-hitfinish",
    "taiko-drum-hitfinish2",
    "taiko-drum-hitwhistle",
    "taiko-drum-hitwhistle2",
    "fail-background",
    "section-fail",
    "approachcircle",
    "hitcircle",
    "hitcircleoverlay",
    "reversearrow",
    "comboburst",
    "comboburst-0",
    "comboburst-1",
    "comboburst-2",
    "comboburst-3",
    "comboburst-4",
    "default-0",
    "default-1",
    "default-2",
    "default-3",
    "default-4",
    "default-5",
    "default-6",
    "default-7",
    "default-8",
    "default9",
    "followpoint-0",
    "followpoint-1",
    "followpoint-2",
    "followpoint-3",
    "followpoint-4",
]

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
