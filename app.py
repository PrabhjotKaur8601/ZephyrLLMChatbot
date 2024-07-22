import gradio as gr
from huggingface_hub import InferenceClient
from typing import List, Tuple
import fitz  # PyMuPDF
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

client = InferenceClient("HuggingFaceH4/zephyr-7b-beta")

class MyApp:
    def __init__(self) -> None:
        self.documents = []
        self.embeddings = None
        self.index = None
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.load_pdf("OSHA3317first-aid.pdf")
        self.build_vector_db()

    def load_pdf(self, file_path: str) -> None:
        doc = fitz.open(file_path)
        self.documents = []
        for page_num in range(len(doc)):
            page = doc[page_num]
            text = page.get_text()
            self.documents.append({"page": page_num + 1, "content": text})
        print("PDF processed successfully!")

    def build_vector_db(self) -> None:
        self.embeddings = self.model.encode([doc["content"] for doc in self.documents])
        self.index = faiss.IndexFlatL2(self.embeddings.shape[1])
        self.index.add(np.array(self.embeddings))
        print("Vector database built successfully!")

    def search_documents(self, query: str, k: int = 3) -> List[str]:
        query_embedding = self.model.encode([query])
        D, I = self.index.search(np.array(query_embedding), k)
        results = [self.documents[i]["content"] for i in I[0]]
        return results if results else ["No relevant information found."]

app = MyApp()

def respond(message: str, history: List[Tuple[str, str]]):
    system_message = """You are a knowledgeable AI assistant specializing in workplace first aid, drawing information from the provided Fundamentals of a Workplace First-Aid Program materials. You can provide clear and concise explanations of first aid procedures, emergency response protocols, and legal requirements related to workplace injuries. You can also generate practical scenarios and answer hypothetical questions about first aid situations. Always refer to the provided materials to ensure accuracy and relevance in your responses."""
    messages = [{"role": "system", "content": system_message}]

    for user, assistant in history:
        messages.append({"role": "user", "content": user})
        messages.append({"role": "assistant", "content": assistant})

    messages.append({"role": "user", "content": message})

    # RAG - Retrieve relevant documents
    retrieved_docs = app.search_documents(message)
    context = "\n".join(retrieved_docs)
    messages.append({"role": "system", "content": "Relevant information: " + context})

    full_response = ""
    for message in client.chat_completion(
        messages,
        max_tokens=500,
        stream=True,
        temperature=0.7,
        top_p=0.9,
    ):
        token = message.choices[0].delta.content
        if token:
            full_response += token

    yield full_response

demo = gr.Blocks()

with demo:
    gr.Markdown(
        """‼️Disclaimer: This guide provides educational information on workplace first-aid. It is not a substitute for professional medical advice, training, or local regulations. We are not responsible for any injuries,losses, or damages resulting from its use. Always seek professional medical guidance and adhere to relevant laws.‼️"""
    )
    
    chatbot = gr.ChatInterface(
        respond,
        examples=[
            ["How can I implement a workplace first-aid program?"],
            ["What are the essential components of a workplace first-aid program?"],
            ["Can employees be trained in first aid through the RAGBasedLLM program?"],
            ["How does a workplace first-aid program improve employee safety?"],
            ["What should be included in a workplace first-aid kit?"],
            ["What are the legal requirements for workplace first-aid?"],
            ["How can I ensure my workplace first-aid program is effective?"],
            ["What role do employees play in a workplace first-aid program?"]
        ],
        title='Fundamentals of a Workplace First-Aid Program Assistant 💊⚕️'
    )

if __name__ == "__main__":
    demo.launch()