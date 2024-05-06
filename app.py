from flask import Flask,render_template,request
import sqlite3
app=Flask(__name__)
@app.route('/', methods=['GET','POST'])
def index():
    if request.method =='POST':
        username=request.form['username']
        password=request.form['password']
        conn=create_connection()
        conn.cursor().execute('''SELECT * FROM VJS WHERE USERNAME==? AND PASSWORD==?''',(username,password))
        data=conn.cursor().fetchall()
        conn.commit()
        conn.close() 
        print(data)
        if data:
            return render_template('home.html')
        else:
            return "Wrong credentials"
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/registration', methods=['GET','POST'])
def registration():
    if request.method=='POST':
        uname=request.form['username']
        pswd=request.form['password']
        conn=create_connection()
        conn.cursor().execute('''INSERT INTO VJS (USERNAME,PASSWORD) VALUES(?,?)''',(uname,pswd))
        conn.commit()
        conn.close()
    return render_template('registration.html')

@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/palnadu')
def palnadu():
    return render_template('palnadu.html')
@app.route('/nandyal')
def nandyal():
    return render_template('nandyal.html')
@app.route('/prakasham')
def prakasham():
    return render_template('prakasham.html')
@app.route('/nellore')
def nellore():
    return render_template('nellore.html')
@app.route('/bapatla')
def bapatla():
    return render_template('bapatla.html')
@app.route('/srikakulam')
def srikakulam():
    return render_template('srikakulam.html')
@app.route('/vizianagaram')
def vizianagaram():
    return render_template('vizianagaram.html')
@app.route('/manyam')
def manyam():
    return render_template('manyam.html')
@app.route('/ananthapuram')
def ananthapuram():
    return render_template('ananthapuram.html')
@app.route('/eastgodavari')
def eastgodavari():
    return render_template('eastgodavari.html')
@app.route('/konaseema')
def konaseema():
    return render_template('konaseema.html')
@app.route('/kakinada')
def kakinada():
    return render_template('kakinada.html')
@app.route('/kadapa')
def kadapa():
    return render_template('kadapa.html')
@app.route('/vizag')
def vizag():
    return render_template('vizag.html')
@app.route('/chittoor')
def chittoor():
    return render_template('chittoor.html')
@app.route('/tirupati')
def tirupati():
    return render_template('tirupati.html')
@app.route('/ntr')
def ntr():
    return render_template('ntr.html')
@app.route('/guntur')
def guntur():
    return render_template('guntur.html')
@app.route('/kurnool')
def kurnool():
    return render_template('kurnool.html')
@app.route('/annamayya')
def annamayya():
    return render_template('annamayya.html')
@app.route('/eluru')
def eluru():
    return render_template('eluru.html')
@app.route('/westgodavari')
def westgodavari():
    return render_template('westgodavari.html')
@app.route('/krishna')
def krishna():
    return render_template('krishna.html')
@app.route('/allurisitaramaraju')
def allurisitaramaraju():
    return render_template('allurisitaramaraju.html')
def create_connection():
    conn=sqlite3.connect('user.db')
    return conn
def create_table():
    conn=create_connection()
    conn.cursor().execute("CREATE TABLE IF NOT EXISTS VJS(USERNAME VARCHAR(50) NOT NULL,PASSWORD VARCHAR(6) NOT NULL)")
    conn.commit()
    conn.close()
if __name__=='__main__':
    create_table()
    app.run(debug=True)