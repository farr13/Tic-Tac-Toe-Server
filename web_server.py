from http.server import SimpleHTTPRequestHandler, HTTPServer

def run_server():
    host = '127.0.0.1'	# Localhost
    port = 8080			# Port number

    # Create the server
    server = HTTPServer((host, port), SimpleHTTPRequestHandler)
    print(f"Server running at http://{host}:{port}/")
    print("Press Ctrl+C to stop the server.")

   

 # Start the server
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        server.server_close()

if __name__ == "__main__":
    run_server()
