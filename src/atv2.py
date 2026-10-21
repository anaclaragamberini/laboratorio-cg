import numpy as np
import streamlit as st

def ampliar(imagem, k=30):
    return imagem.repeat(k, axis=0).repeat(k, axis=1)

st.title("Imagem como matriz")
st.subheader("Bandeira do Japão")

bandeira = np.zeros((12, 18, 3), dtype=np.uint8)

bandeira[:] = (255, 255, 255)

vermelho = (188, 0, 45)

for linha in range(12):
    for coluna in range(18):
        distancia = (linha - 5.5)**2 + (coluna - 8.5)**2

        if distancia <= 3.5**2:
            bandeira[linha, coluna] = vermelho

st.image(ampliar(bandeira))

# Exibindo a matriz de pixels
st.write("Matriz RGB da bandeira:")
st.text(str(bandeira))