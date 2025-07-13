from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

def crear_pdf(nombre_archivo):
    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    width, height = letter

    text = c.beginText()
    text.setTextOrigin(inch, height - inch)
    text.setFont("Helvetica-Bold", 18)
    text.textLine("Mentalidad del Éxito")

    text.moveCursor(0, 20)
    text.setFont("Helvetica", 12)

    contenido = [
        "Felicidades por dar el primer paso hacia tu éxito! Esta guía está diseñada para ayudarte a entender",
        "y adoptar la mentalidad que tienen las personas que alcanzan sus sueños, sin importar las dificultades.",
        "",
        "Paso 1: Cambia tu diálogo interno",
        "La forma en que te hablas a ti mismo tiene un impacto enorme en tus resultados. Empieza a reemplazar",
        "pensamientos negativos por afirmaciones positivas. Ejemplo: Cambia “No puedo hacerlo” por “Voy a aprender y mejorar cada día”.",
        "",
        "Paso 2: Define metas claras y específicas",
        "El éxito sin una meta clara es difícil. Escribe qué quieres lograr y pon fechas para alcanzarlo.",
        "",
        "Paso 3: Rodéate de personas positivas",
        "Las personas a tu alrededor influyen en tu mentalidad. Busca mentores, amigos y colegas que te inspiren y apoyen.",
        "",
        "Paso 4: Aprende de los errores",
        "No temas fracasar. Cada error es una lección que te acerca más a tu objetivo.",
        "",
        "Paso 5: Desarrolla disciplina diaria",
        "El éxito es fruto de la constancia. Dedica al menos 15 minutos al día a tus metas, sin excusas.",
        "",
        "Paso 6: Visualiza tu éxito",
        "Imagínate consiguiendo tus objetivos. Esta técnica te prepara mentalmente y motiva tu acción.",
        "",
        "Paso 7: Mantén una actitud de gratitud",
        "Agradece lo que tienes y lo que vas logrando. Esto aumenta tu energía positiva y atrae más oportunidades.",
        "",
        "Adoptar la mentalidad del éxito es un proceso, pero con estos 7 pasos estarás en el camino correcto.",
        "Recuerda que el cambio comienza en tu mente.",
        "",
        "Si quieres profundizar y recibir técnicas avanzadas para transformar tu mentalidad, te invito a conocer",
        "el ebook completo que ha ayudado a miles de personas a cambiar su vida:",
        "",
        "👉 Enlace de afiliado Hotmart"
    ]

    for line in contenido:
        text.textLine(line)

    c.drawText(text)
    c.showPage()
    c.save()

crear_pdf("Mentalidad_del_Exito_ReportLab.pdf")
print("PDF creado: Mentalidad_del_Exito_ReportLab.pdf")
