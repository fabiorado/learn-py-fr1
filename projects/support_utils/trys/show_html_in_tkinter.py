import tkinter as tk
from tkinter import filedialog
from tkhtmlview import HTMLLabel

def open_html():
    file_path = filedialog.askopenfilename(filetypes=[("HTML Files", "*.html")])
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            html_label.set_content(content)

app = tk.Tk()
app.title("HTML Viewer")

# Create a button to open HTML file
open_button = tk.Button(app, text="Open HTML File", command=open_html)
open_button.pack(pady=20)

# Create TkinterHtml widget
html_label = HTMLLabel(app, html="")
html_label.pack(expand=True, fill=tk.BOTH)

app.mainloop()
