
# --- Helper script to build and persist the FAISS index for RAG ---
import os
from langchain_community.document_loaders import DirectoryLoader, TextLoader, PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

def build_faiss_index(doc_folder="./docs", faiss_dir="faiss_index"):
    """
    Build and persist the FAISS index from documents. Run this ONCE before main workflow.
    Scans the docs/ folder for .txt and .pdf files, embeds them, and saves the FAISS index.
    """
    print("Building FAISS index...")
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    # Load .txt files
    txt_loader = DirectoryLoader(doc_folder, glob="*.txt", loader_cls=TextLoader)
    txt_docs = txt_loader.load()
    # Load .pdf files
    pdf_docs = []
    for filename in os.listdir(doc_folder):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(doc_folder, filename)
            try:
                pdf_loader = PyPDFLoader(pdf_path)
                pdf_docs.extend(pdf_loader.load())
            except Exception as e:
                print(f"Warning: Could not load {pdf_path}: {e}")
    docs = txt_docs + pdf_docs
    if not docs:
        raise ValueError(f"No .txt or .pdf documents found in {doc_folder}. Please add at least one supported file.")
    vectordb = FAISS.from_documents(docs, embeddings)
    vectordb.save_local(faiss_dir)
    print(f"FAISS index created and persisted in {faiss_dir}")


# Run this script directly to build the index
if __name__ == "__main__":
    build_faiss_index()