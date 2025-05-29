# Prompts usados para generar funcionalidades en SQLAlchemy

Este documento presenta una recopilación de preguntas (prompts) realizadas durante el desarrollo del proyecto, con el objetivo de estructurar la base de datos, insertar datos y generar consultas utilizando SQLAlchemy en Python.

---

## 🔧 CONFIGURACIÓN Y MODELAJE

**Prompt 1:**  
> ¿Cómo puedo definir una cadena de conexión para una base de datos SQLite en SQLAlchemy?

**Prompt 2:**  
> ¿Cómo hago para que una reacción tenga una relación única entre usuario y publicación?

---

## 📥 INGRESO DE DATOS

**Prompt 3:**  
> ¿Cómo inserto datos desde archivos CSV a una base de datos usando SQLAlchemy y pandas?

**Prompt 4:**  
> ¿Cómo puedo dividir datos tipo `"usuario|publicacion"` de un CSV para asociarlos correctamente a una publicación en SQLAlchemy?

**Prompt 5:**  
> ¿Cómo puedo cargar emociones como 'alegre', 'enojado', etc., a una tabla de reacciones en SQLAlchemy asegurándome de relacionarlas con usuarios y publicaciones?

---

## 🔍 CONSULTAS FUNCIONALES

### ✅ Consulta 1: Listar publicaciones de un usuario

**Prompt 6:**  
> ¿Cómo hago una función que reciba el nombre de un usuario y devuelva sus 10 primeras publicaciones usando SQLAlchemy?

### ✅ Consulta 2: Publicaciones en las que reaccionó un usuario

**Prompt 7:**  
> ¿Cómo puedo listar las publicaciones en las que un usuario ha reaccionado y mostrar el contenido y tipo de emoción usando SQLAlchemy?

