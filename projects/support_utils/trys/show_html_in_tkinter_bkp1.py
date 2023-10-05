import tkinter as tk
from tkinter import filedialog
from tkinterhtml import TkinterHtml
from tkhtmlview import HTMLText, RenderHTML


file_path = filedialog.askopenfilename(filetypes=[("HTML Files", "*.html")])

# # Create a button to open HTML file
# open_button = tk.Button(app, text="Open HTML File", command=open_html)
# open_button.pack(pady=20)

# # Create TkinterHtml widget
# html_viewer = TkinterHtml(master=app)
# html_viewer.pack(expand=True, fill=tk.BOTH)

root = tk.Tk()
root.title("HTML Viewer")
html_label = HTMLText(root, html=RenderHTML(file_path))
html_label.pack(fill="both", expand=True)
html_label.fit_height()
root.mainloop()

