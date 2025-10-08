import pandas as pd

# 1. Ler a base de dados
df = pd.read_csv("dados.csv")

# 2. Mostrar as primeiras linhas para conferir
print("Visualizando os primeiros registros:")
print(df.head())

# 3. Contar quantos registros existem em cada etapa
Etapas = df['Etapa'].value_counts()
print("\nQuantidade de contatos por Etapa:")
print(Etapas)

# 4. Calcular taxa de conversão de cada etapa
print("\nTaxas de conversão:")
total_inicial = Etapas.sum()
for Etapa, qtd in Etapas.items():
    taxa = (qtd / total_inicial) * 100
    print(f"{Etapa}: {taxa:.2f}% do total")
import pandas as pd

# Lendo o arquivo CSV
df = pd.read_csv("dados.csv")

# Mostrando os primeiros registros
print("Visualizando os primeiros registros:")
print(df)

# Extraindo os valores de cada etapa
visitantes = df.loc[df["Etapa"] == "Visitantes", "Quantidade"].values[0]
leads = df.loc[df["Etapa"] == "Leads", "Quantidade"].values[0]
oportunidades = df.loc[df["Etapa"] == "Oportunidades", "Quantidade"].values[0]
vendas = df.loc[df["Etapa"] == "Vendas", "Quantidade"].values[0]

# Calculando as taxas de conversão entre as etapas
taxa_visitantes_leads = (leads / visitantes) * 100
taxa_leads_oportunidades = (oportunidades / leads) * 100
taxa_oportunidades_vendas = (vendas / oportunidades) * 100

# Mostrando os resultados
print("\n📊 Taxas de conversão do funil:")
print(f"Visitantes → Leads: {taxa_visitantes_leads:.2f}%")
print(f"Leads → Oportunidades: {taxa_leads_oportunidades:.2f}%")
print(f"Oportunidades → Vendas: {taxa_oportunidades_vendas:.2f}%")

# Exibindo a conversão total (Visitantes → Vendas)
taxa_total = (vendas / visitantes) * 100
print(f"\nConversão total (Visitantes → Vendas): {taxa_total:.2f}%")
