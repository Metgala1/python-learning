from pathlib import Path
import shutil

folder_path = Path("downloads")
text_path = Path("text")
pdf_path = Path("Pdf")
json_path = Path("Jsons")
photo_path = Path("Photos")
python_path = Path("Python")
csv_path = Path("Csvs")

for p in (text_path, pdf_path, json_path, photo_path, python_path, csv_path):
    p.mkdir()

for file_path in folder_path.iterdir():
    if not file_path.is_file():
        continue
    match file_path.suffix:
        case ".txt":
            shutil.move(str(file_path) , text_path)
        case ".pdf":
            shutil.move(str(file_path) , pdf_path)
        case ".json":
            shutil.move(str(file_path) , json_path)
        case ".jpg":
            shutil.move(str(file_path) , photo_path)
        case ".py":
            shutil.move(str(file_path) , python_path)
        case ".csv":
            shutil.move(str(file_path) , csv_path)
        case _:
            print("Invalid file")
            