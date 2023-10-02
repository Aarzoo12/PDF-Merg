import PyPDF2

pdf_files=["1.pdf","2.pdf"]
merger=PyPDF2.PdfMerger()

for file in pdf_files:
        pdf_file=open(file, 'rb') 
        pdfReader=PyPDF2.PdfReader(pdf_file)
        merger.append(pdfReader)

pdf_file.close()
merger.write('merge.pdf')