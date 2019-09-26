import configparser

class Configuration(object):
    def __init__(self,debug=False):
        section = "Flask-debug" if debug else "Flask"
        cfg = configparser.ConfigParser()
        cfg.read("/var/www/html/flaskApp/cfg.ini" if debug else "/var/www/html/flaskApp/cfg.ini")
        self.debug = cfg.getboolean(section, "DEBUG")
        self.csrf_enabled = cfg.getboolean(section,"CSRF_ENABLED")
        self.threads_per_page = cfg.getint(section,"THREADS_PER_PAGE")
        self.port = cfg.getint(section,"PORT")
        self.host = cfg.get(section,"HOST")