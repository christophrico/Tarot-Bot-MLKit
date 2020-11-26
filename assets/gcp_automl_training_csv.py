import os
import pandas as pd

"""
Use this script to generate the CSV for training an AutoML vision model
Images for each class should be sorted into a folder named for each class,

Run this script from the same directory as the folders.
"""

#change this to the base path of the GCP bucket where your images are
base_gcp_path = "gs://christophrico-462-classification-bucket"

#get all the names of the class folders
class_folders = []
path = "./"
p = os.listdir(path)
for i in p:
    if os.path.isdir(i):
        class_folders.append(i)

#now go through one by one and generate csv of path and class
#csv format:
# set, image_path, class_label
df=pd.DataFrame(columns=['set', 'path', 'label'])

#within each class folder
for img_class in class_folders:
    folder = "{}/{}".format(path, img_class)
    #get the names of the pics
    image_names = os.listdir(folder)
    #for each pic
    for image in image_names:
        #generate the gcp path
        gcp_image_path = "{}/{}/{}".format(base_gcp_path, img_class, image)
        #append it to the df
        df = df.append({
                        "set" : "UNASSIGNED",
                        "path" : gcp_image_path,
                        "label" : img_class
                      },
                      ignore_index = True
                    )

#now save the csv
filename = "classifier_training_data.csv"
df.to_csv(filename)
