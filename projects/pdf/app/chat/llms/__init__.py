from functools import partial
from app.chat.llms.chatopenai import build_llm

llm_configs = ['gpt-4', 'gpt-3.5-turbo']
llm_map = {
    model_name:partial(build_llm, model_name=model_name) for model_name in llm_configs
}