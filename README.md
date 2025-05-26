
# 🗂️ PASID-VALIDATOR

## 📄 Descrição do Projeto
O **PASID-VALIDATOR** é um sistema distribuído desenvolvido com o objetivo de validar dados simulados de forma robusta e escalável. O sistema foi projetado com uma arquitetura baseada em balanceadores de carga e múltiplos serviços, garantindo divisão de tarefas, paralelismo e otimização no processamento de requisições.

## 🎯 Objetivos
- Simular um ambiente distribuído.
- Implementar balanceamento de carga entre serviços.
- Avaliar o tempo médio de resposta (MRT) das requisições.
- Visualizar o desempenho através de gráficos.
- Testar conceitos de tolerância a falhas e escalabilidade.

##  Arquitetura do Sistema

```plaintext
           +---------+
           |  Source | (Cliente Gerador de Requisições)
           +---------+
                |
                v
       +----------------+
       | LoadBalancer 1 | -> Distribui para Service1.1 e Service1.2
       +----------------+
                |
                v
       +----------------+
       | LoadBalancer 2 | -> Distribui para Service2.1 e Service2.2
       +----------------+
```

### 🔹 Componentes
- **Source:** Gera requisições de validação e mede o tempo de resposta (RTT e MRT).
- **LoadBalancer1:** Encaminha requisições para os serviços do primeiro nível (Service1.1 e Service1.2).
- **LoadBalancer2:** Recebe respostas do LB1 e distribui para os serviços do segundo nível (Service2.1 e Service2.2).
- **Services:** Realizam o processamento das requisições, simulando carga de trabalho.

## ⚙️ Tecnologias Utilizadas
- Python (Sockets, Threading)
- Matplotlib (para geração de gráficos)
- Conceitos de Redes (TCP/IP)
- Balanceamento de carga
- Simulação de cargas com time sleep

## 🚀 Funcionamento
1. O cliente (**Source**) envia um número configurável de requisições ao LoadBalancer1.
2. O LoadBalancer1 distribui alternadamente as requisições entre os serviços Service1.1 e Service1.2.
3. Cada serviço processa a requisição, simulando tempo de trabalho com atraso.
4. O LoadBalancer1 repassa a resposta para o LoadBalancer2.
5. O LoadBalancer2 realiza nova distribuição, agora entre Service2.1 e Service2.2.
6. A resposta final retorna ao Source, que registra o tempo total de ida e volta (**RTT**) e gera o gráfico de **MRT (Mean Response Time)**.

## 📊 Análise de Desempenho
- O gráfico gerado mostra o tempo de resposta de cada requisição.
- É possível observar picos, estabilidade ou gargalos na distribuição das requisições, simulando o comportamento de sistemas distribuídos sob carga variável.

## 📈 Geração de Gráficos
- O sistema gera um gráfico representando o **Tempo Médio de Resposta (MRT)** por requisição.
- O gráfico é salvo automaticamente como `mrt_graph.png` e também é exibido na tela.

## Veja abaixo os comandos necessários para rodar o projeto:

Em um terminal rode python load_balancer2.py, 
em outro rode python load_balancer1.py, 
no terceiro rode python source.py. 

Ou pode rodar tudo em uma só execução: utilizando python main.py.



