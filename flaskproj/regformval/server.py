from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

# @app.route('/')
# def default():
#     return render_template('index.html')

@app.route('/')
def shoeSurvey():
    return render_template('dojos.html')

@app.route('/survey', methods=['POST'])
def assembleSurvey():
    message = ""
    fname = request.form['fname']
    loc = request.form['loc']
    lang = request.form['lang']
    comment = request.form['comment']
    print "Post info recvieved !!!!!!!!!!!!"

    if (fname or comment) =="":
      flash("Cannot be empty!") # just pass a string to the flash
    else:
      flash("Success!")
    #
    return render_template('results.html', fname =fname,loc=loc,lang=lang,comment=comment,message=message)


app.run(debug=True)      # Run the app in debug mode.
