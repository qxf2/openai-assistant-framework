"""
This script provides methods for creating, listing, retrieving, 
and deleting assistants using the OpenAI API. 
"""
from openai import OpenAI
from .api_exception_handler import assistant_exception_handler


class AssistantManager:
    """
    A class for managing OpenAI assistants.

    Args:
        client (OpenAI): An instance of the OpenAI class used for making API requests.
        model (str, optional): The model to be used for the assistants.
        Defaults to "gpt-4-1106-preview".
    """

    def __init__(self, api_key: str, model: str = "gpt-4-1106-preview"):
        """
        Initializes the AssistantManager instance with the provided API key and model.

        Args:
            api_key (str): The API key for accessing OpenAI services.
            model (str, optional): The model to be used for the assistants.
            Defaults to "gpt-4-1106-preview".
        """
        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.assistant = None
        self.thread = None
        self.run = None

    @assistant_exception_handler
    def create_assistant(self, name, instructions, tools):
        """
        Creates a new assistant with the given name, instructions, and tools.
        Args:
            name (str): The name of the assistant.
            instructions (str): The instructions for the assistant.
            tools (list): The list of tools for the assistant.
        Returns:
            dict: The created assistant object.
        """
        assistant = self.client.beta.assistants.create(
            name=name, instructions=instructions, tools=tools, model=self.model
        )
        return assistant

    @assistant_exception_handler
    def list_assistants(self):
        """
        Lists all the assistants.
        Returns:
            list: The list of assistants.
        """
        assistants_list = self.client.beta.assistants.list(order="desc", limit="10")
        return assistants_list.data

    @assistant_exception_handler
    def retrieve_assistant(self, assistant_id):
        """
        Retrieves an assistant by its ID.
        Args:
            assistant_id (str): The ID of the assistant.
        Returns:
            dict: The retrieved assistant object.
        """
        retrieved_assistant = self.client.beta.assistants.retrieve(
            assistant_id=assistant_id
        )
        return retrieved_assistant

    @assistant_exception_handler
    def retrieve_assistant_using_name(self, assistant_name):
        """
        Retrieves an assistant by its name.
        Args:
            assistant_name (str): The name of the assistant.
        Returns:
            dict: The retrieved assistant object.
        """
        available_assistant = self.client.beta.assistants.retrieve(
            assistant_name=assistant_name
        )
        return available_assistant

    @assistant_exception_handler
    def delete_assistant(self, assistant_id):
        """
        Deletes an assistant by its ID.
        Args:
            assistant_id (str): The ID of the assistant.
        """
        self.client.beta.assistants.delete(assistant_id)
