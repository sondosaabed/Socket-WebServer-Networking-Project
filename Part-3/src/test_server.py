import socket
import threading
import time

def test_existing_html_file():
    request = "GET /index.html HTTP/1.1\r\nHost: localhost\r\n\r\n"
    expected_output = b"HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\nContent of 'en/index.html'"
    run_test(request, expected_output)

def test_nonexistent_file():
    request = "GET /nonexistent.html HTTP/1.1\r\nHost: localhost\r\n\r\n"
    expected_output = b"HTTP/1.1 404 Not Found\r\nContent-Type: text/html; charset=utf-8\r\n\r\nContent of 'en/404.html'"
    run_test(request, expected_output)

def test_temporary_redirection():
    request = "GET /cr HTTP/1.1\r\nHost: localhost\r\n\r\n"
    expected_output = b"HTTP/1.1 307 Temporary Redirect\r\nContent-Type: text/html; charset=utf-8\r\n\r\nRedirecting to http://cornell.edu"
    run_test(request, expected_output)

def test_css_file():
    request = "GET /style.css HTTP/1.1\r\nHost: localhost\r\n\r\n"
    expected_output = b"HTTP/1.1 200 OK\r\nContent-Type: text/css; charset=utf-8\r\n\r\nContent of 'style.css'"
    run_test(request, expected_output)

def run_test(request, expected_output):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 9967))
    server_socket.listen(1)

    def handle_client():
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('127.0.0.1', 9967))
        time.sleep(1)  # Wait for server to start listening
        client_socket.send(request.encode('utf-8'))
        response = client_socket.recv(1024)
        assert response == expected_output
        client_socket.close()

    threading.Thread(target=handle_client).start()
    client_socket, addr = server_socket.accept()
    handle_client(client_socket)

test_existing_html_file()
test_nonexistent_file()
test_temporary_redirection()
test_css_file()