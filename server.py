from http.server import BaseHTTPRequestHandler, HTTPServer
from io import BytesIO
from os import curdir, sep
import json
import time
from tictoctoe import checkBoard

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_OPTIONS(self):           
        self.send_response(200, "ok")       
        self.send_header('Access-Control-Allow-Origin', '*')                
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With")        
        self.end_headers()

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        if self.path == '/ui/board.html':
            f = open(curdir + sep + 'ui/board.html', 'rb')
            self.wfile.write(f.read())
            f.close()
        
        else:
            self.wfile.write(bytes("<html><head><title>Tic Tac Tol server</title></head>", "utf-8"))
            self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes("<p>This is Emma's web server.</p>", "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        #print(body.decode('utf-8'))

        data = json.loads(body.decode('utf-8'))
        print(data['data'])

        result = checkBoard(data['data'])

        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        response = BytesIO()
        response.write(bytes(json.dumps(result), 'utf-8'))
        self.wfile.write(response.getvalue()) 

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")