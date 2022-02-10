from urllib import response
from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)

app.config['SECRET_KEY'] = "secert"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

@app.route("/")
def home_page():
  return render_template("begin_survey.html", survey=survey)

@app.route("/begin", methods=["POST"])
def survey_started():

  return redirect("/questions/0")

@app.route("/questions/`<int:qid>`")
def show_question(qid):
  question = survey.questions[qid]
  return render_template("question.html", question_num=qid, question=question)

@app.route("/answer", methods=["POST"])
def send_answer():
  responses = []
  choice = request.form["answer"]
  responses.append(choice)


  if(len(responses) == len(survey.questions)):
    print('all good')

  else:
    return redirect(f"/questions/{len(responses)}")
