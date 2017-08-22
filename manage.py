#!/usr/bin/env python
import os

from flask_script import Manager, Shell, Server
from flask_script.commands import ShowUrls, Clean

from pynashapi import create_app, DB

app = create_app(os.getenv('FLASK_CONFIG') or 'default')


def make_context():
    return dict(app=app, DB=DB)


manager = Manager(app)

manager.add_command("runserver", Server())
manager.add_command("show-urls", ShowUrls())
manager.add_command("clean", Clean())
manager.add_command("shell", Shell(make_context=make_context))

if __name__ == '__main__':
    manager.run()
