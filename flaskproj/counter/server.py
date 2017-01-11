from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/countform', methods=['POST'])
def hello_world():
    count = 0
    if "count" in session:
      session["count"] += 1
    else:
      session['count'] = count
      #count=session['count']
    return redirect('/')
    #return render_template('index.html', name ="Matthew!", times = 5)
    #if name in session
    # validate if the data is that dictionary before you user that data else it will break!!
    #if "key" in "dictionary":
    # var = dict["key"]+=1
    # you must do this otherwise you get a key error
    # else :
    #     dict["key"]=0
    # redirects back to the '/' route









app.run(debug=True)      # Run the app in debug mode.
