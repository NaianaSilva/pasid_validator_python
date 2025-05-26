import time
import random

def process_request(data):
    print(f"[Service2.2] Processando {data} ...")
    time.sleep(random.uniform(0.2, 0.8))
    response = f"{data} - processed by Service2.2"
    return response
