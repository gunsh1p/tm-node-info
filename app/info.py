import psutil

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

def get_connections() -> int:
    return len(get_vpn_connections())