import os

FILE = "C:\\Users\\Admin\\Desktop\\HMS tets file destination\\Destination\\"




#to create a new directory when new proffessor is added to the DB
def add_new_dir(dirName: str):

    newPath = os.path.join(FILE, dirName)

    os.makedirs(newPath, exist_ok=True)

    return newPath


#to eventually list all assignments in a directory.
def show_all_in_file(dirName: str):

    path = os.path.join(FILE, dirName)

    all_files = os.listdir(path)

    files = [f for f in all_files if os.path.isfile(os.path.join(path, f))]
    print(files)

    return files

    
