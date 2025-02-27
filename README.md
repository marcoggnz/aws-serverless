# Práctica Introducción a AWS

## Arquitectura General
<strong>Backend (Serverless)</strong>:
- <strong>API Gateway</strong>: gestión de peticiones HTTP y punto de entrada para todas las interacciones (listar anuncios, ver detalles, publicar anuncios, enviar comentarios, ...) de la aplicación web. Es un servicio totalmente gestionado que permite crear y publicar APIs sin necesidad de gestionar servidores.
- <strong>AWS Lambda</strong>: ejecución de la lógica de negocio. Cda endpoint (listar anuncio, publicar anuncio, ...) de la API tiene una función Lambda asociada que procesa la solicitud, interactúa con la base de datos y devuelve la respuesta al usuario.
- <strong>Amazon DynamoDB</strong>: alberga la base de datos NoSQL para almacenar la información de los anuncios, los cmentarios y la información de los usuarios. DynamoDB es una base de datos totalmente gestionada, escalable y de bajo coste, lo que la hace ideal para este tipo de aplicaciones.
- <strong>Amazon S3</strong>: almacena las imágenes asociadas a los anuncios, por ejemplo, fotos de productos. S3 es un servicio de almacenamiento deobjetos que puede escalar fácilmente y es muy económico para almecenar imágenes.
- <strong>Amazon Cognito</strong>: servicio para autenticación y control de accesos. Cognito se integra con el backend para permitir que los usuarios puedan registrarse, iniciar sesión y controlar el acceso a las funcionalidades de publicación de anuncios.
- <strong>Amazon CloudWatch</strong>: servicio utilizado para monitorización de las funciones Lambda, visualización de logs y seguimiento del rendimiento de la aplicación.

<strong>Frontend (Interfaz Web)</strong>:
- Amazon S3 (hosting estático): alojamiento del frontend estático, desarrollado en HTML. S3 tiene un bajo coste y es ideal para hosting de sitios estáticos.
- Amazon CloudFront: puede ser utilizado como red de distribución de contenido (CDN) para mejorar la entrega de contenido estático (imágenes, CSS, JS) a los usuarios.

## Flujo de Trabajo y Servicios Detallados
1) Creación del frontend (HTML)
Desarrollar una interfaz web en la que se puedan listar los anuncios, ver los detalles de un anuncio, permitir la publicación de anuncios, interactuar con los comentarios, y subir imágenes (si es necesario). Este frontend puede ser un sitio web estático con un formulario de contacto, listado de anuncios, y detalles de cada uno.

2) API Gateway y Lambda
Crear las siguientes rutas en API Gateway:
- GET /ads: Devuelve todos los anuncios desde DynamoDB.
- GET /ads/{id}: Devuelve el detalle de un anuncio específico.
- POST /ads: Permite crear un nuevo anuncio.
- POST /ads/{id}/comments: Permite agregar un comentario a un anuncio.
- Para cada ruta, se asigna una función Lambda que interactúa con la base de datos y procesa la información según corresponda.
Ejemplo de funciones Lambda:
- Lambda listar anuncios: Recoge todos los anuncios desde DynamoDB y los devuelve al frontend.
- Lambda publicar anuncio: Recibe el cuerpo del anuncio (título, descripción, precio, etc.), lo valida y lo guarda en DynamoDB.
- Lambda agregar comentario: Agrega un comentario al anuncio correspondiente en DynamoDB.

3) Base de Datos DynamoDB
Se puede crear una tabla llamada Anuncios en DynamoDB. Cada anuncio tendrá un ID único y los comentarios estarán relacionados con el ID de cada anuncio.
Estructura de la tabla DynamoDB:
- Partición de claves: ad_id para identificar un anuncio.
- Atributos: title, description, price, created_at, comments (array de comentarios), etc.
- Utilizamos DynamoDB Streams para que los nuevos anuncios sean indexados de manera eficiente.

4) Almacenamiento de Imágenes en S3
Cuando un usuario publica un anuncio con una imagen, la imagen se sube a un bucket S3 asociado. El enlace de la imagen se guarda junto con el anuncio en DynamoDB.
Se puede usar una política en S3 para controlar los permisos de acceso, de manera que solo se permita la lectura pública de las imágenes.

5) Autenticación con Cognito
Usamos Amazon Cognito para la gestión de usuarios, permitiendo que se registren, inicien sesión y publiquen anuncios. Cognito se puede configurar para proporcionar tokens de autenticación que se usarán en las peticiones al backend (API Gateway).

7) Implementación de la Caducidad de Anuncios
La caducidad de los anuncios se puede manejar de las siguientes maneras:
- TTL (Time To Live) en DynamoDB: Usar la característica TTL de DynamoDB para eliminar automáticamente los anuncios después de un período determinado (por ejemplo, 30 días).
- Lambda Scheduled: Usar AWS Lambda con CloudWatch Events para eliminar los anuncios caducados.

## Automatización y Minimización de Costes
7) Minimización de Costes
- Uso de funciones Lambda para procesar las solicitudes en lugar de instancias EC2. Lambda solo se ejecuta cuando se necesita, lo que elimina los costos de infraestructura cuando no hay tráfico.
- DynamoDB permite escalar automáticamente según el tráfico, y el modelo de precios basado en operaciones es económico cuando no hay muchas solicitudes.
- S3 solo cobra por el almacenamiento real utilizado y las solicitudes realizadas, lo que resulta en costos muy bajos.

## Diagrama de Arquitectura
El diagrama de arquitectura podría tener los siguientes componentes:
- Frontend: Almacenado en S3.
- API Gateway: Gestiona las solicitudes HTTP.
- Lambda: Procesa las solicitudes y maneja la lógica del backend.
- DynamoDB: Almacena los anuncios y los comentarios.
- S3: Almacena las imágenes.
- Cognito: Maneja la autenticación de usuarios.
- CloudWatch: Monitorea la actividad y los logs.

![Architecture diagram][https://github.com/srinivas-polina/Spotify-end-to-end-dataengineering-projects/blob/main/architecture%20diagram.png](https://github.com/marcoggnz/datahack/blob/main/AWSarchitectura-redes.jpg)

## Despliegue de la Solución
Para facilitar el despliegue, puedes usar AWS SAM (Serverless Application Model) o CloudFormation para crear la infraestructura automáticamente desde el código fuente del repositorio.

## Pruebas y Validación
Antes de entregar la solución, asegúrate de incluir pruebas unitarias para las funciones Lambda y pruebas de integración para los endpoints del API Gateway.

## Documentación
La documentación debe incluir:

- Diagrama de arquitectura detallado con explicación de cada servicio.
- Manual de despliegue paso a paso para configurar el sistema desde cero.
- Justificación de las decisiones tecnológicas tomadas.
- Instrucciones para pruebas e integración.
