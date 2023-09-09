import os
from wsgiref import simple_server


def app(environ, start_response):
    start_response("200 OK", [])
    ip = (environ.get("HTTP_X_FORWARDED_FOR") or "?").split(",")[0]
    return [ip.encode()]


simple_server.ServerHandler.server_software = ""
port = int(os.environ.get("PORT") or 8000)
with simple_server.make_server(host="", port=port, app=app) as httpd:
    print(f"Serving on port {port}...")
    httpd.serve_forever()
