from app import app, db, cli
from app.models import User, Post, Event


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Event':Event }
