#!/usr/bin/python3
"""
Module for simple network communication using sockets and JSON serialization.
"""
import socket
import json


def start_server():
    """
    Starts a server that listens for a connection, receives a JSON-serialized
    dictionary, and prints it.
    """
    host = 'localhost'
    port = 65432

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((host, port))
            s.listen()
            conn, addr = s.accept()
            with conn:
                data = conn.recv(1024)
                if data:
                    received_dict = json.loads(data.decode('utf-8'))
                    print("Received Dictionary from Client:")
                    print(received_dict)
    except Exception as e:
        print(f"Server error: {e}")


def send_data(data_dict):
    """
    Connects to the server and sends a dictionary serialized as JSON.
    """
    host = 'localhost'
    port = 65432

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            serialized_data = json.dumps(data_dict).encode('utf-8')
            s.sendall(serialized_data)
    except ConnectionRefusedError:
        print("Connection failed: Server is not responding.")
    except Exception as e:
        print(f"Client error: {e}")
