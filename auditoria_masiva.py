from deepface import DeepFace
import os
import datetime

# ==========================================
# CONFIGURACIÓN DINÁMICA
# ==========================================
DIR_FOTOS = "./fotos"                # Carpeta con fotos
DIR_FOTOS_REALES = "./base_comparacion" # Tu base de datos de fotos reales
ARCHIVO_LOG = "log_auditoria.txt"       # Archivo donde se guardará el historial
MODELO = "Facenet512"                   # 
DETECTOR = "retinaface"                 # 

def registrar_log(mensaje):
    """Escribe los resultados en el archivo y en la consola simultáneamente."""
    with open(ARCHIVO_LOG, "a", encoding="utf-8") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        linea = f"[{timestamp}] {mensaje}\n"
        f.write(linea)
        print(mensaje)

def auditoria_masiva():
    # 1. Validar que las rutas existan
    if not os.path.exists(DIR_FOTOS) or not os.path.exists(DIR_FOTOS_REALES):
        print("Error: Revisa que las carpetas de avatares y fotos reales existan.")
        return

    # 2. Listar archivos válidos (filtramos por extensión)
    extensiones_validas = ('.jpg', '.jpeg', '.png')
    lista_fotos = [f for f in os.listdir(DIR_FOTOS) if f.lower().endswith(extensiones_validas)]
    
    registrar_log(f"=== INICIANDO AUDITORÍA MASIVA ({len(lista_fotos)} archivos) ===")

    for nombre_archivo in lista_fotos:
        path_foto = os.path.join(DIR_FOTOS, nombre_archivo)
        registrar_log(f"🔎 Procesando: {nombre_archivo}")

        try:
            #  Ejecución de la comparación N a N
            resultados = DeepFace.find(
                img_path = path_foto,
                db_path = DIR_FOTOS_REALES,
                model_name = MODELO,
                detector_backend = DETECTOR,
                distance_metric = "cosine",
                enforce_detection = False,  
                silent = True               
            )

            df = resultados[0] # Extraemos el DataFrame de resultados 

            if not df.empty:
                # Calculamos la mejor métrica encontrada
                mejor_distancia = df['distance'].min()
                num_coincidencias = len(df) 

                # Interpretación de resultados para el log 
                if mejor_distancia < 0.4:
                    estado = "ÉXITO: Identidad preservada."
                elif mejor_distancia < 0.6:
                    estado = "PARCIAL: Eres tú con cambios artísticos."
                else:
                    estado = "DÉBIL: La IA alteró demasiado tu rostro."
                
                registrar_log(f"   ✅ {estado} | Distancia: {mejor_distancia:.4f} | Fotos que validan: {num_coincidencias}")
            else:
                registrar_log(f"   ❌ SIN COINCIDENCIAS: Rostro no reconocido como el tuyo.") # [cite: 8]

        except Exception as e:
            registrar_log(f"   ⚠️ ERROR procesando {nombre_archivo}: {str(e)}")

    registrar_log("=== FIN DE LA AUDITORÍA ===\n")

if __name__ == "__main__":
    auditoria_masiva()