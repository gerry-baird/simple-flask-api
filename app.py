from flask import Flask
import logging
import os

logging.basicConfig(level=logging.DEBUG)
#port = int(os.getenv("PORT", 8080))

app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    msg = 'Root APi called : Hello World returned - v2'
    logging.info(msg)
    return 'Hello World! v0.3'


if __name__ == "__main__":
    app.run(host='0.0.0.0')
