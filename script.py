import os

entorno = os.getenv("APP_ENV")

print("✅ Script ejecutado correctamente")
print(f"🌍 Entorno actual: {entorno}")

for i in range(1, 4):
    print(f"Contando: {i}")
