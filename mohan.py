
from http.server import HTTPServer, BaseHTTPRequestHandler

class MyWebsite(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        html = """
        <html>
        <head>
            <title>My AWS Website</title>
            <style>
                body {
                    background: #101827;
                    color: white;
                    text-align: center;
                    font-family: Arial;
                    padding-top: 100px;
                }
                h1 { color: #ff9900; }
            </style>
        </head>
        <body>
            <h1>Hello from AWS EC2!</h1>
            <h2>Welcome to my first cloud project.</h2>
            <p>Python server is running successfully.</p>
            <p>Created by Mohan</p>
        </body>
        </html>
        """

        self.wfile.write(html.encode())


server = HTTPServer(("0.0.0.0", 8000), MyWebsite)

print("Website running on port 8000...")

server.serve_forever()
