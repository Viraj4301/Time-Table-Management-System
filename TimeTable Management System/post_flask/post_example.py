from flask import *  
app = Flask(__name__)  
  
@app.route('/login',methods = ['POST'])  
def login():  
      uname=request.form['uname']  
      passwrd=request.form['pass']  
      if uname=="ketan" and passwrd=="12345":  
          return "Welcome %s" %uname  
   
if __name__ == '__main__':  
   app.run(debug = True)  