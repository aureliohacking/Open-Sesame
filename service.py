import http.server
import socketserver
import os
import send_mail

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

CURR_DIR = os.path.dirname(os.path.realpath(__file__))
print('Before: ' + str(CURR_DIR))

os.chdir('/storage/emulated/0/')

# /data/data/org.kivy.oscservice/files/home/storage/shared
# /data/data/com.termux/files/home/storage/shared
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
print('After: ' + str(CURR_DIR))


with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Servidor ON en el puerto", PORT)
    send_mail.send()
    httpd.serve_forever()