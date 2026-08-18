from http.server import HTTPServer, BaseHTTPRequestHandler

def add(a, b):
  return a + b

def multiply(a, b):
  return a * b

class Handler(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.send_header("Content-type", "text/plain")
    self.end_headers()
    result = f"add(2,3)={add(2,3)}, multiply(2,3)={multiply(2,3)}\n"
    self.wfile.write(result.encode())

if __name__ == "__main__":
  server = HTTPServer(("0.0.0.0", 8000), Handler)
  server.serve_forever()
