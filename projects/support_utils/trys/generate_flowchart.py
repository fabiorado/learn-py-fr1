import json
import webbrowser
from pyflowchart import Flowchart, StartNode, OperationNode, ConditionNode, InputOutputNode, SubroutineNode, EndNode, output_html
import tkinter as tk
from tkinter import ttk

def generate_flowchart():
    # Read JSON file
    with open('projects\support_utils\data_flowchart.json') as f:
        data = json.load(f)

    # Create start node
    start_node = StartNode('Start')

    # Create operation node
    operation_node = OperationNode('Operation')

    # Create condition node
    condition_node = ConditionNode('Condition')

    # Create input/output node
    input_output_node = InputOutputNode(InputOutputNode.INPUT, 'Input/Output')

    # Create subroutine node
    subroutine_node = SubroutineNode('Subroutine')

    # Create end node
    end_node = EndNode('End')

    # Connect nodes
    start_node.connect(operation_node)
    operation_node.connect(condition_node)
    condition_node.connect_yes(input_output_node)
    condition_node.connect_no(subroutine_node)
    subroutine_node.connect(operation_node, 'right')
    input_output_node.connect(end_node)

    # Create flowchart
    flowchart = Flowchart(start_node)

    # Output generated flowchart.js DSL to console
    print(flowchart.flowchart())

    # Output generated flowchart to HTML file
    # with open('flowchart.html', 'w') as f:
    #     f.write(flowchart.flowchart_html())
    output_html('flowchart.html', 'flowchart_test', flowchart.flowchart())

def refresh():
    with open('flowchart.html', 'r') as f:
        html = f.read()
        text.delete(1.0, tk.END)
        text.insert(tk.END, html)

root = tk.Tk()
root.title("Flowchart")

# Code to create UI elements

refresh_button = ttk.Button(root, text="Refresh", command=refresh)
refresh_button.pack()

text = tk.Text(root)
text.pack()

generate_flowchart()

root.mainloop()
