import streamlit as st
from google import genai
from google.genai import types

MODELS = ("gemini-2.5-flash", "gemini-3.8-flash", "gemini-3.5-flash-lite")

TITLE = "📄 Lectura Fácil"
DESCRIPTION = "Convierte cartas y textos oficiales en un lenguaje claro para cualquier persona."

SYSTEM_PROMPT = (
    "Eres un asistente que transforma textos administrativos, legales o burocráticos "
    "en lectura fácil para personas sin conocimientos técnicos ni jurídicos, como "
    "personas mayores o personas que están aprendiendo el idioma.\n"
    "Reglas de lectura fácil:\n"
    "- Usa frases cortas, de una sola idea cada una.\n"
    "- Usa palabras comunes del día a día.\n"
    "- Explica cada palabra difícil con palabras sencillas entre paréntesis.\n"
    "- Usa voz activa y trato de usted, cercano y respetuoso.\n"
    "- No inventes datos, nombres, cantidades ni fechas que no estén en el texto.\n"
    "Devuelve la respuesta en markdown, solo con estas cuatro secciones y en este orden:\n"
    "## En pocas palabras\n"
    "## Explicación fácil\n"
    "## Qué tiene que hacer\n"
    "## Fechas y plazos\n"
    "Si el texto no indica acciones o fechas, escribe 'No se indica' en esa sección. "
    "No añadas nada fuera de estas cuatro secciones."
)

SAMPLE_TEXT = (
    "AYUNTAMIENTO DE VILLANUEVA DEL EJEMPLO. Área de Gestión Tributaria. "
    "Asunto: Notificación de liquidación de la tasa municipal de recogida de residuos "
    "sólidos urbanos, ejercicio 2026. Estimado contribuyente, se pone en su conocimiento "
    "que, de conformidad con la ordenanza fiscal vigente, se ha practicado liquidación "
    "por importe de 86,40 euros correspondiente al inmueble sito en Calle Inventada 14. "
    "El período voluntario de pago finalizará el 30 de noviembre de 2026. Transcurrido "
    "dicho plazo sin que conste el abono, se iniciará el procedimiento de apremio con el "
    "recargo correspondiente. Podrá hacer efectivo el pago en cualquier oficina bancaria "
    "colaboradora presentando este documento."
)


def get_api_key():
    try:
        return st.secrets["GEMINI_API_KEY"]
    except Exception:
        return None


@st.cache_resource
def get_client(api_key):
    return genai.Client(api_key=api_key)


def simplify(client, text):
    config = types.GenerateContentConfig(
        system_instruction=SYSTEM_PROMPT,
        temperature=0.3,
    )
    last_error = None
    for model in MODELS:
        try:
            response = client.models.generate_content(
                model=model,
                contents=text,
                config=config,
            )
            if response.text:
                return response.text, None
        except Exception as error:
            last_error = error
    return None, last_error


st.set_page_config(page_title="Lectura Fácil", page_icon="📄")
st.title(TITLE)
st.caption(DESCRIPTION)

api_key = get_api_key()
if not api_key:
    st.error("Falta el secreto GEMINI_API_KEY. Añádelo en Settings → Secrets de la app.")
    st.stop()

client = get_client(api_key)

if "result" not in st.session_state:
    st.session_state.result = None
if "text" not in st.session_state:
    st.session_state.text = ""

if st.button("Cargar un ejemplo"):
    st.session_state.text = SAMPLE_TEXT
    st.session_state.result = None

text = st.text_area(
    "Pega aquí la carta o el texto oficial",
    value=st.session_state.text,
    height=220,
    placeholder="Por ejemplo, una carta del ayuntamiento, del banco o de la administración.",
)

if st.button("Convertir a lectura fácil", type="primary"):
    if not text.strip():
        st.warning("Escribe o pega primero un texto.")
    else:
        st.session_state.text = text
        with st.spinner("Simplificando el texto..."):
            result, error = simplify(client, text)
        if result:
            st.session_state.result = result
        else:
            st.session_state.result = None
            st.error(
                "Ahora mismo no puedo responder (" + str(error) + "). "
                "Espera un minuto y prueba otra vez."
            )

if st.session_state.result:
    st.divider()
    st.markdown(st.session_state.result)
    st.download_button(
        "Descargar versión fácil",
        data=st.session_state.result,
        file_name="lectura-facil.md",
    )
