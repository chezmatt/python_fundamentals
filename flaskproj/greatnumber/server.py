from flask import Flask, render_template, request, redirect, session
import random
#random.randrange(0, 101)
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def home(*message):
    newRand = random.randrange(0, 101)
    if "myRand" in session:
      myRand = session["myRand"]
      print myRand #debug
    else:
      myRand = newRand
      print myRand #debug
    session["myRand"] = myRand
    return render_template('index.html',message=message, myRand=myRand)

@app.route('/guessform', methods=['POST'])
def processForm():
    myguess = request.form['myguess']
    if "myRand" in session:
      myRand = session["myRand"]
      print myRand #debug
      ##### all logic #######
    #   try:
    #       pass
    #   except Exception as e:
    #       raise

      if myguess =="":
          message = "umm... you didn't choose a number"

      elif int(myguess) == myRand:
          message = "You Won! Try Again!"
          session.pop('myRand')#pop session
          return home(message)

      else:
          message = "You Chose "+ str(myguess) + " Loose."







    else:
      return render_template('index.html', message="No myRand", myRand=myRand)
    return render_template('index.html', message=message, myRand=myRand)
        #return redirect('/')









app.run(debug=True)      # Run the app in debug mode.
