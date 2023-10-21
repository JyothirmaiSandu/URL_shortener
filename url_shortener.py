import tkinter as tk
from tkinter import messagebox
import pyshorteners

def shorten_url():
    long_url = entry.get()
    try:
        short_url = s.tinyurl.short(long_url)
        output_entry.delete(0, tk.END)
        output_entry.insert(0, short_url)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

root = tk.Tk()
root.title("URL Shortener")

s = pyshorteners.Shortener()

label = tk.Label(root, text="Enter Long URL:")
label.pack(pady=(10, 0))

entry = tk.Entry(root, width=50)
entry.pack(pady=(0, 10))

button = tk.Button(root, text="Shorten URL", command=shorten_url)
button.pack()

output_entry = tk.Entry(root, width=50)
output_entry.pack(pady=(10, 0))

root.mainloop()
