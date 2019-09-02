import sys
sys.path.insert(0,'C:/Users/Syed Jawwad Hamdani/Downloads/WisNet_SigVer')               #CHANGE PATH TO POINT TOWARDS ROOT FOLDER I.E. WisNet_SigVer

import numpy as np
from scipy.misc import imread, imsave
from preprocess.normalize import normalize_image, resize_image, crop_center, preprocess_signature
import signet
from cnn_model import CNNModel
import cv2

image_dir = "Web_App/static/anchor_images/"
find_dir = "Web_App/static/quest_images/"

canvas_size = (952, 1360)

def get_features(img):

        model_weight_path = '../models/signet.pkl'
        model = CNNModel(signet, model_weight_path)
        
        processed_sig = np.array([preprocess_signature(img, canvas_size)])
        feature_vect = model.get_feature_vector_multiple(processed_sig, layer='fc2')

        return feature_vect
