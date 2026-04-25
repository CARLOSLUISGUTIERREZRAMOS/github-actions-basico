import os

entorno = os.getenv("APP_ENV")
api_key = os.getenv("API_KEY")

print("✅ Script ejecutado correctamente")
print(f"🌍 Entorno: {entorno}")

if api_key:
    print("🔐 API_KEY recibida correctamente")
else:
    print("❌ API_KEY no encontrada")
