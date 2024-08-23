import os

def find_file(dir, filename):
    for root, dirs, files in os.walk(dir):
        if filename in files:
            return os.path.join(root, filename)
    return None

dir="C:\\Users\\Admin\\Desktop\\HMS tets file destination"
filename="creationTest.txt"
file_path=find_file(dir, filename)

if file_path: 
    print(f"file found: {file_path}")
else:
    print("file not found")
    

#newFile = "creationTest.txt"
#file_path = "C:\\Users\\Admin\\Desktop\\HMS tets file destination"

#with open(f"{file_path}\\{newFile}", 'x') as file:
    #file.write("I hope this worked") 