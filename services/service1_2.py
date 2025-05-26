import time
import random

def process_request(data):
    print(f"[Service1.2] Processando {data} ...")
    time.sleep(random.uniform(0.3, 1.0))
    response = f"{data} - processed by Service1.2"
    return response
