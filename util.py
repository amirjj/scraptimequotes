import glob


def merge_all_files(source_path):
    for file in source_path.glob("*.json"):
        with open(file, "r") as fp:
            data = fp.readlines()
            print(data)
