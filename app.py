
from flask import Flask,flash, render_template, redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy
import time

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'db_housing'

db = SQLAlchemy(app)

class ContactUs (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(50), nullable=False)
    Email = db.Column(db.String(50), nullable=False)
    Message = db.Column(db.String(500), nullable=False)

class User (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(50), nullable=False)
    Email = db.Column(db.String(50), nullable=False, unique=True)
    Password = db.Column(db.String(500), nullable=False)

@app.route("/")
def home():
    return render_template('home.html')



@app.route("/aboutus")
def aboutus():
    return render_template('aboutus.html')

@app.route("/search")
def search():
    return render_template('advsearch.html')

@app.route('/contactus', methods=['GET', 'POST'])
def contactus():
    if request.method == 'POST':
        Name = request.form['name']
        Email = request.form['email']
        Message = request.form['message']
        print(Message)
        contact = ContactUs(Name=Name, Email=Email, Message=Message)
        db.session.add(contact)
        db.session.commit()
        flash('Message Sent Successfully to the Student Housing team')
        return redirect(url_for('home'))
    return render_template('contactus.html')

@app.route("/sl")
def sl():
    return render_template('sl.html')

@app.route("/usf")
def usf():
    return render_template('usf.html')

@app.route("/ut")
def ut():
    return render_template('ut.html')


@app.route("/signin" , methods=['GET', 'POST'])
def signin():
    print(request.method)
    if request.method == 'POST':
        print(request.form)
        Email = request.form['email']
        Password = request.form['psw']
        print(Password)
        users = User.query.all()
        print(users)

        for user in users:
            print(user.Email,user.Password)

        user = User.query.filter_by(Email=Email).first()
        print(user)
        if user is not None and user.Password==Password:
            flash(' Successfully logged to the Student Housing team')
            return redirect(url_for('home'))
        else:
            print('Invalid username or password')
            return render_template('signin.html')


    return render_template('signin.html')


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        print(request.form)
        Name = request.form['name']
        Email = request.form['email']
        Password = request.form['psw']
        print(Password)
        user = User(Name=Name, Email=Email, Password=Password)
        db.session.add(user)
        db.session.commit()
        flash('Registered Successfully to the Student Housing team')
        return redirect(url_for('signin'))
    return render_template('signup.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)



    from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Home Page route
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search")
def search():
    return render_template("advsearch.html")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

@app.route("/sl")
def sl():
    return render_template("sl.html")

@app.route("/usf")
def usf():
    return render_template("usf.html")

@app.route("/ut")
def ut():
    return render_template("ut.html")



# conn = sqlite3.connect('database.db')
# print("Opened database successfully")
# '''conn.execute('DROP TABLE IF EXISTS contactus')
# conn.commit()
# conn.execute('CREATE TABLE IF NOT EXISTS contactus(id Integer Primary key, name String(50), email String(50), message String(500))')
# print("Table created successfully")
# conn.execute('DROP TABLE IF EXISTS user')
# conn.commit()
# conn.execute('CREATE TABLE  IF NOT EXISTS user(id Integer Primary key, name String(50), email String(50), password String(50))')
# print('Table Users created successfully', flush=True)
# conn.close()'''



# @app.route('/contactus', methods=['GET', 'POST'])
# def contactus():
#     if request.method == 'POST':
#         try:
#             name = request.form['name']
#             email = request.form['email']
#             message = request.form['message']

#             with sqlite3.connect('database.db') as con:
#                 cur = con.cursor()
#                 cur.execute("INSERT INTO contactus(name, email, message) VALUES(?, ?, ?)", (name, email, message))
#                 con.commit()
#                 msg = "Message Sent Successfully to the Student Housing team"
#         except:
#             con.rollback()
#             msg = "Falied to send the details"
#         finally:
#             return render_template("home.html",msg=msg)
        

# @app.route("/signin" , methods=['GET', 'POST'])
# def signin():
#     error = None
#     print(request.method)
#     if request.method == 'POST':
#         print(request.form)
#         Email = request.form['email']
#         Password = request.form['psw'] 

#         con = sqlite3.connect('database.db')
#         cursor = con.cursor()
#         cursor.execute('select * from user where email = ? AND psw = ?',(Email,Password))
#         user = cursor.fetchone()
#         if user is not None and user.Password==Password:
#             flash(' Successfully logged to the Student Housing team')
#             return redirect(url_for('home'))
#         else:
#             flash('Invalid username or password')
#             return render_template('signin.html')
#         return render_template('signin.html')
        


# @app.route("/signup", methods=['GET', 'POST'])
# def signup():
#     if request.method == 'POST':
#         print(request.form)
#         Name = request.form['name']
#         Email = request.form['email']
#         Password = request.form['psw']
#         print(Password)

#         con = sqlite3.connect('database.db')
#         cursor = con.cursor()
#         cur.execute("INSERT INTO contactus(name, email, psw) VALUES(?, ?, ?)", (Name,Email,Password))
#         con.commit()
#         msg = "Registered Successfully to the Student Housing team"
#         return redirect(url_for('signin'))
#     return render_template('signup.html')
    

# #del 

# # conn = sqlite3.connect('database.db')
# # c = conn.cursor()
# # c.execute('DELETE FROM user')
# # c.execute('DELETE FROM contactus')
# # conn.commit()
# # conn.close()
