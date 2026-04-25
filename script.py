import os

entorno = os.getenv("APP_ENV")
api_key = os.getenv("API_KEY")
mensaje = os.getenv("MENSAJE")

print("✅ Script ejecutado correctamente")
print(f"📝 Mensaje recibido: {mensaje}")
print(f"🌍 Entorno: {entorno}")

if api_key:
    print("🔐 API_KEY recibida correctamente")
else:
    print("❌ API_KEY no encontrada")
