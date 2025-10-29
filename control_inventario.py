# ==========================================
# Sistema de Gestión de Inventario de Laboratorio
# ==========================================

# 1. SEMESTRE_ACTUAL (Tupla)
SEMESTRE_ACTUAL = ("Otoño", 2025)

# 2. EQUIPOS_UNICOS (Set)
EQUIPOS_UNICOS = {"Osciloscopio", "Multímetro", "Fuente de Poder"}

# 3. inventario (Lista vacía)
inventario = []

# 4. Definición de equipos (Diccionarios)
equipo_1 = {
    "id": "OSC-001",
    "tipo": "Osciloscopio",
    "ubicacion": "Mesa 1",
    "calibraciones": ["2024-01-15", "2025-01-20"]
}

equipo_2 = {
    "id": "FUENTE-001",
    "tipo": "Fuente de Poder",
    "ubicacion": "Mesa 3",
    "calibraciones": ["2023-11-10", "2024-11-15"]
}

# 1️⃣ Poblar el inventario
inventario.append(equipo_1)
inventario.append(equipo_2)

# 2️⃣ Añadir nuevo tipo al set
EQUIPOS_UNICOS.add("Generador de Señales")

# 3️⃣ Añadir equipo nuevo
equipo_3 = {
    "id": "MULTI-001",
    "tipo": "Multímetro",
    "ubicacion": "Mesa 2",
    "calibraciones": []
}
inventario.append(equipo_3)

# 4️⃣ Actualizar equipo OSC-001
for equipo in inventario:
    if equipo["id"] == "OSC-001":
        equipo["calibraciones"].append("2025-10-27")

# 5️⃣ Generar Reporte
print(f"📅 Semestre Actual: {SEMESTRE_ACTUAL[0]} {SEMESTRE_ACTUAL[1]}")
print("\n🔧 Tipos de Equipos Disponibles:")
for tipo in EQUIPOS_UNICOS:
    print(f" - {tipo}")

print("\n📋 Inventario Detallado:")
for equipo in inventario:
    ult_calibracion = equipo["calibraciones"][-1] if equipo["calibraciones"] else "Sin calibraciones registradas"
    print(f"ID: {equipo['id']} | Tipo: {equipo['tipo']} | Última Calibración: {ult_calibracion}")
