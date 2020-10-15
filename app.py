from flask import Flask, request
from sender import Sender
import os
import datetime
import logging
import sys

# Configure Logging
root = logging.getLogger()
root.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)

# Get/set up variables for sending to Splunk
url = os.environ.get("HEC_URL")
token = os.environ.get("HEC_TOKEN")
format = os.environ.get("HEC_FORMAT")
time_format = os.environ.get("HEC_TIME_FORMAT")

# JRL TEMP VALUES
url = "http://127.0.0.1/"
token = "foo"

if url is None:
    print("HEC_URL must be set")
    exit(1)
if token is None:
    print("HEC_TOKEN must be set")
    exit(1)

if time_format is None:
    time_format = "%Y-%m-%d %H:%M:%S"

sender = Sender(url, token)

app = Flask(__name__)

@app.route("/event/<subtype>", methods=["PUT", "POST", "GET"])
def hello_world(subtype):

    app.logger.info("Request method: %s", request.method)
    app.logger.info("Subtype: %s", subtype)
   
    event = request.get_json()

    if event is not None:
        for key in event:
            if (str(key)).endswith("Date"):
                event[key] = datetime.datetime.fromtimestamp(int(event[key]) / 1000).strftime(time_format)
        if format is None:
            msg = ""
            first = True
            for key in event:
                if not first:
                    msg += ", "
                first = False
                msg += key
                msg += ": "
                msg += str(event[key])
    #        sender.send_message(msg)
            app.logger.info(msg)

        else:
    #         sender.send_message(format.format_map(event))
            app.logger.info(event)

    else:
        app.logger.info("Empty event")
        
    return 'OK'
