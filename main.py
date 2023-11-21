from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

import os
import json

app = FastAPI()

# Configuración para servir archivos estáticos desde la carpeta 'imagenes'
app.mount("/imagenes", StaticFiles(directory="imagenes"), name="imagenes")


# Cargar los datos de los vehículos desde el archivo
def cargar_vehiculos():
    try:
        with open(os.path.join("vehiculos", "vehiculos.json"), "r") as file:  # Asegúrate de usar os.path.join
            return json.load(file)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Archivo de vehículos no encontrado")

vehiculos = cargar_vehiculos()

# Función para obtener la URL de la imagen del vehículo
def obtener_url_imagen(id_vehiculo):
    nombre_imagen = f"{id_vehiculo}.png"
    ruta_imagen = os.path.join('imagenes', nombre_imagen)  # Usa os.path.join para la portabilidad de rutas
    # Comprueba si el archivo de imagen existe
    if os.path.isfile(ruta_imagen):
        return ruta_imagen
    else:
        return None


@app.get("/vehiculos")
async def leer_vehiculos():
    for vehiculo in vehiculos:
        vehiculo["imagen_url"] = obtener_url_imagen(vehiculo["id"])
    return vehiculos

@app.get("/vehiculo/{id}")
async def leer_vehiculo(id: int):
    for vehiculo in vehiculos:
        if vehiculo["id"] == id:
            vehiculo["imagen_url"] = obtener_url_imagen(id)
            return vehiculo
    raise HTTPException(status_code=404, detail="Vehículo no encontrado")

@app.get("/imagen_vehiculo/{id}")
async def obtener_imagen_vehiculo(id: int):
    ruta_imagen = obtener_url_imagen(id)
    if ruta_imagen:
        return FileResponse(ruta_imagen)
    else:
        raise HTTPException(status_code=404, detail="Imagen no encontrada")
