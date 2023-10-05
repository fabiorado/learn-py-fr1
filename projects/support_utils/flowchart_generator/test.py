import os

# current_directory = os.getcwd()
current_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_directory, 'projects') #.join('support_utils').join('flowchart_generator').join('flowchart.json')

print(current_directory)
# print(file_path)