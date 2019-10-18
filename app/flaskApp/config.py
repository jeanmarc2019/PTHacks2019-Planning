import configparser
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path += '/cfg.ini'

class Configuration(object):
    def __init__(self,debug=False):
        section = "Flask-debug" if debug else "Flask"
        cfg = configparser.ConfigParser()
        cfg.read(dir_path if debug else "/var/www/html/flaskApp/cfg.ini")
        self.debug = cfg.getboolean(section, "DEBUG")
        self.csrf_enabled = cfg.getboolean(section,"CSRF_ENABLED")
        self.threads_per_page = cfg.getint(section,"THREADS_PER_PAGE")
        self.port = cfg.getint(section,"PORT")
        self.host = cfg.get(section,"HOST")