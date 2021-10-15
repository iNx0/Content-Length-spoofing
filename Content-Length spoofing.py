import SimpleHTTPServer
import SocketServer 

def customHeader(self):
    self.send_response(200)
    self.send_header('Content-Length', '-5')
    self.end_headers()
    self.wfile.write("Hey guys")

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
Handler.do_GET = customHeader
Handler.do_POST = customHeader
Handler.do_HEAD = customHeader
httpd = SocketServer.TCPServer(("0.0.0.0", 8000), Handler)
httpd.serve_forever()