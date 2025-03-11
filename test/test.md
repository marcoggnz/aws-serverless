# Pruebas de la aplicación

## Configuración y pruebas con Postman

Una vez se ha desplegado la aplicación en AWS, se recomienda realizar las pruebas individuales de los endpoints. Una vez que el despliegue haya finalizado, Serverless Framework proporciona una URL pública para cada función Lambda expuesta a través de API Gateway. Se deben guardar estas URLs, ya que son necesarias para probar los endpoints.

Postman es una herramienta muy útil para probar APIs, ya que permite enviar solicitudes HTTP (GET, POST, PUT, DELETE) al servidor y ver las respuestas.

### Prueba del endpoint ```create_ad```:
- Seleccionar POST como el método HTTP.
- Pegar la URL proporcionada por Serverless para la función create-ad.
- En la pestaña Body, selecciona raw y elige el tipo JSON.
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
- Seleccionar POST como el método HTTP.
- Pegar la URL proporcionada por Serverless para la función create-ad.
- En la pestaña Body, selecciona raw y elige el tipo JSON.
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

### Prueba del endpoint ```get_ad```:
- Seleccionar POST como el método HTTP.
- Pegar la URL proporcionada por Serverless para la función create-ad.
- En la pestaña Body, selecciona raw y elige el tipo JSON.
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

### Prueba del endpoint ```create_comment```:
- Seleccionar POST como el método HTTP.
- Pegar la URL proporcionada por Serverless para la función create-ad.
- En la pestaña Body, selecciona raw y elige el tipo JSON.
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

### Prueba del endpoint ```get_comments```:
- Seleccionar POST como el método HTTP.
- Pegar la URL proporcionada por Serverless para la función create-ad.
- En la pestaña Body, selecciona raw y elige el tipo JSON.
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

### Prueba del endpoint ```create_chat_message```:
- Seleccionar POST como el método HTTP.
- Pegar la URL proporcionada por Serverless para la función create-ad.
- En la pestaña Body, selecciona raw y elige el tipo JSON.
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

### Prueba del endpoint ```get_chats```:
- Seleccionar POST como el método HTTP.
- Pegar la URL proporcionada por Serverless para la función create-ad.
- En la pestaña Body, selecciona raw y elige el tipo JSON.
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

### Prueba del endpoint ```get_chat_messages```:
- Seleccionar POST como el método HTTP.
- Pegar la URL proporcionada por Serverless para la función create-ad.
- En la pestaña Body, selecciona raw y elige el tipo JSON.
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

## Prueba con cURL

## Verificación de Logs y Respuestas
Después de realizar las pruebas, se debe verificar los logs en CloudWatch para depurar cualquier error que pueda haber ocurrido. Se puede acceder a los logs de CloudWatch desde la consola de AWS en <strong>CloudWatch > Logs > log group de tu Lambda</strong>.

## Comprobación de Costos en AWS
Dado que uno de los objetivos de la aplicación es minimizar los costos operativos, se debe asegurar que los servicios utilizados (Lambda, DynamoDB, API Gateway, S3) no están incurriendo en costos innecesarios, especialmente cuando no se esté utilizando la aplicación.
