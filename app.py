import streamlit as st
st.title("Mi aplicación para calcular el area de un circulo ⭕")
import math
#Widget para ingresar el radio
radio = st.slider("Selecciona el radio", 0.0, 10.0, 5.0)
#calculo del area
area = math.pi * radio **2
#Mostrar resultado
st.write(f"El área del círculo con radio (radio) es:{area:.2f}")

figura = st.selectbox("Selecciona una figura:", "Circulo", "Triangulo", "Rectángulo", "Cuadrado")
area = None
perimetro = None
if figura == "Circulo":
  st.subheader("Circulo")
  r=st.number_input("Ingresa el radio(r):", min_value=0.0, step=0.1)
  if r > 0:
    area = math.pi * r**2
    perimetro = 2 * math.pi * r
