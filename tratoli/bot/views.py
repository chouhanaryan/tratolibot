from django.shortcuts import render
from django.http import HttpResponse
from .models import Chats
import dateutil.parser
import requests


def index(request):
    return render(request, 'index.html')

def chat(request):
    query = request.POST.get('query')
    parameters = {'v': '20191126', 'q': str(query)}
    headers = {'Authorization': 'Bearer KMDO2Z3N2QFBB2NN7DLAI7HPFQPFQC3B', 'Accept': 'application/json'}
    url = 'https://api.wit.ai/message'
    res = requests.get(url, headers=headers, params=parameters).json()

    if list(res["entities"].keys()) == ['rooms', 'location', 'datetime', 'intent']:
        rooms = res["entities"]["rooms"][0]["value"]
        destination = res["entities"]["location"][0]["value"]
        checkin = dateutil.parser.parse(res["entities"]["datetime"][0]["values"][0]["from"]["value"])
        checkout = dateutil.parser.parse(res["entities"]["datetime"][0]["values"][0]["to"]["value"])

        context = {'rooms': rooms, 'location': destination, 'checkin': checkin, 'checkout': checkout}
        
        chat = Chats()
        chat.rooms = rooms
        chat.checkin = checkin
        chat.checkout = checkout
        chat.destination = destination
        chat.save()

        return render(request, 'chat.html', context=context)

    return render(request, 'error.html')