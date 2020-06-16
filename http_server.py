#!/usr/bin/env python
import http.server
import socketserver
import os
import sys
import threading

BASE_DIR = os.getcwd()
print(f"base_dir: {BASE_DIR}\n")


def start_server(directory, port):
    print(f"Starting server on port: {port}")

    print(f"base_dir: {BASE_DIR}")
    print(f"directory: {directory}")

    web_dir = os.path.join(BASE_DIR, directory)
    os.chdir(web_dir)

    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", port), Handler)

    print(f"Serving at port: {port}")
    httpd.serve_forever()
    


def main():
    print("Starting HTTP Server ...")

    directory=sys.argv[1]
    port=int(sys.argv[2])
    
    os.chdir(BASE_DIR)
    thread = threading.Thread(target=start_server, args=(directory, port,))
    thread.start()


if __name__ == "__main__":
    main()
