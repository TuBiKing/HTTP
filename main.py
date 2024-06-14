import socket
def start_server():
    global server
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('127.0.0.1', 1025))

        server.listen(4)
        while True:
            client_socket, address = server.accept()
            data = client_socket.recv(1024).decode('utf-8')
            print(data)
            HDRS = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n"
            content = "200 chipi chipi chapa chapa".encode('utf-8')
            client_socket.send(HDRS.encode('utf-8') + content)
            client_socket.shutdown(socket.SHUT_WR)
    except KeyboardInterrupt:
        server.close()
        print("Server closed by the client")
if __name__ == '__main__':
    start_server()

