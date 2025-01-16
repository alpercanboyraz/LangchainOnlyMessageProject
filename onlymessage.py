from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain_core.messages import HumanMessage,SystemMessage

load_dotenv()

model = ChatOpenAI(
    model="gpt-4", temperature = 0.1)

TRANSLATION_PROMPT = "Translate the following from English to Spanish"

messages = [
    SystemMessage(content = TRANSLATION_PROMPT),
    HumanMessage(content = "Hi!")
]

if __name__ == "__main__":
    response = model.invoke(messages)
    print(response)