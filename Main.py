from flask import Flask, render_template, request, jsonify
from database.database_handler import Student_DB
from database.users_feedback import UserFeedback

app = Flask(__name__)

# DB_NAME = "students.sqlite3"
# STUDENT_TABLE = "student"

# db = Student_DB(DB_NAME, STUDENT_TABLE)

DB_NAME = "feedback_db.sqlite3"
STUDENT_TABLE = "survey"
db = UserFeedback(DB_NAME, STUDENT_TABLE)


@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')


@app.route("/feedback", methods=['POST'])
def when_feedback():
    name = request.form["name"]
    email = request.form["email"]
    feedback = request.form["feedback"]
    db.add_feedback(name, email, feedback)
    return render_template('home.html')


@app.route("/my_potato_api")
def get_feedbacks():
    return jsonify({"data": db.get_feedbacks()})


if __name__ == '__main__':
    app.debug = True
    app.run(host="", port=5000)




































# @app.route("/result/<name>", methods=['GET','POST'])
# def result(name):
#     # name = request.form['name']
#     db.add_student("S01", "Sai", "09755386957", "Yangon")
#     db.add_student("S02", "Htet", "09421129296", "Mandalay")
#     db.add_student("S03", "Myat", "09750066173", "Pyay")
#     db.add_student("S04", "Htut", "09788266123", "Myawaddy")
#     student = db.get_student_id(name=name)
#     return jsonify({"info": student})
#     # return render_template('result.html', student=student)
#
#
# @app.route("/register/<sid>/<name>/<phone>/<address>", methods=['POST'])
# def register(sid, name, phone, address):
#     # sid = request.form["sid"]
#     # name = request.form["name"]
#     # phone = request.form["phone"]
#     # address = request.form["address"]
#     result_msg = db.add_student(sid, name, phone, address)
#     print(result_msg)
#     return "Success"
#     # return render_template('register.html')
#
#
# @app.route("/delete/", methods=['POST'])
# def delete():
#     sid = request.form["sid"]
#     print(sid)
#     db.remove_student(sid)
#     return render_template('delete.html')
#
#
# @app.route("/update/", methods=['POST'])
# def update():
#     db.update_student(sid="S01",)
#     return render_template('update.html')
