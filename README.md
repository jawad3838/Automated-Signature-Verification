# Automated Signature Verification
Verify the authenticity of signatures by viewing the difference score between two signatures through a web application.

## Pre-requisites
This project was implemented using the following libraries in Python 2:
* scipy version 0.18.0
* pillow version 3.0.0
* OpenCV
* theano version 0.9
* Lasagne: install using this link "https://github.com/Lasagne/Lasagne/archive/master.zip"
* web.py

### How to run the Web Application
* Create a folder and name it anything you want. 
* Extract the contents of the master file in this folder.
* Navigate yourself inside the folder that you created.
* Run the following file from command line:
  "python Web_App/Wisnett_Sig_App.py"
* Open your browser and type localhost in url bar.
* You can upload images of entire documents or cheques and crop the signature part using the "Crop Signature" button.
* Click on calculate features for the signature uploaded first.
* Click on calculate difference score for the singature uploaded second.

