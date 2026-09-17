# ============================================================
# SISTEMA DE DIAGNOSTICO DE EQUIPOS DE COMPUTO
# ============================================================

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import random


class SistemaDiagnosticoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Diagnostico de Equipos - Soporte Tecnico")
        self.root.geometry("820x760")
        self.root.minsize(780, 680)
        self.root.configure(bg="#f1f5f9")

        self.configurar_estilos()
        self.crear_interfaz()

    def configurar_estilos(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure(".", font=("Segoe UI", 10), background="#f1f5f9")
        style.configure("Header.TFrame", background="#1e293b")
        style.configure("Header.TLabel", background="#1e293b", foreground="#ffffff", font=("Segoe UI", 14, "bold"))
        style.configure("SubHeader.TLabel", background="#1e293b", foreground="#94a3b8", font=("Segoe UI", 9))
        
        style.configure("Card.TLabelframe", background="#ffffff", relief="flat")
        style.configure("Card.TLabelframe.Label", background="#ffffff", foreground="#0f172a", font=("Segoe UI", 10, "bold"))
        
        style.configure("Primary.TButton", font=("Segoe UI", 10, "bold"), background="#2563eb", foreground="#ffffff")
        style.map("Primary.TButton",
                  background=[("active", "#1d4ed8"), ("pressed", "#1e40af")])

        style.configure("Secondary.TButton", font=("Segoe UI", 9), background="#e2e8f0", foreground="#334155")
        style.map("Secondary.TButton",
                  background=[("active", "#cbd5e1"), ("pressed", "#94a3b8")])

    def crear_interfaz(self):
        header_frame = ttk.Frame(self.root, style="Header.TFrame", padding=15)
        header_frame.pack(fill="x", side="top")

        ttk.Label(header_frame, text="SISTEMA DE DIAGNOSTICO DE EQUIPOS DE COMPUTO", style="Header.TLabel").pack(anchor="w")
        ttk.Label(header_frame, text="Centro de Soporte Tecnico e Ingenieria de Redes - Evaluacion y Reporte", style="SubHeader.TLabel").pack(anchor="w")

        canvas = tk.Canvas(self.root, bg="#f1f5f9", highlightthickness=0)
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

        # 1. DATOS DEL USUARIO E HISTORIAL
        frame_usuario = ttk.LabelFrame(self.scrollable_frame, text="  1. Datos del Solicitante e Historial  ", style="Card.TLabelframe", padding=12)
        frame_usuario.pack(fill="x", pady=6)

        ttk.Label(frame_usuario, text="Nombre del Usuario:").grid(row=0, column=0, sticky="w", padx=5, pady=4)
        self.entry_nombre = ttk.Entry(frame_usuario, width=32)
        self.entry_nombre.grid(row=0, column=1, padx=5, pady=4)

        ttk.Label(frame_usuario, text="Telefono / Contacto:").grid(row=0, column=2, sticky="w", padx=5, pady=4)
        self.entry_contacto = ttk.Entry(frame_usuario, width=24)
        self.entry_contacto.grid(row=0, column=3, padx=5, pady=4)

        ttk.Label(frame_usuario, text="Direccion / Ubicacion:").grid(row=1, column=0, sticky="w", padx=5, pady=4)
        self.entry_direccion = ttk.Entry(frame_usuario, width=32)
        self.entry_direccion.grid(row=1, column=1, padx=5, pady=4)

        ttk.Label(frame_usuario, text="Es primer reporte?:").grid(row=1, column=2, sticky="w", padx=5, pady=4)
        self.var_primer_reporte = tk.StringVar(value="s")
        frame_primer = ttk.Frame(frame_usuario)
        frame_primer.grid(row=1, column=3, sticky="w", padx=5, pady=4)
        
        ttk.Radiobutton(frame_primer, text="Si (Nuevo)", value="s", variable=self.var_primer_reporte, command=self.toggle_previos).pack(side="left", padx=2)
        ttk.Radiobutton(frame_primer, text="No (Recurrente)", value="n", variable=self.var_primer_reporte, command=self.toggle_previos).pack(side="left", padx=2)

        ttk.Label(frame_usuario, text="Reportes previos:").grid(row=2, column=2, sticky="w", padx=5, pady=4)
        self.entry_previos = ttk.Entry(frame_usuario, width=10)
        self.entry_previos.insert(0, "0")
        self.entry_previos.config(state="disabled")
        self.entry_previos.grid(row=2, column=3, sticky="w", padx=5, pady=4)

        # 2. DATOS DEL EQUIPO
        frame_equipo = ttk.LabelFrame(self.scrollable_frame, text="  2. Informacion del Equipo  ", style="Card.TLabelframe", padding=12)
        frame_equipo.pack(fill="x", pady=6)

        ttk.Label(frame_equipo, text="Tipo de Equipo:").grid(row=0, column=0, sticky="w", padx=5, pady=4)
        self.combo_equipo = ttk.Combobox(frame_equipo, values=[
            "Computadora de escritorio (Desktop)",
            "Laptop / Portatil",
            "All in One (Todo en uno)",
            "Servidor / Estacion de Trabajo",
            "Otro"
        ], state="readonly", width=30)
        self.combo_equipo.current(1)
        self.combo_equipo.grid(row=0, column=1, padx=5, pady=4)

        ttk.Label(frame_equipo, text="Marca y Modelo:").grid(row=0, column=2, sticky="w", padx=5, pady=4)
        self.entry_modelo = ttk.Entry(frame_equipo, width=24)
        self.entry_modelo.insert(0, "Lenovo / Dell / HP...")
        self.entry_modelo.grid(row=0, column=3, padx=5, pady=4)

        # 3. CUESTIONARIO DE DIAGNOSTICO
        frame_diag = ttk.LabelFrame(self.scrollable_frame, text="  3. Evaluacion y Preguntas de Diagnostico  ", style="Card.TLabelframe", padding=12)
        frame_diag.pack(fill="x", pady=6)

        self.vars_preguntas = {
            "electricidad": tk.StringVar(value="s"),
            "enciende": tk.StringVar(value="s"),
            "video": tk.StringVar(value="s"),
            "pitidos": tk.StringVar(value="n"),
            "so": tk.StringVar(value="s"),
            "pantalla_azul": tk.StringVar(value="n"),
            "lento": tk.StringVar(value="n"),
            "red": tk.StringVar(value="n")
        }

        preguntas = [
            ("1. El equipo recibe alimentacion electrica / enciende LED?", "electricidad"),
            ("2. El equipo enciende (giran ventiladores o arranca)?", "enciende"),
            ("3. Muestra imagen en la pantalla (logotipo o texto)?", "video"),
            ("   - En caso de no dar video: Emite pitidos o LEDs de error?", "pitidos"),
            ("4. Inicia correctamente el Sistema Operativo?", "so"),
            ("   - En caso de no iniciar: Muestra pantalla azul o fallo de disco?", "pantalla_azul"),
            ("5. Presenta lentitud extrema, congelamientos o sobrecalentamiento?", "lento"),
            ("6. Presenta fallas continuas con la conexion a Internet / Wi-Fi?", "red"),
        ]

        for i, (texto, clave) in enumerate(preguntas):
            lbl = ttk.Label(frame_diag, text=texto)
            lbl.grid(row=i, column=0, sticky="w", padx=5, pady=3)
            
            f_rad = ttk.Frame(frame_diag)
            f_rad.grid(row=i, column=1, sticky="e", padx=5, pady=3)
            ttk.Radiobutton(f_rad, text="Si", value="s", variable=self.vars_preguntas[clave]).pack(side="left", padx=4)
            ttk.Radiobutton(f_rad, text="No", value="n", variable=self.vars_preguntas[clave]).pack(side="left", padx=4)

        # Botones de Accion
        frame_acciones = ttk.Frame(self.scrollable_frame, padding=10)
        frame_acciones.pack(fill="x", pady=6)

        btn_generar = ttk.Button(frame_acciones, text="Generar Diagnostico y Reporte", style="Primary.TButton", command=self.generar_reporte)
        btn_generar.pack(side="left", padx=6, ipady=4)

        btn_limpiar = ttk.Button(frame_acciones, text="Limpiar Campos", style="Secondary.TButton", command=self.limpiar_campos)
        btn_limpiar.pack(side="left", padx=6, ipady=4)

        # 4. REPORTE Y ESTADISTICAS
        frame_reporte = ttk.LabelFrame(self.scrollable_frame, text="  4. Reporte Oficial de Servicio y Estadisticas  ", style="Card.TLabelframe", padding=12)
        frame_reporte.pack(fill="both", expand=True, pady=6)

        self.txt_reporte = tk.Text(frame_reporte, height=18, width=88, font=("Consolas", 9), bg="#0f172a", fg="#f8fafc", relief="flat", padx=10, pady=10)
        self.txt_reporte.pack(fill="both", expand=True)

    def toggle_previos(self):
        if self.var_primer_reporte.get() == "s":
            self.entry_previos.config(state="normal")
            self.entry_previos.delete(0, tk.END)
            self.entry_previos.insert(0, "0")
            self.entry_previos.config(state="disabled")
        else:
            self.entry_previos.config(state="normal")
            self.entry_previos.delete(0, tk.END)
            self.entry_previos.insert(0, "1")

    def limpiar_campos(self):
        self.entry_nombre.delete(0, tk.END)
        self.entry_contacto.delete(0, tk.END)
        self.entry_direccion.delete(0, tk.END)
        self.var_primer_reporte.set("s")
        self.toggle_previos()
        self.combo_equipo.current(1)
        self.entry_modelo.delete(0, tk.END)
        self.entry_modelo.insert(0, "Lenovo / Dell / HP...")
        
        for k in self.vars_preguntas:
            if k in ["electricidad", "enciende", "video", "so"]:
                self.vars_preguntas[k].set("s")
            else:
                self.vars_preguntas[k].set("n")
        self.txt_reporte.delete("1.0", tk.END)

    def generar_reporte(self):
        nombre = self.entry_nombre.get().strip()
        if not nombre:
            messagebox.showwarning("Atencion", "Por favor ingrese el nombre del usuario.")
            return

        contacto = self.entry_contacto.get().strip() or "No especificado"
        direccion = self.entry_direccion.get().strip() or "No especificada"
        tipo_equipo = self.combo_equipo.get()
        modelo = self.entry_modelo.get().strip() or "Generico / No especificado"

        if self.var_primer_reporte.get() == "s":
            previos = 0
            tipo_usuario = "Nuevo Usuario (Primer Servicio)"
        else:
            try:
                previos = int(self.entry_previos.get().strip())
                if previos < 0:
                    previos = 0
            except ValueError:
                previos = 1
            tipo_usuario = f"Usuario Recurrente ({previos} previos)"

        total_reportes = previos + 1

        pruebas_totales = 0
        pruebas_ok = 0
        pruebas_fail = 0

        p = {k: self.vars_preguntas[k].get() == "s" for k in self.vars_preguntas}

        causas = []
        recomendaciones = []

        if not p["electricidad"]:
            pruebas_totales = 1
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
        elif not p["enciende"]:
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
        elif not p["video"]:
            pruebas_totales = 3
            pruebas_ok = 2
            pruebas_fail = 1
            if p["pitidos"]:
                diagnostico = "Fallo en el POST: Memoria RAM o GPU no detectada."
                causas = ["Modulos de memoria RAM sucios o danados", "Falla de tarjeta grafica/BIOS."]
            else:
                diagnostico = "Fallo de salida de senal de video o pantalla."
                causas = ["Cable HDMI/DisplayPort suelto", "Monitor apagado o display averiado."]
            severidad = "ALTA"
            tiempo = "2 - 3 horas"
            recomendaciones = [
                "Limpiar contactos de memoria RAM con goma suave y reconectar.",
                "Probar con una pantalla o cable de video externo verificado."
            ]
        elif not p["so"]:
            pruebas_totales = 4
            pruebas_ok = 3
            pruebas_fail = 1
            if p["pantalla_azul"]:
                diagnostico = "Error critico de disco / Archivos de arranque danados (BSOD)."
                causas = ["Sectores danados en SSD/HDD", "Corrupcion en particion EFI/MBR."]
            else:
                diagnostico = "Bucle de reinicio o bloqueo durante la carga del SO."
                causas = ["Actualizacion fallida o malware a nivel de sistema."]
            severidad = "MEDIA - ALTA"
            tiempo = "1 - 3 horas"
            recomendaciones = [
                "Verificar deteccion de disco en BIOS y ejecutar reparacion de inicio.",
                "Escaneo de salud SMART y reinstalacion de sistema operativo si se requiere."
            ]
        elif p["lento"]:
            pruebas_totales = 5
            pruebas_ok = 4
            pruebas_fail = 1
            diagnostico = "Degradacion del rendimiento por sobrecalentamiento o saturacion."
            severidad = "MEDIA"
            tiempo = "1 - 2 horas"
            causas = ["Pasta termica seca / polvo", "Disco saturado al 100% o exceso de programas."]
            recomendaciones = [
                "Mantenimiento fisico preventivo (limpieza interna y pasta termica).",
                "Optimizar aplicaciones de inicio y valorar migracion a SSD."
            ]
        elif p["red"]:
            pruebas_totales = 6
            pruebas_ok = 5
            pruebas_fail = 1
            diagnostico = "Problema de conectividad de red / Controladores de Wi-Fi/Ethernet."
            severidad = "BAJA"
            tiempo = "30 - 60 min"
            causas = ["Controlador de red desactualizado o configuracion DNS erronea."]
            recomendaciones = ["Restablecer configuracion de red y actualizar drivers de fabricante."]
        else:
            pruebas_totales = 6
            pruebas_ok = 6
            pruebas_fail = 0
            diagnostico = "Equipo en correcto funcionamiento en pruebas basicas e intermedias."
            severidad = "NORMAL"
            tiempo = "Inmediato"
            causas = ["Sin anomalias detectadas."]
            recomendaciones = ["Mantener respaldos frecuentes y programar servicio preventivo anual."]

        pct_exito = (pruebas_ok / pruebas_totales) * 100 if pruebas_totales > 0 else 100
        num_rep = f"REP-{random.randint(10000, 99999)}"
        fecha_act = datetime.now().strftime("%d/%m/%Y %H:%M")

        sep = "=" * 74
        sub_sep = "-" * 74

        reporte_str = f"""{sep}
              CENTRO DE SOPORTE TECNICO - REPORTE OFICIAL DE SERVICIO
{sep}
Folio de Reporte   : {num_rep}
Fecha y Hora       : {fecha_act}
Estado             : ABIERTO / EVALUADO

{sub_sep}
1. INFORMACION DEL SOLICITANTE Y METRICAS DE HISTORIAL
{sub_sep}
Nombre del Usuario : {nombre}
Contacto / Telefono: {contacto}
Direccion          : {direccion}
Perfil de Usuario  : {tipo_usuario}
Reportes Previos   : {previos} reporte(s)
Reporte Actual     : Reporte #{total_reportes} registrado en sistema

{sub_sep}
2. FICHA DEL EQUIPO
{sub_sep}
Tipo de Dispositivo: {tipo_equipo}
Marca y Modelo     : {modelo}

{sub_sep}
3. METRICAS Y ESTADISTICAS DEL DIAGNOSTICO
{sub_sep}
Total Evaluaciones : {pruebas_totales} pruebas realizadas
Pruebas Aprobadas  : {pruebas_ok} ({pct_exito:.1f}%)
Pruebas Fallidas   : {pruebas_fail}
Nivel de Severidad : {severidad}
Tiempo Estimado    : {tiempo}

{sub_sep}
4. DICTAMEN TECNICO Y RECOMENDACIONES
{sub_sep}
Diagnostico        : {diagnostico}

Posibles Causas:
"""
        for c in causas:
            reporte_str += f"  * {c}\n"

        reporte_str += "\nPlan de Accion Sugerido:\n"
        for r in recomendaciones:
            reporte_str += f"  -> {r}\n"

        reporte_str += f"""
{sep}
                  FIN DEL INFORME - ID: {num_rep}
{sep}"""

        self.txt_reporte.delete("1.0", tk.END)
        self.txt_reporte.insert("1.0", reporte_str)


if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaDiagnosticoApp(root)
    root.mainloop()