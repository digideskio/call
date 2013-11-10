from django.http import HttpResponse
from django.shortcuts import render
from twilio.rest import TwilioRestClient

def play(request):
    return HttpResponse("Hello")

def trigger(request):
    if request.method == 'GET' and request.REQUEST.get('pword', 'N') == 'S':
        client = TwilioRestClient()
        call = client.calls.create(to="+250788383383", from_="+12067454100",
                                   url="http://foo.com/call.xml")

        return HttpResponse("Triggered")

    return HttpResponse("Nope")