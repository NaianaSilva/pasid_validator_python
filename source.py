import socket
import time
from graphs import generate_and_save_graph

class Source:
    def __init__(self, lb1_host='localhost', lb1_port=5001, n_requests=20, interval=0.5):

        self.lb1_host = lb1_host
        self.lb1_port = lb1_port
        self.n_requests = n_requests 
        self.interval = interval
        self.times = []  

    def send_request(self, req_id):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
                s.connect((self.lb1_host, self.lb1_port))
                start_time = time.time() 
                msg = f"REQ-{req_id}"
                s.sendall(msg.encode())

                data = s.recv(1024)  

                end_time = time.time()
                total_time = end_time - start_time
                self.times.append(total_time)

                print(f"[Source] Req {req_id} RTT: {total_time:.3f}s, Resp: {data.decode()}")

        except Exception as e:
            print(f"[Source] Error: {e}")

    def run(self):
        for i in range(self.n_requests):
            self.send_request(i+1)
            time.sleep(self.interval)
        self.report()

    def report(self):
        avg_time = sum(self.times) / len(self.times) if self.times else 0
        print(f"\n[Source] Tempo médio de resposta (MRT): {avg_time:.3f} segundos")
        generate_and_save_graph(self.times) 

if __name__ == "__main__":
    source = Source()
    source.run()
