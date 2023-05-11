from flask import Flask, render_template, request, redirect, url_for,flash, session, send_file

from Mi_app.rutes import *


if __name__ == '__main__':
    app.run(debug= True, port=8080, host="0.0.0.0")
