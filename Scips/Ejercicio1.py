

#Entrada de datos
asistencia = float(input("Ingresa el porcentaje de asistencia: "))
promedio = float(input("Ingresa el promedio del alumno: "))
proyecto = input("¿El alumno entregó el proyecto final? (si/no): ").strip().lower()
autorizacion = input("¿Tiene autorización especial? (si/no): ").strip().lower()


#Proposiciones
P = asistencia >= 80.0
Q = promedio >= 8.0
R = proyecto == "si"
S = autorizacion == "si"


#Logica proposicional
resultado = (P and Q and R) or S

#Imprimir resultados
print("\n--- Desglose de Evaluación ---")
print(f"Asistencia es >= 80%: {P}")
print(f"Promedio es >= 8.0: {Q}")
print(f"Proyecto es 'si': {R}")
print(f"Autorización especial es 'si': {S}")

print(f"\nResultado lógico: {resultado}")

if resultado:
    print("Estado: APROBADO")
else:
    print("Estado: REPROBADO")

