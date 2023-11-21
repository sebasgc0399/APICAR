# API de Vehículos

Esta API es una aplicación FastAPI que permite a los usuarios acceder a datos de vehículos y sus imágenes asociadas. Está desplegada y disponible para pruebas en [https://apicarroslibre.azurewebsites.net/](https://apicarroslibre.azurewebsites.net/).

## Endpoints

La API tiene los siguientes endpoints:

- `/vehiculos`: Retorna un listado de todos los vehículos disponibles.
- `/vehiculo/{id}`: Retorna los detalles de un vehículo específico por su ID.
- `/imagenes/{id_vehiculo}.png`: Retorna la imagen asociada con el ID del vehículo.

## Cómo Utilizar

Puedes acceder a la API a través de la siguiente URL base: `https://apicarroslibre.azurewebsites.net`.

### Obtener Vehículos
Para obtener un listado de todos los vehículos, realiza una solicitud GET a: 
GET https://apicarroslibre.azurewebsites.net/vehiculos

### Obtener Detalles de Vehículo
Para obtener los detalles de un vehículo específico, incluye el ID del vehículo en la URL:
GET https://apicarroslibre.azurewebsites.net/vehiculo/{id}

### Obtener Imagen de Vehículo
Para obtener la imagen de un vehículo, usa el ID del vehículo en la URL:
GET https://apicarroslibre.azurewebsites.net/imagenes/{id_vehiculo}.png

## Instalación Local
Para ejecutar la API localmente, necesitarás Python 3.12 y FastAPI. Instala las dependencias con:

```pip install -r requirements.txt```

Luego, inicia el servidor con:

```uvicorn main:app --host=0.0.0.0 --port=8000```

La API estará disponible en `http://localhost:8000`.

## Despliegue

Esta API está desplegada en Azure Web App y utiliza Azure Blob Storage para el almacenamiento persistente de imágenes.
