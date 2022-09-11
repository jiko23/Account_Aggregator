# Account_Aggregator
To build an end-to-end request-response demo using the Account Aggregator to fetch financial information that shows a successful handshake via Consent API and then FetchData API. SETU has been used.

Programming language used is Python3.6+ .In this assignment FastAPI has been used as it is getting ground faster and more flexible. For REST calls initial choice was HTTPX but later stage to keep things simple Requests has been used. For faster REST calls connection re-use has been used. For testing the API Swagger has been used for better understanding and visibility. Format of input and output is in JSON format.

Requirements:
. FastAPI
. Pydantic
. Python 3.6+
. Uvicorn

Working Demo Link: https://www.loom.com/share/657355de2ba243fab4fca205a2519eb9

Running Steps::
a. Start the local server --> run ‘uvicorn AAIntegration:app –reload’ in terminal
b. In browser ‘http://127.0.0.1:8000/docs’ i.e. for performing the actions in swagger view.
c. If need schema specification details about API then in browser put ‘http://127.0.0.1:8000/redoc’
