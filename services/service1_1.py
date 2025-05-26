import time
import random

def process_request(data):
    print(f"[Service1.1] Processando {data} ...") 
    time.sleep(random.uniform(0.5, 1.5))  
    response = f"{data} - processed by Service1.1" 
    return response 
