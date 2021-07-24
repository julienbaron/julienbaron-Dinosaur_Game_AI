import json
import os
from pathlib import Path

class JsonMethod(object):
    """description of class"""
    
    @staticmethod
    def check_json():
        my_file = Path("data.txt")
        if not my_file.is_file():
            f = open("data.txt", "a+")
            f.close()
            
    @staticmethod
    def read_json(target_data):
        try:
            with open('data.txt') as json_file:
                data = json.load(json_file)
                return data['storage'][target_data]                
        except FileNotFoundError:
            print('Unable to read data from json file')

    @staticmethod
    def write_json(score):
        try:
            data = {}
            data['storage'] = []
            data['storage'].append({
                'high_score': score
                })
            with open('data.txt', 'w') as outfile:
                json.dump(data, outfile)
        except FileNotFoundError:
           print("Unable to record data")  
