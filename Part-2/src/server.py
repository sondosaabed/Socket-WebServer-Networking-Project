import socket
import time
from utils import validate_student_id, lock_screen

"""
    In this script, I implement a Server using Socket Programming with Socket Library
""" 
def check_id(student_id, client_socket ):
    """
        Args:
            student_id: the entered id
            client_socket: the created client socket 
        Return:
            Nothing 
        
        Functionality:
            To perform lock screen and send messages to client and display on server
    """
    if student_id:
        print(f"Received valid student ID: {student_id}")
        # Send a message to the client that the server will lock the screen
        # Display a message on the server side that the OS will lock screen after 10 seconds
        client_socket.send("Locking screen in 10 seconds...".encode("utf-8"))
        print("Windows will lock screen after 10 seconds")

        time.sleep(10) # Wait for 10 seconds
        lock_screen()
        
        # Send a response to the client after locking the screen
        client_socket.send("Screen locked.".encode("utf-8"))
    else:
        # If the received message is not a valid student ID, display an error message
        print("Error: Invalid student ID or message")

def run_server(server_ip = "127.0.0.1", port = 9955):
    """
        Args: 
            Server ip
            Port
        Doesn't retrun values only perform socket connection as server
    """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create a socket object

    server.bind((server_ip, port))  # bind the socket to a specific address and port
    server.listen(0)    # listen for incoming connections
    print(f"Listening on {server_ip}:{port}")

    client_socket, client_address = server.accept()     # accept incoming connections
    print(f"Accepted connection from {client_address[0]}:{client_address[1]}")

    # receive data from the client
    while True:
        request = client_socket.recv(1024)
        request = request.decode("utf-8") # convert bytes to string
        
        # if we receive "close" from the client, then we break out of the loop and close the connection
        # send response to the client which acknowledges that the
        # connection should be closed and break out of the loop
        if request.lower() == "close":
            client_socket.send("closed".encode("utf-8"))
            break

        # Check if the received message is a valid student ID
        student_id = validate_student_id(request)
        check_id(student_id, client_socket)

        # convert string to bytes and send accept response to the client
        response = "accepted".encode("utf-8") 
        client_socket.send(response)  
    
    client_socket.close()
    print("Connection to the client closed")
    server.close()


try:
    run_server()
except Exception as e:
    print(f"Error in : {e}")