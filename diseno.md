#Bases de datos en DynamoDB

Tabla <strong>ads</strong>: almacena los anuncios publicados
- PK: `ad_id` (string): ID del anuncio (PARTITION KEY)
- `author` (string): persona que publica el anuncio
- "title" (string): título del anuncio
- "description" (string): descripción del anuncio
- "price" (float): precio del producto anunciado
- "pub_date" (int): fecha de publicación del anuncio
- "expiration" (int): timestamp con la fecha de expiración del anuncio

Tabla <strong>comments</strong>: almacena los comentarios de un anuncio
- "ad_id" (string): ID del anuncio (PARTITION KEY)
- "timestamp" (string): tiempo de publicación (SORT KEY)
- "author" (string): autor del comentario
- "description" (string): texto del comentario
- "pub_date" (int): fecha de publicación del comentario
- "expiration" (int): fecha de expiración del comentario

Tabla <strong>CHAT</strong>: almacena los mensajes de un chat
- "chat_id" (string): ID del anuncio (PARTITION KEY)
- "timestamp" (string): tiempo de publicación (SORT KEY)
