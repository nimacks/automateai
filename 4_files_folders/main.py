from pathlib import Path

filePath = Path("4_files_folders/files/content.txt")

if filePath.exists():
    print("File exists")
    with open(filePath, "r") as file:
        content = file.read()
        print(content)
        
else:
    print("File does not exist")
    with open(filePath, "w") as file:
        file.write("Hello World!")


# properties of the file
print(filePath.name)
print(filePath.suffix)
print(filePath.parent)
print(filePath.absolute())
print(filePath.is_dir())

print(filePath.is_file())
print(filePath.is_symlink())

