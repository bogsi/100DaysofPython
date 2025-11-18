import psutil
import time

def monitor_cpu(interval=1):
    cpu_usage = psutil.cpu_percent(interval=interval)
    print(f"CPU Usage: {cpu_usage}%")

print(monitor_cpu())

def monitor_memory(interval=1):
    memory_info = psutil.virtual_memory()
    print(f"Memory Usage: {memory_info.percent}%")

print(monitor_memory())

def monitor_disk(interval=1):
    disk_usage = psutil.disk_usage('/')
    print(f"Disk Usage: {disk_usage.percent}%")

print(monitor_disk())

def monitor_network(interval=1):
    net_io = psutil.net_io_counters()
    print(f"Bytes Sent: {net_io.bytes_sent}, Bytes Received: {net_io.bytes_recv}")

print(monitor_network())
