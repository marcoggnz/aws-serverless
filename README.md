# Diseño e implementación de una web de anuncios en AWS

Este repositorio muestra el backend de una aplicación serverless de una web de publicación de anuncios utilizando servicios de AWS.

## Manual de despliegue

Se ha intentado automatizar el despliegue de la aplicación. Para ello hay que previamente preparar el entorno.
1) Instalación de AWS CLI (si no se ha instalado previamente):
```bash
pip install awscli --upgrade --user
```
2) Confirmación de que la instalación de ha realizado correctamente:
```bash
aws --version
```
3) Instalación del plugin Serverless S3 Sync:
```bash
npm --save install serverless
```
4) Instalación del plugin Serverless Finch:
```bash
npm install --save serverless-finch
```
5) Configuración de la consola AWS CLI con los correspondientes datos de la cuenta de AWS que se va a utilizar:
```bash
aws configure
```
6) A continuación debverán introducirse los siguientes datos que se encuentran en la cuenta de AWS:
- Access Key
- Secret Key
- Región de AWS donde se quiere trabajar
7) Despliegue de la aplicación:
```bash
sls deploy
sls client deploy
```
8) Mostrado de información del depsliegue realizado:
```bash
sls info
```
9) Cierre del depliegue cuando se quiera terminar:
```bash
sls remove
```
   

## Arquitectura General
Se ha tratado de utilizar servicios serverless con el fin de minimizar costes operativos cuando la aplicación se encuentra en reposo. A continuación se muestra el diagrama de architectura de la aplicación, aunque algunos de los servicios que aparecen, no han sido implementados. Para más detalles sobre la arquitectura, ver el documento "Diseño de architectura" de la carpeta /doc.

![Architecture diagram](images/https://github.com/marcoggnz/datahack/blob/main/AWSarchitectura-redes.jpg)
