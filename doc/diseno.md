# Diseño de la aplicación

![Architecture diagram](https://github.com/marcoggnz/aws-serverless/blob/main/images/aws-serverless-arch.jpg)

## Servicios utilizados
<strong>Backend (Serverless)</strong>:
- <strong>API Gateway</strong>: gestión de peticiones HTTP y punto de entrada para todas las interacciones (listar anuncios, ver detalles, publicar anuncios, enviar comentarios, ...) de la aplicación web. Es un servicio totalmente gestionado que permite crear y publicar APIs sin necesidad de gestionar servidores.
- <strong>AWS Lambda</strong>: ejecución de la lógica de negocio. Cada endpoint (listar anuncio, publicar anuncio, ...) de la API tiene una función Lambda asociada que procesa la solicitud, interactúa con la base de datos y devuelve la respuesta al usuario.
- <strong>Amazon DynamoDB</strong>: alberga la base de datos NoSQL para almacenar la información de los anuncios, los comentarios y la información de los usuarios. DynamoDB es una base de datos totalmente gestionada, escalable y de bajo coste, lo que la hace ideal para este tipo de aplicaciones.
- <strong>Amazon S3</strong>: almacena las imágenes asociadas a los anuncios, por ejemplo, fotos de productos. S3 es un servicio de almacenamiento de objetos que puede escalar fácilmente y es muy económico para almacenar imágenes.
- <strong>Amazon CloudWatch</strong>: servicio utilizado para monitorización de las funciones Lambda, visualización de logs y seguimiento del rendimiento de la aplicación.

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

## Almacenamiento de Imágenes en S3
Cuando un usuario publica un anuncio con una imagen, la imagen se sube a un bucket S3 asociado. El enlace de la imagen se guarda junto con el anuncio en DynamoDB.
Se puede usar una política en S3 para controlar los permisos de acceso, de manera que solo se permita la lectura pública de las imágenes.

## Automatización y Minimización de Costes
Con el uso de serviicos serverless se garantiza la minimización de costos:
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

Tabla <strong>chats</strong>: almacena los mensajes de un chat
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
Los siguientes servicios son útiles para mejorar la entrega de contenido web, la gestión de tráfico y el acceso a tu aplicación desde cualquier lugar:

<strong>Amazon CloudFront</strong>: CloudFront es un Content Delivery Network (CDN) que mejora la entrega de contenido estático y dinámico, como imágenes, JavaScript, CSS, y HTML.
Implementación:
CloudFront se utilizaría para distribuir el sitio web estático de S3 de manera eficiente, reduciendo la latencia y mejorando la velocidad de carga para los usuarios.
CloudFront ofrece características avanzadas como la configuración de caché, la integración con certificados SSL para HTTPS, y la protección DDoS a través de AWS Shield.

<strong>Amazon Route 53</strong>: es el servicio de DNS de AWS, que  permite gestionar el enrutamiento de tráfico en Internet hacia la aplicación.
Implementación:
Si se necesita asociar el dominio personalizado (por ejemplo, www.tuweb.com) a la aplicación, se usaría Route 53 para configurar los registros DNS.
Además, se puede utilizar Route 53 para crear políticas de enrutamiento basadas en geolocalización o en la latencia de la red, lo que  permite dirigir a los usuarios a la instancia más cercana de tu aplicación.

### Caducidad automática de anuncios
Para asegurar que los anuncios caduquen automáticamente después de un tiempo determinado, puedes implementar una combinación de servicios para gestionar el ciclo de vida de los datos:

<strong>Amazon DynamoDB (TTL - Time to Live)</strong>: DynamoDB tiene una función llamada Time to Live (TTL) que permite definir una fecha y hora para que los elementos en una tabla caduquen automáticamente.
Se puede configurar el atributo expirationDate en la tabla ads y habilitar TTL en DynamoDB para que, una vez alcanzada la fecha de expiración, los anuncios se eliminen automáticamente de la base de datos, ayudando a mantener la eficiencia y reduciendo los costos operativos.

<strong>AWS Lambda + CloudWatch Events</strong>: para eliminar anuncios caducados, se podría configurar una función Lambda que se ejecute periódicamente (por ejemplo, una vez al día) utilizando CloudWatch Events.
Esta función Lambda podría escanear la tabla de anuncios, verificar las fechas de caducidad, y eliminar los anuncios que ya han caducado.

### Búsqueda de anuncios
Para mejorar la búsqueda de anuncios en tu aplicación, especialmente si necesitas realizar búsquedas más complejas o con requisitos de alto rendimiento, estos servicios serían útiles:

Amazon OpenSearch Service: OpenSearch es un motor de búsqueda y análisis en tiempo real basado en Elasticsearch, ideal para implementar características avanzadas de búsqueda en tu aplicación.
- Implementación: se podría indexar todos los anuncios en un clúster de OpenSearch, permitiendo a los usuarios realizar búsquedas de anuncios de forma rápida y eficiente.
OpenSearch soporta búsqueda por texto completo, filtrado de resultados, búsquedas facetas, y mucho más, lo que permitiría una búsqueda avanzada, como buscar por palabra clave, precio, ubicación, etc.

AWS Lambda (con OpenSearch): AWS Lambda se integraría con OpenSearch para realizar consultas dinámicas o para almacenar los resultados de la búsqueda de anuncios.
- Implementación: Se crearían funciones Lambda que reciban las solicitudes de búsqueda desde el frontend y consulten OpenSearch para obtener los anuncios que coincidan con los criterios de búsqueda, devolviendo los resultados a los usuarios.

### Control de acceso mediante usuarios
El control de acceso y la gestión de identidades son fundamentales para asegurar que solo los usuarios autorizados puedan acceder a ciertas funcionalidades, como publicar anuncios o enviar mensajes en los chats.

<strong>Amazon Cognito</strong>: Cognito es un servicio gestionado de autenticación y autorización de usuarios. Permite gestionar el inicio de sesión, el registro, la verificación de direcciones de correo electrónico, y la gestión de contraseñas de forma segura.
- Implementación: se utilizaría Cognito para permitir que los usuarios se registren, inicien sesión y accedan a funcionalidades restringidas de la aplicación, como publicar anuncios, enviar mensajes en los chats, o acceder a información privada. Cognito se integra con AWS API Gateway para proteger los endpoints de la API, asegurando que solo los usuarios autenticados puedan realizar ciertas operaciones. Se puede usar Cognito User Pools para gestionar la autenticación de usuarios y Cognito Identity Pools para obtener credenciales temporales para interactuar con otros servicios de AWS, como S3 o DynamoDB.

<strong>AWS IAM (Identity and Access Management)</strong>: IAM  permite crear y gestionar políticas de acceso para usuarios y recursos de AWS.
- Implementación: se usaría IAM para definir roles y permisos para las funciones Lambda que gestionan los anuncios, comentarios y chats, asegurándose de que cada función Lambda tenga acceso solo a los recursos necesarios (por ejemplo, solo la tabla de ads para la función que maneja anuncios).
IAM también se utilizaría para gestionar los permisos en DynamoDB y en el bucket de S3 donde se almacenan las imágenes de los anuncios.

<strong>API Gateway con Autorización Cognito</strong>: API Gateway permite exponer las funciones Lambda a través de HTTP, y se puede integrar con Cognito para garantizar que solo los usuarios autenticados puedan acceder a ciertos endpoints.
- Implementación: se configuraría API Gateway para que ciertos endpoints (como la creación de anuncios o el envío de mensajes) estén protegidos por autenticación Cognito. Esto garantizará que solo los usuarios autenticados puedan interactuar con estos servicios.
