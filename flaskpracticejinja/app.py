from flask import Flask , request, render_template
from random import randint ,choice, sample
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)

compliments = ["super cool", "not nice", "very stupendous", "lost"]

@app.route('/')
def hompage():
 return render_template("hello.html")

@app.route('/lucky')
def lucky_page():
 num = randint(1,10)
 return render_template("lucky.html", lucky_num=num)

@app.route('/form')
def form_page():
    return render_template("form.html")

@app.route('/greet')
def greet():
  comp = choice(compliments)
  username = request.args["username"]
  return render_template("greet.html", username=username , complete=comp)

@app.route('/spell/<word>')
def spell_word(word):
  return render_template("spellword.html", word=word)

@app.route('/form2')
def form2():
  return render_template("form2.html")

@app.route('/greet2')
def greet2():
  username = request.args["username"]
  wants = request.args.get("wants_compliments")
  nice = sample(compliments, 3)
  return render_template("greet2.html", username=username, wants_compliments =wants, words=nice)
