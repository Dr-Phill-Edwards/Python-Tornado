___
title: Python Tornado Framework Example
...

# Python Tornado Framework Example

## Setup

The Tornado library needs to be installed.  
~~~bash
pip install tornado
~~~

## Run the server

The server is in a module. The environment variable `PYTHONPATH` needs to point to this directory.  
~~~bash
python -m server.Server 8888
~~~

Test that the server is working.  
~~~bash
curl http://localhost:8888
~~~

You should see a welcome message.

