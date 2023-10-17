import tkinter as tk
from tkinter import ttk
import subprocess

def run_script(script_path):
    try:
        process = subprocess.Popen(script_path, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, universal_newlines=True)
        stdout, stderr = process.communicate()
        return stdout
    except Exception as e:
        return str(e)

# Create the main application window
root = tk.Tk()
root.title("Canned_Bread's VOCALOIDDBTOOL Swiss Army Knife")
root.geometry("800x600")  # Set the initial window size

# Make the app responsive
for i in range(3):
    root.columnconfigure(index=i, weight=1)
for i in range(3):
    root.rowconfigure(index=i, weight=1)

# Create a style
style = ttk.Style(root)

# Import the tcl file
root.tk.call("source", "./Forest-ttk-theme-1.0/forest-dark.tcl")

# Set the theme with the theme_use method
style.theme_use("forest-dark")

# Create a notebook for multiple script pages
notebook = ttk.Notebook(root)

# Define the "Trans Tools" page
trans_tools_page = ttk.Frame(notebook)

# Create a Frame for buttons on the "Trans Tools" page
trans_tools_button_frame = ttk.Frame(trans_tools_page)
trans_tools_button_frame.grid(row=0, column=1, padx=10, pady=(30, 10))

# Create a custom style for buttons
ttk.Style().configure('Custom.TButton', background='blue', foreground='white')

# Run button for "Auto_Trans"
def run_auto_trans():
    script_path = "Auto_trans_GUI.py"  # Replace with your script path
    output = run_script(script_path)
    trans_tools_output_text.config(state=tk.NORMAL)
    trans_tools_output_text.delete("1.0", tk.END)
    trans_tools_output_text.insert(tk.END, output)
    trans_tools_output_text.config(state=tk.DISABLED)

run_button_auto_trans = ttk.Button(trans_tools_button_frame, text="Run Auto_Trans", style='Custom.TButton', command=run_auto_trans)
run_button_auto_trans.pack(pady=10)

    
def run_trans_convert():
    script_path = "trans_convert_GUI.py"  # Replace with your script path
    output = run_script(script_path)
    trans_tools_output_text.config(state=tk.NORMAL)
    trans_tools_output_text.delete("1.0", tk.END)
    trans_tools_output_text.insert(tk.END, output)
    trans_tools_output_text.config(state=tk.DISABLED)

run_button_auto_trans = ttk.Button(trans_tools_button_frame, text="Run Trans Converter", style='Custom.TButton', command=run_trans_convert)
run_button_auto_trans.pack(pady=10)

# Create a Label widget with the desired text
trans_tools_description = ttk.Label(
    trans_tools_page,
    text="The first step in Vocaloid creation is the .trans files collection. Here you can run Auto_Trans to generate those for you (based off of WAV filename). \nTrans_converter is a tool that converts the Articulation .trans you get with auto_trans and makes them into Stationary .trans files (yes they're different).",
    wraplength=400  # Adjust this value as needed to fit the text within the desired width
)
trans_tools_description.grid(row=2, column=1, pady=(0, 10), columnspan=3)

# Output text widget for "Trans Tools" page
trans_tools_output_text = tk.Text(trans_tools_page, height=10, width=40, state=tk.DISABLED)
trans_tools_output_text.grid(row=1, column=1)

# Define the "oto.ini _> seg file tools" page
oto_ini_page = ttk.Frame(notebook)

# Create a Frame for buttons on the "oto.ini _> seg file tools" page
oto_ini_button_frame = ttk.Frame(oto_ini_page)
oto_ini_button_frame.grid(row=0, column=1, padx=10, pady=(30, 10))

# Run button for "Your Script 1"
def run_your_script_1():
    script_path = "cannedbread_genon2db_GUI.py"  
    output = run_script(script_path)
    oto_ini_output_text.config(state=tk.NORMAL)
    oto_ini_output_text.delete("1.0", tk.END)
    oto_ini_output_text.insert(tk.END, output)
    oto_ini_output_text.config(state=tk.DISABLED)

run_button_your_script_1 = ttk.Button(oto_ini_button_frame, text="Run genon2db", style='Custom.TButton', command=run_your_script_1)
run_button_your_script_1.pack(pady=10)

# Run button for "Your Script 2"
def run_your_script_2():
    script_path = "lab2seg_GUI.py"  
    output = run_script(script_path)
    oto_ini_output_text.config(state=tk.NORMAL)
    oto_ini_output_text.delete("1.0", tk.END)
    oto_ini_output_text.insert(tk.END, output)
    oto_ini_output_text.config(state=tk.DISABLED)

run_button_your_script_2 = ttk.Button(oto_ini_button_frame, text="Run lab2seg", style='Custom.TButton', command=run_your_script_2)
run_button_your_script_2.pack(pady=10)

# Output text widget for "oto.ini _> seg file tools" page
oto_ini_output_text = tk.Text(oto_ini_page, height=10, width=40, state=tk.DISABLED)
oto_ini_output_text.grid(row=1, column=1)

# Create a Label widget with the desired text
oto_ini_description = ttk.Label(
    oto_ini_page,
    text="Genon2DB is a tool in which you can convert your oto.ini to .lab files for the next step. \nLab2Seg is where you take lab files and convert them into seg files for articulation .trans files (I need to make one for stationary because they're different too).",
    wraplength=400  # Adjust this value as needed to fit the text within the desired width
)
oto_ini_description.grid(row=2, column=1, pady=(0, 10), columnspan=3)


# Define the "Misc. Tools" page
misc_tools_page = ttk.Frame(notebook)

# Create a Frame for buttons on the "Misc. Tools" page
misc_tools_button_frame = ttk.Frame(misc_tools_page)
misc_tools_button_frame.grid(row=0, column=1, padx=10, pady=(30, 10))

# Run button for "Phoneme Grabber"
def run_phoneme_grabber():
    script_path = "phoneme_grabber_GUI.py"  
    output = run_script(script_path)
    trans_tools_output_text.config(state=tk.NORMAL)
    trans_tools_output_text.delete("1.0", tk.END)
    trans_tools_output_text.insert(tk.END, output)
    trans_tools_output_text.config(state=tk.DISABLED)

run_button_phoneme_grabber = ttk.Button(misc_tools_button_frame, text="Run Phoneme Grabber", style='Custom.TButton', command=run_phoneme_grabber)
run_button_phoneme_grabber.pack(pady=10)

# Run button for "Your Script 3" (Miscellaneous script 1)
def run_misc_script_1():
    script_path = "convert_kana_GUI.py"  
    output = run_script(script_path)
    misc_tools_output_text.config(state=tk.NORMAL)
    misc_tools_output_text.delete("1.0", tk.END)
    misc_tools_output_text.insert(tk.END, output)
    misc_tools_output_text.config(state=tk.DISABLED)

run_button_misc_script_1 = ttk.Button(misc_tools_button_frame, text="Run Convert Kana (lab)", style='Custom.TButton', command=run_misc_script_1)
run_button_misc_script_1.pack(pady=10)

# Run button for "Your Script 4" (Miscellaneous script 2)
def run_misc_script_2():
    script_path = "kiritan_script_GUI.py" 
    output = run_script(script_path)
    misc_tools_output_text.config(state=tk.NORMAL)
    misc_tools_output_text.delete("1.0", tk.END)
    misc_tools_output_text.insert(tk.END, output)
    misc_tools_output_text.config(state=tk.DISABLED)

run_button_misc_script_2 = ttk.Button(misc_tools_button_frame, text="Run Phoneme Transfer (wonky)", style='Custom.TButton', command=run_misc_script_2)
run_button_misc_script_2.pack(pady=10)

# Output text widget for "Misc. Tools" page
misc_tools_output_text = tk.Text(misc_tools_page, height=10, width=40, state=tk.DISABLED)
misc_tools_output_text.grid(row=1, column=1)

# Create a Label widget with the desired text
misc_tools_description = ttk.Label(
    misc_tools_page,
    text="Phoneme Grabber is a tool that takes all of your phonemes from an oto.ini file and it generates a text file with all of the phonemes in it. It's useful for editing hiragana.json or phonemes.json.\nConvert Kana (lab) is a tool that converts kana in your labs to phonemes for the seg creation.\nPhoneme transfer is an experimental script that transfers phonemes from one seg file to another (for when you have a voicebank with many pitches and you want the timings to be different but the phonemes to be the same in a set of seg files).",
    wraplength=400  # Adjust this value as needed to fit the text within the desired width
)
misc_tools_description.grid(row=2, column=1, pady=(0, 10), columnspan=3)


# Add the pages to the notebook
notebook.add(trans_tools_page, text="Trans Tools")
notebook.add(oto_ini_page, text="oto.ini _> seg file tools")
notebook.add(misc_tools_page, text="Misc. Tools")

# Pack the notebook
notebook.grid(row=0, column=1, padx=10, pady=(30, 10))

# Center the window and set minsize
root.update()
root.minsize(root.winfo_width(), root.winfo_height())
x_cordinate = int((root.winfo_screenwidth()/2) - (root.winfo_width()/2))
y_cordinate = int((root.winfo_screenheight()/2) - (root.winfo_height()/2))
root.geometry("+{}+{}".format(x_cordinate, y_cordinate))

# Start the main loop
root.mainloop()
