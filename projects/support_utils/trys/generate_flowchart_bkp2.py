import json
import webbrowser
from pyflowchart import Flowchart, StartNode, OperationNode, ConditionNode, InputOutputNode, SubroutineNode, EndNode, output_html
import tkinter as tk

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
        # f.write(flowchart.flowchart())
    output_html('flowchart.html', 'flowchart_test', flowchart.flowchart())
        # output_html(output_name: str, field_name: str, flowchart: str) -> None

def refresh():
    webbrowser.open_new_tab('flowchart.html')

root = tk.Tk()
root.title("Flowchart")

# Code to create UI elements

refresh_button = tk.Button(root, text="Refresh", command=refresh)
refresh_button.pack()

generate_flowchart()

root.mainloop()
