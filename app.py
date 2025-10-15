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

#Mostrar resultados si hay valores válidos
if area is not None and perimetro is not None:
    st.success(f"Área: {area:.2f}")
    st.success(f"Perímetro: {perimetro:.2f}")
    # También puedes usar st.metric si prefieres una visualización diferente:
    # st.metric("Área", f"{area:.2f}")
    # st.metric("Perímetro", f"{perimetro:.2f}")

# Parte 2 — Visualización
import matplotlib.pyplot as plt

st.subheader("🎨 Visualización de la figura")

# Selector de color
color = st.color_picker("Selecciona un color para la figura", "#00f900")

# Crear figura y ejes
fig, ax = plt.subplots()

if figura == "Círculo":
    circle = plt.Circle((0, 0), radio, color=color, fill=False, linewidth=2)
    ax.add_patch(circle)
    ax.set_xlim(-radio * 1.2, radio * 1.2)
    ax.set_ylim(-radio * 1.2, radio * 1.2)

elif figura == "Triángulo":
    puntos = [[0, 0], [base, 0], [base / 2, altura]]
    triangulo = plt.Polygon(puntos, edgecolor=color, fill=False, linewidth=2)
    ax.add_patch(triangulo)
    ax.set_xlim(-1, base + 1)
    ax.set_ylim(-1, altura + 2)

elif figura == "Rectángulo":
    rect = plt.Rectangle((0, 0), base, altura, edgecolor=color, fill=False, linewidth=2)
    ax.add_patch(rect)
    ax.set_xlim(-1, base + 1)
    ax.set_ylim(-1, altura + 1)

elif figura == "Cuadrado":
    rect = plt.Rectangle((0, 0), lado, lado, edgecolor=color, fill=False, linewidth=2)
    ax.add_patch(rect)
    ax.set_xlim(-1, lado + 1)
    ax.set_ylim(-1, lado + 1)

# Ajustes visuales
ax.set_aspect('equal')
ax.axis('off')  # Ocultar ejes

# Mostrar figura 
st.pyplot(fig)

# --- Parte 3: Relaciones trigonométricas ---
with tab3:
    st.header("📈 Funciones trigonométricas")

    # Rango de x (de 0 a 2π por defecto)
    rango_min, rango_max = 0.0, 2 * np.pi
    rango = st.slider("Selecciona el rango de x (radianes)", 0.0, 10.0, (rango_min, rango_max), step=0.1)

    # Amplitud
    amp = st.slider("Amplitud", 0.1, 5.0, 1.0)

    x = np.linspace(rango[0], rango[1], 300)

    # Graficar funciones usando st.line_chart (simple)
    st.write("Función seno:")
    st.line_chart(amp * np.sin(x))

    st.write("Función coseno:")
    st.line_chart(amp * np.cos(x))

    st.write("Función tangente:")
    # Para evitar valores muy grandes en tangente, limitamos un poco y filtramos
    y_tan = amp * np.tan(x)
    y_tan = np.where(np.abs(y_tan) > 10, np.nan, y_tan)  # Remplaza valores muy grandes con NaN para que no distorsione

    st.line_chart(y_tan)

