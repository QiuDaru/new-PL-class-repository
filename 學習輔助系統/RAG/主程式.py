from docx import Document

def read_word_documents(file_paths):
    documents = []
    for file_path in file_paths:
        doc = Document(file_path)
        full_text = []
        for paragraph in doc.paragraphs:
            full_text.append(paragraph.text)
        documents.append("\n".join(full_text))
    return documents

# 假設有一些 Word 文檔的路徑
file_paths = ["document1.docx", "document2.docx", "document3.docx"]
documents = read_word_documents(file_paths)

