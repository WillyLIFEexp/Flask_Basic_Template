from flask import Flask
import os

# Init app for all applications
template_dir = os.path.abspath("./app")
static_dir = os.path.abspath("./app")


app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
