
# index, a page for the main page, this will have a small descripption of the site and a link to the login page and some use cases

# login, a page for the login page, this will have a form for the user to input their username, room, roleplay choices, and difficulty choices

# chat, a page for the chat page, this will have the chat box and the scoring box


from flask import session, redirect, render_template, request, url_for

from app.helpers.startuphelpers import load_session
from refactor.config.Config import FLAGS
from refactor.helpers.datahelper import save_session

from . import main

@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')    

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['name'] = request.form['name']
        session['room'] = request.form['room']
        session['roleplay'] = request.form['roleplay']
        session['difficulty'] = request.form['difficulty']
        print(session)
        save_session(session)
        FLAGS.INTERACTION_STARTED = True
        return redirect(url_for('.chat',name=session['name'], room=session['room'], roleplay=session['roleplay'], difficulty=session['difficulty']))
    return render_template('login.html', session=session, request=request)

@main.route('/chat', methods=['GET', 'POST'])
def chat():
    if FLAGS.INTERACTION_STARTED == True and FLAGS.CHAT_STARTED == False:
        FLAGS.CHAT_STARTED = True
        session = load_session('session.json')
        name = session.get('name', '')
        room = session.get('room', '')
        roleplay = session.get('roleplay', '')
        difficulty = session.get('difficulty', '')
        return render_template('chat.html', name=name, room=room, roleplay=roleplay, difficulty=difficulty, session=session)
    session = load_session('session.json')
    return render_template('chat.html')
# websocket chat connectio