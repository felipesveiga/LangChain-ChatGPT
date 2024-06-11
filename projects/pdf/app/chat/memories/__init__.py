from app.chat.memories.sql_memory import build_memory
from langchain.memory import ConversationBufferMemory
from functools import partial

memory_map = {
    'sql_buffer_map':build_memory
}