from os import environ

environ['_ENV_LOG'] = 'dev'
environment = environ.get('_ENV_LOG')
