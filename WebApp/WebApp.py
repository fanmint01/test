import http.server

server_address = ("", 3000)
handler_class = http.server.CGIHTTPRequestHandler #1 ハンドラを設定
server = http.server.HTTPServer(server_address, handler_class)
server.serve_forever()
