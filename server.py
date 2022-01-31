from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold']=0
    if 'actlist'not in session:
        session['actlist']=[]
    if 'winlose' not in session:
        session['winlose']=True
    if 'color' not in session:
        session['color']=[]
    return render_template("index.html")


@app.route('/gold', methods=['POST'])
def gold():
    if request.form['activity'] == 'farming':
        add=random.randint(10,20)
        session['gold']+=add
        session['actlist'].insert(0,"After farming you have gathered " + str(add) + " gold! for a total of " + str(session['gold']))
        session['color'].insert(0,'green')
    if request.form['activity'] == 'cave':
        add=random.randint(5,10)
        session['gold']+=add
        session['actlist'].insert(0,"After searching the Cave you have gathered " + str(add) + " gold! for a total of " + str(session['gold']))
        session['color'].insert(0,'green')
    if request.form['activity'] == 'house':
        add=random.randint(2,5)
        session['gold']+=add
        session['actlist'].insert(0,"After searching the Cave you have gathered " + str(add) + " gold! for a total of " + str(session['gold']))
        session['color'].insert(0,'green')
    if request.form['activity'] == 'casino':
        session['winlose']=bool(random.getrandbits(1))
        if session['winlose']:
            add=random.randint(0,50)
            session['gold']+=add
            session['actlist'].insert(0,"Luck was on your side! You won " + str(add) + " gold! for a total of " + str(session['gold']))
            session['color'].insert(0,'green')
        else:
            add=random.randint(0,50)
            session['gold']-=add
            session['actlist'].insert(0,"Luck was not on your side! You lost " + str(add) + " gold! leaving you with " + str(session['gold']))
            session['color'].insert(0,'red')
    return redirect('/')

@app.route('/reset',methods=['POST'])
def reset():
    session.clear()
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)