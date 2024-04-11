
import datetime

from flask_socketio import emit
import pickle
import textwrap
import google.generativeai as genai
import os
from flask import session

from IPython.display import display
from IPython.display import Markdown
import json
import yaml
from refactor.config import Config
from refactor.helpers.AI import ai_worker as ai

# the normal chat instance
chat = ai.gemini_chat([])

# the roleplay chat instance
# roleplay_chat = ai.roleplay_chat({})
# that should init after the choice of roleplay

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)

def responder(message):
    history = []
    model = genai.GenerativeModel('gemini-1-pro')
    chat = model.start_chat(history=history)
    return chat

def message_beginner(user,time):
    if user == "AI":
        return f"{time} 💬 AI : "
    else:
        return " 👋 "+time+ " "+ user +"💎: "
    
def create_message(user,msg ,timestamp):
    strt = message_beginner(user,timestamp)
    msg = strt + msg
    return {'msg': msg , 'timestamp':timestamp}

def messanger(msg,user,room):
    message = create_message(user,msg,datetime.datetime.now())
    emit('message', message, room=room)
    print(message)
    return message

def status_message(user,room):
    message = create_message(user, f"{user} has entered the room", datetime.datetime.now())
    emit('message', message, room=room)
    print(message)
    return message

def ai_message(umsg,room):
    msg = chat.send_message(umsg).parts[0].text
    message = create_message("AI",msg,datetime.datetime.now())
    emit('message', message, room=room)
    print(message)#consider putt the save to session here
    # also consider saving the session here
    return message