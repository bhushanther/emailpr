from django.contrib import admin

from .models import Employee, Event, EmailTemplate, EmailLog

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['name',
                        'email']
    

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display=['employee', 'event_type', 'event_date']   


@admin.register(EmailTemplate)
class EmailTemplateAdmin(admin.ModelAdmin):
    list_display=['employee','event_type','subject', 'body']     


@admin.register(EmailLog)
class EmailLogAdmin(admin.ModelAdmin):
    list_display=['event_type','status','error_message', 'sent_at']     





    
