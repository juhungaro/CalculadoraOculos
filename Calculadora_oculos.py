import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# Carregar e exibir o logo
def mostrar_logo():
    logo = Image.open("logo_clinica.jpg")
    st.image(logo, width=300)  

def calcular_economia(custo_anual_oculos, custo_caixa_lentes, caixas_por_ano, custo_frasco_solucao, frascos_por_ano, custo_cirurgia, anos_futuro):
    custos_anuais = []
    custos_acumulados = []
    custo_acumulado = 0
    custo_anual_total = custo_anual_oculos + (custo_caixa_lentes * caixas_por_ano) + (custo_frasco_solucao * frascos_por_ano)
    for ano in range(1, anos_futuro + 1):
        custos_anuais.append(custo_anual_total)
        custo_acumulado += custo_anual_total
        custos_acumulados.append(custo_acumulado)
    return custos_anuais, custos_acumulados

def formatar_moeda(valor):
    return f"R$ {valor:,.2f}"

# Exibir o logo
mostrar_logo()

st.title("Calculadora de Custos de Cirurgia Refrativa")

col1, col2 = st.columns(2)

with col1:
    idade = st.number_input("Idade", min_value=0, max_value=120, step=1)
    custo_anual_oculos = st.number_input("Custo anual com óculos", min_value=0.0, step=0.01)
    custo_caixa_lentes = st.number_input("Custo de uma caixa de lentes de contato", min_value=0.0, step=0.01)
    caixas_por_ano = st.number_input("Número de caixas de lentes por ano", min_value=0.0, step=0.1)

with col2:
    custo_frasco_solucao = st.number_input("Custo de um frasco de solução para lentes", min_value=0.0, step=0.01)
    frascos_por_ano = st.number_input("Número de frascos de solução por ano", min_value=0.0, step=0.1)
    custo_cirurgia = st.number_input("Custo da cirurgia refrativa", min_value=0.0, step=0.01)

anos_futuro = int(77.2 - idade)  # Considerando expectativa de vida de 77.2 anos

if st.button("Calcular"):
    custos_anuais, custos_acumulados = calcular_economia(custo_anual_oculos, custo_caixa_lentes, caixas_por_ano, custo_frasco_solucao, frascos_por_ano, custo_cirurgia, anos_futuro)
    
    economia_vida = custos_acumulados[-1] - custo_cirurgia
    economia_anual_media = economia_vida / anos_futuro
    
    # Cálculo do ponto de equilíbrio
    ponto_equilibrio = next((i for i, valor in enumerate(custos_acumulados) if valor > custo_cirurgia), None)
    
    st.subheader("Resultados")
    st.write(f"Economia total ao longo da vida: {formatar_moeda(economia_vida)}")
    st.write(f"Economia anual média: {formatar_moeda(economia_anual_media)}")
    if ponto_equilibrio:
        st.write(f"A cirurgia se paga em {ponto_equilibrio} anos")
    else:
        st.write("A cirurgia não se paga no período analisado")

    # Gráfico
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(range(1, anos_futuro + 1), custos_acumulados, label="Custos acumulados sem cirurgia")
    ax.axhline(y=custo_cirurgia, color='r', linestyle='--', label="Custo da cirurgia")
    ax.set_xlabel("Anos")
    ax.set_ylabel("Custo (R$)")
    ax.set_title("Comparação de custos ao longo dos anos")
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)

st.info("Esta calculadora fornece uma estimativa. Consulte um oftalmologista para informações específicas sobre sua situação."
        "O calculo da expectativa de vida é de 77,2 anos em SP")
