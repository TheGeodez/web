def hello_app(environ, start_response):
    a = environ["QUERY_STRING"].split('&')
    headers = [('content-type', 'text/plain')]
    start_response('200 OK', headers)
    return [bytes(i + '\n', 'ascii') for i in a]
