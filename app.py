import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)


@app.route('/')
def index():
   return "hello sai krishna"


if __name__ == '__main__':
   app.run()
