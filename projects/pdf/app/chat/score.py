from app.chat.redis import client
from typing import List, Dict, Callable, Literal

def _hincrby(names:List[str], resources:List[str], score:int)->None:
    '''
        Function that updates the scores of all resources of a certain chat.

        Parameters
        ----------
        `names`: List[str]
            A list with the prefix of the tables names.
        `resources`: List[str]
            A list with the name of the resources used in the conversation.
        `score`: int
            The score assigned to the conversation.
    '''
    score = min(max(score, 0), 1)
    for name, resource in zip(names, resources):
        client.hincrby(f'{name}_score_values', resource, score)
        client.hincrby(f'{name}_score_counts', resource, 1)
         

def score_conversation(
    conversation_id: str, score: float, llm: str, retriever: str, memory: str
) -> None:
    """
    This function interfaces with langfuse to assign a score to a conversation, specified by its ID.
    It creates a new langfuse score utilizing the provided llm, retriever, and memory components.
    The details are encapsulated in JSON format and submitted along with the conversation_id and the score.

    :param conversation_id: The unique identifier for the conversation to be scored.
    :param score: The score assigned to the conversation.
    :param llm: The Language Model component information.
    :param retriever: The Retriever component information.
    :param memory: The Memory component information.

    Example Usage:

    score_conversation('abc123', 0.75, 'llm_info', 'retriever_info', 'memory_info')
    """
    names, resources = ['llm', 'retriever', 'memory'], [llm, retriever, memory]
    _hincrby(names, resources, score)

def get_scores():
    """
    Retrieves and organizes scores from the langfuse client for different component types and names.
    The scores are categorized and aggregated in a nested dictionary format where the outer key represents
    the component type and the inner key represents the component name, with each score listed in an array.

    The function accesses the langfuse client's score endpoint to obtain scores.
    If the score name cannot be parsed into JSON, it is skipped.

    :return: A dictionary organized by component type and name, containing arrays of scores.

    Example:

        {
            'llm': {
                'chatopenai-3.5-turbo': [score1, score2],
                'chatopenai-4': [score3, score4]
            },
            'retriever': { 'pinecone_store': [score5, score6] },
            'memory': { 'persist_memory': [score7, score8] }
        }
    """

    pass

def random_component_by_score(component_type:Literal['llm', 'retriever', 'memory'], component_map:Dict[str, Callable]):
    if component_type not in ['llm', 'retriever', 'memory']:
        raise ValueError('Invalid Component Type')
    
    values = client.hgetall(f'{component_type}_score_values')
    counts = client.hgetall(f'{component_type}_score_counts')

    # TODO
    # Fazer uma função que converta os valores dos dicionários em integer!