#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk
import psutil
import threading
import time

class SystemMonitor:
    def __init__(self, root):
        self.root = root
        self.root.title("Системен Монитор")
        self.root.geometry("400x300")
        
        # CPU
        ttk.Label(root, text="CPU:", font=('Arial', 12, 'bold')).pack(pady=5)
        self.cpu_label = ttk.Label(root, text="0%", font=('Arial', 10))
        self.cpu_label.pack()
        
        self.cpu_progress = ttk.Progressbar(root, length=300, mode='determinate')
        self.cpu_progress.pack(pady=5)
        
        # RAM
        ttk.Label(root, text="RAM:", font=('Arial', 12, 'bold')).pack(pady=5)
        self.ram_label = ttk.Label(root, text="0 GB / 0 GB", font=('Arial', 10))
        self.ram_label.pack()
        
        self.ram_progress = ttk.Progressbar(root, length=300, mode='determinate')
        self.ram_progress.pack(pady=5)
        
        # Диск
        ttk.Label(root, text="Диск:", font=('Arial', 12, 'bold')).pack(pady=5)
        self.disk_label = ttk.Label(root, text="0 GB / 0 GB", font=('Arial', 10))
        self.disk_label.pack()
        
        self.disk_progress = ttk.Progressbar(root, length=300, mode='determinate')
        self.disk_progress.pack(pady=5)
        
        # Стартиране на мониторинга
        self.running = True
        self.update_thread = threading.Thread(target=self.update_stats, daemon=True)
        self.update_thread.start()
    
    def get_size_gb(self, bytes):
        return bytes / (1024**3)
    
    def update_stats(self):
        while self.running:
            # CPU
            cpu_percent = psutil.cpu_percent(interval=1)
            self.cpu_progress['value'] = cpu_percent
            self.cpu_label.config(text=f"{cpu_percent}%")
            
            # RAM
            memory = psutil.virtual_memory()
            ram_used_gb = self.get_size_gb(memory.used)
            ram_total_gb = self.get_size_gb(memory.total)
            self.ram_progress['value'] = memory.percent
            self.ram_label.config(text=f"{ram_used_gb:.1f} GB / {ram_total_gb:.1f} GB")
            
            # Диск
            disk = psutil.disk_usage('/')
            disk_used_gb = self.get_size_gb(disk.used)
            disk_total_gb = self.get_size_gb(disk.total)
            disk_percent = (disk.used / disk.total) * 100
            self.disk_progress['value'] = disk_percent
            self.disk_label.config(text=f"{disk_used_gb:.1f} GB / {disk_total_gb:.1f} GB")
            
            time.sleep(2)

if __name__ == "__main__":
    root = tk.Tk()
    app = SystemMonitor(root)
    root.mainloop()