# Import modules for handling archives and GUI
import zipfile, os, rarfile, py7zr
import string, itertools
from tkinter import *
from tkinter import filedialog, messagebox
from threading import Thread

# === GUI FUNCTIONS ===

# Called when user clicks "Browse" to choose archive
def browse_archive():
    # Opens file dialog to pick a .zip, .rar, or .7z file
    file_path.set(filedialog.askopenfilename(filetypes=[
        ("Archive files", "*.zip *.rar *.7z"),
        ("All files", "*.*")
    ]))

# Called when user clicks "Browse Wordlist"
def browse_wordlist():
    # Opens file dialog to pick a .txt wordlist
    wl_path.set(filedialog.askopenfilename(filetypes=[("Text files", "*.txt")]))


# Called when user clicks "Start Crack"
def start_crack():
    archive = file_path.get()  # path to the selected archive
    method = method_var.get()  # chosen method: brute or wordlist
    archive_type = archive_type_var.get()  # archive type: zip, rar, 7z
    max_len = int(length_entry.get())  # max password length

    charset = ''
    # Build the charset based on user selections
    if digits_var.get(): charset += string.digits
    if lowercase_var.get(): charset += string.ascii_lowercase
    if uppercase_var.get(): charset += string.ascii_uppercase
    if symbols_var.get(): charset += "!@#$%^&*"

    # Check if archive path is valid
    if not os.path.exists(archive):
        messagebox.showerror("Error", "Archive file not found!")
        return

    # Run the crack function in a separate thread (to avoid freezing the GUI)
    Thread(target=run_crack, args=(archive, method, archive_type, charset, max_len)).start()


# Decides whether to run brute-force or wordlist attack
def run_crack(archive, method, archive_type, charset, max_len):
    if method == "brute":
        brute_force_crack(archive, archive_type, charset, max_len)
    else:
        wordlist_file = wl_path.get()
        if not os.path.exists(wordlist_file):
            messagebox.showerror("Error", "Wordlist file not found!")
            return
        wordlist_crack(archive, archive_type, wordlist_file)


# === BRUTE-FORCE ATTACK ===
def brute_force_crack(archive, archive_type, charset, max_len):
    try:
        for length in range(1, max_len + 1):
            for pw_tuple in itertools.product(charset, repeat=length):
                password = ''.join(pw_tuple)
                if try_password(archive, archive_type, password):
                    messagebox.showinfo("Success", f"Password found: {password}")
                    return
    except Exception as e:
        messagebox.showerror("Error", str(e))
    messagebox.showinfo("Done", "Password not found.")


# === WORDLIST ATTACK ===
def wordlist_crack(archive, archive_type, wordlist_file):
    with open(wordlist_file, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            password = line.strip()
            if try_password(archive, archive_type, password):
                messagebox.showinfo("Success", f"Password found: {password}")
                return
    messagebox.showinfo("Done", "Password not found in wordlist.")


# Attempts to extract the archive with the given password
def try_password(archive, archive_type, password):
    try:
        if archive_type == "zip":
            with zipfile.ZipFile(archive) as zf:
                zf.extractall(pwd=bytes(password, 'utf-8'))
        elif archive_type == "rar":
            with rarfile.RarFile(archive) as rf:
                rf.extractall(pwd=password)
        elif archive_type == "7z":
            with py7zr.SevenZipFile(archive, mode='r', password=password) as z:
                z.extractall()
        return True
    except:
        return False


# === GUI LAYOUT ===
root = Tk()
root.title("ArchiveCrackerBoss")
root.geometry("500x450")

# Set the icon of the window (used when converting to .exe too)
icon_path = os.path.join(os.path.dirname(__file__), "zippic.ico")
root.iconbitmap(icon_path)

# GUI variable definitions
file_path = StringVar()
wl_path = StringVar()
method_var = StringVar(value="brute")
archive_type_var = StringVar(value="zip")
digits_var = BooleanVar()
lowercase_var = BooleanVar()
uppercase_var = BooleanVar()
symbols_var = BooleanVar()

# GUI components
Label(root, text="Select Archive:").pack()
Entry(root, textvariable=file_path, width=50).pack()
Button(root, text="Browse", command=browse_archive).pack()

Label(root, text="Archive Type:").pack()
OptionMenu(root, archive_type_var, "zip", "rar", "7z").pack()

Label(root, text="Method:").pack()
OptionMenu(root, method_var, "brute", "wordlist").pack()

Label(root, text="Charset:").pack()
Checkbutton(root, text="Digits", variable=digits_var).pack()
Checkbutton(root, text="Lowercase", variable=lowercase_var).pack()
Checkbutton(root, text="Uppercase", variable=uppercase_var).pack()
Checkbutton(root, text="Symbols", variable=symbols_var).pack()

Label(root, text="Max password length:").pack()
length_entry = Entry(root)
length_entry.insert(0, "4")  # default value
length_entry.pack()

Label(root, text="Wordlist (if used):").pack()
Entry(root, textvariable=wl_path, width=50).pack()
Button(root, text="Browse Wordlist", command=browse_wordlist).pack()

Button(root, text="Start Crack", bg="green", fg="white", command=start_crack).pack(pady=10)

# Start the GUI main loop
root.mainloop()
