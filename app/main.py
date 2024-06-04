import socket
import json
from info import get_cpu_percent, get_memory_usage, get_connections

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('0.0.0.0', 10100))
serversocket.listen(5)

while True:
    connection, address = serversocket.accept()
    buf = connection.recv(1024)
    if len(buf) == 0:
        connection.close()
        continue
    try:
        buf = buf.decode()
        assert buf == 'data'
    except Exception:
        connection.close()
        continue
    cpu = get_cpu_percent()
    mem = get_memory_usage()
    conns = get_connections()
    send_data = {
        'cpu': cpu,
        'memory': mem,
        'conns': conns
    }
    connection.send(json.dumps(send_data).encode())
    connection.close()