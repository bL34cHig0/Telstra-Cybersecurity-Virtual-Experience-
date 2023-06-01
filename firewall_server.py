# www.theforage.com - Telstra Cyber Task 3
# Firewall Server Handler

from http.server import BaseHTTPRequestHandler, HTTPServer
import re

host = "localhost"
port = 8000

#########
# Define the regular expressions to match the request path and HTTP headers
path_regex = re.compile(r"/tomcatwar\.jsp")
headers_regex = re.compile(r"(suffix=%>\/\/)|(c1=Runtime)|(c2=<%)|(DNT=1)|(Content-Type: application\/x-w>")

class ServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Check if the request path or headers match the defined regular expressions
        if path_regex.search(self.path) or headers_regex.search(str(self.headers)):
            self.block_request()  # Block the request if it matches
        else:
            self.handle_request()  # Handle the request normally if it doesn't match

    def do_POST(self):
        # Check if the request path or headers match the defined regular expressions
        if path_regex.search(self.path) or headers_regex.search(str(self.headers)):
            self.block_request()  # Block the request if it matches
        else:
            self.handle_request()  # Handle the request normally if it doesn't match

    def block_request(self):
        print("Request blocked due to firewall")
        # Sends a 403 Forbidden response to the blocked request
        self.send_response(403)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<html><head><title>403 Forbidden</title></head>")
        self.wfile.write(b"<body><h1>403 Forbidden</h1>")
        self.wfile.write(b"<p>You don't have permission to access this resource.</p>")
        self.wfile.write(b"</body></html>")

if __name__ == "__main__":
    # Create an HTTP server with the specified host and port, using the ServerHandler class to handle requests
    server = HTTPServer((host, port), ServerHandler)
    print("[+] Firewall Server")
    try:
        server.serve_forever()  # Start the server and keep it running
    except KeyboardInterrupt:
        pass

    server.server_close()
    print("[+] Server terminated. Exiting...")
    exit(0)
