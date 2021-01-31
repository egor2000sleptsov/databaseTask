from sql import Request
db = Request("Timetable.db")
week = 18
week_session = 2
time_table = []

def week_classes(id_group, id_discipline, id_teacher, class_type, hours):
    week_days = db.week_days()
    pairs = db.call_timetable()
    while hours:
        is_searched = False
        for day in week_days:
            if is_searched:
                break
            for pair in pairs:
                busy = False
                for time in time_table:
                    if time[0] == id_group and time[6] == pair[0] and time[5] == day[0]:
                        busy = True
                        break
                if not busy:
                    time_table.append([id_group, id_discipline, "Аудитория", id_teacher, class_type, day[0], pair[0]])
                    hours = hours-1
                    is_searched = True
                    break

def timetable():
    groups = db.groups()
    for group in groups:
        disciplines = db.disciplines(group[0])
        for discipline in disciplines:
            hours = [int(discipline[2]/36), int(discipline[3]/36), int(discipline[4]/36)]
            week_classes(group[0], discipline[0], discipline[2], 1, hours[0])
    print(time_table)

if __name__ == "__main__":
    timetable()