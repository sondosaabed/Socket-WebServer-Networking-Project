from socket import * 

def run_serevr(server_ip, port):
    server = socket(AF_INET, SOCK_STREAM)
    server.bind((server_ip, port))
    
    server.close()