import ollama
import re

deepseek_model = 'deepseek-r1:8b'

def tell_deepseek(input_question: str):
    
    response = ollama.chat(model=deepseek_model, messages=[
    {
        'role': 'user',
        'content': input_question
    }
])

    ollama_response = response['message']['content']
    clean_response = re.sub(r'<think>.*?</think>', '', ollama_response, flags=re.DOTALL)

    return clean_response
