from pymongo import MongoClient
from flask import Flask, request, redirect, url_for
import pandas as pd


app = Flask(__name__)

# Conexión con MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["rueda_vida"]
collection = db["empleados"]

@app.route('/guardar_p', methods=['POST'])
def guardar_p():
    print("✅ Se llamó a la función guardar_p()")  # Ver si Flask recibe el POST

    # Obtener datos del formulario
    print("🔍 Datos recibidos:", request.form)  # Ver qué datos llegan

    accion = request.form.get('accion')
    id = request.form.get('id')
    nombre = request.form.get('nombre')
    apellido = request.form.get('apellido')
    correo = request.form.get('correo')
    departamento = request.form.get('departamento')
    respuestas = request.form.getlist('respuestas')

    if not respuestas:
        print("⚠️ No se recibieron respuestas.")

    respuestas = [int(r) for r in respuestas] if respuestas else []

    preguntas_rueda = {
        "Área Física": respuestas[:5],
        "Área Personal": respuestas[5:10],
        "Área Familiar": respuestas[10:15],
        "Área Económica": respuestas[15:20],
        "Área Profesional": respuestas[20:25],
        "Área Social": respuestas[25:30],
        "Área de Ocio": respuestas[30:35],
        "Área Espiritual": respuestas[35:40]
    }

    empleado = {
        "id": id,
        "nombre": nombre,
        "apellido": apellido,
        "correo": correo,
        "departamento": departamento,
        "respuestas": preguntas_rueda
    }

    print("📌 Datos listos para insertar:", empleado)  # Ver datos antes de guardar

    if accion == "Guardar":
        collection.insert_one(empleado)
        print("✅ Empleado guardado correctamente.")
    elif accion == "Editar":
        collection.update_one({"id": id}, {"$set": empleado})
        print("✅ Datos actualizados.")
    elif accion == "Borrar":
        collection.delete_one({"id": id})
        print("✅ Empleado eliminado.")

    return redirect(url_for('persona'))



@app.route('/exportar_excel', methods=['GET'])
def exportar_excel():
    empleados = list(collection.find({}, {'_id': 0}))  # Excluimos _id para que no moleste

    if not empleados:
        return "⚠️ No hay datos para exportar.", 404

    # Aplanar las respuestas anidadas para poder convertirlo en un DataFrame
    datos_excel = []
    for emp in empleados:
        fila = {
            "ID": emp.get("id", ""),
            "Nombre": emp.get("nombre", ""),
            "Apellido": emp.get("apellido", ""),
            "Correo": emp.get("correo", ""),
            "Departamento": emp.get("departamento", "")
        }

        for area, respuestas in emp.get("respuestas", {}).items():
            for i, val in enumerate(respuestas, start=1):
                fila[f"{area} {i}"] = val

        datos_excel.append(fila)

    # Convertir a DataFrame y exportar
    df = pd.DataFrame(datos_excel)
    nombre_archivo = "empleados_exportados.xlsx"
    df.to_excel(nombre_archivo, index=False)

    return f"✅ Archivo Excel generado: {nombre_archivo}"

