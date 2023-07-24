# Simple REST service that provides a random health tip
import os
import csv
import random

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def getTip():
    Inputfile = "hctips.csv"
    file = open(Inputfile, 'r')
    hcTips = file.readlines()
    hcTip = hcTips[random.randint(1,len(hcTips))]
    return render_template('home.html', hcTip = hcTip)


if __name__ =='__main__':
    port = os.environ.get('FLASK_PORT') or 3333
    port = int(port)
  
    app.run(port=port,host='0.0.0.0')
              
    
