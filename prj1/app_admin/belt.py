import os
import json
import logging
import time

CUR_DIR = os.path.dirname(__file__)
SCRIPT_DIR = os.path.join(CUR_DIR, os.pardir, "data", "scripts")

def get_scripts():
    pass # return a list with the names of the scripts

def get_parameters(script_name: str):
    pass # return a list of (parameter, type, default_value)

def format_command(script_name: str, parameters: str) -> str:
    pass # return a string with the command line

def exec_script(cmd: str):
    pass # just run the command



class Belt:
    '''
    
    '''
    def __init__(self, title) -> None:
        self.title = title.title()
    
    def _get_scripts(self):
        pass
    
    def _write_scripts(self):
        pass

    def add_script(self):
        pass

    def remove_script(self):
        pass


if __name__ == "__main__":
    pass
    