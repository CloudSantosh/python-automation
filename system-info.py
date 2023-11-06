import psutil
def check_system_health():
    # Check CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")

    # Check memory usage
    memory = psutil.virtual_memory()
    print(f"Total Memory: {memory.total / (1024 ** 3):.2f} GB")
    print(f"Available Memory: {memory.available / (1024 ** 3):.2f} GB")
    print(f"Used Memory: {memory.used / (1024 ** 3):.2f} GB")
    print(f"Memory Usage: {memory.percent}%")

if __name__ == "__main__":
    check_system_health()
