"""
This script is used to create OpenAI AI Assistant that helps detect outliers in a provided dataset.

Usage: Create the Assistant first and then update assistant_id with the
created Assistant ID.

Note: Export the 'API_KEY'.
"""
import time
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from modules import (
    api_exception_handler,
    assistant_manager,
    message_manager,
    thread_manager,
    run_manager
)

API_KEY = os.getenv("API_KEY")
ASSISTANT_MANAGER = assistant_manager.AssistantManager(API_KEY)
THREAD_MANAGER = thread_manager.ThreadManager(API_KEY)
MESSAGE_MANAGER = message_manager.MessageManager(API_KEY)
RUN_MANAGER = run_manager.RunManager(API_KEY)

def create_assistant():
    """
    Create an OpenAI AI Assistant for detecting outliers in a given dataset
    """
    name = "Outler Detection Assistant"
    instructions = '''
    You are an expert in outlier data validation. You will be provided a dataset with numbers (integer or floating point). 
    Your task is to identify potential outliers in the dataset or distribution of numbers. 
    Outliers are values that lie outside the overall pattern in a distribution. 
    When asked question consisting of the dataset of numbers, identify the outliers and provide it to the user.
    '''
    tools = [{"type": "code_interpreter"}]
    try:
        assistant = ASSISTANT_MANAGER.create_assistant(name, instructions, tools)
    except api_exception_handler.AssistantError as error:
        print("Error while creating Assistant:", error)
    return assistant

def perform_outlier_detection():
    """
    Perform outlier detection using Outlier detection Assistant
    """
    #Retreive the Outlier detection Assistant details
    try:
        assistant_id = ""
        assistant = ASSISTANT_MANAGER.retrieve_assistant(assistant_id)
        print(f"Validation Assistant details, ID: {assistant.id}, Name: {assistant.name}")
    except api_exception_handler.AssistantError as error:
        print("Error while retreiving assistant details:", error)
        sys.exit(1)

    #Create a new thread
    try:
        thread = THREAD_MANAGER.create_thread()
        thread_id = thread.id
        print("\nCreated Thread: ", thread_id)
    except api_exception_handler.ThreadError as thread_creation_error:
        print("Error while creating thread", thread_creation_error)
        sys.exit(1)

    #Add message to the thread
    try:
        user_question = '''
        Identify the outliers in this dataset - 
        [60, 128, 128, 128, 128, 128, 128, 128, 128, 128, 110, 128, 128, 128, 128, 128, 128, 
        128, 128, 128, 30, 128, 128, 128, 128, 128, 128, 128, 128, 128]
        '''
        message_details = MESSAGE_MANAGER.add_message_to_thread(
            thread_id=thread_id,
            content=user_question
        )
        print("\nDetails of message added to thread: ", message_details)
    except api_exception_handler.MessageError as message_error:
        print("Error adding message to thread:", message_error)
        sys.exit(1)

    #Create a run
    try:
        run_details = RUN_MANAGER.run_assistant(
            thread_id=thread_id,
            assistant_id=assistant_id
        )
        run_id = run_details.id
        print(f"\nStarted run (of {thread_id}) RunID: ", run_id)
    except api_exception_handler.RunError as run_error:
        print("Error while creating a run", run_error)
        sys.exit(1)

    #Check run status and retreive response of the assistant
    try:
        while True:
            # Allow function to complete
            time.sleep(5)
            run_details = RUN_MANAGER.retrieve_run_status(thread_id=thread_id, run_id=run_id)
            print(f"\nStatus of the Run ({run_id}): ", run_details.status)

            if run_details.status == "completed":
                MESSAGE_MANAGER.process_message(thread_id)
                break
            print("\nWaiting for the Assistant to process the message..")
    except api_exception_handler.RunError as run_error:
        print("Error while processing assistant response", run_error)
        sys.exit(1)

    #Cleanup by deleting the thread
    try:
        THREAD_MANAGER.delete_thread(thread_id=thread_id)
        print(f"\nDeleted thread: {thread_id}")
    except api_exception_handler.ThreadError as thread_delete_error:
        print("Error while deleting thread", thread_delete_error)
        sys.exit(1)

if __name__ == "__main__":
    perform_outlier_detection()
