import streamlit as st
import pandas as pd
import base64


st.markdown('''
## TIPS
1a Etapa - 6a TEMPORADA
:spades: :hearts: :diamonds: :clubs:

Dia 28/03/2023 - TERÇA-FEIRA - às 19 h na P2W Setor Hoteleiro Norte

- Buy-in antecipado R$ 70,00 (1K extra em fichas)
- PIX tips2023
- Pontualidade: 1K extra em fichas
- Late Registration até 20:45h
''')
image = Image.open('tips.jpg')
st.image(image, caption='TIPS 2015')

# Define o nome e os campos do arquivo CSV
filename = "tips_2023_03.csv"
fields = ["nome", "data_reserva", "data_pagto"]

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

# Inclui a data de pagamento de um participante
st.write("Incluir data de pagamento:")
pay_name = st.selectbox("Selecione o participante para incluir a data de pagamento", options=df["nome"])
pay_date = st.date_input("Selecione a data de pagamento", value=pd.Timestamp.now().date())
if st.button("Salvar"):
    df.loc[df["nome"] == pay_name, "data_pagto"] = pay_date.strftime("%Y-%m-%d")
    st.write("Data de pagamento incluída com sucesso!")
    st.write(df)

# Salva os dados no arquivo CSV
df.to_csv(filename, index=False)

# Cria um link para fazer download do arquivo CSV
csv = df.to_csv(index=False)
b64 = base64.b64encode(csv.encode()).decode()
st.markdown(f"### Download do arquivo CSV")
href = f'<a href="data:file/csv;base64,{b64}" download="{filename}">Clique aqui para fazer download do arquivo CSV</a>'
st.markdown(href, unsafe_allow_html=True)
