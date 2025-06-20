import PyPDF2

class PDFHandler:
    """
    The class allows merging multiple PDF files into one and extracting text from PDFs using PyPDF2 library.
    """

    def __init__(self, filepaths):
        """
        Takes a list of file paths filepaths as a parameter.
        It creates a list named readers using PyPDF2, where each reader opens a file from the given paths.
        """
        self.filepaths = filepaths
        self.readers = [PyPDF2.PdfReader(fp) for fp in filepaths]

    def merge_pdfs(self, output_filepath):
        """
        Read files in self.readers which stores handles to multiple PDF files.
        Merge them to one pdf and update the page number, then save in disk.
        :param output_filepath: str, output file path to save to
        :return: str, "Merged PDFs saved at {output_filepath}" if successfully merged
        >>> handler = PDFHandler(['a.pdf', 'b.pdf'])
        >>> handler.merge_pdfs('out.pdf')
        Merged PDFs saved at out.pdf
        """
        # Create a PdfWriter object to write the merged PDF
        pdf_writer = PyPDF2.PdfWriter()

        # Iterate over each PdfReader object in self.readers
        for reader in self.readers:
            # Iterate over each page in the current PDF
            for page_num in range(len(reader.pages)):
                # Add each page to the PdfWriter object
                pdf_writer.add_page(reader.pages[page_num])

        # Write the merged PDF to the specified output file path
        with open(output_filepath, 'wb') as output_file:
            pdf_writer.write(output_file)

        return f"Merged PDFs saved at {output_filepath}"

    def extract_text_from_pdfs(self):
        """
        Extract text from pdf files in self.readers
        :return pdf_texts: list of str, each element is the text of one pdf file
        >>> handler = PDFHandler(['a.pdf', 'b.pdf'])
        >>> handler.extract_text_from_pdfs()
        ['Test a.pdf', 'Test b.pdf']
        """
        pdf_texts = []

        # Iterate over each PdfReader object in self.readers
        for reader in self.readers:
            pdf_text = ""
            # Iterate over each page in the current PDF
            for page_num in range(len(reader.pages)):
                # Extract text from each page and append it to pdf_text
                page = reader.pages[page_num]
                pdf_text += page.extract_text()

            # Append the extracted text of the current PDF to pdf_texts list
            pdf_texts.append(pdf_text)

        return pdf_texts