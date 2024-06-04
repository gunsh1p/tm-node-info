import psutil
import time

def get_cpu_percent() -> float:
    return psutil.cpu_percent()

def get_memory_usage() -> tuple:
    data = psutil.virtual_memory()
    percent = data.percent
    used = round(data.used / 2**20, 1)
    total = round(data.total / 2**20, 1)
    
    return (percent, used, total)

def get_vpn_connections():
    vpn_connections = []
    for conn in psutil.net_connections('tcp'):
        if conn.status == 'ESTABLISHED' and conn.laddr.port == 8701:
            vpn_connections.append(conn)
    return vpn_connections

def get_network_speed() -> dict:
    prev_net_io = psutil.net_io_counters()
    time.sleep(1)
    next_net_io = psutil.net_io_counters()

    bytes_sent_diff = next_net_io.bytes_sent - prev_net_io.bytes_sent
    bytes_recv_diff = next_net_io.bytes_recv - prev_net_io.bytes_recv

    speed_sent = bytes_sent_diff / 1024
    speed_recv = bytes_recv_diff / 1024

    if speed_sent > 1024:
        speed_sent /= 1024
        speed_recv /= 1024
        unit = "MB/s"
    else:
        unit = "KB/s"
    return {
        'sent': f'{speed_sent:.2f} {unit}',
        'recieved': f'{speed_recv:.2f} {unit}'
    }

def get_connections() -> int:
    return len(get_vpn_connections())

def get_network_usage() -> tuple:
    connections = get_connections()
    speed = get_network_speed()
    
    return (connections, speed)