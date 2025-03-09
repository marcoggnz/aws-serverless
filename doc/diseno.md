# Diseño de la aplicación

![Architecture diagram]([images/AWSarchitectura-redes.jpg](https://github.com/marcoggnz/aws-serverless/blob/main/images/AWSarchitectura-redes.jpg))

## Servicios utilizados
<strong>Backend (Serverless)</strong>:
- <strong>API Gateway</strong>: gestión de peticiones HTTP y punto de entrada para todas las interacciones (listar anuncios, ver detalles, publicar anuncios, enviar comentarios, ...) de la aplicación web. Es un servicio totalmente gestionado que permite crear y publicar APIs sin necesidad de gestionar servidores.
- <strong>AWS Lambda</strong>: ejecución de la lógica de negocio. Cada endpoint (listar anuncio, publicar anuncio, ...) de la API tiene una función Lambda asociada que procesa la solicitud, interactúa con la base de datos y devuelve la respuesta al usuario.
- <strong>Amazon DynamoDB</strong>: alberga la base de datos NoSQL para almacenar la información de los anuncios, los comentarios y la información de los usuarios. DynamoDB es una base de datos totalmente gestionada, escalable y de bajo coste, lo que la hace ideal para este tipo de aplicaciones.
- <strong>Amazon S3</strong>: almacena las imágenes asociadas a los anuncios, por ejemplo, fotos de productos. S3 es un servicio de almacenamiento de objetos que puede escalar fácilmente y es muy económico para almacenar imágenes.
- <strong>Amazon CloudWatch</strong>: servicio utilizado para monitorización de las funciones Lambda, visualización de logs y seguimiento del rendimiento de la aplicación.

## Servicios adicionales que no han sido implementados
Aunque por falta de tiempo los siguientes servicios no han sido implementados en el despliegue de la aplicación, a continuación se detalla la función que tendrían:
- <strong>Amazon S3</strong> (hosting estático): alojamiento del frontend estático, desarrollado en HTML. S3 tiene un bajo coste y es ideal para hosting de sitios estáticos.
- <strong>Amazon CloudFront</strong>: puede ser utilizado como red de distribución de contenido (CDN) para mejorar la entrega de contenido estático (imágenes, CSS, JS) a los usuarios.
- <strong>Amazon Cognito</strong>: gestión de usuarios, permitiendo que se registren, inicien sesión y publiquen anuncios. Cognito se puede configurar para proporcionar tokens de autenticación que se usarán en las peticiones al backend (API Gateway).

## API Gateway y funciones Lambda
Para el funcionamiento del backend se ha implementado una REST API, que mediante enpoints y el servicio API Gateway, se realizan las diferentes acciones de la aplicación. Se trata de una arquitectura estándar dentro de AWS cuando se trata de aplicaciones serverless.
`POST /ads`: creación de un anuncio

`GET /ads`: mostrado de todos los anuncios

`GET /ads/{ad_id}`: mostrado de un anuncio determinado

`POST /ads/{ad_id}/comments`: publicación de un comentario en un anuncio determinado

`POST /chats`: envío de un mensaje al chat

`GET /chats`: mostrado de los chats

`GET /chats/{chat_id}`: mostrado de todos los mensajes de un chat

Para cada ruta, se asigna una función Lambda que interactúa con la base de datos y procesa la información según corresponda.
Ejemplo de funciones Lambda:
- Lambda listar anuncios: recoge todos los anuncios desde DynamoDB y los devuelve al frontend.
- Lambda publicar anuncio: recibe el cuerpo del anuncio (título, descripción, precio, etc.), lo valida y lo guarda en DynamoDB.
- Lambda agregar comentario: agrega un comentario al anuncio correspondiente en DynamoDB.

3) Base de Datos DynamoDB
Se puede crear una tabla llamada "ads" en DynamoDB. Cada anuncio tendrá un ID único (ad_id) y los comentarios estarán relacionados con el ID de cada anuncio.
Estructura de la tabla DynamoDB:
- Partición de claves: ad_id para identificar un anuncio.
- Atributos: title, description, price, created_at, comments (array de comentarios), etc.
- Utilizamos DynamoDB Streams para que los nuevos anuncios sean indexados de manera eficiente.

4) Almacenamiento de Imágenes en S3
Cuando un usuario publica un anuncio con una imagen, la imagen se sube a un bucket S3 asociado. El enlace de la imagen se guarda junto con el anuncio en DynamoDB.
Se puede usar una política en S3 para controlar los permisos de acceso, de manera que solo se permita la lectura pública de las imágenes.

7) Implementación de la Caducidad de Anuncios
La caducidad de los anuncios se puede manejar de las siguientes maneras:
- TTL (Time To Live) en DynamoDB: Usar la característica TTL de DynamoDB para eliminar automáticamente los anuncios después de un período determinado (por ejemplo, 30 días).
- Lambda Scheduled: Usar AWS Lambda con CloudWatch Events para eliminar los anuncios caducados.

## Automatización y Minimización de Costes
7) Minimización de Costes
- Uso de funciones Lambda para procesar las solicitudes en lugar de instancias EC2. Lambda solo se ejecuta cuando se necesita, lo que elimina los costos de infraestructura cuando no hay tráfico.
- DynamoDB permite escalar automáticamente según el tráfico, y el modelo de precios basado en operaciones es económico cuando no hay muchas solicitudes.
- S3 solo cobra por el almacenamiento real utilizado y las solicitudes realizadas, lo que resulta en costos muy bajos.

## Bases de datos en DynamoDB

Tabla <strong>ads</strong>: almacena los anuncios publicados
- PK: `ad_id` (string): ID del anuncio (PARTITION KEY)
- `title` (string): título del anuncio
- `description` (string): descripción del anuncio
- `price` (float): precio del producto anunciado
- `user_id` (string): ID del usuario que publicó el anuncio
- `createt_at` (): fecha y hora de creación del anuncio
- `expirity_date` (): fecha de caducidad del anuncio
- `image_url` (): URL de la imagen del anuncio

Ejemplo de un item en la tabla:
```json
{
  "ad_id": "12345",
  "title": "Bicicleta de montaña",
  "description": "Bicicleta de montaña usada, en buen estado",
  "price": 150,
  "user_id": "user123",
  "created_at": "2025-02-27T10:00:00Z",
  "expiry_date": "2025-03-27T10:00:00Z",
  "image_url": "https://example.com/image.jpg"
}
```

Tabla <strong>comments</strong>: almacena los comentarios de un anuncio
- `ad_id` (string): ID del anuncio (PK)
- `comment_id` (string): ID del comentario (SK)
- `user_id` (string): ID del usuario que publicó el comentario
- `comment_text` (string): texto del comentario
- `created_at` (int): fecha de publicación del comentario

Ejemplo de un item en la tabla:
```json
{
  "ad_id": "12345",
  "comment_id": "cmt001",
  "user_id": "user456",
  "comment_text": "Me interesa mucho, ¿es negociable el precio?",
  "created_at": "2025-02-27T12:00:00Z"
}
```

Tabla <strong>CHAT</strong>: almacena los mensajes de un chat
- `ad_id` (string): ID del anuncio al que pertenece el chat (PK)
- `chat_id` (string): ID del chat (SK)
- `message` (string): texto del mensaje
- `timestamp` (): fecha y hora a la que el mensaje fue enviado

```json
{
  "ad_id": "12345",
  "chat_id": "chat001",
  "user_id_1": "user123",
  "user_id_2": "user456",
  "message": "Hola, ¿el precio es negociable?",
  "timestamp": "2025-02-27T14:00:00Z"
}
```
## Implementaciones de diseño adicionales
Por falta de tiempo, hay ciertas funcionalidades que no han sido implementadas. Se detallan a continuación algunas de ellas:
### Web

### Caducidad automática de anuncios

### Búsqueda de anuncios

### Control de acces mediante usuarios
