# Diseño de la aplicación

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

## Rest API

`POST /ads`: creación de un anuncio

`GET /ads`: mostrado de todos los anuncios

`GET /ads/{ad_id}`: mostrado de un anuncio determinado

`POST /ads/{ad_id}/comments`: publicación de un comentario en un anuncio determinado

`POST /chats`: envío de un mensaje al chat

`GET /chats`: mostrado de los chats

`GET /chats/{chat_id}`: mostrado de todos los mensajes de un chat
