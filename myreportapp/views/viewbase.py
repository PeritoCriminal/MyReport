import base64
from io import BytesIO
from docx import Document
from docx.shared import Cm, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

# Variável global para contar as imagens
img_label = 0

def insert_image_from_base64_to_docx(doc, base64_string, label, num_img, width_cm=12):
    global img_label  # Declarar a variável como global

    if not base64_string:
        return num_img

    try:
        # Remove o prefixo 'data:image/png;base64,' ou similar, se existir
        if ';base64,' in base64_string:
            base64_string = base64_string.split(';base64,')[1]

        # Decodifica a string Base64 em bytes
        image_data = base64.b64decode(base64_string)

        # Salva a imagem temporariamente em um objeto BytesIO
        image_stream = BytesIO(image_data)

        # Insere um parágrafo e adiciona a imagem a ele
        paragraph = doc.add_paragraph()  # Cria um novo parágrafo
        run = paragraph.add_run()         # Adiciona um run ao parágrafo
        run.add_picture(image_stream, width=Cm(width_cm))  # Adiciona a imagem
        paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER  # Centraliza o parágrafo que contém a imagem

        paragraph_format = paragraph.paragraph_format
        paragraph_format.space_after = Pt(0)
        paragraph_format.keep_with_next = True

        num_img += 1;
        img_label += 1  # Incrementa a contagem de imagens
        legenda = f'Imagem {num_img} - {label}'

        caption_paragraph = doc.add_paragraph()
        caption_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

        caption_format = caption_paragraph.paragraph_format
        caption_format.space_before = Pt(0)
        
        # Adiciona a legenda como um run com formatação
        caption_run = caption_paragraph.add_run(legenda)
        caption_run.italic = True  # Define o texto como itálico
        caption_run.font.size = Pt(11) 

        return num_img

    except Exception as e:
        return f"An error occurred: {e}"