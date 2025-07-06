"""
Importing the required libraries
"""

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.document_loaders import DirectoryLoader, TextLoader, PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

# loading the environment variables
load_dotenv()

"""
the functions get_retriever function checks for if there is any existing index i.e. a vector database present in the directory and uses that for more insights.
the function generate report uses the prompt, rag index to generate the report in a soft and devotional tone with more insights.
"""

def get_retriever(doc_folder="./docs", faiss_dir="faiss_index"):
    # print("inside the retriever")
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    faiss_index_file = os.path.join(faiss_dir, "index.faiss")
    store_file = os.path.join(faiss_dir, "index.pkl")

    if os.path.exists(faiss_index_file) and os.path.exists(store_file):
        print("using the persisted FAISS index")
        vectordb = FAISS.load_local(faiss_dir, embeddings, allow_dangerous_deserialization=True)
    else:
        # print("creating the FAISS index")
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
        print("FAISS index created and persisted")
    retriever = vectordb.as_retriever()
    return retriever

def generate_report(prompt, use_rag=True, top_k=3):
    groq_api_key = os.environ["GROQ_API_KEY"]
    llm = ChatGroq(
        groq_api_key=groq_api_key,
        model_name="meta-llama/llama-4-maverick-17b-128e-instruct",
        temperature=0.3,
        max_tokens=1024
    )
    system_prompt = "You are a spiritual guru/guide in Hindu faith."
    context = ""
    if use_rag:
        retriever = get_retriever()
        relevant_docs = retriever.get_relevant_documents(prompt)[:top_k]
        context = "\n\n".join([doc.page_content for doc in relevant_docs])
    full_prompt = f"{system_prompt}\n\nContext:\n{context}\n\nUser Query:\n{prompt}"
    response = llm.invoke(full_prompt)
    # Only return the generated text, not metadata
    if hasattr(response, 'content'):
        return response.content
    elif isinstance(response, dict) and 'content' in response:
        return response['content']
    elif isinstance(response, str):
        return response
    else:
        return str(response)