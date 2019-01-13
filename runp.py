#!flask/bin/python
from app import app
app.run(debug = False, ssl_context=('./ssl.crt', './ssl.key'))
