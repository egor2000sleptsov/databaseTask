import sqlite3
class Request:
    def __init__(self, file):
        self.connection = sqlite3.connect(file)
        self.cursor = self.connection.cursor()

    def groups(self):
        with self.connection:
            groups = self.cursor.execute("Select * From Study_group").fetchall()
            return groups

    def disciplines(self, id_group):
        with self.connection:
            disciplines = self.cursor.execute("Select id_discipline, id_teacher, lecture_hours, "
                                              "practise_hours, lab_hours, otchet "
                                              "From Study_plan "
                                              "Where id_studygroup = ?", (id_group,)).fetchall()
            return disciplines

    def week_days(self):
        with self.connection:
            week_days = self.cursor.execute("Select * From Week_day").fetchall()
            return week_days

    def call_timetable(self):
        with self.connection:
            para = self.cursor.execute("Select number_class From Call_timetable").fetchall()
            return para