import streamlit as st
import sympy as sp

# Título de la app
st.title("🧮 Calculadora de Integrales Dobles - Paso a Paso")

# Definir variables simbólicas
x, y = sp.symbols('x y')

# Entrada de la función a integrar
func_input = st.text_input("Ingrese la función f(x, y):", "x*y")

# Seleccionar el orden de integración
order = st.radio("Seleccione el orden de integración:", ["dxdy", "dydx"])

# Ingresar los límites
if order == "dxdy":
    x_limits = st.text_input("Límites para x (ej. 0, 2):", "0, 2")
    y_limits = st.text_input("Límites para y (ej. 1, 3):", "1, 3")
else:
    y_limits = st.text_input("Límites para y (ej. 0, 2):", "0, 2")
    x_limits = st.text_input("Límites para x (ej. 1, 3):", "1, 3")

# Botón para calcular
if st.button("Calcular Integral Doble"):

    try:
        # Procesar función y límites
        fxy = sp.sympify(func_input)
        a, b = map(sp.sympify, x_limits.split(","))
        c, d = map(sp.sympify, y_limits.split(","))

        # Mostrar función original
        st.markdown("### Paso 1: Función a integrar")
        st.latex(f"f(x, y) = {sp.latex(fxy)}")

        if order == "dxdy":
            st.markdown("### Paso 2: Orden de integración dxdy")
            st.latex(r"\int_{{y={}}}^{{{}}} \left( \int_{{x={}}}^{{{}}} {} \, dx \right) dy"
                     .format(c, d, a, b, sp.latex(fxy)))
            
            # Primera integración respecto a x
            inner_integral = sp.integrate(fxy, (x, a, b))
            st.markdown("### Paso 3: Resolver la integral interna (respecto a x)")
            st.latex(r"\int_{{x={}}}^{{{}}} {} \, dx = {}"
                     .format(a, b, sp.latex(fxy), sp.latex(inner_integral)))
            
            # Segunda integración respecto a y
            result = sp.integrate(inner_integral, (y, c, d))
            st.markdown("### Paso 4: Resolver la integral externa (respecto a y)")
            st.latex(r"\int_{{y={}}}^{{{}}} {} \, dy = {}"
                     .format(c, d, sp.latex(inner_integral), sp.latex(result)))

        else:  # dydx
            st.markdown("### Paso 2: Orden de integración dydx")
            st.latex(r"\int_{{x={}}}^{{{}}} \left( \int_{{y={}}}^{{{}}} {} \, dy \right) dx"
                     .format(a, b, c, d, sp.latex(fxy)))
            
            # Primera integración respecto a y
            inner_integral = sp.integrate(fxy, (y, c, d))
            st.markdown("### Paso 3: Resolver la integral interna (respecto a y)")
            st.latex(r"\int_{{y={}}}^{{{}}} {} \, dy = {}"
                     .format(c, d, sp.latex(fxy), sp.latex(inner_integral)))
            
            # Segunda integración respecto a x
            result = sp.integrate(inner_integral, (x, a, b))
            st.markdown("### Paso 4: Resolver la integral externa (respecto a x)")
            st.latex(r"\int_{{x={}}}^{{{}}} {} \, dx = {}"
                     .format(a, b, sp.latex(inner_integral), sp.latex(result)))

        st.success(f"✅ Resultado final de la integral doble: {sp.latex(result)}")

    except Exception as e:
        st.error(f"❌ Error en la entrada: {e}")
