from flask import *

from PIL import Image,ImageFilter,ImageEnhance
import os

app=Flask(__name__)
APP_ROOT=os.path.dirname(os.path.abspath(__file__))
@app.route('/')
def success():
   return render_template('login.html')

@app.route('/hi',methods = ['POST', 'GET'])
def login():
    bri=float(request.form['brig'])
    sharp=float(request.form['sharp'])
    con=float(request.form['cont'])
    col=float(request.form['col'])
    t=os.path.join(APP_ROOT,'static\\')
    if not os.path.isdir(t):
      os.mkdir(t)
    print(t+"....TTTT")
    files =request.files.getlist("file")
    dn=files[0].filename
    print(dn)
    des=''.join([t,dn])
    print(des)
    files[0].save(des)
    img=Image.open(des)
    im3 = ImageEnhance.Sharpness(img)
    finimg=im3.enhance(sharp)
    finimg=ImageEnhance.Brightness(finimg)
    finimg=finimg.enhance(bri)
    finimg=ImageEnhance.Contrast(finimg)
    finimg=finimg.enhance(con)
    finimg=ImageEnhance.Color(finimg)
    finimg=finimg.enhance(col)
    finimg=finimg.filter(ImageFilter.DETAIL)
    temp=dn[0:len(dn)-4]
    
    
    print(temp)
    finimg.save(t+temp+"1.jpg")
   
    return render_template("hi.html",name=temp+"1.jpg")


    


    


app.run()