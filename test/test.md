# Pruebas de la aplicación

## Configuración y pruebas con Postman

Una vez se ha desplegado la aplicación en AWS, se recomienda realizar las pruebas individuales de los endpoints. Una vez que el despliegue haya finalizado, Serverless Framework proporciona una URL pública para cada función Lambda expuesta a través de API Gateway. Se deben guardar estas URLs, ya que son necesarias para probar los endpoints.

Postman es una herramienta muy útil para probar APIs, ya que permite enviar solicitudes HTTP (GET, POST, PUT, DELETE) al servidor y ver las respuestas.

### Prueba del endpoint ```create_ad```:
- Seleccionar POST como el método HTTP.
- Pegar la URL proporcionada por Serverless para la función create-ad.
- En la pestaña Body, seleccionar raw y elegir el tipo JSON.
- Ejemplo JSON:
```bash
{
  "title": "Nuevo Anuncio",
  "description": "Anuncio de prueba",
  "price": 50,
  "image_url": "https://example.com/image.jpg"
}
```
- Una vez enviado el archivo JSON, se debe recibir un ID del anuncio.

### Prueba del endpoint ```list_ads```:
- Seleccionar GET como el método HTTP.
- Pegar la URL proporcionada por Serverless para la función list-ads.
- Hacer clic en Send y asegurarse de que se obtiene una lista de anuncios en formato JSON.

### Prueba del endpoint ```get_ad```:
- Seleccionar GET como el método HTTP.
- Pegar la URL proporcionada por Serverless para la función get-ad y añadir el parámetro ad_id en la URL.
- Hacer clic en Send y verificar que se obtienen los detalles del anuncio solicitado.

### Prueba del endpoint ```create_comment```:
- Seleccionar POST como el método HTTP.
- Pegar la URL proporcionada por Serverless para la función create-comment.
- En la pestaña Body, seleccionar raw y elegir el tipo JSON.
- Ejemplo JSON:
```bash
{
  "ad_id": "12345",
  "comment_id": "67890",
  "user": "usuario1",
  "comment": "Este es un comentario."
}
```
- Una vez enviado el archivo JSON, se debe asegurar que el comentario se ha escrito correctamente.

### Prueba del endpoint ```get_comments```:
- Seleccionar GET como el método HTTP.
- Pegar la URL proporcionada por Serverless para la función get-comments y añadir el parámetro ad_id en la URL.
- Hacer clic en Send y verificar que se obtiene la lista de comentarios para ese anuncio.

### Prueba del endpoint ```create_chat_message```:
- Seleccionar POST como el método HTTP.
- Pegar la URL proporcionada por Serverless para la función create-ad.
- En la pestaña Body, selecciona raw y eligir el tipo JSON.
```bash
{
  "ad_id": "12345",
  "chat_id": "abcde",
  "message": "Hola, estoy interesado en este anuncio."
}
```
- Hacer clic en Send y asegurarse de que el mensaje se ha enviado correctamente.

### Prueba del endpoint ```get_chats```:
- Seleccionar GET como el método HTTP.
- Pegar la URL proporcionada por Serverless para la función create-ad.
- Hacer clic en Send y asegurarse de que se obtiene una lista de chats para el anuncio.

### Prueba del endpoint ```get_chat_messages```:
- Seleccionar POST como el método HTTP.
- Pegar la URL proporcionada por Serverless para la función create-ad y añadir los parámetros ad_id y chat_id.
- Hacer clic en Send y asegurarse de que se obtienen los mensajes del chat.

## Prueba con cURL
También se pueden probar los endpoints mediante la línea de comandos. Por ejemplo, para probar el endpoint ```create_ad``` se puede utilizar el comando:
```
curl -X POST https://xxxxxx.execute-api.eu-west-1.amazonaws.com/dev/insert-product \
-H "Content-Type: application/json" \
-d '{"title": "Nuevo Anuncio", "description": "Anuncio de prueba", "price": 50, "image_url": "/path/to/image.jpg"}'
```
## Verificación de Logs y Respuestas
Después de realizar las pruebas, se debe verificar los logs en CloudWatch para depurar cualquier error que pueda haber ocurrido. Se puede acceder a los logs de CloudWatch desde la consola de AWS en <strong>CloudWatch > Logs > log group de tu Lambda</strong>.

## Comprobación de Costos en AWS
Dado que uno de los objetivos de la aplicación es minimizar los costos operativos, se debe asegurar que los servicios utilizados (Lambda, DynamoDB, API Gateway, S3) no están incurriendo en costos innecesarios, especialmente cuando no se esté utilizando la aplicación.
