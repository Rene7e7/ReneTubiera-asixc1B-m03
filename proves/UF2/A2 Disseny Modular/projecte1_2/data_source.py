import openai
import requests

def get_data_from_keyboard():
    oracion = input("Introduce una oración: ")
    return oracion
def get_data_from_chatgpt():
    # Asigna tu API key
    openai.api_key = "sk-proj-cEVwDKd2xjY55H6vfLU8T3BlbkFJc8yC72zjetWbX1ZtQo8Z"

    # Define los parámetTros
    ENGINE = "gpt-3.5-turbo-instruct"
    ANSWER_QUANTITY = 1
    MAX_TOKENS = 2000
    # Pregunta 1
    question = "Què és ChatGPT?"
    print(f"Asking question: {question}")
    completion = openai.Completion.create(engine=ENGINE, prompt=question, n=ANSWER_QUANTITY, max_tokens=MAX_TOKENS)
    print(completion.choices[0].text.strip())

    # Pregunta 2
    question = "Què significa GPT de ChatGPT?"
    print(f"Asking question: {question}")
    completion = openai.Completion.create(engine=ENGINE, prompt=question, n=ANSWER_QUANTITY, max_tokens=MAX_TOKENS)
    print(completion.choices[0].text.strip())

def get_data_from_server(url):
    import requests

    url = 'example.com'
    api_url = 'https://api.api-ninjas.com/v1/urllookup?url={}'.format(url)
    response = requests.get(api_url, headers={'X-Api-Key': 'ug37mn6QegzJ8J3q0oBz3A==vESsyPdBHLLNWS6p'})
    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print("Error:", response.status_code, response.text)


