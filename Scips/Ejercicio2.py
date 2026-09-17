# ==========================================================
# CASO DE ESTUDIO:
# Sistema de autorización para examen
# ==========================================================

print("==============================================")
print(" SISTEMA DE AUTORIZACIÓN PARA EXAMEN FINAL")
print("==============================================")

# ----------------------------------------------------------
# 1. ENTRADA DE DATOS
# ----------------------------------------------------------

asistencia = float(
    input("Ingresa el porcentaje de asistencia: ")
)

promedio = float(
    input("Ingresa el promedio: ")
)

proyecto = input(
    "¿Entregó el proyecto? (si/no): "
).lower()

autorizacion = input(
    "¿Tiene autorización especial? (si/no): "
).lower()

lista_oficial = input(
    "¿Aparece en la lista oficial? (si/no): "
).lower()

sin_adeudos = input(
    "¿El alumno no tiene adeudos? (si/no): "
).lower()


# ----------------------------------------------------------
# 2. CONVERTIMOS LOS DATOS EN PROPOSICIONES
# ----------------------------------------------------------

# P es verdadera cuando la asistencia es >= 80
P = asistencia >= 80

# Q es verdadera cuando el promedio es >= 8
Q = promedio >= 8

# R es verdadera cuando entregó el proyecto
R = proyecto == "si"

# S es verdadera cuando tiene autorización especial
S = autorizacion == "si"

# T es verdadera cuando aparece en la lista oficial
T = lista_oficial == "si"

# U es verdadera cuando no tiene adeudos
U = sin_adeudos == "no"


# ----------------------------------------------------------
# 3. MOSTRAMOS LAS PROPOSICIONES
# ----------------------------------------------------------

print("\n==============================================")
print(" VALORES DE LAS PROPOSICIONES")
print("==============================================")

print("P - Asistencia suficiente:", P)
print("Q - Promedio aprobatorio:", Q)
print("R - Proyecto entregado:", R)
print("S - Autorización especial:", S)
print("T - Aparece en la lista oficial:", T)
print("U - No tiene adeudos:", U)


# ----------------------------------------------------------
# 4. NEGACIÓN
# ----------------------------------------------------------

# NOT cambia True por False y False por True
negacion_P = not P

print("\nNEGACIÓN")
print("¬P =", negacion_P)


# ----------------------------------------------------------
# 5. CONJUNCIÓN
# ----------------------------------------------------------

# AND necesita que ambas condiciones sean verdaderas
conjuncion = P and Q

print("\nCONJUNCIÓN")
print("P ∧ Q =", conjuncion)


# ----------------------------------------------------------
# 6. DISYUNCIÓN
# ----------------------------------------------------------

# OR necesita que al menos una condición sea verdadera
disyuncion = Q or S

print("\nDISYUNCIÓN")
print("Q ∨ S =", disyuncion)


# ----------------------------------------------------------
# 7. CONDICIONAL
# ----------------------------------------------------------

# P -> Q equivale a:
#
#       NOT P OR Q
#
# Es decir:
# Si P ocurre, entonces Q debe ocurrir.

condicional = (not P) or Q

print("\nCONDICIONAL")
print("P → Q =", condicional)


# ----------------------------------------------------------
# 8. BICONDICIONAL
# ----------------------------------------------------------

# El bicondicional es verdadero
# cuando P y Q tienen el mismo valor.

bicondicional = P == Q

print("\nBICONDICIONAL")
print("P ↔ Q =", bicondicional)


# ----------------------------------------------------------
# 9. USO DE PARÉNTESIS
# ----------------------------------------------------------

# La regla es:
#
# (P AND Q AND R AND T AND U) OR S
#
# Se requiere cumplir las condiciones académicas, administrativas (lista y sin adeudos),
# o bien contar con una autorización especial.

expresion = (P and Q and R and T and U) or S

print("\nEXPRESIÓN CON PARÉNTESIS")
print("((P ∧ Q ∧ R ∧ T ∧ U) ∨ S) =", expresion)


# ----------------------------------------------------------
# 10. DECISIÓN FINAL
# ----------------------------------------------------------

if expresion:
    print("\nRESULTADO:")
    print("El alumno PUEDE presentar el examen.")
else:
    print("\nRESULTADO:")
    print("El alumno NO puede presentar el examen.")    