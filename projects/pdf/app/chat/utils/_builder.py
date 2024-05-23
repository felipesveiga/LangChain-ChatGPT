from app.chat.llms import llm_map, build_llm
from app.chat.vectorstore import retriever_map, build_retriever
from app.chat.memories import memory_map, build_memory
from random import choice
from app.web.api import (
    get_conversation_components,
    set_conversation_components
)
from app.chat.models import ChatArgs
from typing import Callable, Tuple

def _builder_return(chat_args:ChatArgs, llm:str, retriever:str, memory:str)->Tuple[Callable]:
    mappers = [llm_map, retriever_map, memory_map]
    args = [llm, retriever, memory]
    return (mapper[arg](chat_args) for mapper, arg in zip(mappers, args))

def _builder(chat_args:ChatArgs)->Tuple[Callable]:
    conversation_id = chat_args.conversation_id
    components = get_conversation_components(conversation_id)

    if components['llm']:
        llm, retriever, memory = components['llm'], components['retriever'], components['memory']
    else:
        llm, retriever, memory = choice(list(llm_map.keys())), choice(list(retriever_map.keys())), choice(list(memory_map.keys()))
        set_conversation_components(conversation_id, llm, retriever, memory)
    return _builder_return(chat_args, llm, retriever, memory)