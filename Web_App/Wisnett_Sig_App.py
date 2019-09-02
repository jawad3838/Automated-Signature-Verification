import web
import os
from Extract_features import get_features
import cv2
import numpy as np
from signature_crop import get_cropped_image


canvas_size = (900, 700)
render = web.template.render('templates/')

urls = ('/', 'index')

app = web.application(urls, globals())

current_anchor = None
current_anchor_img = None
current_anchor_img_cropped_dir = None
target_img_cropped_dir = None
face_name = None
img_name=None
faces = None
add_image = None
find_image = None

#model="trained_model/model.pb"
#class_names=np.load('classnames.npy')
#embeds=np.load('embed.npy')
#labels=np.load('labels.npy')
image_dir='static/anchor_images/'
find_dir='static/quest_images/'

anchor_feat_dir = 'static/anchor_features/'
quest_feat_dir = 'static/quest_features/'

class index:
	def GET(self):
		return render.index(None,None,None,None,None)


	def POST(self):
		#save user inputs
		i = web.input()
                global current_anchor_img
                global current_anchor_img_cropped_dir
                global face_name
                global img_name
                global current_anchor 
                global target_img_cropped_dir 
                global faces 
                global add_image
                global find_image
		# if add face form submit
		if i.form_name == "add_face":
			files = web.webapi.rawinput().get('file1')
			face_name = i.new_face_name 
                        img_name = None                          

                        target = image_dir+face_name
                        if face_name not in os.listdir(image_dir):
                                os.mkdir(image_dir+face_name)

                        content = files.file.read()
                        with open(target +'/'+ files.filename,'wb') as f:
                                f.write(content)
                        
                        img_name = os.path.splitext(files.filename)[0]
                        
                        current_anchor_img = target +'/'+ files.filename
                        
                        current_anchor_img_cropped = get_cropped_image(target +'/'+ files.filename)
                        cv2.imwrite(target+'/'+img_name+'_cropped.png',current_anchor_img_cropped)

                        current_anchor_img_cropped_dir = target + '/' + img_name +'_cropped.png'
                        
                        #if face_name not in os.listdir(anchor_feat_dir):
                        #        os.mkdir(anchor_feat_dir+face_name)
  
                        #current_feat_dir = anchor_feat_dir+face_name+'/'
                        #current_img_dir = image_dir+face_name+'/'


                        #img = cv2.imread(current_anchor_img,0)
                        #img = cv2.resize(current_anchor_img_cropped,canvas_size)
                        #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                        #feature_vect = get_features(img)

                        #current_anchor = current_feat_dir+img_name
                        #np.save(current_anchor,feature_vect)

                        add_image = current_anchor_img
			faces=None
			find_image=None
					
                elif i.form_name == "calc_feat":				
                        add_image = None
                        faces=None
                        find_image=None

                        if face_name not in os.listdir(anchor_feat_dir):
                                os.mkdir(anchor_feat_dir+face_name)
  
                        current_feat_dir = anchor_feat_dir+face_name+'/'
                        current_img_dir = image_dir+face_name+'/'


                        img = cv2.imread(current_anchor_img_cropped_dir,0)
                        img = cv2.resize(img,canvas_size)
                        #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                        feature_vect = get_features(img)

                        current_anchor = current_feat_dir+img_name+'_cropped'
                        np.save(current_anchor,feature_vect) 
                                               

		elif i.form_name == "find_face":
			files = web.webapi.rawinput().get('file2')
			content = files.file.read()
			target = find_dir + files.filename					
			with open(target, 'wb') as f:
				f.write(content)
			
                        find_image=target

                        filename = os.path.splitext(files.filename)[0]
                        print("working1")
                        target_img_cropped = get_cropped_image(target)
                        print("working2")
                        cv2.imwrite(find_dir+filename+'_cropped.png',target_img_cropped)                        
                        target_img_cropped_dir = find_dir+filename+'_cropped.png'
                        
                elif i.form_name == "calc_feat2":
                        current_anchor_feat = np.load(current_anchor +'.npy')

                        img = cv2.imread(target_img_cropped_dir,0)
                        img = cv2.resize(img,canvas_size)
                        feature_vect = get_features(img)

                        difference = np.linalg.norm(current_anchor_feat - feature_vect)
                        print(difference)
                        
                        faces = difference
                        
		return render.index(faces, add_image, find_image, current_anchor_img_cropped_dir, target_img_cropped_dir)

if __name__ == "__main__":
    app.run()