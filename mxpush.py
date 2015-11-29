import json, requests
from flask import Flask, jsonify, request
import ConfigParser
from matrix_client.api import MatrixHttpApi
app = Flask(__name__)

config = ConfigParser.ConfigParser()
config.read('/etc/mxpush.conf')
TOKEN = config.get("Matrix", "token")
HOMESERVEr = config.get("Matrix", "homeserver")
ROOMID = config.get("Matrix", "room_id")
  
@app.route("/", methods=["POST"])
def handleNotification():
  req = request.get_json()
  print(req)
  
  matrix = MatrixHttpApi(HOMESERVER, token=req['notification']['devices'][0]['pushkey'])
  print(matrix.send_message_event(room_id=ROOMID, event_type='net.terracrypt.matrix.push', content=req))
  
  return jsonify({})

if __name__ == "__main__":
    app.config['TRAP_BAD_REQUEST_ERRORS'] = True
    app.run(host='0.0.0.0')
