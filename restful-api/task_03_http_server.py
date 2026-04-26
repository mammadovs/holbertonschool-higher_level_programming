#!/usr/bin/python3
import http.server
import json

class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """
    A simple HTTP server to handle basic API endpoints.
    """

    def do_GET(self):
        """
        Handles GET requests for different endpoints.
        """
        if self.path == '/':
            # Basic text response
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/data':
            # JSON response with sample data
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode('utf-8'))

        elif self.path == '/status':
            # Simple health check endpoint
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == '/info':
            # Information about the API
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(info).encode('utf-8'))

        else:
            # 404 Error handling for undefined endpoints
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

def run_server(port=8000):
    """
    Initializes and starts the HTTP server.
    """
    server_address = ('', port)
    httpd = http.server.HTTPServer(server_address, SimpleAPIHandler)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
