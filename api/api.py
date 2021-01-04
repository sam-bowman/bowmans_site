import time, os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app  =  Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
CORS(app)

@app.route('/time')
def get_current_time():
    return {'time': time.time(), "secret_key": os.getenv('SECRET_KEY')}

if __name__ == '__main__':
    app.run()
