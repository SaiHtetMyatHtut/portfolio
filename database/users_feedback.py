import sqlite3 as sql


class UserFeedback:

    def __init__(self, db_name, table_name):
        self.db_name = db_name
        self.table_name = table_name
        con = sql.connect(self.db_name)
        cur = con.cursor()
        cur.execute(f"drop table if exists {table_name}")
        cur.execute(f"create table {table_name} (Name text, Email text, Feedback text)")
        con.commit()

    def add_feedback(self, name, email, feedback):
        con = sql.connect(self.db_name)
        cur = con.cursor()
        cur.execute(f"insert into {self.table_name} values ('{name}','{email}','{feedback}')")
        con.commit()
        return "Success"

    def get_feedbacks(self):
        con = sql.connect(self.db_name)
        cur = con.cursor()
        students = cur.execute(f"select * from {self.table_name}").fetchall()
        con.commit()
        data = list()
        for x in students:
            data.append({"name": x[0], "email": x[1], "feedback": x[2]})
        return data
