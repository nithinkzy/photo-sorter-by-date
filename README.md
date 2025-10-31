# 📸 Photo & Video Organizer

Automatically organize **years of photos, RAWs, and videos** into clean, date-based folders — by year and month — with zero manual work.

---

## ✨ Features

- 🗓️ Sorts by **actual photo taken date (EXIF)**  
- 🕒 Falls back to **file modified time** if EXIF is missing  
- 🔄 Separates **RAW, JPG/PNG, and Video** files  
- 🧱 Creates a clean folder structure:  
  ```
  2021/
   ├── [02] Feb - 14/
   │    ├── [0] RAW/
   │    ├── [1] VIDEO/
   │    └── photo.jpg
  ```
- ⚙️ Prevents duplicate overwrites  
- 💬 Prints an easy-to-read summary when finished  

---

## 🚀 How to Use

### 1️⃣ Install Dependencies
Make sure you have Python 3 installed. Then install Pillow:
```bash
pip install Pillow
```

### 2️⃣ Set Your Input and Output Folders
Open the script and update these lines:
```python
INPUT_FOLDER = r"D:\in\Photos"
OUTPUT_FOLDER = r"D:\in\sorted"
```

### 3️⃣ Run the Script
```bash
python organize_photos.py
```
You’ll be asked for confirmation before the organization begins.

---

## 🧠 Why I Built This

Over the past decade, I’ve collected **tens of thousands of photos** from different sources:  
📱 Phone screenshots  
📸 RAW + JPGs from my DSLR  
🚁 Drone shots  
💾 Photos friends shared or copied to my drives  

Every time I tried to organize them, it somehow got worse — duplicates, mixed folders, and chaos.  

So I built this simple Python tool that does what every photo app should do —  
**organize everything beautifully by date, type, and folder.**

---

## 📸 Example Output

```
2020/
 ├── [03] Mar - 12/
 │    ├── [0] RAW/
 │    ├── [1] VIDEO/
 │    └── IMG_1234.JPG
2021/
 ├── [07] Jul - 05/
 │    ├── [0] RAW/
 │    ├── [1] VIDEO/
 │    └── vacation.png
```

---

## 🧩 Requirements

- Python 3.7 +
- Pillow (`pip install Pillow`)
- Works on Windows, macOS, and Linux


---

## 🔗 Links

💡 **GitHub Repository:** [https://github.com/yourusername/photo-organizer](https://github.com/nithinkzy/photo-sorter-by-date/)  
📢 **Linkedin:** [LinkedIn Post](https://www.linkedin.com/posts/nithin-kollerethu_github-nithinkzyphoto-sorter-by-date-activity-7389862933327147008-L9rO?utm_source=share&utm_medium=member_desktop&rcm=ACoAACWh5qkBnmTsBdhEcGB01XpolSovEeGO33c)

---

## 🧑‍💻 Contribute

Pull requests and suggestions are welcome!  
If you have ideas (like adding cloud sync, face clustering, or duplicate detection), open an issue — I’d love to collaborate.

---

## 📄 License

This project is released under the **MIT License** — free to use, modify, and share.

---

### ⭐ If this helped you bring order to your photo chaos, give it a star on GitHub!
