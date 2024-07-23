import tkinter as tk
from tkinter import messagebox
import sqlite3

# Function to create the database and table
def create_db():
    conn = sqlite3.connect('codes.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS codes
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       code TEXT NOT NULL)''')
    # Insert sample codes (you can add more or change these codes as needed)
    cursor.execute("INSERT INTO codes (code) VALUES ('1234')")
    cursor.execute("INSERT INTO codes (code) VALUES ('5678')")
    conn.commit()
    conn.close()

# Function to check if the code exists in the database
def check_code():
    entered_code = entry.get()
    conn = sqlite3.connect('codes.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM codes WHERE code=?", (entered_code,))
    result = cursor.fetchone()
    conn.close()
    if result:
        messagebox.showinfo("Success", "Open")
    else:
        messagebox.showerror("Error", "Invalid Code")

# Function to handle button clicks on the virtual keyboard
def press_key(key):
    entry.insert(tk.END, key)

# Function to clear the entry field
def clear_entry():
    entry.delete(0, tk.END)

# Set up the main application window
root = tk.Tk()
root.title("Code Entry")
root.geometry("800x480")  # Adjusted for typical 7-inch screen size

# Style configuration
font_large = ("Arial", 18)
font_medium = ("Arial", 14)
btn_color = "#4CAF50"
btn_fg_color = "#FFFFFF"
bg_color = "#2E2E2E"
entry_bg = "#FFFFFF"
entry_fg = "#000000"

# Entry field
entry = tk.Entry(root, font=font_large, justify='center', bg=entry_bg, fg=entry_fg)
entry.grid(row=0, column=0, columnspan=10, pady=10, padx=10, sticky="ew")

# Virtual keyboard
keys_frame = tk.Frame(root, bg=bg_color)
keys_frame.grid(row=1, column=0, sticky="nsew")

# Full QWERTY keyboard layout
keys = [
    ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
    ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
    ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
    ['z', 'x', 'c', 'v', 'b', 'n', 'm'],
    ['Clear', 'Submit']
]

# Create button grid
for row_index, row in enumerate(keys):
    for col_index, key in enumerate(row):
        if key == 'Clear':
            btn = tk.Button(keys_frame, text=key, font=font_medium, command=clear_entry,
                            bg=btn_color, fg=btn_fg_color, width=6, height=2)
        elif key == 'Submit':
            btn = tk.Button(keys_frame, text=key, font=font_medium, command=check_code,
                            bg=btn_color, fg=btn_fg_color, width=6, height=2)
        else:
            btn = tk.Button(keys_frame, text=key, font=font_medium, command=lambda k=key: press_key(k),
                            bg=btn_color, fg=btn_fg_color, width=6, height=2)
        btn.grid(row=row_index, column=col_index, padx=2, pady=2)

# Adjust column and row weights for proper scaling
for i in range(10):
    keys_frame.grid_columnconfigure(i, weight=1)
for i in range(len(keys)):
    keys_frame.grid_rowconfigure(i, weight=1)

# Initialize the database
create_db()

# Run the application
root.mainloop()
