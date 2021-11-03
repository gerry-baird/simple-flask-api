from flask import Flask
import logging

app = Flask(__name__)

logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s')
file_handler = logging.FileHandler('grump.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

@app.route('/')
def hello_world():  # put application's code here
    logger.info('Root APi called : Hello World returned')
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
