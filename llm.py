import os
os.environ["OPENAI_API_TYPE"] = "azure"
os.environ["OPENAI_API_VERSION"] = "2023-05-15"
os.environ["OPENAI_API_BASE"] = "https://chatlogo.openai.azure.com"
os.environ["OPENAI_API_KEY"] = os.environ['OPENAI_API_KEY']

def get_openai():
    from langchain.llms import AzureOpenAI
    llm = AzureOpenAI(
        deployment_name="davinci-003",
        max_tokens=2000,
        temperature=0.2
    )
    return llm
