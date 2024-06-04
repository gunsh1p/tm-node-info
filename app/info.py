import psutil
import subprocess

def get_cpu_percent() -> float:
    return psutil.cpu_percent()

def get_memory_usage() -> tuple:
    data = psutil.virtual_memory()
    percent = data.percent
    used = round(data.used / 2**33, 1)
    total = round(data.total / 2**33, 1)
    
    return (percent, used, total)

def get_connections() -> int:
    output = subprocess.check_output(["netstat", "-an", "-p", "tcp", "|", "grep", "8701", "|", "grep," "ESTABLISHED", "|", "wc", "-l"])
    return int(output)