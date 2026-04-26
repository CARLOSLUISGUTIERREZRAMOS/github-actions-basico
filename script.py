import os

mensaje = os.getenv("MENSAJE", "Sin mensaje")
entorno = os.getenv("APP_ENV")

print("✅ Script desde una feature branch")
print(f"📝 Mensaje: {mensaje}")
print(f"🌍 Entorno: {entorno}")
