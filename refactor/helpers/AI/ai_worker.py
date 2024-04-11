#ai workers 
from flask import session
from flask_socketio import emit
import datetime
from refactor import socketio

import datetime
from refactor.helpers.AI.prompts import roleplay as rpp
from refactor.helpers.AI.prompts import scoring as sp
import pickle
import textwrap
import google.generativeai as genai
import os
from flask import session

from IPython.display import display
from IPython.display import Markdown
import json
import yaml
from refactor.config.Config import Config

os.environ['GOOGLE_API_KEY'] = Config.GOOGLE_API_KEY
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

# single send and response no history streaming
def gemini(model_name='gemini-pro.',content="testing phrase"):
    chunky = ""
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(content, stream=True)
    for chunk in response:
      print(chunk.text)
      chunky += chunk.text
    return chunky + "\n "

# chat history streaming
def gemini_chat(message_history):
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=message_history)
    return chat


# scxoring response stricked json response
def roleplay_chat(roleplay:dict,rpp:rpp=rpp)->object:
    ''' 
    Simulates a roleplay chat based on the given roleplay details.

    Args:
        roleplay (dict): Dictionary containing roleplay details including 
                         system instructions, title, role, skill, name, objective, difficulty.
        rpp (str): Roleplay prompt to be used. Default is rpp.roleplayPrompt
    Returns:
        chat: (object) 
        use chat.send_message(content) to send a message to the chat

    '''
    chat_history = []
    instruction = rpp.roleplayPrompt(roleplay)
    
    model = genai.GenerativeModel(
    "models/gemini-1-pro-latest",
    system_instruction=instruction)
    chat = model.start_chat(history=chat_history)
    return chat

def score_chat(roleplay,scoring_prompt:sp=sp):
    #grab the scoring prompt and json prompt
    scoring_prompt = scoring_prompt.scoringprompt(roleplay)
    #start a new chat just for scoring
    model = genai.GenerativeModel(
    "models/gemini-1-pro-latest",
    system_instruction=scoring_prompt)
    chat = model.start_chat(history=[])

    return chat

def chatScoreResponce(message,scoreChat):
    scoreChat.send_message(message)
    res = scoreChat.history[-1].parts[-1].text
    role = scoreChat.history[-1].role
    return  role,res, scoreChat.history

def chatResponce(message,chat):
    chat.send_message(message)
    res = chat.history[-1].parts[-1].text
    role = chat.history[-1].role
    return  role,res, chat.history
    
def json_response(message , instruction):
    model = genai.GenerativeModel('gemini-pro', system_instruction=instruction)
    resp = model.generate_content(message)
    data = json.dumps(resp)
    json_data = json.loads(data)
    jd = json_data[7:-3]
    jd = json_data[7:-3]
    # check if the response is a json response
    # check  the complete response
    if jd.startswith("{") and jd.endswith("}"):
        return jd
    else:
        return "response is not a json response"
    
