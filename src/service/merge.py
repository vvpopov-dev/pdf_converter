import os
import tempfile

from io import BytesIO
from PyPDF2 import PdfMerger



def merge_pdf(*pdf_files, user_id: int):
    merger = PdfMerger()

    for file in pdf_files:
        merger.append(file)

    pdf_bytes = BytesIO()
    merger.write(pdf_bytes)
    merger.close()

    pdf_bytes.seek(0)

    return pdf_bytes
