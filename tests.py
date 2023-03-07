from unittest import TestCase
from app import app

app.config['WTF_CSRF_ENABLED'] = False
