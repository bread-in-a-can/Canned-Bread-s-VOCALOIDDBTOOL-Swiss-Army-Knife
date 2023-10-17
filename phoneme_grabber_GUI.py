import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import subprocess

# Function to parse an oto.ini file and extract phonemes
def parse_oto_ini(oto_file):
    phonemes = set()
    with open(oto_file, 'rb') as file:
        for line in file:
            try:
                line = line.decode('shift-jis')
            except UnicodeDecodeError:
                continue
            parts = line.strip().split('=')
            if len(parts) == 2:
                phoneme_data = parts[1].split(',')[0].strip()
                phoneme_data = phoneme_data.replace(' ', '\n')  # Replace space with newline
                phonemes.update(phoneme_data.split('\n'))  # Add individual phonemes to the set
    return phonemes

# Function to run the phoneme grabber script
def run_phoneme_grabber():
    oto_file = oto_file_entry.get()
    output_folder = output_folder_entry.get()
    
    try:
        phonemes = parse_oto_ini(oto_file)
        
        output_file = f'{output_folder}/phonemes.txt'
        with open(output_file, 'w', encoding='utf-8') as file:
            for phoneme in sorted(phonemes):
                file.write(phoneme + '\n')
        
        messagebox.showinfo('Success', f'Phonemes extracted and saved to {output_file}')
    except Exception as e:
        messagebox.showerror('Error', f'An error occurred: {str(e)}')

# Create the main application window
root = tk.Tk()
root.title('Phoneme Grabber')

# Import the tcl file for the Forest theme
root.tk.call("source", "./Forest-ttk-theme-1.0/forest-dark.tcl")

# Set the theme with the theme_use method
style = ttk.Style(root)
style.theme_use("forest-dark")

# Create a frame for the input fields
input_frame = ttk.Frame(root, padding=10)
input_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky='w')

# Oto.ini file input
oto_file_label = ttk.Label(input_frame, text='oto.ini File:')
oto_file_label.grid(row=0, column=0, sticky='w')

oto_file_entry = ttk.Entry(input_frame, width=40)
oto_file_entry.grid(row=0, column=1, padx=(5, 0), sticky='w')

oto_file_button = ttk.Button(input_frame, text='Browse', command=lambda: browse_file(oto_file_entry))
oto_file_button.grid(row=0, column=2, padx=(5, 0), sticky='w')

# Output folder input
output_folder_label = ttk.Label(input_frame, text='Output Folder:')
output_folder_label.grid(row=1, column=0, sticky='w')

output_folder_entry = ttk.Entry(input_frame, width=40)
output_folder_entry.grid(row=1, column=1, padx=(5, 0), sticky='w')

output_folder_button = ttk.Button(input_frame, text='Browse', command=lambda: browse_directory(output_folder_entry))
output_folder_button.grid(row=1, column=2, padx=(5, 0), sticky='w')

# Run button
run_button = ttk.Button(root, text='Run Phoneme Grabber', command=run_phoneme_grabber)
run_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Function to open a file dialog and populate an entry field
def browse_file(entry_field):
    file_path = filedialog.askopenfilename(filetypes=[('oto.ini files', '*.ini')])
    if file_path:
        entry_field.delete(0, tk.END)
        entry_field.insert(0, file_path)

# Function to open a directory dialog and populate an entry field
def browse_directory(entry_field):
    folder_path = filedialog.askdirectory()
    if folder_path:
        entry_field.delete(0, tk.END)
        entry_field.insert(0, folder_path)

# Start the GUI application
root.mainloop()
