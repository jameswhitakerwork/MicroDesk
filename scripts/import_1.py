import os, sys, csv, datetime

proj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# This is so Django knows where to find stuff.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoApp.settings")
sys.path.append(proj_path)

# This is so my local_settings.py gets loaded.
os.chdir(proj_path)

# This is so models get loaded.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from hr.models import Staff, Contract, Position

reader = None

if __name__ == "__main__":
    with open("scripts/iom_staff_1.csv", 'rb') as csvfile:
        r = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in r:
            dt = datetime.datetime.strptime(row[7], '%d.%m.%Y').date()
            staff = Staff()
            staff.last_name = row[0]
            staff.first_name = row[1]
            staff.personnel_no = row[2]
            staff.nationality = row[4]
            staff.entry_on_duty = dt
            try:
                staff.save()
            except:
                pass

            position = Position()
            position.title = row[3]
            position.duty_station_id = 6
            if "huuk" in row[5]:
                position.duty_station_id = 2
            elif "pei" in row[5]:
                position.duty_station_id = 1
            elif "osra" in row[5]:
                position.duty_station_id = 5
            elif "j" in row[5]:
                position.duty_station_id = 4
            elif "ap" in row[5]:
                position.duty_station_id = 3


            print dt
            position.start_date = dt
            position.save()

            contract = Contract()
            contract.staff = staff
            contract.position = position
            dt = datetime.datetime.strptime(row[6], '%d.%m.%Y').date()
            print dt
            contract.end_date = dt
            contract.renew_after_expires = True
            contract.save()
            print "Staff, position and contract added"
        print 'completed'



