import socket
import threading 
from services import service1_1, service1_2


LB2_HOST = 'localhost'
LB2_PORT = 6001

SERVICES = [service1_1.process_request, service1_2.process_request]

class LoadBalancer1:
    def __init__(self, host='localhost', port=5001):
        self.host = host
        self.port = port
        self.current = 0  

    def round_robin(self):
        svc = SERVICES[self.current]
        self.current = (self.current + 1) % len(SERVICES)
        return svc
    
    def handle_client(self, conn, addr):
        try:
            data = conn.recv(1024).decode()
            print(f"[LB1] Recebeu: {data} de {addr}")

            service = self.round_robin()
            proc_result = service(data)

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((LB2_HOST, LB2_PORT))
                s.sendall(proc_result.encode())
                resp = s.recv(1024).decode()
                print(f"[LB1] Resposta LB2: {resp}")
                
            conn.sendall(resp.encode())

        except Exception as e:
            print(f"[LB1] Erro: {e}")
        finally:
            conn.close()

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            print(f"[LB1] Escutando em {self.host}:{self.port}...")
            while True:
                conn, addr = s.accept()
                threading.Thread(target=self.handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    lb1 = LoadBalancer1()
    lb1.start()
