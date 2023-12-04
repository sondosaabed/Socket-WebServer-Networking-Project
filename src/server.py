import socket

def run_serevr(server_ip, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((server_ip, port))
    
    server.close()

run_serevr("127.0.0.1", 8000)