import json
import urllib.request
import numpy as np

import requests
from PIL import Image
from io import BytesIO
import os
import cv2


#Opening the JSON files and saving the data
def LoadData(path):

    with open(path, "r") as myfile :
        data = myfile.read()
    data = json.loads(data)
    return data

#Removing the images that have no labels
def Remove_Unlabeled_Images(data):
    # Labled_data =  correctly labeled images
    Labled_data = []
    for x in range(len(data)):
        if data[x]["Label"] != {}:
            Labled_data.append(data[x])
    return Labled_data

# Pulling the images from labelbox server and saving them on PC  with accurate ID
def SaveData(Labled_data):
    train = []
    #store_path = "c:/Users/sinam/PycharmProjects/SoftwareProject/biene/obj/"
    for x in range(len(Labled_data)):
        url = Labled_data[x].get("Labeled Data")
        id = Labled_data[x].get("ID")

        url_response = urllib.request.urlopen(url)

        # Storing on PC in the folder we have selected

        urllib.request.urlretrieve(url,"c:/Users/sinam/PycharmProjects/SoftwareProject/biene/org/{}.jpg".format(id))
# Reads the data from Labelbox server and it can also optimize or resize (if needed)
def ResizeAndSave(Labled_data):

    store_path = "c:/Users/sinam/PycharmProjects/SoftwareProject/biene/org/"
    for x in range(len(Labled_data)):
        url = Labled_data[x].get("Labeled Data")
        id = Labled_data[x].get("ID")
        response = requests.get(url)
        print(x)
        pilImage = Image.open(BytesIO(response.content))
        pilImage = optimize(pilImage)
        #pilImage = pilImage.resize((1000, 1000), Image.ANTIALIAS)
        # Storing on PC in the folder we have selected

        cv2.imwrite("opt/{}.jpg".format(id),pilImage,[cv2.IMWRITE_JPEG_QUALITY, 70])

#This section estraxts the label details and coordinats of each label line.
def GetPoints(Labled_data, w=140, h=140):
    # dicts to keep the boxes
    annots = {}
    # imgs = []
    # IDs = []
    for x in range(len(Labled_data)):
        label = Labled_data[x]["Label"]["objects"]
        ID = Labled_data[x]["ID"]
        annots[ID] = []

        for i in range(len(label)):
            if "line" in label[i].keys():
                punkt = label[i].get("line")
                line = []
                # iterate over a line's points
                for i in punkt:
                    line.append(i.get("x"))
                    line.append(i.get("y"))

                # calculate the center of the line and append the defined width and height to the list
                center = [(line[0] + line[2]) / 2, (line[1] + line[3]) / 2] + [w, h]
                annots[ID].append(center)

    return annots

#Creates the text files of valid.txt and train.txt
def Generate_annot(annots, path_dataset, path_label ):
    w = 4000
    h = 3000
    #Randomly chooses 10% of dataset as validation data
    percent = 10
    prct = int(np.ceil((len(annots) * percent) / 100))

    # path to store the label text files
    store_path_train_valid = path_dataset #"C:/Users/sinam/PycharmProjects/biene"
    store_path_label = path_label #"C:/Users/sinam/PycharmProjects/biene/Label"
    range_list = np.arange(0, len(annots))
    random_list = np.random.choice(range_list, prct)
    print(random_list)

    for k in annots.keys():

        # create text file to write the boxes in
        with open(os.path.join(store_path_label, k + '.txt'), '+w') as r:
            # iterate over boxes
            for b in annots[k]:

                # normalize and write the boxes into the text file in the following format
                # class cx cy w h
                r.write('0 {} {} {} {} \n'.format(b[0] / w, b[1] / h, b[2] / w, b[3] / h))
        # creates the valid.txt file that we provide to yolo
        with open(os.path.join(store_path_train_valid, "val-colab" + '.txt'), '+w') as va:
            for i, k in enumerate(annots.keys()):
                if i in random_list:
                    va.write(store_path_train_valid + "/" + k + '.jpg\n')
        # creates the train.txt file that we provide to yolo
        with open(os.path.join(store_path_train_valid, "train-colab" + '.txt'), '+w') as tr:
            for i, k in enumerate(annots.keys()):
                if i not in random_list:
                    tr.write(store_path_train_valid + "/" + k + '.jpg\n')
# We use these functions to reduce noise, increase sharpness or apply CLAHE

def optimize(Image):
    img = cv2.cvtColor(np.array(Image), cv2.COLOR_RGB2GRAY)
    denoise = cv2.fastNlMeansDenoising(img,None,5,5,7)
    kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    sharp = cv2.filter2D(denoise, -1, kernel)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    cla = clahe.apply(sharp)

    return cla