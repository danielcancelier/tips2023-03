import streamlit as st
import pandas as pd
from PIL import Image

# Define o nome e os campos do arquivo CSV
filename = "tips_2023_03.csv"
fields = ["nome", "data_reserva", "data_pagto"]

st.markdown('''
## 1a Etapa TIPS - 6a TEMPORADA
:spades: :hearts: :diamonds: :clubs:

## Dia 28/03/2023 - TERÇA-FEIRA - às 19 h na P2W Setor Hoteleiro Norte

- Buy-in antecipado R$ 70,00 (1K extra em fichas)
- PIX tips2023
- Pontualidade: 1K extra em fichas
- Late Registration até 20:45h
''')
image = Image.open('tips.jpg')
st.image(image, caption='TIPS 2015')

# Cria o arquivo CSV caso ainda não exista
try:
    pd.read_csv(filename)
except:
    pd.DataFrame(columns=fields).to_csv(filename, index=False)

# Lê os dados do arquivo CSV
df = pd.read_csv(filename)

# Exibe a lista de participantes
st.write("Lista de participantes:")
st.write(df)

# Adiciona um novo participante
st.write("Adicionar novo participante:")
new_name = st.text_input("Nome")
if st.button("Adicionar"):
    new_data = pd.DataFrame([[new_name, pd.Timestamp.now().strftime("%Y-%m-%d"), ""]], columns=fields)
    df = pd.concat([df, new_data], ignore_index=True)
    st.write("Participante adicionado com sucesso!")
    st.write(df)

# Exclui um participante
st.write("Excluir participante:")
delete_name = st.selectbox("Selecione o participante a ser excluído", options=df["nome"])
if st.button("Excluir"):
    df = df[df["nome"] != delete_name]
    st.write("Participante excluído com sucesso!")
    st.write(df)

# Salva os dados no arquivo CSV
df.to_csv(filename, index=False)