from datetime import datetime


time = datetime.now().strftime("%H:%M")


def attendance_csv(name, time=time):
    with open("Attendance.csv", "r+") as file:
        attendance_data = file.readlines()
        existing_name = [data.split(',')[0] for data in attendance_data]
        if name not in existing_name:
            file.writelines(f"\n{name},{time}")

def attendance_sql(name, time=time):
    pass
