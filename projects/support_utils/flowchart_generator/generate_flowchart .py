
"""
TODO

- Change the location of the "flowchart.png" file
- Change the status of each process (success, failed or running)
- Implement "subgraphs" to organize
- Format.. centralize
- Create the "refresh" method that regenerates the JSON file and updates the diagram

- NTH : Try to change the format to HTML ???

Refferences:

https://graphviz.readthedocs.io/en/stable/examples.html
https://www.graphviz.org/doc/info/shapes.html
https://sketchviz.com/graphviz-examples

"""
import tkinter as tk
from tkinter import ttk
from graphviz import Digraph
import json
import os

# winget install graphviz
os.environ["PATH"] += os.pathsep + 'C:\\Program Files\\Graphviz\\bin\\'

current_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_directory, 'flowchart.json')
png_file_path = 'flowchart.png'

def generate_flowchart(json_data):
    dot = Digraph(comment='The Flowchart')
    
    # Using the "dot" language
    for attr in json_data["attributes"]:
        dot.attr(rankdir=attr["rankdir"])

    # default shape
    dot.attr('node', shape='rect')

    for node in json_data["nodes"]:
        dot.node(node["id"], label=node["label"])
        
    for edge in json_data["edges"]:
        dot.edge(edge["from"], edge["to"])

    return dot

def refresh():
    global graph
    with open(file_path, "r") as f:
        data = json.load(f)
    graph = generate_flowchart(data)
    graph.render(filename='flowchart', format='png', cleanup=True)
    canvas.delete("all")
    img = tk.PhotoImage(file=png_file_path)
    canvas.create_image(0, 0, anchor=tk.NW, image=img)
    canvas.image = img

# Load JSON data
with open(file_path, "r") as f:
    data = json.load(f)

# Generate the initial flowchart
graph = generate_flowchart(data)
graph.render(filename='flowchart', format='png', cleanup=True)

# Create main window
root = tk.Tk()
root.title("Flowchart Viewer")

# Create canvas to display flowchart
canvas = tk.Canvas(root, width=800, height=600)
img = tk.PhotoImage(file=png_file_path)
canvas.create_image(0, 0, anchor=tk.NW, image=img)
canvas.pack()

# Create Refresh button
refresh_button = ttk.Button(root, text="Refresh", command=refresh)
refresh_button.pack()

root.mainloop()


