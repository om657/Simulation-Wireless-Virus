# virus_sim.py
import time
import threading
import random

infected_devices = []

def simulate_infection():
    global infected_devices
    base_ip = "192.168.0"
    for i in range(1, 21):  # Scan 20 devices
        ip = f"{base_ip}.{i}"
        time.sleep(random.uniform(0.5, 1.5))
        infected_devices.append({
            "ip": ip,
            "status": "infected",
            "timestamp": time.strftime("%H:%M:%S")
        })

def start_simulation():
    thread = threading.Thread(target=simulate_infection)
    thread.start()
