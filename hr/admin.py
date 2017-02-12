from django.contrib import admin

# Register your models here.

from .models import *

class ContractAdmin(admin.ModelAdmin):
    pass

class StaffAdmin(admin.ModelAdmin):
    list_display = (
        'last_name',
        'first_name',
        'staff_type',
    )

    list_editable = (
        'staff_type',
    )

    list_filter = ['staff_type', ]
    search_fields = ('last_name',)


class PositionAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'duty_station',
        'program',
        'reports_to',
    )

    list_editable = (
        'duty_station',
        'program',
        'reports_to',
    )

    list_filter = ['duty_station', 'program', 'reports_to']


admin.site.register(Contract, ContractAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Shirt_Size)
admin.site.register(Staff_Type)
admin.site.register(Warden_Zone)
admin.site.register(Grade)
admin.site.register(Contract_Type)
admin.site.register(Position_Status)
admin.site.register(Duty_Station)
admin.site.register(Program)
admin.site.register(Gender)
