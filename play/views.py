from django.http import HttpResponse
from django.shortcuts import render
from twilio.rest import TwilioRestClient
from twilio import twiml
from random import randint

def play(request):
    r = twiml.Response()
    offset = randint(1, 9)
    r.play("http://quiet-atoll-4001.herokuapp.com/static/wavs/sfx_%d.wav" % offset)
    return HttpResponse(str(r))

def trigger(request):
    if request.method == 'GET' and request.REQUEST.get('pword', 'N') == 'S':
        client = TwilioRestClient()
        call = client.calls.create(to="+250788383383", from_="+12067454100",
                                   url="http://quiet-atoll-4001.herokuapp.com/play/")

        return HttpResponse("Triggered")

    return HttpResponse("Nope")