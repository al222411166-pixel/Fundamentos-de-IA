# ============================================================
# SISTEMA DE TRIAJE MEDICO Y ASIGNACION DE CITAS (TERMINAL)
# Evaluacion de Signos Vitales, Logica Proposicional y Citas
# ============================================================

from datetime import datetime, timedelta
import random


def solicitar_si_no(mensaje):
    """Solicita una respuesta si/no y retorna booleano True para si, False para no."""
    while True:
        resp = input(f"{mensaje} (s/n): ").strip().lower()
        if resp in ["s", "si", "sí", "y", "yes"]:
            return True
        elif resp in ["n", "no"]:
            return False
        print("  [!] Entrada invalida. Ingrese 's' para si o 'n' para no.")


def solicitar_float(mensaje, min_val=0.0, max_val=500.0, valor_defecto=None):
    """Solicita un valor numerico flotante dentro de un rango."""
    while True:
        prompt = f"{mensaje} "
        if valor_defecto is not None:
            prompt += f"[por defecto {valor_defecto}]: "
        else:
            prompt += ": "
        entrada = input(prompt).strip()
        if not entrada and valor_defecto is not None:
            return float(valor_defecto)
        try:
            val = float(entrada)
            if min_val <= val <= max_val:
                return val
            print(f"  [!] El valor debe estar entre {min_val} y {max_val}.")
        except ValueError:
            print("  [!] Ingrese un valor numerico valido.")


def solicitar_int(mensaje, min_val=0, max_val=130, valor_defecto=None):
    """Solicita un numero entero dentro de un rango."""
    while True:
        prompt = f"{mensaje} "
        if valor_defecto is not None:
            prompt += f"[por defecto {valor_defecto}]: "
        else:
            prompt += ": "
        entrada = input(prompt).strip()
        if not entrada and valor_defecto is not None:
            return int(valor_defecto)
        try:
            val = int(entrada)
            if min_val <= val <= max_val:
                return val
            print(f"  [!] Ingrese un numero entero entre {min_val} y {max_val}.")
        except ValueError:
            print("  [!] Ingrese un numero entero valido.")


def main():
    print("=" * 74)
    print("      SISTEMA EXPERTO DE TRIAJE MEDICO Y ASIGNACION DE CITAS")
    print("            Evaluacion Clinica y Lógica Proposicional")
    print("=" * 74)

    # ----------------------------------------------------------
    # 1. ENTRADA DE DATOS DEL PACIENTE
    # ----------------------------------------------------------
    print("\n" + "-" * 50)
    print("1. DATOS DEL PACIENTE")
    print("-" * 50)

    nombre = input("Nombre completo del paciente: ").strip()
    while not nombre:
        print("  [!] El nombre no puede estar vacio.")
        nombre = input("Nombre completo del paciente: ").strip()

    edad = solicitar_int("Edad del paciente (años)", min_val=1, max_val=120, valor_defecto=35)
    direccion = input("Direccion / Ubicacion: ").strip() or "No especificada"

    # ----------------------------------------------------------
    # 2. CAPTURA DE SIGNOS VITALES Y SOMATOMETRIA
    # ----------------------------------------------------------
    print("\n" + "-" * 50)
    print("2. SIGNOS VITALES Y SOMATOMETRIA")
    print("-" * 50)

    pa_sis = solicitar_float("Presion Arterial Sistolica (mmHg)", min_val=40, max_val=300, valor_defecto=120)
    pa_dia = solicitar_float("Presion Arterial Diastolica (mmHg)", min_val=30, max_val=200, valor_defecto=80)
    fc = solicitar_float("Frecuencia Cardiaca (latidos por minuto)", min_val=30, max_val=250, valor_defecto=75)
    spo2 = solicitar_float("Saturacion de Oxigeno SpO2 (%)", min_val=40, max_val=100, valor_defecto=98)
    peso = solicitar_float("Peso corporal (kg)", min_val=2, max_val=350, valor_defecto=70)
    talla = solicitar_float("Estatura (metros)", min_val=0.4, max_val=2.5, valor_defecto=1.70)

    imc = peso / (talla ** 2) if talla > 0 else 0.0

    # ----------------------------------------------------------
    # 3. SINTOMAS Y FACTORES DE RIESGO
    # ----------------------------------------------------------
    print("\n" + "-" * 50)
    print("3. SINTOMAS Y FACTORES DE RIESGO")
    print("-" * 50)

    fiebre = solicitar_si_no("¿Presenta fiebre alta (> 38 °C)?")
    dolor_pecho = solicitar_si_no("¿Presenta dolor opresivo en el pecho o dificultad para respirar (disnea)?")
    tos = solicitar_si_no("¿Presenta tos persistente o dolor agudo de garganta?")

    # ----------------------------------------------------------
    # 4. CONSTRUCCION DE PROPOSICIONES LOGICAS
    # ----------------------------------------------------------
    # P: Presion arterial fuera de rango normal
    P = (pa_sis >= 140 or pa_sis <= 90) or (pa_dia >= 90 or pa_dia <= 60)

    # Q: Frecuencia cardiaca anormal (taquicardia o bradicardia)
    Q = fc > 100 or fc < 50

    # R: SpO2 en nivel critico de hipoxemia
    R = spo2 < 92

    # S: Sintomas de infeccion respiratoria / febril
    S = fiebre or tos

    # T: Alerta por sospecha de evento cardiovascular / disnea aguda
    T = dolor_pecho

    # U: IMC fuera de rango saludable (obesidad o desnutricion)
    U = imc >= 30 or imc < 18.5

    print("\n" + "=" * 55)
    print(" VALORES DE LAS PROPOSICIONES LOGICAS")
    print("=" * 55)
    print(f"P - Presion arterial alterada (>=140/90 o <=90/60) : {P}")
    print(f"Q - Frecuencia cardiaca anormal (>100 o <50 lpm)   : {Q}")
    print(f"R - Desaturacion de Oxigeno SpO2 (< 92%)          : {R}")
    print(f"S - Cuadro sintomatico de fiebre o tos            : {S}")
    print(f"T - Dolor toracico opresivo / Disnea aguda         : {T}")
    print(f"U - Indice de masa corporal anormal (IMC: {imc:.1f})   : {U}")

    # ----------------------------------------------------------
    # 5. REGLAS DE INFERENCIA Y EVALUACION DE TRIAJE
    # ----------------------------------------------------------
    # Regla Alta: SpO2 critico, Dolor toracico, o combinacion de presion y ritmo cardiaco anormales
    condicion_alta = R or T or (P and Q)

    # Regla Media: Alteracion de presion, sintomas febriles o ritmo alterado (sin criterios de gravedad extrema)
    condicion_media = (P or S or Q) and not condicion_alta

    if condicion_alta:
        prioridad = "ALTA -> TRIAJE ROJO"
        modalidad = "Atencion inmediata en URGENCIAS"
        dia_cita = "INMEDIATO (Hoy mismo - Atencion Continua)"
        hora_cita = datetime.now().strftime("%H:%M")

        if T or (P and Q):
            especialidad = "Urgencias / Cardiologia"
            motivo = "Riesgo cardiovascular agudo o inestabilidad hemodinamica."
        elif R:
            especialidad = "Urgencias / Neumologia"
            motivo = "Insuficiencia respiratoria aguda / SpO2 critico."
        else:
            especialidad = "Urgencias Generales"
            motivo = "Descompensacion aguda de signos vitales."

    elif condicion_media:
        prioridad = "MEDIA -> TRIAJE AMARILLO"
        modalidad = "Cita prioritaria para el MISMO DIA"
        dia_cita = datetime.now().strftime("%d/%m/%Y") + " (Mismo dia)"
        hora_cita = "16:30"

        if S:
            especialidad = "Medicina General / Neumologia"
            motivo = "Cuadro febril e infeccion respiratoria en curso."
        elif P:
            especialidad = "Medicina Interna"
            motivo = "Descontrol de presion arterial para ajuste terapeutico."
        else:
            especialidad = "Medicina General"
            motivo = "Valoracion clinica prioritaria por sintomas moderados."

    else:
        prioridad = "NORMAL -> TRIAJE VERDE"
        modalidad = "Cita programada para OTRO DIA"
        fecha_futura = datetime.now() + timedelta(days=random.randint(2, 5))
        dia_cita = fecha_futura.strftime("%d/%m/%Y")
        hora_cita = "10:00"

        if U:
            especialidad = "Medicina Preventiva / Nutricion"
            motivo = "Seguimiento nutricional y control de indice de masa corporal."
        else:
            especialidad = "Medicina General / Consulta Externa"
            motivo = "Chequeo de rutina y revision preventiva."

    # ----------------------------------------------------------
    # 6. GENERACION DEL COMPROBANTE CLINICO
    # ----------------------------------------------------------
    folio = f"MED-{random.randint(1000, 9999)}"
    sep = "=" * 74
    sub_sep = "-" * 74

    print("\n" + sep)
    print("               COMPROBANTE CLINICO Y AGENDAMIENTO DE CITA")
    print(sep)
    print(f"Folio de Cita     : {folio}")
    print(f"Fecha de Emision  : {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    print(f"Estado            : AGENDADO / ASIGNADO")
    print(sub_sep)
    print("1. FICHA DEL PACIENTE")
    print(sub_sep)
    print(f"Nombre            : {nombre}")
    print(f"Edad              : {edad} años")
    print(f"Direccion         : {direccion}")
    print(sub_sep)
    print("2. REGISTRO CLINICO DE SIGNOS VITALES")
    print(sub_sep)
    print(f"Presion Arterial  : {pa_sis:.0f}/{pa_dia:.0f} mmHg")
    print(f"Frecuencia Card.  : {fc:.0f} lpm")
    print(f"Oxigenacion SpO2  : {spo2:.0f}%")
    print(f"Peso / Talla      : {peso:.1f} kg / {talla:.2f} m (IMC: {imc:.1f})")
    print(sub_sep)
    print("3. EVALUACION DE PROPOSICIONES LOGICAS")
    print(sub_sep)
    print(f"P (Presion alterada)       : {P}")
    print(f"Q (Frecuencia cardiaca anor): {Q}")
    print(f"R (Oxigenacion < 92%)      : {R}")
    print(f"S (Fiebre o Tos)           : {S}")
    print(f"T (Dolor toracico/disnea)  : {T}")
    print(f"U (IMC fuera de rango)     : {U}")
    print(sub_sep)
    print("4. DICTAMEN Y AGENDAMIENTO")
    print(sub_sep)
    print(f"Nivel de Prioridad: {prioridad}")
    print(f"Modalidad Asignada: {modalidad}")
    print(f"Fecha de Cita     : {dia_cita}")
    print(f"Hora Asignada     : {hora_cita}")
    print(f"Especialidad      : {especialidad}")
    print(f"Motivo / Remision : {motivo}")
    print(sep)
    print("Por favor presentarse 15 minutos antes con su identificacion oficial.")
    print(sep + "\n")


if __name__ == "__main__":
    main()