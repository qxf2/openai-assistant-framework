"""
This script is used to create OpenAI AI Assistant that helps in performing
numerical validation - identify whether the numbers in a dataset fall
within the range of 0 and 1.

Usage: Create the Assistant first and then update assistant_id with the
created Assistant ID.

Note: Export the 'API_KEY' and ensure the CSV file is present.
"""
import time
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from modules import (
    api_exception_handler,
    assistant_manager,
    message_manager,
    file_manager,
    thread_manager,
    run_manager,
)

API_KEY = os.getenv("API_KEY")
ASSISTANT_MANAGER = assistant_manager.AssistantManager(API_KEY)
THREAD_MANAGER = thread_manager.ThreadManager(API_KEY)
MESSAGE_MANAGER = message_manager.MessageManager(API_KEY)
RUN_MANAGER = run_manager.RunManager(API_KEY)
FILE_MANAGER = file_manager.FileManager(API_KEY)

FILE_NAME = "utils/github_scores.csv"


def create_assistant():
    """
    Create an OpenAI AI Assistant for performing numerical validation i.e
    checking whether all numbers in provided CSV file are between 0 and 1
    """
    name = "Numerical Validation Assistant"
    instructions = """
    You are an expert in numerical data validation. You will be provided a CSV file having 3 columns - repo_score, date and repo_name.
    The values of the repo_score column are floating point numbers. Your task is to verify that all the numbers in this repo_score column
    meet the following condition:
     - All values must be between 0 and 1 (inclusive) i.e each value must be greater than or equal to 0.0 and less than or equal to 1.0

    Return a JSON object with two keys:
    1. "valid": true if the dataset meets the criteria, false otherwise
    2. "failed_values": a list containing numbers along with repo names that do not satisfy the condition
    """
    tools = [{"type": "code_interpreter"}]
    try:
        numerical_assistant = ASSISTANT_MANAGER.create_assistant(name, instructions, tools)
        print(numerical_assistant)
    except api_exception_handler.AssistantError as error:
        print("Error while creating Assistant:", error)
    return numerical_assistant


def perform_numerical_validation():
    """
    Perform numerical validation using the Numerical validation Assistant
    """
    # Retreive the Outlier detection Assistant details
    try:
        assistant_id = ""
        assistant = ASSISTANT_MANAGER.retrieve_assistant(assistant_id)
        print(f"Validation Assistant details, ID: {assistant.id}, Name: {assistant.name}")
    except api_exception_handler.AssistantError as error:
        print("Error while retreiving assistant details:", error)
        sys.exit(1)

    # Upload the CSV file
    try:
        file_id = FILE_MANAGER.upload_file(FILE_NAME)
    except api_exception_handler.FileError as file_upload_error:
        print("Error while uploading file: ", file_upload_error)
        sys.exit(1)

    # Create a new thread
    try:
        thread = THREAD_MANAGER.create_thread()
        thread_id = thread.id
        print("\nCreated Thread: ", thread_id)
    except api_exception_handler.ThreadError as thread_creation_error:
        print("Error while creating thread", thread_creation_error)
        sys.exit(1)

    # Add message to the thread
    try:
        user_question = "Validate the provided CSV file and give out the results"
        message_details = MESSAGE_MANAGER.add_message_and_file_to_thread(
            thread_id=thread_id, content=user_question, file_id=file_id
        )
        print("\nDetails of message added to thread: ", message_details)
    except api_exception_handler.MessageError as message_error:
        print("Error while creating thread:", message_error)
        sys.exit(1)

    # Create a run
    try:
        run_details = RUN_MANAGER.run_assistant(thread_id=thread_id, assistant_id=assistant_id)
        run_id = run_details.id
        print(f"\nStarted run (of {thread_id}) RunID: ", run_id)
    except api_exception_handler.RunError as run_error:
        print("Error while creating a run", run_error)
        sys.exit(1)

    # Check run status and retreive response of the assistant
    try:
        while True:
            time.sleep(5)
            run_details = RUN_MANAGER.retrieve_run_status(thread_id=thread_id, run_id=run_id)
            print(f"\nStatus of the Run ({run_id}): ", run_details.status)

            if run_details.status == "completed":
                MESSAGE_MANAGER.process_message(thread_id)
                break
            print("\nWaiting for the Assistant to process the message")
    except api_exception_handler.RunError as run_error:
        print("Error while processing assistant response", run_error)
        sys.exit(1)
    except api_exception_handler.MessageError as message_error:
        print("Error while retreiving response", message_error)
        sys.exit(1)

    # Cleanup by deleting the thread
    try:
        THREAD_MANAGER.delete_thread(thread_id=thread_id)
        print(f"\nDeleted thread: {thread_id}")
    except api_exception_handler.ThreadError as thread_delete_error:
        print("Error while deleting thread", thread_delete_error)
        sys.exit(1)


if __name__ == "__main__":
    perform_numerical_validation()
