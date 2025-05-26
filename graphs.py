
import matplotlib.pyplot as plt

def generate_and_save_graph(times, filename='mrt_graph.png'):
    
    plt.figure(figsize=(10, 6))  
    plt.plot(times, label='Tempo de Resposta (s)', marker='o', color='blue')

    plt.xlabel('Requisição')
    plt.ylabel('Tempo (s)')
    plt.title('MRT - Mean Response Time')
    plt.legend()
    plt.grid(True)
    plt.savefig(filename, format='png')
    print(f"[INFO] Gráfico salvo como {filename}")
    plt.show()

    plt.close()


