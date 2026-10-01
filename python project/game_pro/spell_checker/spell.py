from langchain_groq import ChatGroq
from rich import print
from rich.console import Console #rick=package..console=module..console k ander console class h 
from rich.markdown import Markdown #rick=package..markdown=module..markdown k ander markdown class h 



def getmodel():
    return ChatGroq(model='openai/gpt-oss-120b',api_key=key)


def spell_checker():
    con = Console()
    text = input("Enter the text ...")
    llm=getmodel()
    res =llm.invoke(f"give me all incorrect spelling in the given text {text}")
    print(res)
