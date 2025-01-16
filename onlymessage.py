from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage,SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
load_dotenv()


#region Model name and creativity
MODEL_NAME = "gpt-4"
TEMPERATURE = 0.1

model = ChatOpenAI(
    model=MODEL_NAME,
    temperature=TEMPERATURE
)
#endregion

#region System and Human Prompt
#SYSTEM_PROMPT = "Translate the following from English to Spanish"
#HUMAN_PROMPT = "Hi!"
#messages = [
#   SystemMessage(content = TRANSLATION_PROMPT),
#   HumanMessage(content = HUMAN_PROMPT)
#]
#endregion

#region DYNAMIC !!  System and Human Prompt
system_prompt = "Translate the following into {language}"
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system",system_prompt) , ("user", "{text}")
    ]
)
#endregion


parser = StrOutputParser()
chain = prompt_template | model | parser

if __name__ == "__main__":

    print(chain.invoke({"language" : "italian", "text" : "Hello World"}))