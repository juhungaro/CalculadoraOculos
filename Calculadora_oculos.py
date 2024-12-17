import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def calcular_economia(custo_anual_com_oculos, custo_cirurgia, taxa_inflacao, anos_futuro):
    """Calcula a economia ao longo dos anos, considerando a inflação.

    Args:
        custo_anual_com_oculos (float): Custo anual com óculos.
        custo_cirurgia (float): Custo da cirurgia.
        taxa_inflacao (float): Taxa de inflação anual.
        anos_futuro (int): Número de anos para o cálculo.

    Returns:
        list: Lista com os custos anuais ajustados pela inflação.
        float: Economia total.
    """
# Cálculo correto da economia total
    custo_total_oculos = sum(custos_anuais)
    economia_total = custo_total_oculos - custo_cirurgia
    return custos_anuais, economia_total

# Coleta de dados
custo_anual_com_oculos = float(st.number_input("Qual o custo médio anual com óculos?"))
custo_cirurgia = float(st.number_input("Qual o custo da cirurgia?"))
taxa_inflacao = st.number_input('Taxa de inflação anual esperada (%):', min_value=0.0, max_value=100.0) / 100
anos_futuro = st.number_input("Em quantos anos você gostaria de estimar a economia?", min_value=1)

# Cálculos e visualização
custos_anuais, economia_total = calcular_economia(custo_anual_com_oculos, custo_cirurgia, taxa_inflacao, anos_futuro)

st.write(f"Economia total nos próximos {anos_futuro} anos: R$ {economia_total:.2f}")

# Criar um DataFrame para mostrar os dados em uma tabela
df = pd.DataFrame({'Ano': range(1, anos_futuro + 1), 'Custo Anual': custos_anuais})
st.table(df)

# Criar um gráfico
plt.plot(range(1, anos_futuro + 1), custos_anuais, label="Custo anual com óculos")
plt.axhline(y=custo_cirurgia, color='r', linestyle='--', label="Custo da cirurgia")
plt.xlabel("Anos")
plt.ylabel("Custo (R$)")
plt.title("Economia ao longo dos anos")
plt.legend()
plt.show()

# Aplicar o estilo 'darkgrid'
sns.set_style('darkgrid')

# Criar a figura e os eixos
fig, ax = plt.subplots(figsize=(10, 6))  # Ajustar o tamanho da figura

# Plotar os dados
ax.plot(range(1, anos_futuro + 1), custos_anuais, color='green', marker='o', label="Custo anual com óculos")
ax.axhline(y=custo_cirurgia, color='red', linestyle='--', label="Custo da cirurgia")

# Adicionar título, rótulos e legenda
ax.set_title("Evolução do Custo ao Longo dos Anos", fontsize=16)
ax.set_xlabel("Anos")
ax.set_ylabel("Custo (R$)")
ax.legend(loc='upper left')

# Formatar os eixos
ax.grid(True, linestyle='--', alpha=0.7)
ax.set_xticks(range(1, anos_futuro + 1))  # Ajustar os ticks do eixo x

# Adicionar uma anotação
ax.annotate(f"Economia total: R$ {economia_total:.2f}", xy=(anos_futuro/2, custo_cirurgia/2),
            ha='center', va='center', fontsize=12, bbox=dict(facecolor='white', alpha=0.8))

# Exibir o gráfico no Streamlit
st.pyplot(fig)
