import os
import shutil
from pathlib import Path

def organize_folder(target_path):
    folders = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Docs": [".pdf", ".docx", ".txt", ".md"],
        "Code": [".py", ".js", ".html", ".css"],
        "Music": [".mp3", ".wav"]
    }

    path = Path(target_path)
    if not path.exists():
        print("❌ Path doesn't exist, buddy!")
        return

    for file in path.iterdir():
        if file.is_file():
            ext = file.suffix.lower()
            for folder_name, extensions in folders.items():
                if ext in extensions:
                    dest_dir = path / folder_name
                    dest_dir.mkdir(exist_ok=True)
                    shutil.move(str(file), str(dest_dir / file.name))
                    print(f"📦 Moved {file.name} to {folder_name}/")

if __name__ == "__main__":
    print("🏠 Running organizer on the current folder...")
    print("Simulation: I'll check extensions and move them to tidy folders!")
