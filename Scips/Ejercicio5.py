# ============================================================
# SISTEMA DE DIAGNOSTICO DE EQUIPOS DE COMPUTO (TERMINAL)
# Centro de Soporte Tecnico e Ingenieria de Redes
# ============================================================

from datetime import datetime
import random


def solicitar_si_no(mensaje):
    """Solicita una respuesta si/no y retorna booleano True para si, False para no."""
    while True:
        resp = input(f"{mensaje} (s/n): ").strip().lower()
        if resp in ["s", "si", "sí", "y", "yes"]:
            return True
        elif resp in ["n", "no"]:
            return False
        print("  [!] Entrada invalida. Por favor responda 's' para si o 'n' para no.")


def main():
    print("=" * 70)
    print("      SISTEMA DE DIAGNOSTICO DE EQUIPOS DE COMPUTO - SOPORTE TECNICO")
    print("         Evaluacion de Fallas de Hardware, Software y Red")
    print("=" * 70)

    # ----------------------------------------------------------
    # 1. DATOS DEL SOLICITANTE E HISTORIAL
    # ----------------------------------------------------------
    print("\n" + "-" * 50)
    print("1. DATOS DEL SOLICITANTE E HISTORIAL")
    print("-" * 50)

    nombre = input("Nombre del usuario / solicitante: ").strip()
    while not nombre:
        print("  [!] El nombre no puede estar vacio.")
        nombre = input("Nombre del usuario / solicitante: ").strip()

    contacto = input("Telefono / Contacto: ").strip() or "No especificado"
    direccion = input("Direccion / Ubicacion: ").strip() or "No especificada"

    es_primer_reporte = solicitar_si_no("¿Es el primer reporte del usuario?")
    if es_primer_reporte:
        previos = 0
        tipo_usuario = "Nuevo Usuario (Primer Servicio)"
    else:
        while True:
            try:
                previos_input = input("Numero de reportes previos registrados: ").strip()
                previos = int(previos_input)
                if previos < 0:
                    print("  [!] Ingrese un numero mayor o igual a 0.")
                    continue
                break
            except ValueError:
                print("  [!] Por favor ingrese un numero entero valido.")
        tipo_usuario = f"Usuario Recurrente ({previos} previos)"

    total_reportes = previos + 1

    # ----------------------------------------------------------
    # 2. INFORMACION DEL EQUIPO
    # ----------------------------------------------------------
    print("\n" + "-" * 50)
    print("2. INFORMACION DEL EQUIPO")
    print("-" * 50)

    print("Seleccione el tipo de equipo:")
    print("  1) Computadora de escritorio (Desktop)")
    print("  2) Laptop / Portatil")
    print("  3) All in One (Todo en uno)")
    print("  4) Servidor / Estacion de Trabajo")
    print("  5) Otro")
    
    opciones_equipo = {
        "1": "Computadora de escritorio (Desktop)",
        "2": "Laptop / Portatil",
        "3": "All in One (Todo en uno)",
        "4": "Servidor / Estacion de Trabajo",
        "5": "Otro"
    }

    op_equipo = input("Opcion (1-5) [por defecto 2]: ").strip()
    tipo_equipo = opciones_equipo.get(op_equipo, "Laptop / Portatil")
    print(f"  -> Dispositivo: {tipo_equipo}")

    modelo = input("Marca y Modelo del equipo (ej. Lenovo ThinkPad / Dell OptiPlex): ").strip() or "Generico / No especificado"

    # ----------------------------------------------------------
    # 3. CUESTIONARIO Y PRUEBAS DE DIAGNOSTICO
    # ----------------------------------------------------------
    print("\n" + "-" * 50)
    print("3. CUESTIONARIO DE DIAGNOSTICO TECNICO")
    print("-" * 50)

    p_electricidad = solicitar_si_no("1. ¿El equipo recibe alimentacion electrica / enciende LED?")
    p_enciende = True
    p_video = True
    p_pitidos = False
    p_so = True
    p_pantalla_azul = False
    p_lento = False
    p_red = False

    if not p_electricidad:
        p_enciende = False
        p_video = False
        p_so = False
    else:
        p_enciende = solicitar_si_no("2. ¿El equipo enciende (giran ventiladores o arranca)?")
        if not p_enciende:
            p_video = False
            p_so = False
        else:
            p_video = solicitar_si_no("3. ¿Muestra imagen en la pantalla (logotipo o texto)?")
            if not p_video:
                p_pitidos = solicitar_si_no("   -> En caso de no dar video: ¿Emite pitidos o parpadeos LED de error?")
                p_so = False
            else:
                p_so = solicitar_si_no("4. ¿Inicia correctamente el Sistema Operativo?")
                if not p_so:
                    p_pantalla_azul = solicitar_si_no("   -> En caso de no iniciar: ¿Muestra pantalla azul (BSOD) o error de disco?")
                else:
                    p_lento = solicitar_si_no("5. ¿Presenta lentitud extrema, congelamientos o sobrecalentamiento?")
                    p_red = solicitar_si_no("6. ¿Presenta fallas continuas con la conexion a Internet / Wi-Fi?")

    # ----------------------------------------------------------
    # 4. EVALUACION DEL DIAGNOSTICO Y METRICAS
    # ----------------------------------------------------------
    causas = []
    recomendaciones = []

    if not p_electricidad:
        pruebas_totales = 1
        pruebas_ok = 0
        pruebas_fail = 1
        diagnostico = "Falla de suministro electrico o circuito de entrada primario."
        severidad = "CRITICA"
        tiempo = "1 - 2 horas"
        causas = [
            "Cable de alimentacion o cargador defectuoso.",
            "Toma de corriente o regulador sin energia.",
            "Fuente de poder interna danada o centro de carga averiado."
        ]
        recomendaciones = [
            "Probar en un enchufe verificado y revisar estado del cargador/cable.",
            "Realizar medicion de voltaje con multimetro en fuente o centro de carga."
        ]
    elif not p_enciende:
        pruebas_totales = 2
        pruebas_ok = 1
        pruebas_fail = 1
        diagnostico = "Fallo en la secuencia de arranque / Cortocircuito en placa madre."
        severidad = "ALTA"
        tiempo = "2 - 4 horas"
        causas = [
            "Boton de encendido desconectado o averiado.",
            "Cortocircuito en la tarjeta madre o fuente de poder en proteccion.",
            "Bateria en corto (en laptops)."
        ]
        recomendaciones = [
            "Drenado de energia residual (pulsar boton 30s sin alimentacion).",
            "Revision de conexiones de panel frontal y fuente de alimentacion."
        ]
    elif not p_video:
        pruebas_totales = 3
        pruebas_ok = 2
        pruebas_fail = 1
        if p_pitidos:
            diagnostico = "Fallo en el POST: Memoria RAM o GPU no detectada."
            causas = [
                "Modulos de memoria RAM sucios o danados.",
                "Falla de tarjeta grafica/BIOS."
            ]
        else:
            diagnostico = "Fallo de salida de senal de video o pantalla."
            causas = [
                "Cable HDMI/DisplayPort suelto o averiado.",
                "Monitor apagado o display averiado."
            ]
        severidad = "ALTA"
        tiempo = "2 - 3 horas"
        recomendaciones = [
            "Limpiar contactos de memoria RAM con goma suave y reconectar.",
            "Probar con una pantalla o cable de video externo verificado."
        ]
    elif not p_so:
        pruebas_totales = 4
        pruebas_ok = 3
        pruebas_fail = 1
        if p_pantalla_azul:
            diagnostico = "Error critico de disco / Archivos de arranque danados (BSOD)."
            causas = [
                "Sectores danados en SSD/HDD.",
                "Corrupcion en particion EFI/MBR o conflicto de controladores."
            ]
        else:
            diagnostico = "Bucle de reinicio o bloqueo durante la carga del SO."
            causas = [
                "Actualizacion fallida del sistema o infeccion por malware."
            ]
        severidad = "MEDIA - ALTA"
        tiempo = "1 - 3 horas"
        recomendaciones = [
            "Verificar deteccion de disco en BIOS y ejecutar reparacion de inicio.",
            "Escaneo de salud SMART y reinstalacion de sistema operativo si se requiere."
        ]
    elif p_lento:
        pruebas_totales = 5
        pruebas_ok = 4
        pruebas_fail = 1
        diagnostico = "Degradacion del rendimiento por sobrecalentamiento o saturacion."
        severidad = "MEDIA"
        tiempo = "1 - 2 horas"
        causas = [
            "Pasta termica seca / acumulacion de polvo en disipadores.",
            "Disco saturado al 100% o exceso de programas en segundo plano."
        ]
        recomendaciones = [
            "Mantenimiento fisico preventivo (limpieza interna y pasta termica).",
            "Optimizar aplicaciones de inicio y valorar migracion a SSD."
        ]
    elif p_red:
        pruebas_totales = 6
        pruebas_ok = 5
        pruebas_fail = 1
        diagnostico = "Problema de conectividad de red / Controladores de Wi-Fi/Ethernet."
        severidad = "BAJA"
        tiempo = "30 - 60 min"
        causas = [
            "Controlador de red desactualizado o configuracion DNS erronea.",
            "Tarjeta de red inalámbrica deshabilitada o antena floja."
        ]
        recomendaciones = [
            "Restablecer configuracion de red y actualizar drivers de fabricante."
        ]
    else:
        pruebas_totales = 6
        pruebas_ok = 6
        pruebas_fail = 0
        diagnostico = "Equipo en correcto funcionamiento en pruebas basicas e intermedias."
        severidad = "NORMAL"
        tiempo = "Inmediato"
        causas = ["Sin anomalias detectadas."]
        recomendaciones = [
            "Mantener respaldos frecuentes y programar servicio preventivo anual."
        ]

    pct_exito = (pruebas_ok / pruebas_totales) * 100 if pruebas_totales > 0 else 100
    num_rep = f"REP-{random.randint(10000, 99999)}"
    fecha_act = datetime.now().strftime("%d/%m/%Y %H:%M")

    # ----------------------------------------------------------
    # 5. REPORTE OFICIAL DE SERVICIO Y ESTADISTICAS
    # ----------------------------------------------------------
    sep = "=" * 74
    sub_sep = "-" * 74

    print("\n" + sep)
    print("          CENTRO DE SOPORTE TECNICO - REPORTE OFICIAL DE SERVICIO")
    print(sep)
    print(f"Folio de Reporte   : {num_rep}")
    print(f"Fecha y Hora       : {fecha_act}")
    print(f"Estado             : ABIERTO / EVALUADO")
    print(sub_sep)
    print("1. INFORMACION DEL SOLICITANTE Y METRICAS DE HISTORIAL")
    print(sub_sep)
    print(f"Nombre del Usuario : {nombre}")
    print(f"Contacto / Telefono: {contacto}")
    print(f"Direccion          : {direccion}")
    print(f"Perfil de Usuario  : {tipo_usuario}")
    print(f"Reportes Previos   : {previos} reporte(s)")
    print(f"Reporte Actual     : Reporte #{total_reportes} registrado en sistema")
    print(sub_sep)
    print("2. FICHA DEL EQUIPO")
    print(sub_sep)
    print(f"Tipo de Dispositivo: {tipo_equipo}")
    print(f"Marca y Modelo     : {modelo}")
    print(sub_sep)
    print("3. METRICAS Y ESTADISTICAS DEL DIAGNOSTICO")
    print(sub_sep)
    print(f"Total Evaluaciones : {pruebas_totales} pruebas realizadas")
    print(f"Pruebas Aprobadas  : {pruebas_ok} ({pct_exito:.1f}%)")
    print(f"Pruebas Fallidas   : {pruebas_fail}")
    print(f"Nivel de Severidad : {severidad}")
    print(f"Tiempo Estimado    : {tiempo}")
    print(sub_sep)
    print("4. DICTAMEN TECNICO Y RECOMENDACIONES")
    print(sub_sep)
    print(f"Diagnostico        : {diagnostico}")
    print("\nPosibles Causas:")
    for c in causas:
        print(f"  * {c}")
    print("\nPlan de Accion Sugerido:")
    for r in recomendaciones:
        print(f"  -> {r}")
    print(sep)
    print(f"                      FIN DEL INFORME - ID: {num_rep}")
    print(sep + "\n")


if __name__ == "__main__":
    main()