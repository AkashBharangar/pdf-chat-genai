# 📄 PDF Chat with Groq (RAG System)

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![RAG](https://img.shields.io/badge/Architecture-RAG-purple.svg)
![LLM](https://img.shields.io/badge/LLM-Llama%203-orange.svg)
![Groq API](https://img.shields.io/badge/Inference-Groq%20API-red.svg)
![NLP](https://img.shields.io/badge/NLP-Document%20QA-green.svg)
![GenAI](https://img.shields.io/badge/GenAI-Project-blueviolet.svg)
![Status](https://img.shields.io/badge/Status-Active%20Learning-brightgreen.svg)

A beginner-friendly **Retrieval-Augmented Generation (RAG)** project that allows users to chat with the contents of a PDF document using the **Groq API** and **Llama 3**.

This project demonstrates the fundamental concepts behind modern GenAI applications:

- PDF text extraction
- Text chunking
- Context retrieval
- Prompt engineering
- Retrieval-Augmented Generation (RAG)

---

## 🚀 Features

- Upload and process PDF files
- Extract text using `pypdf`
- Split documents into manageable chunks
- Retrieve relevant chunks based on user questions
- Send retrieved context to a Groq-hosted LLM
- Interactive command-line chat experience

---

## 🏗️ Project Architecture

```text
User uploads PDF
        │
        ▼
Extract Text (PyPDF)
        │
        ▼
Chunk Text
        │
        ▼
Store Chunks in Memory
        │
        ▼
User Question
        │
        ▼
Retrieve Relevant Chunks
        │
        ▼
Send Context + Question to Groq LLM
        │
        ▼
Generate Answer
```

---

## 📂 Project Structure

```text
pdf-chat-genai/
│
├── app.py
├── pdf_loader.py
├── chunker.py
├── rag_engine.py
├── .env
├── requirements.txt
└── README.md
```

---

## 🛠️ Tech Stack

| Component | Technology |
|------------|------------|
| LLM | Groq API |
| Model | Llama 3 |
| PDF Processing | PyPDF |
| Environment Variables | python-dotenv |
| Language | Python |

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/pdf-chat-genai.git
cd pdf-chat-genai
```

### 2. Create Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install pypdf groq python-dotenv
```

---

## 🔑 Environment Setup

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

Get your API key from the Groq Console.

---

## ▶️ Running the Project

Start the application:

```bash
python app.py
```

Example:

```text
Enter PDF path: sample.pdf

📄 Extracting text...
✂️ Chunking text...
✅ Total chunks created: 25

Ask a question:
What is this document about?
```

---

## 🧠 Concepts Learned

This project covers several important GenAI concepts:

### 1. PDF Processing

Extracting raw text from PDF documents using PyPDF.

### 2. Chunking

Breaking large documents into smaller pieces that fit within LLM context windows.

### 3. Retrieval

Finding the most relevant chunks for a user query.

### 4. Context Injection

Providing retrieved chunks as context to the language model.

### 5. RAG (Retrieval-Augmented Generation)

Combining retrieval and generation to answer questions from custom documents.

---

## ⚙️ Current Retrieval Method

The project currently uses a simple keyword-overlap scoring system:

```python
score = len(query_words.intersection(chunk_words))
```

This keeps the implementation easy to understand while demonstrating the retrieval workflow.

---

## 🚀 Future Improvements

Possible upgrades:

- Vector embeddings
- Semantic search
- FAISS integration
- ChromaDB integration
- Streamlit UI
- Multi-PDF support
- Chat history
- Source citations
- Metadata filtering
- Hybrid search

---

## 📚 Learning Outcomes

After completing this project, you will understand:

- How RAG systems work
- How to process PDF documents
- Why chunking is important
- How retrieval improves LLM responses
- How to integrate Groq APIs into GenAI applications

---

## 🖼️ Example Workflow

```text
PDF → Text Extraction
      ↓
Chunking
      ↓
Retrieval
      ↓
Context Injection
      ↓
Groq LLM
      ↓
Answer Generation
```

---

## 🤝 Contributing

Feel free to fork the repository, create improvements, and submit pull requests.

---

## 📄 License

This project is open-source and available under the MIT License.

---

## ⭐ Acknowledgements

- Groq for fast LLM inference
- Llama 3 models
- PyPDF for PDF text extraction

---

### Author

Built as a learning project while exploring Retrieval-Augmented Generation (RAG) and Generative AI application development.
