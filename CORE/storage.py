import os

FILE = "C:\\Users\\Admin\\Desktop\\HMS tets file destination\\Destination\\"





def add_new_dir(dirName: str):

    newPath = os.path.join(FILE, dirName)

    os.makedirs(newPath, exist_ok=True)

    return newPath