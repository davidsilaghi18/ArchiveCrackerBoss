# 🧠 ArchiveCrackerBoss

**ArchiveCrackerBoss** is a GUI-based tool written in Python that helps you recover passwords from encrypted `.zip`, `.rar`, and `.7z` archive files using brute-force or wordlist attacks.

## 💻 Features

- ✅ Supports `.zip`, `.rar`, and `.7z` formats
- 🔒 Brute-force mode with customizable character sets:
  - Digits (0-9)
  - Lowercase letters (a-z)
  - Uppercase letters (A-Z)
  - Symbols (!, @, #, etc.)
- 📂 Wordlist mode for dictionary attacks
- 📈 Progress feedback and UI interface
- 🖱️ Built with `tkinter` for a simple graphical interface

## 📸 Screenshot
![image](https://github.com/user-attachments/assets/c6871a89-0808-4b6c-961a-c5f4914a0de2)
![image](https://github.com/user-attachments/assets/6847f4e4-3e6e-49f7-98b5-4294d7712f9d)
<img width="1128" alt="Screenshot 2025-05-05 133908" src="https://github.com/user-attachments/assets/06063dd1-eeb0-425c-9964-6ff60d6c3b1b" />

## 🚀 How to Use

### Option 1: Run from Source (Python required)

1. Clone this repo:
   ```bash
   git clone https://github.com/davidsilaghi18/ArchiveCrackerBoss.git
   cd ArchiveCrackerBoss

2. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. Run the app:
   ```bash
   python unzipall_gui.py

### Download the Windows Installer

🔽 You can download the .exe version (no Python required):
https://www.dropbox.com/scl/fi/ho22j0oobowvgjh9ecdur/ArchiveCrackerBossSetup.exe?rlkey=484ebar7fjfmb6nujop67l6oa&st=oup9141e&dl=1

### 🧩 Requirements (if running from source)
Python 3.x

py7zr

rarfile

tkinter (comes with Python by default)


## 📁 Files

| File              | Description                             |
|-------------------|-----------------------------------------|
| `unzipall_gui.py` | Main Python GUI application             |
| `zippic.ico`      | Application icon                        |
| `UnRAR.exe`       | Required for `.rar` file support (Windows) |
| `README.md`       | Project documentation                   |
| `requirements.txt`| List of required Python packages        |

---

## 👨‍💻 Author

**David Silaghi**  
📍 Roskilde University  
🔗 [GitHub Profile](https://github.com/davidsilaghi18)


### 📜 License
This project is for educational purposes. You are free to use, modify, and share it with credit.


