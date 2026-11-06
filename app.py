import json
from http.server import BaseHTTPRequestHandler, HTTPServer


def health_status():
    return {
        "app": "NovaBank",
        "status": "ok",
        "version": "v2"
    }


def get_account_balance(account_id):
    return {
        "account_id": account_id,
        "balance": 1000
    }


class NovaBankHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            response = health_status()
            self.send_response(200)
        else:
            response = {"message": "NovaBank API is running"}
            self.send_response(200)

        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8080), NovaBankHandler)
    print("NovaBank server running on port 8080")
    server.serve_forever()
