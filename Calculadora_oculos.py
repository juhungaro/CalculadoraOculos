import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def calcular_economia(custo_anual_com_oculos, custo_caixa_lentes, caixas_por_ano, custo_frasco_solucao, frascos_por_ano, custo_cirurgia, taxa_inflacao, anos_futuro):
    custos_anuais = []
    for ano in range(1, anos_futuro + 1):
        custo_anual_total = custo_anual_com_oculos + custo_caixa_lentes * caixas_por_ano + custo_frasco_solucao * frascos_por_ano
        custo_anual_ajustado = custo_anual_total * (1 + taxa_inflacao)**ano
        custos_anuais.append(custo_anual_ajustado)
    return custos_anuais

  Args:
        custo_anual_com_oculos (float): Custo anual com óculos.
        custo_caixa_lentes (float): Custo de uma caixa de lentes de contato.
        caixas_por_ano (float): Número de caixas de lentes por ano.
        custo_frasco_solucao (float): Custo de um frasco de solução.
        frascos_por_ano (float): Número de frascos por ano.
        custo_cirurgia (float): Custo da cirurgia.
        anos_futuro (int): Número de anos para o cálculo.

    Returns:
        list: Lista com os custos anuais ajustados pela inflação.

  
# Coleta de dados do usuário
idade = st.number_input("Quantos anos você tem?")
custo_anual_com_oculos = float(st.number_input("Quanto você paga pelos seus óculos de grau por ano?"))
custo_caixa_lentes = float(st.number_input("Quanto você paga por uma caixa de lentes de contato?"))
caixas_por_ano = float(st.number_input("Quantas caixas de lentes de contato você usa por ano?"))
custo_frasco_solucao = float(st.number_input("Quanto você paga por um frasco de solução para lentes de contato?"))
frascos_por_ano = float(st.number_input("Quantos frascos de solução para lentes de contato você usa por ano?"))
custo_cirurgia = float(st.number_input("Qual o custo da cirurgia?"))
taxa_inflacao = st.number_input('Taxa de inflação anual esperada (%):', min_value=0.0, max_value=100.0) / 100
anos_futuro = 77.2 - idade  # Considerando expectativa de vida de 77.2 anos


# Cálculos
custos_anuais = calcular_economia(custo_anual_com_oculos, custo_cirurgia, taxa_inflacao, anos_futuro)
custo_total_oculos = sum(custos_anuais)
economia_total = custo_total_oculos - custo_cirurgia

# Cálculo do custo total ao longo da vida com óculos e lentes de contato
custo_total_vida = custo_total_oculos + (custo_caixa_lentes * caixas_por_ano + custo_frasco_solucao * frascos_por_ano) * anos_futuro

# Cálculo da economia ao longo da vida
economia_vida = custo_total_vida - custo_cirurgia

# Cálculo da economia anual média
economia_anual_media = economia_vida / anos_futuro

# Exibe os resultados
st.write(f"Economia total ao longo da vida: R$ {economia_vida:.2f}")
st.write(f"Economia anual média: R$ {economia_anual_media:.2f}")

# Cria a figura e o eixo
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

