from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the question below.
Here is the conversation history: {context}
Question: {question}
Answer:
"""

model = OllamaLLM(model="llama3", format="json")  # Explicit format
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation():
    context = ""
    print("Welcome to the AI ChatBot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        # Debug: Inspect inputs to invoke
        print(f"DEBUG - Inputs: {{'context': context, 'question': user_input}}")

        try:
            result = chain.invoke({"context": context, "question": user_input})
            print("Bot: ", result)
            context += f"\nUser: {user_input}\nAI: {result}"
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    handle_conversation()
