import requests
import urllib
from PIL import Image
import os
import pandas as pd
import numpy as np

data = pd.read_json('Indian_Number_plates.json',lines=True)
pd.set_option('display.max_colwidth', -1)

# delete the extras column
del data['extras']

# Extract the points of the bounding boxes because thats what we want
data['points'] = data.apply(lambda row: row['annotation'][0]['points'], axis=1)

# And drop the rest of the annotation info
del data['annotation']

# The directories needed
current_dir = os.path.dirname(os.path.realpath('Implementation')) # Implementation refers to the file name
image_data_dir = os.path.join(current_dir, 'Plates/')
if not os.path.exists(image_data_dir):
    os.makedirs(image_data_dir)

for index, row in data.iterrows():
    # Get the image from the URL
    resp = urllib.request.urlopen(row[0])
    im = np.array(Image.open(resp)) # This is a numpy 3D array 
    x_point_top = row[1][0]['x']*im.shape[1]
    y_point_top = row[1][0]['y']*im.shape[0]
    x_point_bot = row[1][1]['x']*im.shape[1]
    y_point_bot = row[1][1]['y']*im.shape[0]

    # Cut the plate from the image and use it as output
    plateImage = Image.fromarray(im).crop((x_point_top, y_point_top, x_point_bot, y_point_bot))
    plateImage.convert("RGB").save(image_data_dir+str(index)+".jpg")