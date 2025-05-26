import time
import random

def process_request(data):
    print(f"[Service2.1] Processando {data} ...")
    time.sleep(random.uniform(0.4, 1.2))
    response = f"{data} - processed by Service2.1"
    return response
