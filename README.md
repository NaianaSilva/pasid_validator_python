# pasid_validator_python
validador PASID

# 🗂️ PASID-VALIDATOR

## 📄 Descrição do Projeto
O **PASID-VALIDATOR** é um sistema distribuído desenvolvido com o objetivo de validar dados simulados de forma robusta e escalável. O sistema foi projetado com uma arquitetura baseada em balanceadores de carga e múltiplos serviços, garantindo divisão de tarefas, paralelismo e otimização no processamento de requisições.

## 🎯 Objetivos
- Simular um ambiente distribuído.
- Implementar balanceamento de carga entre serviços.
- Avaliar o tempo médio de resposta (MRT) das requisições.
- Visualizar o desempenho através de gráficos.


🔹 Componentes:

Source: Gera requisições de validação e mede o tempo de resposta (RTT e MRT).

LoadBalancer1: Encaminha requisições para os serviços do primeiro nível (Service1.1 e Service1.2).

LoadBalancer2: Recebe respostas do LB1 e distribui para os serviços do segundo nível (Service2.1 e Service2.2).

Services: Realizam o processamento das requisições, simulando carga de trabalho.


⚙️ Tecnologias Utilizadas:

Python (Sockets, Threading)

Matplotlib (para geração de gráficos)

Conceitos de Redes (TCP/IP)

Balanceamento de carga

Simulação de cargas com time.sleep()


🚀 Funcionamento

1. O cliente (Source) envia um número configurável de requisições ao LoadBalancer1.

2. O LoadBalancer1 distribui alternadamente as requisições entre os serviços Service1.1 e Service1.2.

3. Cada serviço processa a requisição, simulando tempo de trabalho com atraso (sleep()).

4. O LoadBalancer1 repassa a resposta para o LoadBalancer2.

5. O LoadBalancer2 realiza nova distribuição, agora entre Service2.1 e Service2.2.

6. A resposta final retorna ao Source, que registra o tempo total de ida e volta (RTT) e gera o gráfico de MRT (Mean Response Time).