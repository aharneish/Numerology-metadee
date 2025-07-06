# Devotional Numerology App


This is a Streamlit web application that generates a personalized numerology report with spiritual insights. It uses RAG (Retrieval-Augmented Generation) with FAISS and Groq LLMs for enhanced, context-aware responses.

**Numerology Calculations:**
- **Life Path Number:** Calculated from your date of birth (DOB).
- **Destiny Number:** Also calculated from your DOB.
- **Soul Urge Number:** Calculated from the vowels in your full name.

All numbers are mapped to relevant Hindu deities for deeper spiritual context. Master numbers (11, 22, 33) are handled appropriately.

## Features
- Enter your full name and date of birth to receive a numerology profile and a devotional report.
- Destiny number is calculated from DOB (not name).
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
- `numerology.py` — Numerology logic (Life Path, Destiny, Soul Urge calculations; Destiny uses DOB)
- `llm_inference.py` — LLM and RAG pipeline
- `create index.py` — Helper to build the FAISS index
- `test_numerology.py` — Automated tests
- `samplereport.txt` — Sample evaluation profile and checklist
- `docs/` — Folder for your knowledge base documents
