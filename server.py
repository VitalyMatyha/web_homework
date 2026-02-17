from http.server import HTTPServer, BaseHTTPRequestHandler


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()

        with open("contacts.html", "r", encoding="utf-8") as file:
            html = file.read()

        self.wfile.write(html.encode("utf-8"))

#
server = HTTPServer(("localhost", 8000), Handler)
print("http://localhost:8000")
server.serve_forever()
