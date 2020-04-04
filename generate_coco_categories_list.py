  

import os
import pandas as pd
import json

if __name__ == "__main__":
    # get annotation path
    filename = 'instances_val2017.json'
    with open(filename, 'rt') as file:
        doc = json.load(file)
    
    
    # run through the categories
    categories = doc['categories']
    
    # convert to dataframe
    df_main = pd.DataFrame(categories)
    
    # get csv
    df_main.to_csv('coco_categories.csv', index=False)
    
    
    
    