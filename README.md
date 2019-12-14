# berightback

Deter theft by showing people that you're watching them.

Runs on Debian-based linux under Python 3.7.

## Setup

### Install dependencies

#### `python`

Install the latest version of Python if you haven't already, and install `venv`.

Create a virtual environment with `$ python -m venv venv`.

Enter the environment with `$ source venv/bin/activate`

Install requirements with `$ pip install -r requirements.txt`.

#### `motion`

`motion` is required for webcam streaming:

`$ sudo apt install motion`

#### `xtrlock`

For locking your screen while showing Firefox in kiosk mode. `xtrlock` will prevent interacting with the desktop until password is correctly input followed a return.

`$ sudo apt install xtrlock`

You'll also need to update (or install) Firefox to version 71 for to run `fullscreen_lock.sh`.

## Running

To run the server by itself, just activate the virtual environment and run `$ python berightback.py`. You can access it in a web browser at `localhost:8080`, and see a live stream from another device by scanning the QR code in the top right.

To view the website fullscreen and lock your display, make sure you have `xtrlock` and Firefox 71 installed, and run `$ fullscreen_lock.sh`.
