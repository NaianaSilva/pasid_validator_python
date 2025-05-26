import threading 
import time 
import source
import load_balancer1
import load_balancer2

def start_lb1():
    lb1 = load_balancer1.LoadBalancer1()
    lb1.start()

def start_lb2():
    lb2 = load_balancer2.LoadBalancer2()
    lb2.start()

if __name__ == "__main__":
    
    t1 = threading.Thread(target=start_lb1, daemon=True)
    t2 = threading.Thread(target=start_lb2, daemon=True)

    t1.start()
    t2.start()

    time.sleep(1) 

    src = source.Source()
    src.run()
