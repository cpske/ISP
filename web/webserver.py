# A simple web server.
# It accepts requests from the network on port PORT
# and sends a 200 OK response with simple text.
# It also prints the request on the terminal.
#
# Imagine you had to write all the code to handle requests,
# routing, session management, etc., yourself.  A lot of work.
# That's why we have frameworks.
#
# Python strings: a byte-string looks like b'data\nmore data\n'
# To convert to a regular string:
# string = str( bstr, 'utf-8' )
# string = bstr.decode()   or .decode('utf-8')
# To convert unicode to byte string:  bstr = string.encode()
import socket

HOST = ''
PORT = 8080
MAX_REQUEST_SIZE = 65535
try:
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.bind((HOST, PORT))
except Error as e:
    print("Excepption raised while setting up socket:")
    print(e)

# 1 means accept at most 1 simultaneous connection
# We should accept many connections, and
# use a worker thread to handle each one.
listen_socket.listen(1)
print("Listening for connections on port", PORT)
# socket.accept() will wait for a connection.
# It returns a connection object and an address (a tuple).
# The address contains (ip_address, port) of the remote host.
connection, address = listen_socket.accept()
request = connection.recv(MAX_REQUEST_SIZE)
# What did we get?
print("Got a connection from host", address[0], "port", address[1])
print("")
# The request and response are byte-strings, not regular unicode strings.
# Use request.decode() for a readable version.
print( request )
# Send a response and close the connection
response = """HTTP/1.1 200 OK
Content-type: text/html

<html>
    <body>
        <h1>Got your Request</h1>
        <p>I'll get to work on it right away!</p>
        <p>Have a nice day.:-)</p>
    </body>
</html>
"""
connection.sendall(response.encode()) 
connection.close()
# A real server would loop and accept another connection now.
# For demo, just close the socket to free the port.
listen_socket.close()
