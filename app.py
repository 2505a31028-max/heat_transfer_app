import streamlit as st
import math

# Set Page Title and Configuration
st.set_page_config(page_title="Conduction Heat Transfer Calculator", page_icon="🔥", layout="centered")

st.title("🔥 Conduction Heat Transfer Calculator")
st.write("Calculate the heat transfer rate ($Q$) through different wall geometries.")

# Sidebar Menu Selection
geometry = st.sidebar.selectbox(
    "Select Wall Geometry:",
    ["Plane Wall", "Cylindrical Wall", "Spherical Wall"]
)

st.header(f"Geometry: {geometry}")

# --- 1. PLANE WALL ---
if geometry == "Plane Wall":
    st.markdown("Formula: **$Q = \\frac{k \\cdot A \\cdot (T_1 - T_2)}{L}$**")
    
    col1, col2 = st.columns(2)
    with col1:
        k = st.number_input("Thermal Conductivity k (W/m·K)", min_value=0.0001, value=0.8, step=0.1)
        A = st.number_input("Surface Area A (m²)", min_value=0.0001, value=10.0, step=0.5)
        L = st.number_input("Wall Thickness L (m)", min_value=0.0001, value=0.2, step=0.01)
    
    with col2:
        T1 = st.number_input("Inner Temperature T1 (°C or K)", value=100.0)
        T2 = st.number_input("Outer Temperature T2 (°C or K)", value=25.0)

    if st.button("Calculate Heat Transfer Rate"):
        Q = (k * A * (T1 - T2)) / L
        st.success(f"**Heat Transfer Rate ($Q$):** {Q:.4f} W (Watts)")

# --- 2. CYLINDRICAL WALL ---
elif geometry == "Cylindrical Wall":
    st.markdown("Formula: **$Q = \\frac{2 \\cdot \\pi \\cdot k \\cdot L \\cdot (T_1 - T_2)}{\\ln(r_2 / r_1)}$**")
    
    col1, col2 = st.columns(2)
    with col1:
        k = st.number_input("Thermal Conductivity k (W/m·K)", min_value=0.0001, value=0.8, step=0.1)
        L = st.number_input("Length of Cylinder L (m)", min_value=0.0001, value=5.0, step=0.5)
        r1 = st.number_input("Inner Radius r1 (m)", min_value=0.0001, value=0.05, step=0.01)
        r2 = st.number_input("Outer Radius r2 (m)", min_value=0.0001, value=0.1, step=0.01)
    
    with col2:
        T1 = st.number_input("Inner Temperature T1 (°C or K)", value=150.0)
        T2 = st.number_input("Outer Temperature T2 (°C or K)", value=30.0)

    if st.button("Calculate Heat Transfer Rate"):
        if r2 <= r1:
            st.error("Outer radius ($r_2$) must be greater than inner radius ($r_1$).")
        else:
            Q = (2 * math.pi * k * L * (T1 - T2)) / math.log(r2 / r1)
            st.success(f"**Heat Transfer Rate ($Q$):** {Q:.4f} W (Watts)")

# --- 3. SPHERICAL WALL ---
elif geometry == "Spherical Wall":
    st.markdown("Formula: **$Q = \\frac{4 \\cdot \\pi \\cdot k \\cdot r_1 \\cdot r_2 \\cdot (T_1 - T_2)}{r_2 - r_1}$**")
    
    col1, col2 = st.columns(2)
    with col1:
        k = st.number_input("Thermal Conductivity k (W/m·K)", min_value=0.0001, value=0.8, step=0.1)
        r1 = st.number_input("Inner Radius r1 (m)", min_value=0.0001, value=0.1, step=0.01)
        r2 = st.number_input("Outer Radius r2 (m)", min_value=0.0001, value=0.2, step=0.01)
    
    with col2:
        T1 = st.number_input("Inner Temperature T1 (°C or K)", value=200.0)
        T2 = st.number_input("Outer Temperature T2 (°C or K)", value=20.0)

    if st.button("Calculate Heat Transfer Rate"):
        if r2 <= r1:
            st.error("Outer radius ($r_2$) must be greater than inner radius ($r_1$).")
        else:
            Q = (4 * math.pi * k * r1 * r2 * (T1 - T2)) / (r2 - r1)
            st.success(f"**Heat Transfer Rate ($Q$):** {Q:.4f} W (Watts)")