import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

# Parámetros
COSTE_POR_MILLON_TOKENS = 7
TOKENS_POR_MENSAJE = 1000

# Función para calcular el coste
def calcular_coste(num_usuarios, mensajes_por_usuario, tokens_por_mensaje=TOKENS_POR_MENSAJE, coste_por_M_tokens=COSTE_POR_MILLON_TOKENS  ):
    tokens_por_usuario = mensajes_por_usuario * tokens_por_mensaje
    tokens_totales = num_usuarios * tokens_por_usuario
    coste = (tokens_totales / 1_000_000) * coste_por_M_tokens
    return coste

# Interfaz de Streamlit
st.title('Simulación de Costes de una Pipeline de IA')
st.write('Ajusta el número de usuarios y el número de mensajes por usuario para ver el coste.')

num_usuarios = st.slider('Número de Usuarios', 1, 100000, 10000)
mensajes_por_usuario = st.slider('Mensajes por Usuario', 1, 50, 5)
tokens_por_mensaje = st.slider('Tokens por usuario', 400, 2000, 1000)
coste_por_M_tokens= st.slider('Coste por M Tokens', 0.4, 30.0, 7.0)

coste = calcular_coste(num_usuarios, mensajes_por_usuario, tokens_por_mensaje, coste_por_M_tokens)
st.write(f'El coste estimado es: ${coste:.2f}')

# Crear datos para la gráfica 3D
usuarios = np.arange(1, 100000, 1000)
mensajes = np.arange(1, 20, 5)
X, Y = np.meshgrid(usuarios, mensajes)
Z = calcular_coste(X, Y)

# Gráfica 3D
fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y)])
fig.update_layout(title='Coste de la Pipeline de IA', scene=dict(
    xaxis_title='Número de Usuarios',
    yaxis_title='Mensajes por Usuario',
    zaxis_title='Coste ($)'
))

st.plotly_chart(fig)