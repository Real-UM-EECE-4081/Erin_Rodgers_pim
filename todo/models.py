from email import message
from email.policy import default
from django.db import models

# # Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=45)
    description = models.TextField(default='', blank=True)
    due_date = models.DateTimeField(null=True)
    complete_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=45, choice=(('Created','Created'),('Finished','Finished')), default='Created')  
    category = models.CharField(max_length=45, default="",choices=(('IMPORTANT', 'IMPORTANT'), ('URGENT', 'URGENT'), ('NORMAL', 'NORMAL')))
    priority = models.CharField(max_length=45, default="",choices=(('PRIORITY', 'PRIORITY'), ('NON-PRIORITY', 'NON-PRIORITY')))
    task_image = models.ImageField(upload_to='images/',blank=True, null=True)
    send_mail(
        'Email verification',
        message,
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )
    
    def __str__(self):
        return self.name
