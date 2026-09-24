from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI


def get_chat_response(prompt, memory, openai_api_key, openai_api_base_url):
    model = ChatOpenAI(model="gpt-5.2", api_key=openai_api_key, base_url=openai_api_base_url)
    chain = ConversationChain(llm=model, memory=memory)

    response = chain.invoke({"input": prompt})

    return response["response"]