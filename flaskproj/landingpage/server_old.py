from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def default():
    return render_template('index.html')

@app.route('/dojo')
def shoeSurvey():
    return render_template('dojos.html')

@app.route('/survey', methods=['POST'])
def assembleSurvey():
    print "Post info recvieved !!!!!!!!!!!!"
    name1 = request.form['fname']
    loc = request.form['loc']
    lang = request.form['lang']
    comment = request.form['comment']

    # formres = {
    # name1 : name1,
    # loc : loc,
    # lang : lang,
    # comment : comment
    # }
    return render_template('results.html', name1 =name1,loc=loc,lang=lang,comment=comment)
    #return redirect('/results')

# @app.route('/results')
#
# def results(formres):
#     name = formres['name1']
#     loc = formres['loc']
#     lang = formres['lang']
#     comment = formres['comment']
#     return render_template('results.html',name,loc,lang,comment)

app.run(debug=True)      # Run the app in debug mode.

    # if name in session
    # validate if the data is that dictionary before you user that data else it will break!!
    # if "key" in "dictionary":
    #   var = dict["key"]+=1
    # you must do this otherwise you get a key error
    # else :
    #     dict["key"]=0
     # redirects back to the '/' route
