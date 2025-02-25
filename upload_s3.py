import os
import boto3
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

# Obtener credenciales desde .env
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")
BUCKET_NAME = os.getenv("BUCKET_NAME")

# Crear el cliente S3
s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION,
)

def subir_a_s3(archivo_local, clave_s3):
    """Sube un archivo a S3."""
    try:
        s3.upload_file(archivo_local, BUCKET_NAME, clave_s3)
        print(f"✅ Archivo '{archivo_local}' usa esta ruta 'https://videosincidentes.amazonaws.com/{clave_s3}'")
        return f"s3://{BUCKET_NAME}/{clave_s3}"
    except Exception as e:
        print(f"❌ Error al subir el archivo: {e}")
        return None

# Prueba la función
if __name__ == "__main__":
    archivo = input("📂 Ingresa la ruta del archivo: ").strip()
    
    if not os.path.isfile(archivo):
        print("❌ El archivo no existe. Verifica la ruta.")
        exit(1)

    nombre_archivo = os.path.basename(archivo)
    clave_s3 = f"videos/{nombre_archivo}"

    subir_a_s3(archivo, clave_s3)
