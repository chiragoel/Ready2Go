This is a code  to detect whether lesion is present on skin or not.
File data_gen1.py contains the code to extract features from the  given image dataset. The 
corresponding features have been stored in input_ image_pro.csv file.
I have downloaded the image dataset through a package on pypi.org.(google_images_downloader)


But since the dataset is very small so I have generated a synthetic dataset which is coded in the 
file data.py and the corresponding data stored in input.csv file.
In model.ipynb file I have compared the accuracies of 3 models - 
1. SVM
2. Random Forest
3. Logistic Regression
and  found out that SVM had the best accuracy of 52.3% .
Since this is a randomnly generated dataset the accuracy of corresponding models is bound to be low.
There is a chance that a real dataset will give us a better accuracy for all the mdels.     