import streamlit as st
st.title("Mi aplicación para calcular el area de un circulo ⭕")
import math
#Widget para ingresar el radio
radio = st.slider("Selecciona el radio", 0.0, 10.0, 5.0)
#calculo del area
area = math.pi * radio **2
#Mostrar resultado
st.write(f"El área del círculo con radio (radio) es: {area:.2f}")

#Parte 1:
import streamlit as st
import math

st.title("📐 Calculadora de Áreas y Perímetros")

# 1. Selección de figura
figura = st.selectbox("Selecciona una figura:", ["Círculo", "Triángulo", "Rectángulo", "Cuadrado"])

area = None
perimetro = None

# 2. Inputs según figura seleccionada
if figura == "Círculo":
    radio = st.slider("Selecciona el radio (r)", 0.0, 100.0, 10.0)
    area = math.pi * radio ** 2
    perimetro = 2 * math.pi * radio

elif figura == "Triángulo":
    base = st.number_input("Base (b)", min_value=0.0, value=5.0)
    altura = st.number_input("Altura (h)", min_value=0.0, value=3.0)
    lado_a = st.number_input("Lado a", min_value=0.0, value=5.0)
    lado_b = st.number_input("Lado b", min_value=0.0, value=4.0)
    lado_c = st.number_input("Lado c", min_value=0.0, value=6.0)
    area = 0.5 * base * altura
    perimetro = lado_a + lado_b + lado_c

elif figura == "Rectángulo":
    base = st.number_input("Base (b)", min_value=0.0, value=6.0)
    altura = st.number_input("Altura (h)", min_value=0.0, value=4.0)
    area = base * altura
    perimetro = 2 * (base + altura)

elif figura == "Cuadrado":
    lado = st.number_input("Lado (l)", min_value=0.0, value=5.0)
    area = lado ** 2
    perimetro = 4 * lado

# 3. Mostrar resultados si hay valores válidos
if area is not None and perimetro is not None:
    st.success(f"Área: {area:.2f}")
    st.success(f"Perímetro: {perimetro:.2f}")
    # También puedes usar st.metric si prefieres una visualización diferente:
    # st.metric("Área", f"{area:.2f}")
    # st.metric("Perímetro", f"{perimetro:.2f}")

import matplotlib.pyplot as plt

# Picker de color para personalizar la figura
color = st.color_picker("Elige un color para la figura", "#0000FF")

# Visualización de la figura
fig, ax = plt.subplots()

if figura == "Círculo":
    circle = plt.Circle((0, 0), radio, color=color, fill=False, linewidth=3)
    ax.add_artist(circle)
    ax.set_xlim(-radio * 1.5, radio * 1.5)
    ax.set_ylim(-radio * 1.5, radio * 1.5)
    ax.set_aspect('equal')
    ax.axis('off')

elif figura == "Triángulo":
    # Coordenadas aproximadas de un triángulo a partir de la base y altura
    puntos = [[0, 0], [base, 0], [base / 2, altura]]
    triangulo = plt.Polygon(puntos, closed=True, fill=False, edgecolor=color, linewidth=3)
    ax.add_patch(triangulo)
    ax.set_xlim(-1, base + 1)
    ax.set_ylim(-1, altura + 1)
    ax.set_aspect('equal')
    ax.axis('off')

elif figura == "Rectángulo":
    rectangulo = plt.Rectangle((0, 0), base, altura, fill=False, edgecolor=color, linewidth=3)
    ax.add_patch(rectangulo)
    ax.set_xlim(-1, base + 1)
    ax.set_ylim(-1, altura + 1)
    ax.set_aspect('equal')
    ax.axis('off')

elif figura == "Cuadrado":
    cuadrado = plt.Rectangle((0, 0), lado, lado, fill=False, edgecolor=color, linewidth=3)
    ax.add_patch(cuadrado)
    ax.set_xlim(-1, lado + 1)
    ax.set_ylim(-1, lado + 1)
    ax.set_aspect('equal')
    ax.axis('off')

# Mostrar la figura en Streamlit
st.pyplot(fig)

