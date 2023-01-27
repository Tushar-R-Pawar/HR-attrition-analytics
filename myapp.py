from flask import Flask, render_template, request
import numpy as np
from mlmodel import *

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("page1.html")

@app.route("/getprediction", methods=["POST"])
def getpredict():
    a1=request.form['a1']
    a2=request.form['a2']
    a3=request.form['a3']
    a4=request.form['a4']
    a5=request.form['a5']
    a6=request.form['a6']
    a7=request.form['a7']
    a8=request.form['a8']
    a9=request.form['a9']
    a10=request.form['a10']
    a11=request.form['a11']
    a12=request.form['a12']
    a13=request.form['a13']
    a14=request.form['a14']
    a15=request.form['a15']
    a16=request.form['a16']
    a17=request.form['a17']
    a18=request.form['a18']
    a19=request.form['a19']
    a20=request.form['a20']
    a21=request.form['a21']
    a22=request.form['a22']
    a23=request.form['a23']
    a24=request.form['a24']
    a25=request.form['a25']
    a26=request.form['a26']
    a27=request.form['a27']
    
    
    newob=[a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26,a27]
    print(newob)
    model = makeprediction()
    ans = model.predict(np.array([newob],dtype=float))
    yp=[]
    if ans==1:
        yp.append('definatly')
    elif ans==0:
        yp.append('not')

   
    
    
    
    return render_template("page2.html",data=yp[0])
    

if(__name__ =="__main__"):
    app.run(debug=True)

