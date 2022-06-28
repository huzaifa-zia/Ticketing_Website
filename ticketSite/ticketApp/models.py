from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.contrib.auth.models import User
from django.db.models import IntegerField,Model

# Create your models here.
# the ticket status helps the IT department make sure which tickets they are working on and which ones have been completed and makes it easier on them
class TicketStatus(models.TextChoices):
	TO_DO = 'To Do'
	IN_PROGRESS = 'In Progress'
	IN_REVIEW = 'In Review'
	DONE = 'Done'

#the ticket class makes sure all variables are assigned and pop up when the user fills out the ticket
class Ticket(models.Model):
    author = models.CharField(max_length= 50, null = True)
    ticket_type = models.CharField(max_length = 1,null = True)
    urgency = models.PositiveIntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(10)])
    description = models.TextField()
    title = models.CharField(max_length=100)
    assignee = models.ForeignKey(User, null=True, blank = True, on_delete=models.CASCADE)
    status = models.CharField(max_length=25, choices=TicketStatus.choices, default=TicketStatus.TO_DO)
    created_at = models.DateTimeField('created at', auto_now_add=True)
    updated_at = models.DateTimeField('updated at', auto_now=True)
