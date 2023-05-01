# Python is a popular programming language used for various applications, including web development. A local web
# client in Python refers to a client-side application or script that runs on a user's computer and interacts with a
# web server to retrieve and display web content.

# In the context of Python web development, a local web client can refer to a variety of tools or libraries that
# facilitate communication between a Python application running on the user's computer and a web server. Some
# examples include the requests' library, which allows Python scripts to send HTTP requests and receive responses,
# and the urllib library, which provides a set of functions for working with URLs and accessing web resources.

# Local web clients can be useful for a variety of tasks, such as retrieving data from web APIs or scraping web
# content for analysis. They can also be used to build simple user interfaces that display web content within a
# desktop or command-line application.

import requests

url = "https://www.example.com"
response = requests.get(url)

print(response.text)

# In this code, we first import the requests' library. We then define a URL to fetch data from and make a GET request
# using requests.get(). The response object returned by requests.get() contains the data returned by the server,
# which we can access using the text attribute. In this example, we simply print the response text to the console.

# Note that requests is a third-party library and needs to be installed before it can be used.
