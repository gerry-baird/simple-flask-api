FROM registry.redhat.io/ubi8/python-38


COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN python3 -m pip install -r requirements.txt
COPY ./app.py /app/app.py

# Run the application
CMD flask run --host=0.0.0.0 --port=8080