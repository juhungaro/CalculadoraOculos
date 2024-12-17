import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def calcular_economia(custo_anual_com_oculos, custo_cirurgia, taxa_inflacao, anos_futuro):
  """Calcula a economia ao longo dos anos, considerando a inflação.

  Args:
      custo_anual_com_oculos (float): Custo anual com óculos.
      custo_cirurgia (float): Custo da cirurgia.
      taxa_inflacao (float): Taxa de inflação anual.
      anos_futuro (int): Número de anos para o cálculo.

  Returns:
      list: Lista com os custos anuais ajustados pela inflação.
  """

  custos_anuais = []
  for ano in range(1, anos_futuro + 1):
      custo_anual_ajustado = custo_anual_com_oculos * (1 + taxa_inflacao)**ano
      custos_anuais.append(custo_anual_ajustado)

  return custos_anuais

# Coleta de dados do usuário
custo_anual_com_oculos = float(st.number_input("Qual o custo médio anual com óculos?"))
custo_cirurgia = float(st.number_input("Qual o custo da cirurgia?"))
taxa_inflacao = st.number_input('Taxa de inflação anual esperada (%):', min_value=0.0, max_value=100.0) / 100
anos_futuro = st.number_input("Em quantos anos você gostaria de estimar a economia?", min_value=1)

# Cálculos
custos_anuais = calcular_economia(custo_anual_com_oculos, custo_cirurgia, taxa_inflacao, anos_futuro)
custo_total_oculos = sum(custos_anuais)
economia_total = custo_total_oculos - custo_cirurgia

# Exibe os resultados
st.write(f"Economia total nos próximos {anos_futuro} anos: R$ {economia_total:.2f}")

# Cria um DataFrame para mostrar os dados em uma tabela
df = pd.DataFrame({'Ano': range(1, anos_futuro + 1), 'Custo Anual': custos_anuais})
st.table(df)

# Criar a figura e o eixo
fig, ax = plt.subplots()

# Plotar o gráfico
ax.plot(range(1, anos_futuro + 1), custos_anuais, label="Custo anual com óculos")
ax.axhline(y=custo_cirurgia, color='r', linestyle='--', label="Custo da cirurgia")
ax.set_xlabel("Anos")
ax.set_ylabel("Custo (R$)")
ax.set_title("Economia ao longo dos anos")
ax.legend()

# Exibir o gráfico no Streamlit
st.pyplot(fig)

