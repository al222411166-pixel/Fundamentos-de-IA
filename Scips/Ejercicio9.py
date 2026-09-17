import os
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
from pymongo import MongoClient


# Archivo .env
ruta_env = Path(__file__).resolve().parent.parent / '.env'
load_dotenv(dotenv_path=ruta_env)

# Credenciales y configuracion
mongo_user = os.getenv("Mongo_User")
mongo_password = os.getenv("Mongo_Password")
mongo_cluster = os.getenv("Mongo_Cluster")
mongo_db = os.getenv("Mongo_db")
mongo_collection = os.getenv("Mongo_Colleccion")

# Variables .env
if not all([mongo_user, mongo_password, mongo_cluster, mongo_db, mongo_collection]):
    print("[ERROR] Faltan variables en el archivo .env.")
    print("Asegurate de tener definidas: Mongo_User, Mongo_Password, Mongo_Cluster, Mongo_db, Mongo_Colleccion")
    exit(1)


# Conexion a MongoDB Atlas
uri = f"mongodb+srv://{mongo_user}:{mongo_password}@{mongo_cluster}/?retryWrites=true&w=majority"

print("==================================================")
print("CONECTANDO A MONGODB ATLAS...")
print(f"Cluster: {mongo_cluster}")
print(f"Base de Datos: {mongo_db}")
print(f"Coleccion: {mongo_collection}")
print("==================================================")

try:
    # Cliente de MongoDB
    client = MongoClient(uri, serverSelectionTimeoutMS=5000)

    # Base de datos y la coleccion
    db = client[mongo_db]
    collection = db[mongo_collection]

    # Dato a registrar (vendedor, producto, precio, fecha)
    nueva_venta = {
        "vendedor": "Rolando",
        "producto": "Laptop Gamer ASUS TUF A15",
        "precio": 18500.50,
        "fecha": datetime.now()
    }

    print("\nInsertando venta...")
    print(f"   - Vendedor: {nueva_venta['vendedor']}")
    print(f"   - Producto: {nueva_venta['producto']}")
    print(f"   - Precio:   ${nueva_venta['precio']}")
    print(f"   - Fecha:    {nueva_venta['fecha']}")

    # Base de datos
    resultado = collection.insert_one(nueva_venta)

    print("\n[OK] Dato registrado exitosamente en la base de datos.")
    print(f"ID generado (_id): {resultado.inserted_id}")

    # Consultar datos recientes
    dato_en_db = collection.find_one({"_id": resultado.inserted_id})
    print("\n--------------------------------------------------")
    print("REGISTRO VERIFICADO EN MONGODB ATLAS:")
    print("--------------------------------------------------")
    for campo, valor in dato_en_db.items():
        print(f"   {campo}: {valor}")
    print("==================================================")

except Exception as e:
    print(f"\n[ERROR] Ocurrio un error al conectar o registrar el dato: {e}")

finally:
    if 'client' in locals():
        client.close()
        print("Conexion con MongoDB cerrada correctamente.")
