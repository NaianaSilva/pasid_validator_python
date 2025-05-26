import socket
import threading
from services import service2_1, service2_2

SERVICES = [service2_1.process_request, service2_2.process_request]

class LoadBalancer2:
    def __init__(self, host='localhost', port=6001):
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
            print(f"[LB2] Recebeu: {data} de {addr}")

            service = self.round_robin()
            result = service(data)

            conn.sendall(result.encode())
        except Exception as e:
            print(f"[LB2] Erro: {e}")
        finally:
            conn.close()

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            print(f"[LB2] Escutando em {self.host}:{self.port}...")
            while True:
                conn, addr = s.accept()
                threading.Thread(target=self.handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    lb2 = LoadBalancer2()
    lb2.start()
