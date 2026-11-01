# AGENTS.md · Lectura Fácil

## Qué es este proyecto

Una app de Streamlit que convierte textos administrativos en lectura fácil. Pensada para personas sin perfil técnico que reciben cartas oficiales y no las entienden.

## Cómo está hecho

- Python 3.12.
- Streamlit para la interfaz.
- `google-genai` para llamar a la API de Gemini.
- Un único archivo `app.py`.

## Reglas

- La clave de la API nunca se escribe en el código. Se lee de `st.secrets["GEMINI_API_KEY"]`.
- El código va en inglés y sin comentarios.
- Los textos que ve el usuario van en español.
- Toda la lógica de lectura fácil vive en `SYSTEM_PROMPT`.

## Cómo comprobar que funciona

1. Copia `.streamlit/secrets.toml.example` a `.streamlit/secrets.toml` y pon una clave válida.
2. Ejecuta `streamlit run app.py`.
3. Pulsa "Cargar un ejemplo" y luego "Convertir a lectura fácil".
4. Comprueba que salen las cuatro secciones.

## Qué no hacer

- No subir `.streamlit/secrets.toml` a GitHub.
- No añadir comentarios al código.
- No guardar datos personales reales en el repositorio.
