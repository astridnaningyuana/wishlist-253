import sqlite3 as lite
from flask import Flask, render_template, request, url_for, redirect , session

app = Flask(__name__)




@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('main'))



@app.route("/") #tergantung permintaan user
def main(): #backend
    if 'username' in session:
        username_session = session['username']
        return render_template('index_login.html', session_user_name=username_session)

        if 'first_name' in session:
            first_name_session = session['first_name']
            return render_template('index_login.html', session_user_first_name=first_name_session)
    else:
        return render_template ('index.html') #backend



@app.route('/goSignIn/', methods=['GET','POST'])
def goSignIn():
    error=""
    if request.method == 'POST':
        username_form = request.form['username']
        password_form = request.form['password']

        con=lite.connect('app1.db')
        cur=con.cursor()
        cur.execute("SELECT COUNT(1) FROM User WHERE username = (?)", [username_form])
        if cur.fetchone()[0]:
            cur.execute("SELECT password FROM User WHERE username =(?)", [username_form])
            for row in cur.fetchall():
                if password_form == row[0]:
                    session['username'] = request.form['username']

                    return redirect(url_for('main'))
                else:
                    error = "Invalid Credential - Error Password"
            else:
                error = "Invalid Credential - Error Username!!!"
    return render_template('login.html', error=error)

# @app.route('/updatecar')
# def updatecar():
#     con=lite.connect("app1.db")
#     con.row_factory = lite.Row
#
#     cur = con.cursor()
#     cur.execute("select * from Cars")
#
#     rows = cur.fetchall();
#     con.close()
#     return render_template("updatecar.html", rows = rows)

# @app.route('/savecar', methods=['GET', 'POST'])
# def savecar():
#     if request.method == 'POST':
#         idcar = request.form['idcar']
#         namecar =request.form['namecar']
#         pricecar = request.form['pricecar']
#
#         con = lite.connect('app1.db')
#
#         with con:
#             cur=con.cursor()
#             cur.execute("INSERT INTO Cars Values (?,?,?)", (idcar,namecar,pricecar))
#             con.commit()
#
#         return redirect(url_for('carlist'))

@app.route('/login')
def login():
    return render_template ("login.html")

# @app.route('/ceklogin', methods=['GET','POST'] )
# def ceklogin():
#     con=lite.connect("app1.db")
#     con.row_factory = lite.Row
#
#     cur = con.cursor()
#     cur.execute("select * from Users")
#
#     rows = cur.fetchall();
#     if request.method == 'POST':
#         username= request.form['username']
#         password= request.form['password']
#         cur.execute("select * from Users where username = (?)",[username])
#         rows = cur.fetchall();
#         con.close()
#
#         if password == rows.password:
#             return "Login Success!"
#         else:
#             return "Login Gagal!"



@app.route('/updatecar')
def updatecar():
    con=lite.connect("app1.db")
    con.row_factory = lite.Row

    cur = con.cursor()
    cur.execute("select id from Cars")

    rows = cur.fetchall();
    con.close()
    return render_template("updatecar.html", rows = rows)

@app.route('/upcar', methods=['GET', 'POST'])
def upcar():
    if request.method == 'POST':
        idcar = request.form['idcar']
        namecar =request.form['namecar']
        pricecar = request.form['pricecar']
        idselect = request.form['idselect']

        con = lite.connect('app1.db')
        cur = con.cursor()

        with con:
            cur.execute("UPDATE Cars SET Id=?, Name=?, Price=? WHERE Id=?", (idcar, namecar, pricecar, idselect))
            con.commit()

    return redirect(url_for('carlist'))

@app.route('/carlist_delete/<int:idcar>', methods=['GET' , 'POST'])
def carlist_delete(idcar):
    try:
        idcar=str(idcar)
        con=lite.connect('app1.db')
        cur=con.cursor()

        with con:
            cur.execute("DELETE FROM Cars WHERE Id=(?)",[idcar])
            con.commit()

            return redirect(url_for('carlist'))

    except:
        return redirect(url_for('carlist'))



@app.route('/deletecar')
def deletecar():
    con=lite.connect("app1.db")
    con.row_factory = lite.Row

    cur = con.cursor()
    cur.execute("select id from Cars")

    rows = cur.fetchall();
    con.close()
    return render_template ("deletecar.html", rows = rows)


@app.route('/delcar', methods=['GET', 'POST'])
def delcar():
    if request.method == 'POST':
        idcar = request.form['idcar']

        con = lite.connect('app1.db')
        cur=con.cursor()

        with con:
            cur.execute("DELETE FROM Cars WHERE Id=(?)",[idcar])
            con.commit()

    return redirect(url_for('carlist'))



@app.route('/insertcar')
def insertcar():
    return render_template ("insertcar.html")

@app.route('/savecar', methods=['GET', 'POST'])
def savecar():
    if request.method == 'POST':
        idcar = request.form['idcar']
        namecar =request.form['namecar']
        pricecar = request.form['pricecar']

        con = lite.connect('app1.db')

        with con:
            cur=con.cursor()
            cur.execute("INSERT INTO Cars Values (?,?,?)", (idcar,namecar,pricecar))
            con.commit()

        return redirect(url_for('carlist'))

@app.route("/carlist")
def carlist():
    con=lite.connect("app1.db")
    con.row_factory = lite.Row

    cur = con.cursor()
    cur.execute("select * from Cars")

    rows = cur.fetchall();
    con.close()
    return render_template("car_list.html", rows = rows)

@app.route("/showSignUp") #nama showSignUp methodnya disamakan
def showSignUp(): #backend
    con=lite.connect("app1.db")
    con.row_factory = lite.Row

    cur = con.cursor()
    cur.execute("select id from User")

    rows = cur.fetchall();
    con.close()
    return render_template ("signup.html", rows = rows)


@app.route('/saveuser', methods=['GET','POST']) #METHOD
def saveuser():
    if request.method == 'POST':
        id= request.form['id']
        firstname = request.form['firstname']
        lastname =request.form['lastname']
        gender=request.form['gender']
        email= request.form['email']
        username = request.form['username']
        password = request.form['password']
        idselect = request.form['idselect']

        con = lite.connect('app1.db')

        with con:
            cur=con.cursor()
            cur.execute("INSERT INTO User (id,first_name, last_name, gender, email, username, password ) Values (?,?,?,?,?,?,?)", (id,firstname,lastname,gender,email,username,password))
            con.commit()

        return redirect(url_for('userlist'))

@app.route('/userlist')
def userlist():
    con=lite.connect("app1.db")
    con.row_factory = lite.Row

    cur = con.cursor()
    cur.execute("select * from User")

    rows = cur.fetchall();
    con.close()
    return render_template("user_list.html", rows = rows)




app.secret_key = 'baksosolo'
if __name__ == "__main__":
    app.run(debug="True")


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug="True") #host bisa dibuka di pc lain, port='5000', debug=tidak perlu ctrl c
