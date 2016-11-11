activate_this = '/var/www/phenodoop/phenodoop/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import sys
import logging
logging.basicConfig(stream=sys.stderr)

sys.path.insert(0,"/var/www/phenodoop/")
sys.path.insert(0,"/var/www/phenodoop/phenodoop/")
sys.path.insert(0,"/var/www/phenodoop/phenodoop/static/")

from phenodoop import app as application
