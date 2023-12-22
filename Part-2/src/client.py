"""
    In this Script I implenet the client python using socket Programming
"""
import socket

def run_client(server_ip = "127.0.0.1",  server_port = 9955):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create a socket object    
    client.connect((server_ip, server_port))# establish connection with server

    while True:
        msg = input("Enter Student ID: ") # input message and send it to the server
        client.send(msg.encode("utf-8")[:1024])

        response = client.recv(1024) # receive message from the server
        response = response.decode("utf-8")

        if response.lower() == "closed": # if server sent us "closed" in the payload, we break out of the loop and close our socket
            break

        print(f"Received: {response}")

    # close client socket (connection to the server)
    client.close()
    print("Connection to server closed")

try:
    run_client()
except Exception as e:
    print(f"Error in: {e}")