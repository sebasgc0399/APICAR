from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
import json
import os

app = FastAPI()

# Cargar los datos de los vehículos desde el archivo
def cargar_vehiculos():
    try:
        with open("./vehiculos/vehiculos.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

vehiculos = cargar_vehiculos()

# Función para obtener la URL de la imagen del vehículo
def obtener_url_imagen(id_vehiculo):
    ruta_imagen = os.path.join('./imagenes', f"{id_vehiculo}.png")
    return ruta_imagen if os.path.exists(ruta_imagen) else None

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
