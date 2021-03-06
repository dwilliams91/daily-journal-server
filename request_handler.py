from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from entries import get_all_entries, get_single_entry, delete_entry, create_entry, get_entry_from_search, update_entry
from moods import get_all_moods
from hashtags import get_all_hashtags

class HandleRequests(BaseHTTPRequestHandler):
    def parse_url(self, path):
        path_params = path.split("/")
        resource = path_params[1]

        # Check if there is a query string parameter
        if "?" in resource:
            # GIVEN: /customers?email=jenna@solis.com

            param = resource.split("?")[1]  # email=jenna@solis.com
            resource = resource.split("?")[0]  # 'customers'
            pair = param.split("=")  # [ 'email', 'jenna@solis.com' ]
            key = pair[0]  # 'email'
            value = pair[1]  # 'jenna@solis.com'

            return ( resource, key, value )

        # No query string parameter
        else:
            id = None

            try:
                id = int(path_params[2])
            except IndexError:
                pass  # No route parameter exists: /animals
            except ValueError:
                pass  # Request had trailing slash: /animals/

            return (resource, id)
    # Here's a class function
    def _set_headers(self, status):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    # Another method! This supports requests with the OPTIONS verb.
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type, Accept')
        self.end_headers()
    
    def do_GET(self):
        self._set_headers(200)
        response = {}

        # Parse URL and store entire tuple in a variable
        parsed = self.parse_url(self.path)

        # Response from parse_url() is a tuple with 2
        # items in it, which means the request was for
        # `/animals` or `/animals/2`
        if len(parsed) == 2:
            ( resource, id ) = parsed
            
            if resource == "entries":
                if id is not None:
                    response = f"{get_single_entry(id)}"
                else:
                    response = f"{get_all_entries()}"

            if resource =="moods":
                if id is not None:
                    print("don't do anything yet")
                else:
                    response = f"{get_all_moods()}"
            if resource=="hashtags":
                response=f"{get_all_hashtags()}"

        elif len(parsed)==3:
            ( resource, key, value ) = parsed
            
            if resource=="entries" and key=="q":
                response=get_entry_from_search(value)
            
            
        
        self.wfile.write(response.encode())

    def do_DELETE(self):
    # Set a 204 response code
        self._set_headers(204)

    # Parse the URL
        (resource, id) = self.parse_url(self.path)

    # Delete a single animal from the list
        if resource == "entries":
            delete_entry(id)


    # Encode the new animal and send in response
        self.wfile.write("".encode())

    def do_POST(self):
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        post_body=json.loads(post_body)

        (resource, id)= self.parse_url(self.path)

        new_entry= None

        if resource =="entries":
            new_entry=create_entry(post_body)
        # PUT HASHTAG LOGIC HERE
        
        self.wfile.write(f"{new_entry}".encode())
        

    def do_PUT(self):
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        (resource, id) = self.parse_url(self.path)


        success=False

        if resource=="entries":
            success=update_entry(id, post_body)

        if success:
            self._set_headers(204)
        else:
            self._set_headers(404)
        self.wfile.write("".encode())

def main():
        host = ''
        port = 8088
        HTTPServer((host, port), HandleRequests).serve_forever()

if __name__ == "__main__":
        main()