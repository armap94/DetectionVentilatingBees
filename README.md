# DeepLearningBees
Detection of Ventilating Bees - Summer 2020 - Freie Universitaet Berlin

## Detection of Ventilating Bees - Summer 2020 - Freie Universitaet Berlin

**Group Members:**
1.Arman Paknia (armap94@zedat.fu-berlin.de)
2.Sina Moslehi (moslehi85@aol.de)
3.Maja von Borstal 
4.Sebastian Lehninger (seb@zedat.fu-berlin.de)

**Link to Our Google Colab** : [Link] (https://colab.research.google.com/drive/11bneBKTn1g8uhO63kbs4p0TeaPmpd-lE?usp=sharing)

Upon request for access we will recieve and email and verify access. 

Link to **Google Drive** containing all necessary files :[Link] (https://drive.google.com/drive/folders/11QKyyls6lnmCQnkwisJ1vtQ1-ACOJgB6?usp=sharing)

# Steps to Using the code on Google Colab:

* Step 1:
Upon opening the google Colab file and the Google Drive storage. Duplicate all the files located in Drive into your own Google Drive and save a copy of the Google Colab file into your own Google account. 

* Step 2:
Copy all the data inside "Bienen" into your personal Drive under the same folder name as "Bienen" and maintain the same hierarchy of files. 

* Step 3:
After running the section of code on Colab about mounting your Drive (provided that content of "Bienen" has been copied to your local drive with accurate hierarchy) running test or training tasks should be straightforward. 

* Step 4:
Using the variety of weight files stored under 'mydrive/bienen/backup' you can evaluate the performance of the model using the 'map' or 'detect' commands or train any model further.  

# Extra Notes:
* For training a model from start use the darknet53.conv.74 file from '/pretrained_weghts'
* Obj : Containing images and label data of original images
* Obj_opt : Optimized images with sharpening and noise reduction (+ label data) 
* obj_clahe : Images improved with sharpening, noise reduction and Contrast Limited Histogram Equalization (+ label data)
* train.ipynb : used to create train.ipynb for generating label files, valid.txt and train.txt files
* utils_data.py : a collection of utility and functions used in train.ipynb for generating label files, valid.txt and train.txt files



