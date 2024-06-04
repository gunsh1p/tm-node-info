import socket
import json
from info import get_cpu_percent, get_memory_usage, get_connections

def server_program():
    port = 10100

    server_socket = socket.socket()
    server_socket.bind(('0.0.0.0', port))

    server_socket.listen(10)
    while True:
        conn, address = server_socket.accept()
        print(f'Connection from {address}')
        while True:
            data = conn.recv(1024)
            if not data or data != 0x1:
                break
            cpu = get_cpu_percent()
            mem = get_memory_usage()
            conns = get_connections()
            send_data = {
                'cpu': cpu,
                'memory': mem,
                'conns': conns
            }
            conn.send(json.dumps(send_data).encode())
        conn.close()

if __name__ == '__main__':
    server_program()