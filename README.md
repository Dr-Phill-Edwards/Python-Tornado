___
title: Python Tornado Framework Example
...

# Python Tornado Framework Example

## Setup

The Tornado and Okta libraries needs to be installed.  
~~~bash
pip install okta okta-jwt tornado
~~~

## Run the server

The server is in a module. The environment variable `PYTHONPATH` needs to point to this directory.  
~~~bash
python -m server.Server 8080
~~~

Test that the server is working.  
~~~bash
curl http://localhost:8080
~~~

You should see a welcome message.

