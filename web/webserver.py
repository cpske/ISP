# A simple web server in under 30 lines of code (excluding comments).
# It accepts requests from the network on port PORT
# and sends a 200 OK response with simple text.
#
# Imagine you had to write all the code to handle requests,
# routing, session management, etc., yourself.  A lot of work.
# That's why we have frameworks.
#
# Python strings: network data is sent as byte-strings.
# A byte-string looks like b'data\nmore data\n'
# To convert byte-string regular string:
#     string = str( bstr, 'utf-8' )
# or  string = bstr.decode()   or bstr.decode('utf-8')
# To convert unicode string to byte string:  
#     bstr = string.encode()
import sys, socket, datetime

HOST = ''
PORT = 80
MAX_REQUEST_SIZE = 65535

try:
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.bind((HOST, PORT))
    # Put the socket into listening mode to accept connections
    listen_socket.listen()
except:
    print("Exception raised while creating socket:")
    print( sys.exc_info()[0] )
    print( sys.exc_info()[1] )
    sys.exit(1)

while True:
    # Wait for a connection and return a connection object and an address.
    # The address contains (ip_address, port) of the remote host.
    print("Waiting for connections on port", PORT)
    connection, address = listen_socket.accept()
    request = connection.recv(MAX_REQUEST_SIZE)
    # What did we get?
    print("Got a connection from host", address[0], "port", address[1])
    print("")
    # The request and response are byte-strings, not regular unicode strings.
    # Use request.decode() for a readable version.
    print( request.decode(), "\n" )
    # include timestamp in reply so multiple requests are distinguishable. 
    timestamp = datetime.datetime.now().strftime("%H:%H:%S")
    # Send a response and close the connection
    response = f"""HTTP/1.1 200 OK
    Content-type: text/html

    <html>
      <body>
            <h2>Hello {address[0]}! Got your Request at {timestamp}</h2>
            <p>I'll get to work on it right away.</p>
            <p>Have a nice day.:-)</p>
        </body>
    </html>
    """
    connection.sendall(response.encode()) 
    connection.close()

# If you ever get out of the loop... close the socket to free the port.
listen_socket.close()