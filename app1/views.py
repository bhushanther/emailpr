from django.shortcuts import render
from django.core.mail import send_mail
import datetime
from .models import Event, Employee, EmailLog
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

 



@api_view(['GET'])
def get_events(request):
 if request.method == 'GET':
    current_date = datetime.date.today()
    print(current_date)

    current_month = current_date.month
    current_day = current_date.day

    event1 = Employee.objects.filter(event__event_date__month=current_month, event__event_date__day=current_day).values('id', 'name', 'email', 'event__event_type', 'event__subject', 'event__body')
   
   
    
    if event1:
        for i in range(len(event1)):
            id=event1[i]['id']
            name=event1[i]['name']
            email=event1[i]['email']
            event_event_type=event1[i]['event__event_type']
            subject=event1[i]['event__subject']
            message=event1[i]['event__body']
         
            
            subject = subject
            message = message
            from_email = 'bhushther@gmail.com'
            recipient_list = [email]
            
            try:
                send_mail(subject, message, from_email, recipient_list )
            except:
                report = EmailLog.objects.create(
                    event_type=event_event_type, 
                    status='delivery fail', 
                    error_message='error in message', 
                    sent_at=current_date
                ) 
                report.save()
                return Response({'msg': 'mail not sent'})
            else: 
                report = EmailLog.objects.create(
                    event_type=event_event_type, 
                    status='delivery success', 
                    error_message='no error', 
                    sent_at=current_date
                )
                report.save() 
                
        return Response({'success': 'email sent'}, status.HTTP_200_OK)
    else:
        return Response({'msg': 'no record found'}, status.HTTP_200_OK)
