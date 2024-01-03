"""
This script provides methods for uploading and listing files using the OpenAI API.
"""
from openai import OpenAI
from .api_exception_handler import file_exception_handler


class FileManager:
    """
    A class that handles file operations using the OpenAI API.
    """

    def __init__(self, api_key: str):
        """
        Initializes the FileManager instance with an API key.
        Args:
        - api_key (str): The API key for accessing the OpenAI API.
        """
        self.client = OpenAI(api_key=api_key)

    @file_exception_handler
    def upload_file(self, file_name):
        """
        Uploads a file to the OpenAI API and returns the file ID.
        Args:
        - file_name (str): The name of the file to upload.
        Returns:
        - str: The ID of the uploaded file.
        """
        file = self.client.files.create(
            file=open(file_name, "rb"),
            purpose="assistants"
        )
        return file.id

    @file_exception_handler
    def list_files(self):
        """
        Retrieves a list of all files uploaded to the OpenAI API.
        Returns:
        - list: A list of file objects representing the uploaded files.
        """
        files_list = self.client.files.list()
        return files_list
