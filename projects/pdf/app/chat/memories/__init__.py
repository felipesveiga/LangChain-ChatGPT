from app.chat.memories.sql_memory import build_memory
from app.chat.memories.window_memory import window_buffer_memory_builder
from langchain.memory import ConversationBufferMemory
from functools import partial

memory_map = {
    'sql_buffer_memory':build_memory,
    'sql_window_memory':window_buffer_memory_builder
}