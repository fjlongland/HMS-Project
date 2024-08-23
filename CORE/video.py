import os

newFile = "creationTest.txt"
file_path = "C:\\Users\\Admin\\Desktop\\HMS tets file destination"

with open(f"{file_path}\\{newFile}", 'x') as file:
    file.write("I hope this worked") 