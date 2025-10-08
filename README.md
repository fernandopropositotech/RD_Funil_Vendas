# Projeto: Funil de Vendas (simulação inspirada na RD Station)

## Objetivo
Criar uma análise simples de funil de vendas: visitantes → leads → oportunidades → vendas.  
Mostrar onde a empresa perde mais contatos e pensar em soluções.

## Contexto
Muitas empresas investem em marketing, mas não conseguem transformar visitantes em vendas.  
Esse projeto simula esse cenário e mostra como analisar os gargalos.

## Dados usados
Dados fictícios (inventados para aprendizado).  
Exemplo:
- Visitantes: 1000  
- Leads: 200  
- Oportunidades: 50  
- Vendas: 20  

## Resultados esperados
- Gráfico do funil de vendas.  
- Porcentagens de conversão entre etapas.  
- Insights para melhorar.

## Estrutura
- README.md → Explicação do projeto  
- dados.csv → (vamos criar depois)  
- analise_funil.py → (vamos criar depois)  
- funil.png → (gráfico gerado depois)

## Autor
Fernando Caruzo
import pandas as pd

# 1. Ler a base de dados
df = pd.read_csv("dados.csv")

# 2. Mostrar as primeiras linhas para conferir
print("Visualizando os primeiros registros:")
print(df.head())

# 3. Contar quantos registros existem em cada etapa
etapas = df['etapa'].value_counts()
print("\nQuantidade de contatos por etapa:")
print(etapas)

# 4. Calcular taxa de conversão de cada etapa
print("\nTaxas de conversão:")
total_inicial = etapas.sum()
for etapa, qtd in etapas.items():
    taxa = (qtd / total_inicial) * 100
    print(f"{etapa}: {taxa:.2f}% do total")

