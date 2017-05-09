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

from assets.models import Asset, Check, AssetType
from hr.models import Staff, Program


if __name__ == "__main__":
    with open("scripts/Inventory_2.csv", 'rb') as csvfile:
        r = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in r:
            print row
            assets = Asset.objects.filter(no=row[4])
            if not assets:
                asset = Asset()
                asset.no = row[4]
                asset.sub_no = row[5]
                dt = datetime.datetime.strptime(row[10], '%d/%m/%Y').date()
                asset.capitalized = dt
                types = AssetType.objects.filter(name=row[3])
                print types
                if types:
                    asset.asset_type = types.first()
                else:
                    s = AssetType(name=row[3])
                    s.save()
                    asset.asset_type = s
                asset.descr = row[11]
                asset.add_descr = row[12]
                asset.serial = row[14]
                asset.office_id = 6
                if "huuk" in row[17]:
                    asset.office_id = 2
                elif "pei" in row[17]:
                    asset.office_id = 1
                elif "osra" in row[17]:
                    asset.office_id = 5
                elif "j" in row[17]:
                    asset.office_id = 4
                elif "ap" in row[17]:
                    asset.office_id = 3
                p = Program.objects.filter(name=row[21])
                if p:
                    asset.program = p.first()
                else:
                    program = Program(name=row[21])
                    program.save()
                    asset.program = program
                asset.save()

                check = Check()
                check.asset = asset
                if len(row[20]) > 1:
                    staff = Staff.objects.filter(personnel_no=int(row[19]))
                    if staff:
                        s = staff.first()
                        check.staff = s
                        check.check_type = 'out'
                        check.save()
                    else:
                        None
                



