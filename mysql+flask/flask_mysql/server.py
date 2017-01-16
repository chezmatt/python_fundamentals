from flask import Flask, render_template, request, redirect, url_for, session
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'mydb')
# an example of running a query
# allfriends = mysql.query_db("SELECT * FROM users")
#print testinfo

testinfo =[{
    'first_name': u'Ann',
    'last_name': u'Washington',
    'id': 127L,
    }, {
    'first_name': u'Elizabeth',
    'last_name': u'Washington',
    'id': 463L,
    }, {
    'first_name': u'Emily',
    'last_name': u'Washington',
    'id': 899L,
    }, {
    'first_name': u'Larry',
    'last_name': u'Washington',
    'id': 997L,
}]
print '''************ TEST INFO **************'''
print '''                                     '''
print testinfo
print ''''                                    '''
@app.route('/')
def default():
    query = "SELECT * FROM users WHERE users.last_name = 'Washington'"
    friends = mysql.query_db(query)
    print friends
    return render_template('index.html', testinfo=testinfo, allfriends=testinfo)
    #return "welcome"
@app.route('/friends/<user_id>')
def show(user_id):
    # Write query to select specific user by id. At every point where
    # we want to insert data, we write ":" and variable name.
    query = "SELECT * FROM fr WHERE id = :specific_id"
    print query
    # Then define a dictionary with key that matches :variable_name in query.
    data = {'specific_id': user_id}
    print data
    # Run query with inserted data.
    friends = mysql.query_db(query, data)
    print friends
    # Friends should be a list with a single object,
    # so we pass the value at [0] to our template under alias one_friend.
    return render_template('index.html', allfriends=friends)
















if __name__ == "__main__":
    app.run(debug=True)
