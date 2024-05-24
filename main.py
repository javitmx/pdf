from flask import Flask, render_template, request, send_file
from fpdf import FPDF

app = Flask(__name__)

# Ruta para el formulario HTML


@app.route('/')
def index():
    return render_template('form.html')

# Ruta para procesar el formulario y generar el PDF


@app.route('/generate_pdf', methods=['POST'])
def generate_pdf():
    # Obtener datos del formulario
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    edad = request.form['edad']
    celular = request.form['celular']

    # Crear el archivo PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Información Personal", ln=True, align="C")
    pdf.cell(200, 10, txt="", ln=True, align="C")
    pdf.cell(200, 10, txt=f"Nombre: {nombre}", ln=True, align="L")
    pdf.cell(200, 10, txt=f"Apellido: {apellido}", ln=True, align="L")
    pdf.cell(200, 10, txt=f"Edad: {edad}", ln=True, align="L")
    pdf.cell(200, 10, txt=f"Número de Celular: {celular}", ln=True, align="L")

    # Guardar el archivo PDF en el servidor
    pdf_file = "informacion_personal.pdf"
    pdf.output(pdf_file)

    # Enviar el archivo PDF como respuesta
    return send_file(pdf_file, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
