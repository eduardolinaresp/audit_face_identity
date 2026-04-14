# 👤 Auditoría de Identidad Biométrica (IA vs. Real)

Este proyecto permite realizar una **auditoría masiva de identidad** comparando avatares generados por Inteligencia Artificial contra una base de datos de fotografías reales. Utiliza modelos de aprendizaje profundo (Deep Learning) para determinar si la estructura facial y los rasgos esenciales se preservaron durante la generación.

## 🚀 Características Principales

* [cite_start]**Motor de Inferencia:** Utiliza **Facenet512**, el modelo más preciso para extraer rasgos estructurales[cite: 1, 5].
* [cite_start]**Detector de Rostros:** Implementa **RetinaFace**, optimizado para detectar caras incluso en imágenes con "ruido" artístico[cite: 1].
* **Procesamiento N a N:** Capacidad de procesar múltiples avatares contra una base de datos local de forma automatizada.
* **Privacidad Total:** El procesamiento es **100% local**. Las imágenes no se envían a la nube ni a APIs externas.
* **Registro (Logging):** Generación de un historial detallado (`log_auditoria.txt`) con métricas de distancia y estados de validación.

## 🛠️ Requisitos del Sistema

* **Hardware Recomendado:** Mínimo 8 GB de RAM (Optimizado para evitar swaps de memoria).
* **Entorno:** Python 3.10+
* **Librerías Clave:** TensorFlow 2.21.0, DeepFace y tf-keras.

## 📦 Instalación y Configuración

1. **Clonar el repositorio y crear entorno virtual:**
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```
2. **Instalar dependencias:**
   ```powershell
   pip install -r requirements.txt   
   ```
3. **Preparar directorios:**
   * Coloca tus fotos reales en `/base_comparacion`.
   * Coloca tus fotos a auditar en `/fotos`.

## 🖥️ Uso

Para iniciar el proceso de auditoría masiva, ejecuta:

```powershell
python auditoria_masiva.py
```

### Interpretación de Resultados

El script utiliza la **distancia de coseno** para medir la similitud. Los estados en el log se definen según la proximidad biométrica:

| Distancia | Estado | Significado |
| :--- | :--- | :--- |
| **< 0.40** | ✅ Éxito | Identidad preservada; la IA respetó tus rasgos. |
| **0.40 - 0.60** | ⚠️ Parcial | Identidad parcial; cambios artísticos notables. |
| **> 0.60** | ❌ Débil | La IA alteró demasiado la estructura facial. |

## 🔒 Seguridad y Git

Este repositorio está configurado para **no rastrear datos biométricos**. Las carpetas de imágenes contienen archivos `.gitkeep` para preservar la estructura, pero las reglas del `.gitignore` aseguran que tus fotos personales y archivos de caché (`.pkl`) nunca salgan de tu máquina local.

### Notas Técnicas
* El archivo `.pkl` es un caché generado para acelerar las comparaciones futuras. Si actualizas tu base de fotos reales, bórralo para regenerar los vectores.
* Se recomienda cerrar aplicaciones pesadas durante la ejecución para optimizar el uso de los 8 GB de RAM por parte de TensorFlow.   
   
