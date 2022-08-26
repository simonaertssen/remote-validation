# -*- coding: utf-8 -*-
from flask import Flask, make_response

app = Flask(__name__)


@app.route("/")
def send_welcome():
    """
    Host the main page.
    """
    return make_response("Welcome to telelicense.com\n", 200)


if __name__ == "__main__":
    app.run(ssl_context=('.env/cert.pem', '.env/key.pem'))
