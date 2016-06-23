from flask import Flask, render_template, redirect, url_for, request

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    return "Hello, World!"  # return a string

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template

# route for handling the login page logic
@app.route('/login', methods=['get', 'post'])
def login():
    error = None
    if request.method == 'post':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
			session['logged_in'] = True
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	return redirect(url_for('welcome'))
	
# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)