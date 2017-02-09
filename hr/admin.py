from django.contrib import admin

# Register your models here.

from .models import *

class PositionInline(admin.TabularInline):
    model = Position


class StaffAdmin(admin.ModelAdmin):
    list_display = (
        'last_name',
        'first_name',
        'staff_type',
        'position',
        'active_contract'
    )

    list_editable = (
        'staff_type',
    )

    list_filter = ['staff_type', ]
    search_fields = ('last_name',)

    inlines = [PositionInline, ]


class PositionAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'duty_station',
        'program',
        'reports_to',
        'active_contract'
    )

    list_editable = (
        'duty_station',
        'program',
        'reports_to',
    )

    list_filter = ['duty_station', 'program', 'reports_to']


class ContractAdmin(admin.ModelAdmin):
    list_display = ('position', 'staff',
                    'contract_type',
                    'grade',
                    'start_date',
                    'end_date')
    date_hierarchy = 'end_date'


admin.site.register(Staff, StaffAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Contract, ContractAdmin)

admin.site.register(Shirt_Size)
admin.site.register(Staff_Type)
admin.site.register(Warden_Zone)
admin.site.register(Action)
admin.site.register(Grade)
admin.site.register(Contract_Type)
admin.site.register(Position_Status)
admin.site.register(Duty_Station)
admin.site.register(Program)
admin.site.register(Gender)
