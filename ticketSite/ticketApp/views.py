from django.shortcuts import render
from django.shortcuts import render
from .models import Ticket
from django.http import HttpResponse



#takes in a request and renders the index.html template with the tickets, passes information from the browser to the view
def index(request):
  
    tickets = Ticket.objects.order_by('-urgency')[:5]
    return render(request,'index.html', {'tickets': tickets})

#Get the ticket with the primary key of ticket_id and pass it to the template ticket_by_id.html.
def ticket_by_id(request, ticket_id):
   
    ticket = Ticket.objects.get(pk=ticket_id)
    return render(request, 'ticket_by_id.html', {'ticket':ticket})