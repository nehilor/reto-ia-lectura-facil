# Especificación · Lectura Fácil

## 1. Problema y usuario

- **Problema:** las cartas y notificaciones oficiales (ayuntamiento, banco, administración) están escritas en lenguaje burocrático y muchas personas no entienden qué dicen ni qué tienen que hacer.
- **Usuario:** una persona mayor, o una persona que está aprendiendo el idioma, que recibe un documento oficial en papel y no tiene a nadie cerca que se lo explique.
- **Cómo lo resuelve hoy:** pide ayuda a un familiar, va a una oficina a preguntar, o simplemente lo deja sin entender y se arriesga a perder un plazo.
- **Qué parte resuelve la IA:** reescribir el texto en lectura fácil y extraer la acción y la fecha. Lo que queda fuera: realizar el trámite o dar asesoría legal.

## 2. Qué hace el producto

El usuario pega el texto de la carta y la app devuelve una versión en lectura fácil con cuatro bloques: un resumen en pocas palabras, una explicación sencilla, qué tiene que hacer y las fechas o plazos importantes.

## 3. Entradas y salidas

| Entrada | Proceso | Salida |
|---|---|---|
| Texto administrativo pegado por el usuario | Reescritura con Gemini siguiendo reglas de lectura fácil | Texto claro en cuatro secciones, descargable |

## 4. La pieza de IA

- **Qué usa:** la API de Gemini. La app prueba en orden `gemini-2.5-flash`, `gemini-3.8-flash` y `gemini-3.5-flash-lite`, y usa el primero disponible.
- **Por qué:** reescribir en lenguaje claro y resumir acciones y fechas es una tarea de lenguaje natural que un modelo generativo resuelve bien y sin reglas fijas.
- **Qué pasa si falla:** si se agota la cuota o hay un error de red, la app muestra un mensaje claro y pide reintentar en un minuto.

## 5. Flujo del usuario

1. Abre la app.
2. Pega la carta o pulsa "Cargar un ejemplo".
3. Pulsa "Convertir a lectura fácil".
4. Lee la versión fácil y, si quiere, la descarga.

## 6. Restricciones

- Coste cero: capa gratuita de la API de Gemini y despliegue gratuito.
- La clave de la API nunca va en el código: se guarda en los secretos de la plataforma.
- Sin datos personales reales: para probar se usan ejemplos inventados.
- Pensada para personas sin conocimientos técnicos.

## 7. Criterios de aceptación

| Criterio | Se cumple si |
|---|---|
| Entrada vacía | La app avisa y no llama al modelo |
| Texto válido | Devuelve las cuatro secciones en orden |
| Sin fechas en el texto | La sección de fechas dice "No se indica" |
| Fallo del modelo | Muestra un mensaje de error claro y no se rompe |
| Clave ausente | Muestra cómo añadir el secreto y se detiene |

## 8. Fuera de alcance (por ahora)

- Subir archivos PDF o imágenes.
- Realizar el trámite o rellenar formularios.
- Asesoría legal o fiscal.

## 9. Despliegue

- **Ruta:** A · Streamlit Community Cloud.
- **Dónde va la clave:** Settings → Secrets, con la línea `GEMINI_API_KEY = "..."`.
