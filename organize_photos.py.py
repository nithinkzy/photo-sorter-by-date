import os
import shutil
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS
from pathlib import Path

# ==================================================
# 📂 SETTINGS — UPDATE THESE AS NEEDED
# ==================================================
INPUT_FOLDER = r"D:\in\Photos"   # ← folder with unsorted media
OUTPUT_FOLDER = r"D:\in\sorted"                     # ← where sorted folders will go
# ==================================================

# Supported file types
RAW_EXTENSIONS = {'.CR2', '.CR3', '.NEF', '.ARW', '.RAF', '.ORF', '.RW2', '.DNG'}
VIDEO_EXTENSIONS = {'.MP4', '.MOV', '.AVI', '.MTS', '.MKV', '.WMV'}
IMAGE_EXTENSIONS = {'.JPG', '.JPEG', '.PNG'}

def get_exif_date(image_path):
    """Try to get photo date from EXIF metadata."""
    try:
        image = Image.open(image_path)
        exif = image._getexif()
        if exif:
            for tag, value in exif.items():
                if TAGS.get(tag) == 'DateTimeOriginal':
                    return datetime.strptime(value, '%Y:%m:%d %H:%M:%S')
    except Exception:
        pass
    return None

def get_file_date(file_path):
    """Fallback: use file's modification time."""
    ts = os.path.getmtime(file_path)
    return datetime.fromtimestamp(ts)

def organize_media(input_folder, output_folder):
    input_folder = Path(input_folder)
    output_folder = Path(output_folder)

    # Counters for summary
    count_raw = count_video = count_photo = 0

    for file_path in input_folder.rglob('*'):
        if not file_path.is_file():
            continue

        ext = file_path.suffix.upper()

        # Skip non-media files
        if ext not in RAW_EXTENSIONS and ext not in VIDEO_EXTENSIONS and ext not in IMAGE_EXTENSIONS:
            continue

    
            # Get the date for sorting
        date = get_exif_date(file_path)
        if date is None:
            date = get_file_date(file_path)
        if date is None:
            print(f"⚠ Skipping file (no date found): {file_path}")
            continue

        year_folder = output_folder / str(date.year)
        month_folder = f"[{date.month:02d}] {date.strftime('%b')} - {date.day:02d}"
        month_path = year_folder / month_folder


        # Subfolders
        raw_folder = month_path / "[0] RAW"
        video_folder = month_path / "[1] VIDEO"

        # Decide destination + update counters
        if ext in RAW_EXTENSIONS:
            dest_folder = raw_folder
            count_raw += 1
        elif ext in VIDEO_EXTENSIONS:
            dest_folder = video_folder
            count_video += 1
        else:
            dest_folder = month_path
            count_photo += 1

        dest_folder.mkdir(parents=True, exist_ok=True)
        dest_file = dest_folder / file_path.name

        # Avoid overwriting duplicates
        counter = 1
        while dest_file.exists():
            dest_file = dest_folder / f"{file_path.stem}_{counter}{file_path.suffix}"
            counter += 1

        shutil.move(str(file_path), str(dest_file))
        print(f"Moved: {file_path.name} → {dest_file}")

    total = count_raw + count_video + count_photo

    # ✅ Summary
    print("\n" + "=" * 50)
    print("📸 ORGANIZATION SUMMARY")
    print("=" * 50)
    print(f"Total files organized: {total}")
    print(f"  • RAW files:   {count_raw}")
    print(f"  • Photos:      {count_photo}")
    print(f"  • Videos:      {count_video}")
    print("=" * 50)
    print("✅ All photos and videos organized successfully!")

if __name__ == "__main__":
    print("📸 Image & Video Organizer\n")
    print(f"Input Folder:  {INPUT_FOLDER}")
    print(f"Output Folder: {OUTPUT_FOLDER}\n")

    confirm = input("Proceed with organization? (y/n): ").strip().lower()
    if confirm == 'y':
        organize_media(INPUT_FOLDER, OUTPUT_FOLDER)
    else:
        print("❌ Operation cancelled.")
