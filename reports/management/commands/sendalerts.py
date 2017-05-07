from django.core.management.base import BaseCommand, CommandError
from django.contrib.sites.models import Site

from django.core.mail import send_mail
from reports.models import Report


class Command(BaseCommand):
    help = 'Sends alerts and reminders for reports'

    def handle(self, *args, **options):
        print 'handled'
        current_site = Site.objects.get_current()
        domain = current_site.domain
        for report in Report.objects.all():
            deadline = str(report.deadline)
            link = domain + '/reports/submit-report/%s' % report.id
            print report.reportee
            if not report.report:
                if report.days_left() == 14:
                    subject = "%s is due in 2 weeks" % report.name
                    print subject
                    message = "%s is due on the %s. Go to %s to submit this report." % (report.name, deadline, link)
                    print message
                    send_mail(
                        subject,
                        message,
                        'iommicronesiatrackerapp@gmail.com',
                        [report.reportee]
                    )
                if report.days_left() == 7:
                    subject = "%s is due in 1 week" % report.name
                    print subject
                    message = "%s is due on the %s. Go to %s to submit this report." % (report.name, deadline, link)
                    print message
                    send_mail(
                        subject,
                        message,
                        'iommicronesiatrackerapp@gmail.com',
                        [report.reportee]
                    )
                if report.days_left() == 1:
                    subject = "%s is due tomorrow" % report.name
                    print subject
                    message = "%s is due on the %s. Go to %s to submit this report." % (report.name, deadline, link)
                    print message
                    send_mail(
                        subject,
                        message,
                        'iommicronesiatrackerapp@gmail.com',
                        [report.reportee]
                    )
                if report.days_left() < 0:
                    subject = "%s is overdue by %s days" % (report.name, str(report.days_left))
                    print subject
                    message = "%s was due on the %s. Go to %s to submit this report." % (report.name, deadline, link)
                    print message
                    send_mail(
                        subject,
                        message,
                        'iommicronesiatrackerapp@gmail.com',
                        [report.reportee]
                    )