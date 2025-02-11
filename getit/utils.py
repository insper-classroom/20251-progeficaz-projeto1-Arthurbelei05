import json
import os

def load_data(filename):
    with open(f'static/data/{filename}', "r") as arquivo:
        data = json.load(arquivo)
    return data

def load_template(nome_template):
    with open(f'static/templates/{nome_template}', "r") as string:
        string = string.read()
        return string
    
    
