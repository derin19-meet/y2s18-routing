from databases import *
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/student/<string:student_name>/<string:student_year>/<int:student_id>')
def display_student(student_id, student_name,student_year):
    return render_template('student.html', student_id=student_id, student_name=student_name, 
    student_year=student_year)

app.run(debug=True)
