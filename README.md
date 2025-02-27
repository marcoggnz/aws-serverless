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

2) API Gateway y Lambda

3) Base de Datos DynamoDB

4) Almacenamiento de Imágenes en S3

5) Autenticación con Cognito

6) Implementación de la Caducidad de Anuncios

## Automatización y Minimización de Costes
7) Minimización de Costes
