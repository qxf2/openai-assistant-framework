"""
This script provides methods for creating, listing, retreiving
and deleting threads using the OpenAI API.
"""
from openai import OpenAI
from .api_exception_handler import thread_exception_handler

class ThreadManager:
    """
    A class for managing threads using the OpenAI API.
    Args:
        api_key (str): The API key for accessing the OpenAI API.
    Attributes:
        client: An instance of the OpenAI class used for making API calls.
        threads: A dictionary that stores the created threads.
        The keys are the thread IDs and the values are the thread objects.
    """

    def __init__(self, api_key: str):
        """
        Initializes a new instance of the ThreadManager class with the provided API key.
        Args:
            api_key (str): The API key for accessing the OpenAI API.
        """
        self.client = OpenAI(api_key=api_key)
        self.threads = {}

    @thread_exception_handler
    def create_thread(self):
        """
        Creates a new thread using the OpenAI API.
        Returns:
            The created thread.
        """
        thread = self.client.beta.threads.create()
        return thread

    @thread_exception_handler
    def retrieve_thread(self, thread_id):
        """
        Retrieves a thread by its ID using the OpenAI API.
        Args:
            thread_id: The ID of the thread to retrieve.
        Returns:
            The retrieved thread.
        """
        thread = self.client.beta.threads.retrieve(thread_id)
        return thread

    @thread_exception_handler
    def list_threads(self):
        """
        Lists all threads using the OpenAI API.
        Returns:
            A list of threads.
        """
        return list(self.threads.values())

    @thread_exception_handler
    def delete_thread(self, thread_id):
        """
        Deletes a thread by its ID using the OpenAI API.
        Args:
            thread_id: The ID of the thread to delete.
        """
        self.client.beta.threads.delete(thread_id)
