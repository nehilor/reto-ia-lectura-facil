# Lectura Fácil

**Enlace a la app:** https://reto-ia-lectura-facil-lytixxzofy7zoxqckblkau.streamlit.app/
**Autor/a:** [tu nombre]

- **Qué usa:** API de Gemini (`gemini-2.5-flash`), Streamlit, `google-genai`.
- **Ruta de despliegue:** A · Streamlit Community Cloud.

## Pitch

Muchas personas mayores y personas que aprenden el idioma reciben cartas oficiales que no entienden y se arriesgan a perder plazos. Lectura Fácil reescribe esas cartas en lenguaje claro y dice en pocas líneas qué hay que hacer y para cuándo. La IA aporta lo que una plantilla fija no puede: entiende cualquier carta y la explica con palabras sencillas. En las pruebas, la sección "Qué tiene que hacer" fue la más útil, así que la dejé siempre visible. Lo siguiente sería aceptar fotos de la carta para no tener que teclearla.

## El problema

Las notificaciones de la administración, los bancos y los ayuntamientos están escritas en un lenguaje técnico y lleno de términos difíciles. Una persona mayor, o alguien que está aprendiendo el idioma, muchas veces no entiende qué le piden ni qué plazo tiene. Hoy lo resuelve pidiendo ayuda a un familiar o yendo a preguntar a una oficina, y a veces simplemente lo deja pasar. Merece la pena resolverlo porque entender un plazo a tiempo evita recargos y problemas.

## Qué hace la app

1. El usuario pega el texto de la carta o carga un ejemplo.
2. Pulsa un botón.
3. Recibe una versión fácil con cuatro bloques: en pocas palabras, explicación fácil, qué tiene que hacer y fechas y plazos.
4. Puede descargar el resultado.

## La pieza de IA

Usa la API de Gemini. La app prueba varios modelos en orden (`gemini-2.5-flash` y los modelos del curso `gemini-3.8-flash` y `gemini-3.5-flash-lite`) y usa el primero disponible, así que sigue funcionando si uno se retira o se agota su cuota. Las reglas de lectura fácil van en el system prompt. Si todos fallan, la app muestra un mensaje claro y no se rompe.

## Cómo la he construido

Partí de la plantilla de la Ruta A de la asignatura y la adapté de un chat a una herramienta de un solo paso. Trabajé con un asistente de IA: le pasé el `AGENTS.md`, le pedí la lógica de lectura fácil en el system prompt y revisé a mano el manejo de errores y los secretos.

## Prueba y mejora

[Rellena después de la prueba entre compañeros: quién la probó, qué pasó y qué cambiaste.]

## Ejecutar en local (opcional)

```
# Pon la clave en .streamlit/secrets.toml y ejecuta
streamlit run app.py
```

## Capturas

[La app funcionando, la app ante un caso límite, un momento de tu trabajo con la IA y la prueba.]
