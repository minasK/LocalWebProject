# A local web server in Python is a simple HTTP server that runs on your computer and serves web pages or files to
# web clients, such as web browsers or other applications. It allows you to test and develop web applications on your
# local machine without having to deploy them to a remote server.

# Python provides a built-in http.server module that makes it easy to create a local web server. The http.server
# module can be used to create a simple file server that serves static files from a specified directory on your
# computer, or a more advanced server that handles dynamic content using Python scripts.

# Here's an example of how to create a simple file server in Python using the http.server module:

import http.server
import socketserver

ipaddress = "192.168.1.2"
PORT = 2025

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer((ipaddress, PORT), Handler) as httpd:
    print("Serving at port...", PORT, "address:", ipaddress)
    httpd.serve_forever()

# In this example, we create a new TCP server on port 8000 that serves files from the current directory using the
# SimpleHTTPRequestHandler class from the http.server module. When you run this code, you can access the files served
# by the server by opening a web browser and navigating to http://localhost:8000/.

# Note that this is a very basic example of a local web server and should not be used in production environments. If
# you need a more advanced web server, you may want to consider using a third-party library or framework,
# such as Flask or Django.

# This code creates a web server  that listens on port 8000 and serves files from the current working directory. When
# you run this code, you should see a message in the console indicating that the server is running. You can then open
# a web browser and navigate to http://localhost:8000 to see the files being served. Before it was localhost instead of
# linuxas


# I have request but not reply from the other machines. how can i respond (with a simple ethernet)
# I a doing tcp syn, but not syn-ack and ack
# also, I want to make a server that I will put the ip address like 192.168.1.2 and every pc can go there
# see also the messages in the wireshark to try solve
# how did the pc go in there? does it need permission change?
