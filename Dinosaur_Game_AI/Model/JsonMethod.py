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
        with open('data.txt') as json_file:
            return True if os.path.getsize('data.txt') > 0 else False
      
            
    @staticmethod
    def read_json(target_data, existing_data):
        try:
            with open('data.txt') as json_file:
                if existing_data == True:
                    data = json.load(json_file)
                    return data[target_data][0].get('high_score') #need to be reviewed
        except FileNotFoundError:
            print('Unable to read data from json file')

    @staticmethod
    def write_json(target_data, score):
        data = {}
        data[target_data] = []
        data[target_data].append({
            'high_score': score
            })
        with open('data.txt', 'w') as outfile:
            json.dump(data, outfile) 
