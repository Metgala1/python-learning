from pathlib import Path
import shutil

# Locate the folder containing this script.
script_directory = Path(__file__).resolve().parent

# Choose the folder we want to organize.
downloads_folder = "downloads"

# Map extensions to destination folder names.
categories = {
    ".pdf": "PDFs",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".txt": "Text",
    ".csv": "CSV",
    ".py": "Python",
}

# Check whether the folder exists.
if not downloads_folder.is_dir():
    print("The folder to organize does not exist.")
else:
    # Examine each item in the folder.
    for item in downloads_folder.iterdir():

        # Ignore directories.
        if not item.is_file():
            continue

        # Normalize the extension.
        extension = item.suffix.lower()

        # Choose a category.
        category = categories.get(extension, "Other")

        # Create the destination directory.
        destination_folder = downloads_folder / category
        destination_folder.mkdir(exist_ok=True)

        # Build the destination file path.
        destination_path = destination_folder / item.name

        # Avoid overwriting an existing destination file.
        if destination_path.exists():
            print(f"Skipping existing file: {destination_path}")
            continue

        # Move the file.
        shutil.move(item, destination_path)

        print(f"Moved {item.name} to {category}/")

    print("Organization complete!")
    
    Path("file.txt")	
# Represents a filesystem path
# .name	Gets the filename
# .stem	Gets the filename without its final suffix
# .suffix	Gets the final extension
# .suffixes	Gets all suffixes
# .exists()	Checks whether a path exists
# .is_file()	Checks whether a path is a regular file
# .is_dir()	Checks whether a path is a directory
# .mkdir()	Creates a directory
# .iterdir()	Lists immediate directory contents
# .glob()	Finds matching items in one directory
# .rglob()	Finds matching items recursively
# .rename()	Renames a path
# .unlink()	Deletes a file or symbolic link
# shutil.move()	Moves files or directories