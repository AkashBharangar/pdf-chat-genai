from dotenv import load_dotenv
load_dotenv()

from pdf_loader import extract_text_from_pdf
from chunker import chunk_text
from rag_engine import retrieve_relevant_chunks, get_answer

def main():
    pdf_path = input("Enter PDF path: ")

    print("\n📄 Extracting text...")
    text = extract_text_from_pdf(pdf_path)
    print("\n text \n" + text)

    print("✂️ Chunking text...")
    chunks = chunk_text(text)
    print("\n Chunks \n", chunks)

    print(f"✅ Total chunks created: {len(chunks)}")

    while True:
        query = input("\nAsk a question (or type 'exit'): ")

        if query.lower() == "exit" or query == "":
            break

        print("\n🔎 Retrieving relevant chunks...")
        relevant_chunks = retrieve_relevant_chunks(query, chunks)
        print("\n relevant_chunks \n", relevant_chunks)
        

        print("🤖 Generating answer...\n")
        answer = get_answer(query, relevant_chunks)

        print("Answer:\n", answer)

if __name__ == "__main__":
    main()