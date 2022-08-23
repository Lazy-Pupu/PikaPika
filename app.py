from flask import Flask
from db import db
from queue import Queue, Empty
from threading import Thread

from scripts.folderMonitor import monitor_folder

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.app = app
db.init_app(app)
commands = Queue()

Thread(target=monitor_folder, daemon=True, kwargs={'folder_path':["C:\\Users\\huluh\\Downloads\\", "C:\\Users\\huluh\\Desktop"]}).start()




@app.route('/')
def hello_world():  # put application's code here
    commands.put_nowait({'action': 'something'})
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
