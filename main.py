import html
from flask import Flask, render_template,request, redirect
from datetime import *



app = Flask(__name__)

# İçerik sayfasını çalıştırma
@app.route('/')
def index():
    year = (datetime.now().year) - 2008 #nice
    return render_template('index.html', year=year)

@app.route('/einstein')
def einstein()->'html':
    return render_template('einstein.html',page_title='Wellcome to Little Einstein Project')

@app.route('/sum',methods=['POST'])
def sum()->'html':
    x=int(request.form['firstValue'])
    y=int(request.form['secondValue'])
    return render_template('result.html',page_title='Calculation result',sum_result=(x+y),first_value=x,second_value=y,)

@app.route('/ana_sayfa')
def ana_sayfa():
    return render_template("ana_sayfa.html")

@app.route('/hakkımızda')
def hakkimizda():
    return render_template("hakkimizda.html")


# Dinamik beceriler
@app.route('/', methods=['POST'])
def process_form():

    button_python = request.form.get('button_python')
    return render_template('index.html', button_python=button_python)



if __name__ == "__main__":
    app.run(port=4000, debug=True)
