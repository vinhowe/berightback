from flask import Flask
from flask import render_template
from pyroute2 import IPDB
import argparse
import netifaces
from pathlib import Path
import subprocess as sp

ap = argparse.ArgumentParser()

ap.add_argument("-m", "--msg", required=False,
   help="message to display (default 'I'll be right back!')")
ap.add_argument("-p", "--port", required=False, help="port (default: 8080)")
args = vars(ap.parse_args())

motion_conf_dir = Path().absolute() / 'motion.conf'
print(motion_conf_dir)

process = sp.Popen(['motion', '-p', motion_conf_dir], stdout=sp.PIPE, stderr=sp.PIPE)

app = Flask(__name__)

default_msg = "I'll be right back!"
default_port = '8080'
msg = args['msg']
port = args['port']

# show webcam page
@app.route("/")
def webcam():
    iface = netifaces.gateways()['default'][netifaces.AF_INET][1]
    ip_addr = netifaces.ifaddresses(iface)[netifaces.AF_INET][0]['addr']
    print(f"serving from {ip_addr}")
    return render_template('webcam.html', ip_addr=ip_addr, msg=msg if msg is not None else default_msg)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port if port is not None else default_port)
