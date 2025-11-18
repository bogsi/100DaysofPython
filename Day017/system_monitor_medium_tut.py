import psutil
import time
import logging

# Set up logging configuration
logging.basicConfig(filename='system_monitor.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def monitor_system():
    while True:
        # CPU Usage
        cpu_usage = psutil.cpu_percent(interval=1)
        print(f"CPU Usage: {cpu_usage}%")
        if cpu_usage > 80:
            print("Warning: High CPU usage detected!")

        # Memory Usage
        memory = psutil.virtual_memory()
        print(f"Memory Usage: {memory.percent}%")
        if memory.percent > 80:
            print("Warning: High Memory usage detected!")

        # Disk Usage
        disk_usage = psutil.disk_usage('/')
        print(f"Disk Usage: {disk_usage.percent}%")
        if disk_usage.percent > 80:
            print("Warning: High Disk usage detected!")

        # Network Usage
        network =  psutil.net_io_counters()
        print(f"Bytes Sent: {network.bytes_sent}, Bytes Received: {network.bytes_recv}")

        # Add a separator for readability
        print("-" * 40)

        # Pause for 5 seconds before the next update
        time.sleep(5)  

if __name__ == "__main__":
    monitor_system()

def __init__(self):
