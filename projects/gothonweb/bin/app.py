# encoding =utf-8
from gothonweb import map
import web
import os

urls = ('/game', 'GameEngine')

app = web.application(urls, globals())

#little hack so that debug mode works with sessions
if web.config.get('_session') is None:
    store = web.session.DiskStore('sessions')
    session = web.session.Session(app.store, initalizer={'room': None})
    web.config_session = session
else:
    session = web.config_session

render = web.template.render(
    os.path.expanduser(
        '/Users/VON/WorkSpace/Learn Python The Hard Way/projects/gothonweb/templates/'
    ),
    base="layout")


class Index(object):
    # def GET(self):
    #     form = web.input(name="Nobody", greet=None)
    #     if form.greet:
    #         greeting = "%s, %s" % (form.greet, form.name)
    #         return render.index(greeting=greeting)
    #     else:
    #         return "ERROR:greet is required"
    # greeting = "Hello World"
    # return render.index(greeting=greeting)

    def GET(self):
        #this is used to "setup" the session with starting values
        session.room = map.START
        web.seeother("/game")


class GameEngine(object):
    def Get(self):
        if session.room:
            return render.show_room(room=session.room)
        else:
            # why's  is there here doo you need it
            return render.you_died()

    def POST(self):
        form = web.input(action=None)

        #there is a bug here..can you fix it?
        if session.room and form.action:
            session.room = session.room.go(form.action)
            web.seeother("/game")


if __name__ == "__main__":
    app.run()

    # def GET(self):
    #     return render.hello_form()

    # def POST(self):
    #     form = web.input(name="Nobody", greet="Hello")
    #     greeting = "%s %s" % (form.greet, form.name)
    #     return render.index(greeting=greeting)

