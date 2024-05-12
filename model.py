import PyPDF2

# ** Extração do texto para depois fazer a transformação para voz **

class PDFData:
    def __init__(self, file_path):
        self.file_path = file_path
        self.text = self._extract_text()

    def _extract_text(self):
        with open(self.file_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            return ''.join(page.extract_text() for page in pdf_reader.pages)