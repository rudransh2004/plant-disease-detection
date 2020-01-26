from twilio.rest import Client
from keras.models import model_from_json
import numpy as np
import pyttsx3 
engine = pyttsx3.init() 
from keras.preprocessing import image
from keras import backend as K
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("disease_detector.h5")
print("Loaded model from disk")
loaded_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
if K.image_data_format() == "channels_first":
    input_shape = (3, 150, 150)
    
else:
    input_shape = (150, 150 , 3)

img_pred = image.load_img("C:/Users/hp/test3.jpg", target_size = (150,150))
img_pred = image.img_to_array(img_pred)
img_pred = np.expand_dims(img_pred, axis = 0)
rslt = loaded_model.predict(img_pred)
x = np.argmax(rslt, axis=-1)
print(x)
account_sid = "please enter your own account_sid"
auth_token "please enter your own auth_token" 
engine = pyttsx3.init()  
if x == [0] :
    print("Pepper_bell_Bacterial_spot")
   
    engine.say("plant has the following disease. Pepper bell Bacterial spot")
   
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
                body="Pepper_bell_Bacterial_spot",
                from_='+12xxxxxxxxxx',#please your own twilio phone number
                to='+91 xxxxxxxxxx',#please enter the phone number on which you want to send the message
                )
    print(message.sid)     
elif x == [1]:
    print("Pepper_bell_healthy")
    engine.say("plant has the following disease. Pepper bell healthy ")
elif x == [2]:
    print("Potato_Early_bright")
    engine.say("plant has the following disease.Potato Early bright ")
    
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
                body="Potato_Early_bright",
                from_='+12xxxxxxxx',
                to='+xxxxxxxxxxxx'
                )
    print(message.sid)     


elif x == [3]:
    print("Potato__healthy")
    engine.say("plant has the following disease. Potato healthy"   )     
    client = Client(account_sid,auth_token)
    message = client.messages \
        .create(
                body = "the plant has the following disease, Potato healthy",
                from_= '+12xxxxxxxxxxx',
                to ='+91 xxxxxxxxxxxxx'
                )
    print(message.sid)
        

elif x == [4]:
    print("Potato_Late_blight")
    engine.say("plant has the following disease. potato late blight")
    client =Client(account_sid,auth_token)
    message = client.messages \
        .create(
                body = " the plant has the following disease , Potato late blight",
                from_= "+xxxxxxxxxxxx",
                to = '+xxxxxxxxxxxxx',
                )
    print(message.sid)
elif x == [5]:
    print("Tomato_Target_Spot")
    engine.say("plant has the following disease. tomato target spot")
    client = Client(account_sid,auth_token)
    message = client.messages \
        .create(
                body = " the plant has the following disease , Tomato target spot",
                from_= "+1xxxxxxxxxxx",
                to = ' +91 xxxxxxxxxxxx',
                )
    print(message.sid)    
elif x == [6]:
    print("Tomato_Tomato_mosaic_virus")    
    engine.say("plant has the following disease tomato tomato mosaic virus")
    client = Client(account_sid, auth_token)
    message = client.messages \
         .create(
                 body = " the plant has the following disease, Tomato mosaic virus",
                 from_= "+xxxxxxxxxxx",
                 to = "+91xxxxxxxxxxxxx",
                 )
    print(message.sid)             
elif x == [7]:
    print("Tomato__Tomato_YellowLeaf__Curl_Virus")
    engine.say("Plant has the following disease. Tomato Yellow Leaf Curl Virus. ")
    client = Client(account_sid, auth_token)
    message = client.messages \
         .create(
                 body = " the plant has the following disease, Tomato YellowLeaf Curl Virus",
                 from_= "+xxxxxxxxxx",
                 to = "+91xxxxxxxxxxxx",
                 )
    print(message.sid)      
elif x == [8]:
    print("Tomato_Bacterial_Spot")    
    engine.say("plant has the following disease. Tomato Bacterial Spot")
    client = Client(account_sid, auth_token)
    message = client.messages \
         .create(
                 body = " the plant has the following disease, Tomato Bacterial Spot",
                 from_= "+xxxxxxxxxxx",
                 to = "+91xxxxxxxxxxx",
                 )
    print(message.sid)      
elif x == [9]:
    print("Tomato_Early_blight")    
    engine.say("Tomato Early Blight")
    client = Client(account_sid, auth_token)
    message = client.messages \
         .create(
                 body = " the plant has the following disease, Tomato Early Blight",
                 from_= "xxxxxxxxxxxxx",
                 to = "+91xxxxxxxxxxxxx",
                 )
    print(message.sid)      
    
elif x == [10]:
    print("Tomato_healthy") 
    engine.say("plant has the following disease. Tomato healthy")
    client = Client(account_sid, auth_token)
    message = client.messages \
         .create(
                 body = " the plant has the following disease, Tomato healthy",
                 from_= "+xxxxxxxx",
                 to = "+xxxxxxxxxxxx",
                 )
    print(message.sid)      
elif x == [11]:
    print("Tomato_Late_blight")
    engine.say("plant has the following disease. Tomato late blight")
    client = Client(account_sid, auth_token)
    message = client.messages \
         .create(
                 body = " the plant has the following disease, Tomato Late Blight",
                 from_= "+1xxxxxxxxxx,
                 to = "+91 xxxxxxxxxxxx",
                 )
    print(message.sid)      
elif x == [12]:
    print("Tomato_Leaf_Mold")
    engine.say("plant has the following disease. tomato leaf mold")
    client = Client(account_sid, auth_token)
    message = client.messages \
         .create(
                 body = " the plant has the following disease, Tomato Leaf Mold",
                 from_= "+xxxxxxxxxxxxxxx",
                 to = "+91xxxxxxxxxx",
                 )
    print(message.sid)      
elif x == [13]:
    print("Tomato_Septoria_leaf_spot")    
    engine.say("plant has the following disease. tomato septoria leaf spot")
    client = Client(account_sid, auth_token)
    message = client.messages \
         .create(
                 body = " the plant has the following disease, Tomato Septoria leaf spot",
                 from_= "+12xxxxxxxxxxx",
                 to = "+91 xxxxxxxxxxx",
                 )
    print(message.sid)      
elif x == [14]:
    print("Tomato_Spider_mites_Two_spotted_spider_mite")    
    engine.say("plant has the following disease. tomato spider mites two spotted spider mite")
    client = Client(account_sid, auth_token)
    message = client.messages \
         .create(
                 body = " the plant has the following disease, Tomato Spider Mites Two Spotted Spider Mite",
                 from_= "+xxxxxxxxxxxx",
                 to = "+xxxxxxxxxxx",
                 )
    print(message.sid)      

print(rslt)    
engine.runAndWait() 
    
    
    
    
