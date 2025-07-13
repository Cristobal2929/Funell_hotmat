from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Mentalidad del Exito', ln=True, align='C')
        self.ln(5)

    def chapter_title(self, num, label):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, f'Paso {num}: {label}', ln=True)
        self.ln(3)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 8, body)
        self.ln()

pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

pdf.set_font('Arial', '', 12)
intro = (
    "Felicidades por dar el primer paso hacia tu exito! Esta guia esta disenada "
    "para ayudarte a entender y adoptar la mentalidad que tienen las personas que "
    "alcanzan sus suenos, sin importar las dificultades.\n"
)
pdf.multi_cell(0, 10, intro)

pasos = [
    ("Cambia tu dialogo interno", "La forma en que te hablas a ti mismo tiene un impacto enorme en tus resultados. Empieza a reemplazar pensamientos negativos por afirmaciones positivas. Ejemplo: Cambia 'No puedo hacerlo' por 'Voy a aprender y mejorar cada dia'."),
    ("Define metas claras y especificas", "El exito sin una meta clara es dificil. Escribe que quieres lograr y pon fechas para alcanzarlo."),
    ("Rodeate de personas positivas", "Las personas a tu alrededor influyen en tu mentalidad. Busca mentores, amigos y colegas que te inspiren y apoyen."),
    ("Aprende de los errores", "No temas fracasar. Cada error es una leccion que te acerca mas a tu objetivo."),
    ("Desarrolla disciplina diaria", "El exito es fruto de la constancia. Dedica al menos 15 minutos al dia a tus metas, sin excusas."),
    ("Visualiza tu exito", "Imaginate consiguiendo tus objetivos. Esta tecnica te prepara mentalmente y motiva tu accion."),
    ("Manten una actitud de gratitud", "Agradece lo que tienes y lo que vas logrando. Esto aumenta tu energia positiva y atrae mas oportunidades."),
]

for i, (titulo, texto) in enumerate(pasos, start=1):
    pdf.chapter_title(i, titulo)
    pdf.chapter_body(texto)

conclusion = (
    "Adoptar la mentalidad del exito es un proceso, pero con estos 7 pasos estaras "
    "en el camino correcto. Recuerda que el cambio comienza en tu mente.\n\n"
    "Si quieres profundizar y recibir tecnicas avanzadas para transformar tu mentalidad, "
    "te invito a conocer el ebook completo que ha ayudado a miles de personas a cambiar su vida:\n\n"
    "👉 Enlace de afiliado Hotmart"
)

pdf.multi_cell(0, 10, conclusion)

pdf.output("Mentalidad_del_Exito.pdf")

print("PDF creado: Mentalidad_del_Exito.pdf")
