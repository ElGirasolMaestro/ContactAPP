from flask import Flask, render_template, request;
from flask_mysqldb import MySQL

app=Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'flaskcontacts'
mysql = MySQL(app)

@app.route('/') 
def Index():
    return render_template('index.html')

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute('INSTER INTO contacts (fullname, phone, email) VALUES (%s, %s, %s)',(fullname, phone, email))
        mysql.connection.commit()
        return 'received'

@app.route('/edit')
def edit_contact():
    return 'edit contact'

@app.route('/delete')
def delete_contact():
    return 'delete contact'

if __name__=='__main__':
    app.run(port=3000, debug = True)
