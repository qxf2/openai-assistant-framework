"""
This script provides methods for creating, retrieving, 
and submitting tool outputs for runs using the OpenAI API.
"""
from openai import OpenAI
from .api_exception_handler import run_exception_handler

class RunManager:
    """
    A class for managing the execution of assistants on threads.
    Args:
        api_key (str): The API key for accessing the OpenAI API.
    Attributes:
        client: An instance of the OpenAI class for making API calls.
        runs: A dictionary to store information about the runs.
    """

    def __init__(self, api_key: str):
        """
        Initializes the RunManager instance with an API key.     
        Args:
        - api_key (str): The API key for accessing the OpenAI API.
        """
        self.client = OpenAI(api_key=api_key)
        self.runs = {}

    @run_exception_handler
    def run_assistant(self, thread_id, assistant_id, instructions=None):
        """
        Runs an assistant on a thread and returns the run object.
        Args:
            thread_id (str): The ID of the thread.
            assistant_id (str): The ID of the assistant.
            instructions (str, optional): The instructions for the assistant. Defaults to None.
        Returns:
            dict: The run object.
        """
        run = self.client.beta.threads.runs.create(
            thread_id=thread_id,
            assistant_id=assistant_id,
            instructions=instructions
        )
        return run

    @run_exception_handler
    def retrieve_run_status(self, thread_id, run_id):
        """
        Retrieves the status of a run and returns the status object.
        Args:
            thread_id (str): The ID of the thread.
            run_id (str): The ID of the run.
        Returns:
            dict: The status object.
        """
        return self.client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run_id
        )

    @run_exception_handler
    def submit_run_output(self, thread_id, run_id, tool_outputs):
        """
        Submits the output of a run.
        Args:
            thread_id (str): The ID of the thread.
            run_id (str): The ID of the run.
            tool_outputs (dict): The tool outputs to submit.
        """
        self.client.beta.threads.runs.submit_tool_outputs(
            thread_id=thread_id,
            run_id=run_id,
            tool_outputs=tool_outputs
        )
