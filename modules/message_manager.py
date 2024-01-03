"""
This script provides methods for creating, listing, retrieving messages using the OpenAI API.
"""
from openai import OpenAI
from .api_exception_handler import message_exception_handler

class MessageManager:
    """
    A class that manages thread messages.

    Attributes:
        client (OpenAI): An instance of the OpenAI class used for making API requests.
        messages (dict): A dictionary to store the messages in the thread.
    """

    def __init__(self, api_key: str):
        """
        Initializes the MessageManager instance with an API key.
        Args:
            api_key (str): The API key for making API requests.
        """
        self.client = OpenAI(api_key=api_key)
        self.messages = {}

    @message_exception_handler
    def add_message_to_thread(self, thread_id, content, role="user"):
        """
        Adds a message to a thread with an optional role.
        Args:
            thread_id (str): The ID of the thread.
            content (str): The content of the message.
            role (str, optional): The role of the message. Defaults to "user".
        Returns:
            message: The created message object.
        """
        message = self.client.beta.threads.messages.create(
            thread_id=thread_id,
            role=role,
            content=content
        )
        return message

    @message_exception_handler
    def add_message_and_file_to_thread(self, thread_id, content, file_id, role="user"):
        """
        Adds a message and a file to a thread with an optional role.
        Args:
            thread_id (str): The ID of the thread.
            content (str): The content of the message.
            file_id (str): The ID of the file.
            role (str, optional): The role of the message. Defaults to "user".
        Returns:
            message: The created message object.
        """
        message = self.client.beta.threads.messages.create(
            thread_id=thread_id,
            role=role,
            content=content,
            file_ids=[file_id]
        )
        return message

    @message_exception_handler
    def list_messages_by_thread(self, thread_id):
        """
        Lists all messages in a thread.
        Args:
            thread_id (str): The ID of the thread.
        Returns:
            messages: The list of messages in the thread.
        """
        messages = self.client.beta.threads.messages.list(thread_id=thread_id)
        return messages

    @message_exception_handler
    def process_message(self, thread_id):
        """
        Processes the latest message in a thread.
        Args:
            thread_id (str): The ID of the thread.
        """
        messages = self.list_messages_by_thread(thread_id)

        if messages.data:
            latest_response = messages.data[0].content[0].text.value
            print("\nAssistant: ", latest_response)
        else:
            print("No messages found.")
