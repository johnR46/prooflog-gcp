from os import environ

environ['environment'] = 'production'
environment = environ.get('environment')
