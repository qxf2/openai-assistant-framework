"""
This module provides a set of methods for creating and managing exceptions for
assistant-related operations.
"""

import time
from openai import BadRequestError, APIError, RateLimitError, AuthenticationError

class AssistantError(Exception):
    "To raise exceptions generated while handling assistants"

class FileError(Exception):
    "To raise exceptions generated while handling files"

class MessageError(Exception):
    "To raise exceptions generated while handling messages"

class RunError(Exception):
    "To raise exceptions generated while handling runs"

class ThreadError(Exception):
    "To raise exceptions generated while handling threads"

def assistant_exception_handler(func):
    """
    A decorator function that handles OpenAI API errors that might arise when using assistant methods.
    Args:
        func: The function that calls the OpenAI API methods related to assistants.
    Returns:
        function: The wrapped function that handles the OpenAI API errors.
    Raises:
        AssistantError: A custom exception class that wraps the OpenAI API errors.
    """
    def inner_function(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except BadRequestError as request_error:
            raise AssistantError(request_error)
        except RateLimitError as rate_error:
            raise AssistantError(rate_error)
        except AuthenticationError as auth_error:
            raise AssistantError(auth_error)
        except APIError as api_error:
            raise AssistantError(api_error)
    return inner_function

def file_exception_handler(func):
    """
    A decorator function that handles OpenAI API errors that might arise when using file methods.
    Args:
        func (function): The function that calls the OpenAI API methods related to files.
    Returns:
        function: The wrapped function that handles the OpenAI API errors.
    Raises:
        FileError: A custom exception class that wraps the OpenAI API errors.
    """
    def inner_function(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError as file_not_found_error:
            raise FileError(file_not_found_error)
        except RateLimitError as rate_error:
            raise FileError(rate_error)
        except AuthenticationError as auth_error:
            raise FileError(auth_error)
        except APIError as api_error:
            raise FileError(api_error)
        except PermissionError as permission_error:
            raise FileError(permission_error)
        except TimeoutError as time_out_error:
            time.sleep(5)
            func(*args, **kwargs)
            raise FileError(time_out_error)
        except ValueError as value_error:
            raise FileError(value_error)
    return inner_function

def message_exception_handler(func):
    """
    A decorator function that handles OpenAI API errors that might arise when using message methods.
    Args:
        func (function): The function that calls the OpenAI API methods related to messages.
    Returns:
        function: The wrapped function that handles the OpenAI API errors.
    Raises:
        MessageError: A custom exception class that wraps the OpenAI API errors.
    """
    def inner_function(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except BadRequestError as request_error:
            raise MessageError(request_error)
        except RateLimitError as rate_error:
            raise MessageError(rate_error)
        except AuthenticationError as auth_error:
            raise MessageError(auth_error)
        except APIError as api_error:
            raise MessageError(api_error)
    return inner_function

def thread_exception_handler(func):
    """
    A decorator function that handles OpenAI API errors that might arise when using thread methods.
    Args:
        func (function): The function that calls the OpenAI API methods related to threads.
    Returns:
        function: The wrapped function that handles the OpenAI API errors.
    Raises:
        ThreadError: A custom exception class that wraps the OpenAI API errors.
    """
    def inner_function(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except BadRequestError as request_error:
            raise ThreadError(request_error)
        except RateLimitError as rate_error:
            raise ThreadError(rate_error)
        except AuthenticationError as auth_error:
            raise ThreadError(auth_error)
        except APIError as api_error:
            raise ThreadError(api_error)
    return inner_function

def run_exception_handler(func):
    """
    A decorator function that handles OpenAI API errors that might arise when using run methods.
    Args:
        func (function): The function that calls the OpenAI API methods related to run.
    Returns:
        function: The wrapped function that handles the OpenAI API errors.
    Raises:
        RunError: A custom exception class that wraps the OpenAI API errors.
    """
    def inner_function(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except BadRequestError as request_error:
            raise RunError(request_error)
        except RateLimitError as rate_error:
            raise RunError(rate_error)
        except AuthenticationError as auth_error:
            raise RunError(auth_error)
        except APIError as api_error:
            raise RunError(api_error)
        except PermissionError as permission_error:
            raise RunError(permission_error)
        except TimeoutError as timeout_error:
            raise RunError(timeout_error)
    return inner_function
