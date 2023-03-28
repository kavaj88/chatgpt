from wsgiref.simple_server import make_server
from wsgi_test import application

http = make_server('', 8000, application)
print('Serving HTTP on port 8000....')
http.serve_forever()
