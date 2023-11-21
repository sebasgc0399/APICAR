from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import json
import os

app = FastAPI()

base_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(base_dir, 'imagenes')
app.mount("/imagenes", StaticFiles(directory=images_dir), name="imagenes")

# Cargar los datos de los vehículos desde el archivo
def cargar_vehiculos():
    try:
        with open(os.path.join("vehiculos", "vehiculos.json"), "r") as file:
            return json.load(file)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Archivo de vehículos no encontrado")

vehiculos = cargar_vehiculos()

def obtener_ruta_imagen(id_vehiculo):
    return os.path.join('imagenes', f"{id_vehiculo}.png")

def obtener_url_imagen_d(id_vehiculo):
    return f"https://apicarroslibre.azurewebsites.net/imagenes/{id_vehiculo}.png"

@app.get("/vehiculos")
async def leer_vehiculos():
    for vehiculo in vehiculos:
        vehiculo["imagen_url"] = obtener_url_imagen_d(vehiculo["id"])
    return vehiculos

@app.get("/vehiculo/{id}")
async def leer_vehiculo(id: int):
    vehiculo = next((v for v in vehiculos if v["id"] == id), None)
    if vehiculo:
        vehiculo["imagen_url"] = obtener_url_imagen_d(id)
        return vehiculo
    raise HTTPException(status_code=404, detail="Vehículo no encontrado")

@app.get("/imagenes/{id_vehiculo}.png")
async def obtener_imagen_vehiculo(id_vehiculo: int):
    ruta_imagen = obtener_ruta_imagen(id_vehiculo)
    if os.path.isfile(ruta_imagen):
        return FileResponse(ruta_imagen)
    else:
        raise HTTPException(status_code=404, detail="Imagen no encontrada")
