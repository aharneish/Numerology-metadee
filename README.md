# Devotional Numerology App

This is a Streamlit web application that generates a personalized numerology report with spiritual insights. It uses RAG (Retrieval-Augmented Generation) with FAISS and Groq LLMs for enhanced, context-aware responses.

It takes in the input of your Full Name (First Name + Last Name (Surname)) and your Date of Birth in the format YYYY-MM-DD using which it calculates Life Path Number, Destiny/Expression Number and Soul Urge Number. The Destiny/Expression number, Life Path Number, Soul Urge Numbers are mapped to Deities which provide more insights into the personality of the user.

## Features
- Enter your full name and date of birth to receive a numerology profile and a devotional report.
- Supports both `.txt` and `.pdf` documents for RAG context.
- Beautiful, chat-like UI inspired by ChatGPT.
- Automated tests for numerology logic.

## Setup

1. **Clone the repository and install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Environment Variables:**
   - Set your Groq API key in a `.env` file:
     ```
     GROQ_API_KEY=your_groq_api_key_here
     ```

3. **Prepare Documents:**
   - Place your Hindu numerology and spiritual `.txt` or `.pdf` files in the `docs/` directory.

4. **Build the FAISS Index:**
   ```bash
   python create\ index.py
   ```

5. **Run the Streamlit App:**
   ```bash
   streamlit run app.py
   ```

6. **Run Tests:**
   ```bash
   python test_numerology.py
   ```

## File Structure
- `app.py` — Streamlit web app
- `numerology.py` — Numerology logic
- `llm_inference.py` — LLM and RAG pipeline
- `create index.py` — Helper to build the FAISS index
- `test_numerology.py` — Automated tests
- `docs/` — Folder for your knowledge base documents

## License
MIT
