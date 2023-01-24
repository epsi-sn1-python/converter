import http.server
import socketserver
from urllib.parse import urlparse,parse_qs
from converter_proj.converter import SelectConverter

PORT = 8000 

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self) -> None:
        #get choice from query

        #get amount from query
        urlparsed=urlparse(self.path)
        queryparsed=parse_qs(urlparsed.query)
        choice,amount=queryparsed['choice'][0],queryparsed['amount'][0]

        #use select converter with given choice
        converter=SelectConverter.get_converter(int(choice))

        #use converter to convert amount
        result=converter.convert(int(amount))

        #return amount converted
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        response=f'your choice is {choice} and your amount is {amount}, the result is {result}'
        self.wfile.write(str.encode(response))

        #method1
        #urlparsed=urlparse(self.path)
        #params_1=parse_qs(urlparsed.query)
        #print(params_1)

        #method2
        #params_query=self.path.split('?')[1]
        #before_params_2=[tuple(p.split("=")) for p in params_query.split('&')]
        #params_2=dict(before_params_2)
        #print(params_2)   




with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
