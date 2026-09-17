# ============================================================
# SISTEMA DE TRIAJE MEDICO Y ASIGNACION DE CITAS
# ============================================================

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
import random


class TriajeMedicoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Triaje Medico y Asignacion de Citas")
        self.root.geometry("860x780")
        self.root.minsize(800, 700)
        self.root.configure(bg="#f8fafc")

        self.configurar_estilos()
        self.crear_interfaz()

    def configurar_estilos(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure(".", font=("Segoe UI", 10), background="#f8fafc")
        style.configure("Header.TFrame", background="#0f766e")
        style.configure("Header.TLabel", background="#0f766e", foreground="#ffffff", font=("Segoe UI", 14, "bold"))
        style.configure("SubHeader.TLabel", background="#0f766e", foreground="#ccfbf1", font=("Segoe UI", 9))

        style.configure("Card.TLabelframe", background="#ffffff", relief="flat")
        style.configure("Card.TLabelframe.Label", background="#ffffff", foreground="#0f172a", font=("Segoe UI", 10, "bold"))

        style.configure("Primary.TButton", font=("Segoe UI", 10, "bold"), background="#0d9488", foreground="#ffffff")
        style.map("Primary.TButton",
                  background=[("active", "#0f766e"), ("pressed", "#115e59")])

        style.configure("Secondary.TButton", font=("Segoe UI", 9), background="#e2e8f0", foreground="#334155")
        style.map("Secondary.TButton",
                  background=[("active", "#cbd5e1"), ("pressed", "#94a3b8")])

    def crear_interfaz(self):
        header_frame = ttk.Frame(self.root, style="Header.TFrame", padding=15)
        header_frame.pack(fill="x", side="top")

        ttk.Label(header_frame, text="SISTEMA EXPERTO DE DIAGNOSTICO MEDICO Y GESTION DE CITAS", style="Header.TLabel").pack(anchor="w")
        ttk.Label(header_frame, text="Evaluacion de Signos Vitales y Remision Clinica", style="SubHeader.TLabel").pack(anchor="w")

        canvas = tk.Canvas(self.root, bg="#f8fafc", highlightthickness=0)
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas, padding=15)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # 1. DATOS DEL PACIENTE
        frame_paciente = ttk.LabelFrame(self.scrollable_frame, text="  1. Datos del Paciente  ", style="Card.TLabelframe", padding=12)
        frame_paciente.pack(fill="x", pady=6)

        ttk.Label(frame_paciente, text="Nombre del Paciente:").grid(row=0, column=0, sticky="w", padx=5, pady=4)
        self.entry_nombre = ttk.Entry(frame_paciente, width=32)
        self.entry_nombre.grid(row=0, column=1, padx=5, pady=4)

        ttk.Label(frame_paciente, text="Edad (años):").grid(row=0, column=2, sticky="w", padx=5, pady=4)
        self.entry_edad = ttk.Entry(frame_paciente, width=12)
        self.entry_edad.insert(0, "35")
        self.entry_edad.grid(row=0, column=3, sticky="w", padx=5, pady=4)

        ttk.Label(frame_paciente, text="Direccion / Ubicacion:").grid(row=1, column=0, sticky="w", padx=5, pady=4)
        self.entry_direccion = ttk.Entry(frame_paciente, width=32)
        self.entry_direccion.grid(row=1, column=1, padx=5, pady=4)

        # 2. SIGNOS VITALES
        frame_signos = ttk.LabelFrame(self.scrollable_frame, text="  2. Captura de Signos Vitales  ", style="Card.TLabelframe", padding=12)
        frame_signos.pack(fill="x", pady=6)

        ttk.Label(frame_signos, text="Presion Sistolica (mmHg):").grid(row=0, column=0, sticky="w", padx=5, pady=4)
        self.entry_sistolica = ttk.Entry(frame_signos, width=14)
        self.entry_sistolica.insert(0, "120")
        self.entry_sistolica.grid(row=0, column=1, padx=5, pady=4)

        ttk.Label(frame_signos, text="Presion Diastolica (mmHg):").grid(row=0, column=2, sticky="w", padx=5, pady=4)
        self.entry_diastolica = ttk.Entry(frame_signos, width=14)
        self.entry_diastolica.insert(0, "80")
        self.entry_diastolica.grid(row=0, column=3, padx=5, pady=4)

        ttk.Label(frame_signos, text="Frecuencia Cardiaca (lpm):").grid(row=1, column=0, sticky="w", padx=5, pady=4)
        self.entry_fc = ttk.Entry(frame_signos, width=14)
        self.entry_fc.insert(0, "75")
        self.entry_fc.grid(row=1, column=1, padx=5, pady=4)

        ttk.Label(frame_signos, text="Oxigenacion SpO2 (%):").grid(row=1, column=2, sticky="w", padx=5, pady=4)
        self.entry_spo2 = ttk.Entry(frame_signos, width=14)
        self.entry_spo2.insert(0, "98")
        self.entry_spo2.grid(row=1, column=3, padx=5, pady=4)

        ttk.Label(frame_signos, text="Peso (kg):").grid(row=2, column=0, sticky="w", padx=5, pady=4)
        self.entry_peso = ttk.Entry(frame_signos, width=14)
        self.entry_peso.insert(0, "70")
        self.entry_peso.grid(row=2, column=1, padx=5, pady=4)

        ttk.Label(frame_signos, text="Estatura (m):").grid(row=2, column=2, sticky="w", padx=5, pady=4)
        self.entry_talla = ttk.Entry(frame_signos, width=14)
        self.entry_talla.insert(0, "1.70")
        self.entry_talla.grid(row=2, column=3, padx=5, pady=4)

        # 3. SINTOMAS Y SIGNOS DE ALERTA
        frame_sintomas = ttk.LabelFrame(self.scrollable_frame, text="  3. Sintomas y Factores de Riesgo  ", style="Card.TLabelframe", padding=12)
        frame_sintomas.pack(fill="x", pady=6)

        self.var_fiebre = tk.BooleanVar(value=False)
        self.var_pecho = tk.BooleanVar(value=False)
        self.var_tos = tk.BooleanVar(value=False)

        chk_fiebre = ttk.Checkbutton(frame_sintomas, text="Fiebre alta (> 38 C)", variable=self.var_fiebre)
        chk_fiebre.grid(row=0, column=0, sticky="w", padx=8, pady=4)

        chk_pecho = ttk.Checkbutton(frame_sintomas, text="Dolor opresivo en el pecho / Dificultad para respirar (Disnea)", variable=self.var_pecho)
        chk_pecho.grid(row=0, column=1, sticky="w", padx=8, pady=4)

        chk_tos = ttk.Checkbutton(frame_sintomas, text="Tos persistente o dolor de garganta", variable=self.var_tos)
        chk_tos.grid(row=1, column=0, sticky="w", padx=8, pady=4)

        frame_acciones = ttk.Frame(self.scrollable_frame, padding=10)
        frame_acciones.pack(fill="x", pady=6)

        btn_evaluar = ttk.Button(frame_acciones, text="Evaluar y Agendar Cita", style="Primary.TButton", command=self.evaluar_triaje)
        btn_evaluar.pack(side="left", padx=6, ipady=4)

        btn_limpiar = ttk.Button(frame_acciones, text="Limpiar Formulario", style="Secondary.TButton", command=self.limpiar_campos)
        btn_limpiar.pack(side="left", padx=6, ipady=4)

        # 4. RESOLUCION Y COMPROBANTE DE CITA
        frame_resultado = ttk.LabelFrame(self.scrollable_frame, text="  4. Resolucion y Comprobante de Cita  ", style="Card.TLabelframe", padding=12)
        frame_resultado.pack(fill="both", expand=True, pady=6)

        self.frame_badge = tk.Frame(frame_resultado, bg="#e2e8f0", padx=10, pady=8)
        self.frame_badge.pack(fill="x", pady=(0, 10))

        self.lbl_badge_titulo = tk.Label(self.frame_badge, text="PRIORIDAD: PENDIENTE DE EVALUACION", font=("Segoe UI", 11, "bold"), bg="#e2e8f0", fg="#334155")
        self.lbl_badge_titulo.pack(anchor="w")

        self.lbl_badge_desc = tk.Label(self.frame_badge, text="Capture los datos y presione 'Evaluar'", font=("Segoe UI", 9), bg="#e2e8f0", fg="#475569")
        self.lbl_badge_desc.pack(anchor="w")

        self.txt_comprobante = tk.Text(frame_resultado, height=16, width=88, font=("Consolas", 9), bg="#0f172a", fg="#f8fafc", relief="flat", padx=10, pady=10)
        self.txt_comprobante.pack(fill="both", expand=True)

    def limpiar_campos(self):
        self.entry_nombre.delete(0, tk.END)
        self.entry_direccion.delete(0, tk.END)
        self.entry_edad.delete(0, tk.END)
        self.entry_edad.insert(0, "35")

        self.entry_sistolica.delete(0, tk.END)
        self.entry_sistolica.insert(0, "120")
        self.entry_diastolica.delete(0, tk.END)
        self.entry_diastolica.insert(0, "80")

        self.entry_fc.delete(0, tk.END)
        self.entry_fc.insert(0, "75")
        self.entry_spo2.delete(0, tk.END)
        self.entry_spo2.insert(0, "98")

        self.entry_peso.delete(0, tk.END)
        self.entry_peso.insert(0, "70")
        self.entry_talla.delete(0, tk.END)
        self.entry_talla.insert(0, "1.70")

        self.var_fiebre.set(False)
        self.var_pecho.set(False)
        self.var_tos.set(False)

        self.frame_badge.config(bg="#e2e8f0")
        self.lbl_badge_titulo.config(text="PRIORIDAD: PENDIENTE DE EVALUACION", bg="#e2e8f0", fg="#334155")
        self.lbl_badge_desc.config(text="Capture los datos y presione 'Evaluar'", bg="#e2e8f0", fg="#475569")
        self.txt_comprobante.delete("1.0", tk.END)

    def evaluar_triaje(self):
        nombre = self.entry_nombre.get().strip()
        if not nombre:
            messagebox.showwarning("Atencion", "Por favor ingrese el nombre del paciente.")
            return

        try:
            edad = int(self.entry_edad.get().strip())
            pa_sis = float(self.entry_sistolica.get().strip())
            pa_dia = float(self.entry_diastolica.get().strip())
            fc = float(self.entry_fc.get().strip())
            spo2 = float(self.entry_spo2.get().strip())
            peso = float(self.entry_peso.get().strip())
            talla = float(self.entry_talla.get().strip())
        except ValueError:
            messagebox.showerror("Error en datos", "Por favor ingrese valores numericos validos en signos vitales y edad.")
            return

        direccion = self.entry_direccion.get().strip() or "No especificada"
        imc = peso / (talla ** 2) if talla > 0 else 0

        fiebre = self.var_fiebre.get()
        dolor_pecho = self.var_pecho.get()
        tos = self.var_tos.get()

        P = (pa_sis >= 140 or pa_sis <= 90) or (pa_dia >= 90 or pa_dia <= 60)
        Q = fc > 100 or fc < 50
        R = spo2 < 92
        S = fiebre or tos
        T = dolor_pecho
        U = imc >= 30 or imc < 18.5

        condicion_alta = R or T or (P and Q)
        condicion_media = (P or S or Q) and not condicion_alta

        if condicion_alta:
            prioridad = "ALTA"
            modalidad = "Atencion inmediata en URGENCIAS"
            dia_cita = "INMEDIATO (Hoy mismo - Atencion Continua)"
            hora_cita = datetime.now().strftime("%H:%M")
            
            self.frame_badge.config(bg="#ef4444")
            self.lbl_badge_titulo.config(text="PRIORIDAD: ALTA -> TRIAJE ROJO (URGENCIAS)", bg="#ef4444", fg="#ffffff")
            self.lbl_badge_desc.config(text="Paciente requiere valoracion medica inmediata en sala de urgencias.", bg="#ef4444", fg="#ffffff")

            if T or (P and Q):
                especialidad = "Urgencias / Cardiologia"
                motivo = "Riesgo cardiovascular o compromiso hemodinamico agudo."
            elif R:
                especialidad = "Urgencias / Neumologia"
                motivo = "Insuficiencia respiratoria aguda / SpO2 critico."
            else:
                especialidad = "Urgencias Generales"
                motivo = "Descompensacion aguda de signos vitales."

        elif condicion_media:
            prioridad = "MEDIA"
            modalidad = "Cita prioritaria para el MISMO DIA"
            dia_cita = datetime.now().strftime("%d/%m/%Y") + " (Mismo dia)"
            hora_cita = "16:30"

            self.frame_badge.config(bg="#f59e0b")
            self.lbl_badge_titulo.config(text="PRIORIDAD: MEDIA -> AMARILLO (CITA HOY)", bg="#f59e0b", fg="#ffffff")
            self.lbl_badge_desc.config(text="Paciente requiere consulta prioritaria.", bg="#f59e0b", fg="#ffffff")

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
            prioridad = "NORMAL"
            modalidad = "Cita programada para OTRO DIA"
            fecha_futura = datetime.now() + timedelta(days=random.randint(2, 5))
            dia_cita = fecha_futura.strftime("%d/%m/%Y")
            hora_cita = "10:00"

            self.frame_badge.config(bg="#10b981")
            self.lbl_badge_titulo.config(text="PRIORIDAD: NORMAL -> VERDE (CITA PROGRAMADA)", bg="#10b981", fg="#ffffff")
            self.lbl_badge_desc.config(text="Signos vitales estables. Consulta regular agendada.", bg="#10b981", fg="#ffffff")

            if U:
                especialidad = "Medicina Preventiva / Nutricion"
                motivo = "Seguimiento nutricional y control de indice de masa corporal."
            else:
                especialidad = "Medicina General / Consulta Externa"
                motivo = "Chequeo de rutina y revision preventiva."

        folio = f"MED-{random.randint(1000, 9999)}"
        sep = "=" * 74
        sub_sep = "-" * 74

        texto_resumen = f"""{sep}
       COMPROBANTE CLINICO Y AGENDAMIENTO DE CITA
{sep}
Folio de Cita     : {folio}
Fecha de Emision  : {datetime.now().strftime('%d/%m/%Y %H:%M')}
Estado            : AGENDADO / ASIGNADO

{sub_sep}
1. FICHA DEL PACIENTE
{sub_sep}
Nombre            : {nombre}
Edad              : {edad} años
Direccion         : {direccion}

{sub_sep}
2. REGISTRO CLINICO DE SIGNOS VITALES
{sub_sep}
Presion Arterial  : {pa_sis:.0f}/{pa_dia:.0f} mmHg
Frecuencia Card.  : {fc:.0f} lpm
Oxigenacion SpO2  : {spo2:.0f}%
Peso / Talla      : {peso:.1f} kg / {talla:.2f} m (IMC: {imc:.1f})

{sub_sep}
3. EVALUACION DE PROPOSICIONES LOGICAS
{sub_sep}
P (Presion alterada)       : {P}
Q (Frecuencia cardiaca anor): {Q}
R (Oxigenacion < 92%)      : {R}
S (Fiebre o Tos)           : {S}
T (Dolor toracico/disnea)  : {T}
U (IMC fuera de rango)     : {U}

{sub_sep}
4. DICTAMEN Y AGENDAMIENTO
{sub_sep}
Nivel de Prioridad: {prioridad}
Modalidad Asignada: {modalidad}
Fecha de Cita     : {dia_cita}
Hora Asignada     : {hora_cita}
Especialidad      : {especialidad}
Motivo / Remision : {motivo}

{sep}
Por favor presentarse 15 minutos antes con su identificacion oficial.
{sep}"""

        self.txt_comprobante.delete("1.0", tk.END)
        self.txt_comprobante.insert("1.0", texto_resumen)


if __name__ == "__main__":
    root = tk.Tk()
    app = TriajeMedicoApp(root)
    root.mainloop()