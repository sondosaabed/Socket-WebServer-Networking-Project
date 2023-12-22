import socket

def get_content_type(file_path):
    """
        Args: 
            Takes file_path of the desired file as a string
        Returns:
            The content Type of the file based on the extenstion
    """
    if file_path.endswith('.html'):
        return 'text/html; charset=utf-8'
    elif file_path.endswith('.css'):
        return 'text/css; charset=utf-8'
    elif file_path.endswith('.png'):
        return 'image/png'
    elif file_path.endswith('.jpg'):
        return 'image/jpeg'
    else:
        return 'text/html; charset=utf-8'

def temp_redirection(request_path, client_socket):
    """
        Args:
            Request_path, Client_socket
        Returns:
            Status Code as Temor. Redirection as 307
    """
    redirect_to = {'/cr': 'http://cornell.edu', 
                    '/so': 'http://stackoverflow.com', 
                    '/rt': 'http://ritaj'}
    response_data = f"Redirecting to {redirect_to[request_path]}".encode('utf-8')
    client_socket.send(response_data)
    client_socket.close()
    return '307 Temporary Redirect'

def handle_404(client_socket, lang='en'):
    """
        Args: 
            Client socket to send the response
            lang: if ar will sent the ar/404.html 
                or else will sent the english and the en is default
    """
    custom_404_path = f'{lang}/404.html'
    with open(custom_404_path, 'r', encoding='utf-8') as custom_404_file:
        data = custom_404_file.read().encode('utf-8')
        content_type = get_content_type(custom_404_path)
        status_code = '404 Not Found'
        send_response(client_socket, status_code, content_type, data)

def send_response(client_socket, status_code, content_type, data):
    """
        To sent a header & data to a client
        Args:
            client_socket, status_code, content_type, data
    """
    response_headers = f"HTTP/1.1 {status_code}\r\nContent-Type: {content_type}\r\n\r\n"
    response_data = response_headers.encode('utf-8') + data
    client_socket.send(response_data)

def handle_request(client_socket, request_path):
    """
        Args: 
            client_socket, request_path takes and client socket to be send to and a request path to render
            handles all cases of temrory redirection & file doesn't exists
    """
    if request_path in ['/', '/index.html', '/main_en.html', '/en']:
        file_path = 'en/index.html'
        lang = 'en'
    elif request_path in ['/main_ar.html', '/ar']:
        file_path = 'ar/index.html'
        lang = 'ar'
    elif request_path in ['/cr', '/so', '/rt']:
        status_code= temp_redirection(request_path, client_socket)
        return
    else:
        file_path = request_path.lstrip('/')
        lang = 'en' if file_path.startswith('en/') else 'ar'
    try:
        with open(file_path, 'rb') as file:
            data = file.read()
            content_type = get_content_type(file_path)
            status_code = '200 OK'
            send_response(client_socket, status_code, content_type, data)
    except FileNotFoundError:
        handle_404(client_socket, lang)

def handle_client(server_socket):
    """
        To take requests from the users
        Args:
            Server_socket
    """
    client_socket, addr = server_socket.accept()
    request = client_socket.recv(1024).decode('utf-8')

    print(f"Received request from {addr}:\n{request}")# Print HTTP request on the terminal
    
    request_parts = request.split(' ')# Extract the requested path
    if len(request_parts) >= 2:
        request_path = request_parts[1]
        handle_request(client_socket, request_path) # Handle the request

def start_server(localhost='127.0.0.1', port=9966):
    """
        Handles the client until they leave
        Args:
            takes the local host ip
            takes the port number as required 
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((localhost, port))
    server_socket.listen(1)
    print("Server listening on port 9966...")

    while True:
        handle_client(server_socket)