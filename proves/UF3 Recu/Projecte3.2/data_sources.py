

LISTA = ["palabra1", "palabra2", "palabra3", ...]

def get_data_from_keyboard():
    """Obtiene datos desde el teclado."""
    oracion = input("Introduce una oración: ")
    return oracion

def get_data_from_chatgpt():
    """Obtiene datos de ChatGPT usando la API de OpenAI."""
    # Asigna tu API key
    openai.api_key = "ug37mn6QegzJ8J3q0oBz3A==vESsyPdBHLLNWS6p"

    # Define los parámetros
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
    """Obtiene datos de un servidor utilizando una URL."""
    api_url = 'https://api.api-ninjas.com/v1/urllookup?url={}'.format(url)
    response = requests.get(api_url, headers={'X-Api-Key': 'ug37mn6QegzJ8J3q0oBz3A==vESsyPdBHLLNWS6p'})
    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print("Error:", response.status_code, response.text)
