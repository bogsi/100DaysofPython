#!/usr/bin/env python3
import psutil
import time
import os

def get_size(bytes):
    """Конвертира байтове в четим формат"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024.0:
            return f"{bytes:.2f} {unit}"
        bytes /= 1024.0

def monitor_system():
    """Показва системните ресурси"""
    os.system('clear')  # За macOS/Linux
    
    # CPU информация
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_count = psutil.cpu_count()
    
    # RAM информация
    memory = psutil.virtual_memory()
    
    # Дисково пространство
    disk = psutil.disk_usage('/')
    
    print("=" * 50)
    print("           СИСТЕМЕН МОНИТОР")
    print("=" * 50)
    
    print(f"\n🖥️  CPU:")
    print(f"   Използване: {cpu_percent}%")
    print(f"   Ядра: {cpu_count}")
    
    print(f"\n💾 RAM:")
    print(f"   Общо: {get_size(memory.total)}")
    print(f"   Използвано: {get_size(memory.used)} ({memory.percent}%)")
    print(f"   Свободно: {get_size(memory.available)}")
    
    print(f"\n💿 Диск (/):")
    print(f"   Общо: {get_size(disk.total)}")
    print(f"   Използвано: {get_size(disk.used)} ({disk.used/disk.total*100:.1f}%)")
    print(f"   Свободно: {get_size(disk.free)}")
    
    print(f"\n⏰ Последно обновление: {time.strftime('%H:%M:%S')}")

if __name__ == "__main__":
    try:
        while True:
            monitor_system()
            time.sleep(2)  # Обновява на всеки 2 секунди
    except KeyboardInterrupt:
        print("\n\nМониторът е спрян.")