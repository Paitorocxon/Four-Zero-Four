#   ____                             ________                                 ____
#  /\  _`\                          /\_____  \                               /\  _`\
#  \ \ \L\_\___   __  __  _ __      \/____//'/'     __   _ __   ___          \ \ \L\_\___   __  __  _ __
#   \ \  _\/ __`\/\ \/\ \/\`'__\_______  //'/'    /'__`\/\`'__\/ __`\  _______\ \  _\/ __`\/\ \/\ \/\`'__\
#    \ \ \/\ \L\ \ \ \_\ \ \ \//\______\//'/'___ /\  __/\ \ \//\ \L\ \/\______\\ \ \/\ \L\ \ \ \_\ \ \ \/
#     \ \_\ \____/\ \____/\ \_\\/______//\_______\ \____\\ \_\\ \____/\/______/ \ \_\ \____/\ \____/\ \_\
#      \/_/\/___/  \/___/  \/_/         \/_______/\/____/ \/_/ \/___/            \/_/\/___/  \/___/  \/_/
#
# You don't need to understand this... sometimes me neither. All i wanted, was to share a file with my mother in the livingroom...
# Smol webserver-thingy i'm currently working on!
# put your html files in the html folder but without ".html" at the end.
#
# e.g: you want an index file? Just create a file named "index" in html (e.g: "touch html/index")
# grz, Pait

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from urlparse import parse_qs
import cgi, os, sys, traceback

class GP(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
    def do_HEAD(self):
        self._set_headers()
    def do_GET(self):
	print '\x1b[0;32m'
        self._set_headers()
        print self.path
        print parse_qs(self.path[2:])

	if os.path.isdir("html/"):
		print "(html directory exists!)"
	else:
		os.makedirs("html/")

	FourZeroFour = "<html><body><h1><font color=red><b>[404]</b></font></h1><br><hr>[FourZeroFour 1.0]<br></body></html>"
	htmlcontent = ""
	request_string = "html/"
	request_string += self.path.replace('/','')
	if self.path.replace('/','') is not '':
		if os.path.exists(request_string):
			htmlcontent = open(request_string,'r').read()
		else:
			#if (os.path.exists("html/index")):
			#	htmlcontent = open("html/index",'r').read()
			#else:
			        htmlcontent = FourZeroFour
	else:
		if (os.path.exists("html/index")):
			htmlcontent = open("html/index",'r').read()
		else:
			htmlcontent = FourZeroFour

	#Send it to the Browser! Hey!
	if htmlcontent is FourZeroFour:
		print '\x1b[6;37;41m' + '[ERROR!] CODE 404!'
		print self.path
		print parse_qs(self.path[2:])
	print '\x1b[0;32m'
	self.wfile.write(htmlcontent)
    def do_POST(self):
        self._set_headers()
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST'}
        )

def run(server_class=HTTPServer, handler_class=GP, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print "  j88D   .d88b.    j88D"
    print " j8~88  .8P  88.  j8~88"
    print "j8' 88  88  d'88 j8' 88"
    print "V88888D 88 d' 88 V88888D"
    print "    88  `88  d8'     88"
    print "    VP   `Y88P'      VP"
    print '\x1b[0;33m'+'Server started!'
    print '\x1b[0;32m'
    httpd.serve_forever()
def main():
    try:
	run()
    except KeyboardInterrupt:
	print ''
	print '\x1b[1;31m'+'Server stopped!'
    except Exception:
	print '\x1b[0;31m'
	traceback.print_exc(file=sys.stdout)
    sys.exit(0)
if __name__ == "__main__":
    main();
