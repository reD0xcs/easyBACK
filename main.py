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
def press_key(key, btn):
    entry.insert(tk.END, key)
    # Change the button's appearance to indicate it was pressed
    btn.config(relief=tk.SUNKEN)
    # Reset the button's appearance after 0.2 seconds
    root.after(200, lambda: btn.config(relief=tk.RAISED))

# Function to clear the entry field
def clear_entry():
    entry.delete(0, tk.END)

# Set up the main application window
root = tk.Tk()
root.title("Code Entry")
root.geometry("800x480")
root.config(bg="#2E2E2E")

# Style configuration
font_large = ("Arial", 20)
font_medium = ("Arial", 14)
btn_color = "#4CAF50"
btn_fg_color = "#FFFFFF"
btn_active_bg = "#66BB6A"  # A shade darker for active state
btn_active_fg = "#FFFFFF"
bg_color = "#2E2E2E"
entry_bg = "#FFFFFF"
entry_fg = "#000000"

# Entry field
entry = tk.Entry(root, font=font_large, justify='center', bg=entry_bg, fg=entry_fg)
entry.pack(pady=10)

# Virtual keyboard
keys_frame = tk.Frame(root, bg=bg_color)
keys_frame.pack()

# Full QWERTY keyboard layout
keys = [
    ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
    ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
    ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
    ['z', 'x', 'c', 'v', 'b', 'n', 'm'],
    ['Clear', 'Submit']
]

# Add buttons for each key
for row in keys:
    row_frame = tk.Frame(keys_frame, bg=bg_color)
    row_frame.pack(side=tk.TOP, pady=2)
    for key in row:
        if key == 'Clear':
            btn = tk.Button(row_frame, text=key, font=font_medium, command=clear_entry,
                            bg=btn_color, fg=btn_fg_color, activebackground=btn_active_bg,
                            activeforeground=btn_active_fg, width=4, height=2)
        elif key == 'Submit':
            btn = tk.Button(row_frame, text=key, font=font_medium, command=check_code,
                            bg=btn_color, fg=btn_fg_color, activebackground=btn_active_bg,
                            activeforeground=btn_active_fg, width=4, height=2)
        else:
            btn = tk.Button(row_frame, text=key, font=font_medium, bg=btn_color,
                            fg=btn_fg_color, activebackground=btn_active_bg,
                            activeforeground=btn_active_fg, width=4, height=2)
            btn.config(command=lambda k=key, b=btn: press_key(k, b))
        btn.pack(side=tk.LEFT, padx=2)

# Initialize the database
create_db()

# Run the application
root.mainloop()
