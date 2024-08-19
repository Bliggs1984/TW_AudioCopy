import sys
import os
import shutil
import tkinter as tk
from tkinter import filedialog

def find_audio_folders(root_folder):
    audio_folders = []
    for dirpath, dirnames, filenames in os.walk(root_folder):
        if "01_AUDIO" in dirnames:
            audio_folders.append(os.path.join(dirpath, "01_AUDIO"))
    return audio_folders

def copy_to_audio_folders(source_file, audio_folders):
    filename = os.path.basename(source_file)
    for folder in audio_folders:
        dest_path = os.path.join(folder, filename)
        shutil.copy2(source_file, dest_path)
        print(f"Copied {filename} to {folder}")

def select_root_folder():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    folder_path = filedialog.askdirectory(title="Select the root folder containing PDP Projects")
    root.destroy()
    return folder_path

# Prompt user to select root folder
root_folder = select_root_folder()

if not root_folder:
    print("No folder selected. Exiting.")
    input("Press Enter to exit...")
    sys.exit()

# Find all "01_AUDIO" folders
audio_folders = find_audio_folders(root_folder)

if not audio_folders:
    print("No '01_AUDIO' folders found.")
    input("Press Enter to exit...")
    sys.exit()

# Get the list of files dragged onto the script
files = sys.argv[1:]

# Process each file
for file in files:
    copy_to_audio_folders(file, audio_folders)

input("Press Enter to exit...")