import os
import json
import re
import argparse
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

# Load the hiragana JSON data from the same directory as the script
script_directory = os.path.dirname(os.path.abspath(__file__))
hiragana_json_path = os.path.join(script_directory, 'hiragana.json')

with open(hiragana_json_path, 'r', encoding='utf-8') as file:
    hiragana_data = json.load(file)

# Create a dictionary for easy lookup
hiragana_dict = {entry['kana']: entry['phoneme'] for entry in hiragana_data}

# Create a set to store unknown kana characters
unknown_kana = set()

# Function to convert kana sequence to phonemes
def convert_kana_sequence_to_phonemes(kana_sequence):
    words = kana_sequence.split()
    phonemes = []
    for word in words:
        phoneme = hiragana_dict.get(word, word)
        if phoneme == word:
            unknown_kana.add(word)  # Add unknown kana characters to the set
        phonemes.append(phoneme)
    return ' '.join(phonemes)

# Function to process a single .lab file
def process_lab_file(input_path):
    with open(input_path, 'r', encoding='utf-8') as lab_file:
        lab_content = lab_file.read()

    lines = lab_content.split('\n')
    converted_lines = []

    for line in lines:
        if not line:
            continue
        parts = line.split()
        if len(parts) == 3:
            start_time, end_time, kana_sequence = parts
            phoneme_sequence = convert_kana_sequence_to_phonemes(kana_sequence)
            converted_lines.append(f"{start_time} {end_time} {phoneme_sequence}")

    converted_lab_content = '\n'.join(converted_lines)

    with open(input_path, 'w', encoding='utf-8') as lab_file:
        lab_file.write(converted_lab_content)

def browse_labs_directory():
    directory = filedialog.askdirectory()
    if directory:
        labs_directory_entry.delete(0, tk.END)
        labs_directory_entry.insert(0, directory)

def convert_labs():
    labs_directory = labs_directory_entry.get()

    if not os.path.exists(labs_directory):
        messagebox.showerror("Error", "LABs directory does not exist.")
        return

    for filename in os.listdir(labs_directory):
        if filename.endswith(".lab"):
            input_path = os.path.join(labs_directory, filename)
            process_lab_file(input_path)

    # Create a text file to store unknown kana characters
    unknown_kana_file_path = os.path.join(script_directory, 'unknown_kana.txt')
    with open(unknown_kana_file_path, 'w', encoding='utf-8') as unknown_kana_file:
        for kana in unknown_kana:
            unknown_kana_file.write(kana + '\n')

    messagebox.showinfo("Success", "Conversion complete. Unknown kana characters saved to 'unknown_kana.txt'.")

# Create the main application window
root = tk.Tk()
root.title("Kana to Phonemes converter (lab)")

# Import the tcl file
root.tk.call("source", "./Forest-ttk-theme-1.0/forest-dark.tcl")

# Set the theme with the theme_use method
style = ttk.Style()
style.theme_use("forest-dark")

# Create a frame for the input fields
input_frame = ttk.Frame(root, padding=10)
input_frame.grid(row=0, column=0, padx=10, pady=10, sticky='w')

# LABs directory
labs_directory_label = ttk.Label(input_frame, text='LABs Directory:')
labs_directory_label.grid(row=0, column=0, sticky='w')

labs_directory_entry = ttk.Entry(input_frame, width=40)
labs_directory_entry.grid(row=0, column=1, padx=(5, 0), sticky='w')

labs_directory_button = ttk.Button(input_frame, text='Browse', command=browse_labs_directory)
labs_directory_button.grid(row=0, column=2, padx=(5, 0), sticky='w')

# Convert button
convert_button = ttk.Button(root, text='Convert LABs', command=convert_labs)
convert_button.grid(row=1, column=0, padx=10, pady=10)

# Start the GUI application
root.mainloop()
