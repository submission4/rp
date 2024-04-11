# Description: This file contains the event handlers for the socketio server
#
# The event handlers are responsible for handling the messages recieved from the socketio server
# and sending responses back to the socketio server
# The event handlers are also responsible for managing the AI session and scoring

import datetime
from flask import session
from flask_socketio import emit, join_room, leave_room
from refactor import socketio , main
from . import main
from refactor.config.Config import FLAGS 
import refactor.helpers.chathelper as messanger
from refactor.helpers.commands.handler import command_response, command_check
from refactor.helpers.datahelper import save_session, load_session
@socketio.on('join', namespace='/chat')
def join(data):
    print('joined')
    session['name'] = data['name']
    session['room'] = data['room']
    join_room(session['room'])
    messanger.status_message(session["room"], session["name"])
    if FLAGS.INTERACTION_STARTED == True:
        load_session(session)
    else:
        save_session(session)
        FLAGS.INTERACTION_STARTED = True

    print(f"session {session}")

@socketio.on('connect', namespace='/chat')
def connect():
    print('connected')

@socketio.on('disconnect', namespace='/chat')
def disconnect():
    print('disconnected')
    emit('message', {'msg': f"💬{session['name'] } has left the chat room {session['room']}"},
         timestamp=datetime.datetime.now(), room=session["room"] )

@socketio.on('message', namespace='/chat')
def message(data):
    print(f"message {data}")
    FLAGS.INTERACT = False
    user_msg = messanger.messanger(session["room"], data['msg'], session["name"])
    # when we get a message from user the ai should respond with a message
    ai_msg = messanger.ai_message(data['msg'], session["room"])
    FLAGS.INTERACT = True
    session["user_message"] = user_msg
    session["ai_message"] = ai_msg

@socketio.on('system_message', namespace='/chat')
def system_message(data):
    print(f"system message {data}")
    messanger.messanger(data["msg"], "AI")
    #do something with the system message

@socketio.on('score', namespace='/chat')
def score_the_roleplay(data):
    print(f"scoring the roleplay {data}")
    messanger.messanger(data["msg"], "AI")
    # do the scoring here and send the score to the front end to be displayed in the score box
    # also update the score box with the score
    FLAGS.SCORING = True
    # do the scoring here
    # update the score box
    FLAGS.SCORING_COMPLETE = True
    messanger.messanger( "Roleplay has been scored", "AI")

@socketio.on('new_message', namespace='/chat')
def new_message(data):
    print(f"new message {data}")
    messanger.messanger(data["msg"], "AI")
    # do something with the new message