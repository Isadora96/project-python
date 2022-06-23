from flask import Flask

app = Flask(__name__)

from hamburguerblog.core.views import core
from hamburguerblog.error_pages.handlers import error_pages

app.register_blueprint(core)
app.register_blueprint(error_pages)