import os
import sys
from wsgiref import simple_server


def app(environ, start_response):
    start_response("200 OK", [])
    return [environ["HTTP_X_FORWARDED_FOR"].encode()]


simple_server.ServerHandler.server_software = ""
port = int(os.environ.get("PORT", 8000))
with simple_server.make_server(host="", port=port, app=app) as httpd:
    print(f"Serving on port {port}...")
    httpd.serve_forever()
