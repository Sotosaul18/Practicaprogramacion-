import streamlit as st
st.title("Mi aplicación para calcular el area de un circulo ⭕")
import math
#Widget para ingresar el radio
radio = st.slider("Selecciona el radio", 0.0, 10.0, 5.0)
#calculo del area
area = math.pi * radio **2
#Mostrar resultado
st.write(f"El área del círculo con radio (radio) es:{area:.2f}")

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

st.set_page_config(page_title="Calculadora Geométrica y Trigonometría", layout="centered")
st.title("📐 Calculadora Geométrica y Trigonometría")

# Tabs para separar secciones
tab1, tab2 = st.tabs(["🧮 Geometría", "📊 Trigonometría"])

# -------------------------------------
# TAB 1 — GEOMETRÍA
# -------------------------------------
with tab1:
    st.header("Figuras geométricas: área, perímetro y visualización")
    
    figura = st.selectbox("Selecciona una figura:", ["Círculo", "Triángulo", "Rectángulo", "Cuadrado"])
    color = st.color_picker("Selecciona un color para la figura", "#000000")

    area = None
    perimetro = None

    fig, ax = plt.subplots()

    if figura == "Círculo":
        radio = st.slider("Selecciona el radio (r)", 0.0, 100.0, 10.0)
        area = math.pi * radio ** 2
        perimetro = 2 * math.pi * radio
        circle = plt.Circle((0, 0), radio, color=color, fill=False, linewidth=2)
        ax.add_artist(circle)
        ax.set_xlim(-radio*1.2, radio*1.2)
        ax.set_ylim(-radio*1.2, radio*1.2)

    elif figura == "Triángulo":
        base = st.number_input("Base (b)", min_value=0.0, value=6.0)
        altura = st.number_input("Altura (h)", min_value=0.0, value=4.0)
        lado_a = st.number_input("Lado a", min_value=0.0, value=5.0)
        lado_b = st.number_input("Lado b", min_value=0.0, value=4.0)
        lado_c = st.number_input("Lado c", min_value=0.0, value=6.0)
        area = 0.5 * base * altura
        perimetro = lado_a + lado_b + lado_c
        # Triángulo visual aproximado
        triangle = plt.Polygon([[0, 0], [base, 0], [base / 2, altura]], edgecolor=color, fill=False, linewidth=2)
        ax.add_patch(triangle)
        ax.set_xlim(-1, base + 1)
        ax.set_ylim(-1, altura + 2)

    elif figura == "Rectángulo":
        base = st.number_input("Base (b)", min_value=0.0, value=6.0)
        altura = st.number_input("Altura (h)", min_value=0.0, value=4.0)
        area = base * altura
        perimetro = 2 * (base + altura)
        rect = plt.Rectangle((0, 0), base, altura, edgecolor=color, fill=False, linewidth=2)
        ax.add_patch(rect)
        ax.set_xlim(-1, base + 1)
        ax.set_ylim(-1, altura + 1)

    elif figura == "Cuadrado":
        lado = st.number_input("Lado (l)", min_value=0.0, value=5.0)
        area = lado ** 2
        perimetro = 4 * lado
        square = plt.Rectangle((0, 0), lado, lado, edgecolor=color, fill=False, linewidth=2)
        ax.add_patch(square)
        ax.set_xlim(-1, lado + 1)
        ax.set_ylim(-1, lado + 1)

    ax.set_aspect('equal')
    ax.axis('off')
    st.pyplot(fig)

    if area is not None and perimetro is not None:
        st.success(f"Área: {area:.2f}")
        st.success(f"Perímetro: {perimetro:.2f}")

    # EXTRA: Teorema de Pitágoras
    with st.expander("➕ Calculadora del Teorema de Pitágoras"):
        cateto1 = st.number_input("Cateto a", min_value=0.0, value=3.0)
        cateto2 = st.number_input("Cateto b", min_value=0.0, value=4.0)
        hipotenusa = math.sqrt(cateto1**2 + cateto2**2)
        st.metric("Hipotenusa (c)", f"{hipotenusa:.2f}")

# -------------------------------------
# TAB 2 — TRIGONOMETRÍA
# -------------------------------------
with tab2:
    st.header("Funciones trigonométricas")

    rango_inicio = st.slider("Inicio del rango (x)", 0.0, 10.0, 0.0)
    rango_fin = st.slider("Fin del rango (x)", 0.1, 20.0, 2 * math.pi)
    amp = st.slider("Amplitud", 0.1, 5.0, 1.0)

    x = np.linspace(rango_inicio, rango_fin, 500)

    st.subheader("Función seno")
    st.line_chart(amp * np.sin(x))

    st.subheader("Función coseno")
    st.line_chart(amp * np.cos(x))

    st.subheader("Función tangente")
    y_tan = amp * np.tan(x)
    y_tan[np.abs(y_tan) > 10] = np.nan  # Para evitar saltos infinitos
    st.line_chart(y_tan)

    # EXTRA: Onda amortiguada
    with st.expander("🌊 Visualizador de ondas amortiguadas"):
        freq = st.slider("Frecuencia", 0.5, 5.0, 1.0)
        amp_wave = st.slider("Amplitud de la onda", 0.1, 3.0, 1.0)
        x_wave = np.linspace(0, 20, 500)
        y_wave = amp_wave * np.exp(-0.1 * x_wave) * np.sin(freq * x_wave)

        fig_wave, ax_wave = plt.subplots()
        ax_wave.plot(x_wave, y_wave, color="purple")
        ax_wave.set_title("f(x) = e^(-0.1x) * sin(fx)")
        st.pyplot(fig_wave)

