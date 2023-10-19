import os
import argparse
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


def add_sil_phonemes(input_directory, output_directory, add_sil_at_beginning, add_sil_at_end):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Process each seg file in the input directory
    for seg_file_name in os.listdir(input_directory):
        if seg_file_name.endswith(".seg"):
            input_seg_file = os.path.join(input_directory, seg_file_name)
            output_seg_file = os.path.join(output_directory, seg_file_name)

            # Read the original .seg file
            with open(input_seg_file, 'r') as infile:
                lines = infile.readlines()

            # Find the line index where the "=====" line appears
            separator_line_index = lines.index("=================================================\n")

            # Extract the timing information from the first non-empty phoneme line
            first_non_empty_phoneme_start = None
            first_non_empty_phoneme_end = None

            for line in lines[separator_line_index + 1:]:
                phoneme_values = line.strip().split('\t')
                if len(phoneme_values) >= 3:
                    first_non_empty_phoneme_start = phoneme_values[1]
                    first_non_empty_phoneme_end = phoneme_values[2]
                    break

            if add_sil_at_beginning:
                # Insert "Sil" at the top with the calculated end time
                new_sil_line = f"Sil\t\t0.000000\t\t{first_non_empty_phoneme_end}\n"
                lines.insert(separator_line_index + 1, new_sil_line)

            if add_sil_at_end:
                # Calculate the number of phonemes
                num_phonemes = len(lines) - separator_line_index

            # Update the "nPhonemes" line with the calculated count
            for i, line in enumerate(lines):
                if line.startswith("nPhonemes"):
                    current_value = int(line.split()[-1])
                    new_value = current_value + 1
                    lines[i] = f"nPhonemes {new_value}\n"
                    break

                # Find the last non-empty phoneme's end time
                last_non_empty_phoneme_end = first_non_empty_phoneme_end
                for line in reversed(lines[separator_line_index + 1:]):
                    phoneme_values = line.strip().split('\t')
                    if len(phoneme_values) >= 3:
                        last_non_empty_phoneme_end = phoneme_values[2]
                        break

                # Find the largest end time in the .seg file
                largest_end_time = max(float(phoneme_values[2]) for line in lines[separator_line_index + 1:])

                # Format the largest_end_time to include all decimals and zero if it's a whole number
                if largest_end_time.is_integer():
                    largest_end_time = f"{largest_end_time:.6f}"
                else:
                    largest_end_time = str(largest_end_time)

                    # Set the "Sil" at the end with the largest end time
                    lines[-1] = f"Sil\t\t{last_non_empty_phoneme_end}\t\t{last_non_empty_phoneme_end}\n"


            # Open the output .seg file for writing
            with open(output_seg_file, 'w') as outfile:
                # Write the entire modified list back to the file
                outfile.writelines(lines)

            print("Sil phonemes added to", seg_file_name)

    print("All modifications complete.")

def browse_input_directory():
    input_directory = filedialog.askdirectory()
    input_directory_entry.delete(0, tk.END)
    input_directory_entry.insert(0, input_directory)

def browse_output_directory():
    output_directory = filedialog.askdirectory()
    output_directory_entry.delete(0, tk.END)
    output_directory_entry.insert(0, output_directory)

def execute_script():
    input_directory = input_directory_entry.get()
    output_directory = output_directory_entry.get()
    add_sil_at_beginning = add_sil_at_beginning_var.get()
    add_sil_at_end = add_sil_at_end_var.get()
    add_sil_phonemes(input_directory, output_directory, add_sil_at_beginning, add_sil_at_end)
    result_label.config(text="Modifications complete.")

# Create the main window
root = tk.Tk()
root.title("Add 'Sil' Phonemes")

# Import the tcl file
root.tk.call("source", "./Forest-ttk-theme-1.0/forest-dark.tcl")

# Set the theme with the theme_use method
style = ttk.Style()
style.theme_use("forest-dark")

# Create and configure widgets
input_directory_label = ttk.Label(root, text="Input Directory:")
input_directory_entry = ttk.Entry(root)
browse_input_button = ttk.Button(root, text="Browse", command=browse_input_directory)

output_directory_label = ttk.Label(root, text="Output Directory:")
output_directory_entry = ttk.Entry(root)
browse_output_button = ttk.Button(root, text="Browse", command=browse_output_directory)

add_sil_at_beginning_var = tk.BooleanVar()
add_sil_at_beginning_checkbox = ttk.Checkbutton(root, text="Add 'Sil' at the beginning", variable=add_sil_at_beginning_var)

add_sil_at_end_var = tk.BooleanVar()
add_sil_at_end_checkbox = ttk.Checkbutton(root, text="Add 'Sil' at the end (EXPERIMENTAL/BROKEN)", variable=add_sil_at_end_var)

execute_button = ttk.Button(root, text="Execute", command=execute_script)
result_label = ttk.Label(root, text="")

# Layout widgets
input_directory_label.grid(row=0, column=0, padx=10, pady=5)
input_directory_entry.grid(row=0, column=1, padx=10, pady=5)
browse_input_button.grid(row=0, column=2, padx=10, pady=5)

output_directory_label.grid(row=1, column=0, padx=10, pady=5)
output_directory_entry.grid(row=1, column=1, padx=10, pady=5)
browse_output_button.grid(row=1, column=2, padx=10, pady=5)

add_sil_at_beginning_checkbox.grid(row=2, column=1, padx=10, pady=5)
add_sil_at_end_checkbox.grid(row=3, column=1, padx=10, pady=5)

execute_button.grid(row=4, column=1, padx=10, pady=10)
result_label.grid(row=5, column=1, padx=10, pady=5)

root.mainloop()
