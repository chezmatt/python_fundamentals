from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
  return render_template('index.html', name ="Matthew!", times = 5)

@app.route('/ninjas')
def ninjas():
   return render_template('ninjas.html')

@app.route('/dojos/new')
def newDojos():
   return render_template('dojos.html')
# if name in session
# validate if the data is that dictionary before you user that data else it will break!!
# if "key" in "dictionary":
#   var = dict["key"]+=1
# you must do this otherwise you get a key error
# else :
#     dict["key"]=0




app.run(debug=True)      # Run the app in debug mode.
