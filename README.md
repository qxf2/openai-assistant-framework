# OpenAI Assistant Framework
A Python framework for creating and managing OpenAI assistants using the OpenAI API.

## Introduction

This project is a simple framework that allows you to create and manage OpenAI assistants using the OpenAI API. It provides classes and methods for performing tasks such as creating assistants, uploading files, creating threads, sending messages, creating runs, checking run status, and processing assistant responses. It also provides custom exception handling for the OpenAI API errors.

This project was created as part of a research task of exploring OpenAI for performing data validation tasks. It is not intended to be a production-ready or a comprehensive solution, but rather a starting point and a reference for further development and experimentation.


## Installation and usage

To install and run this project, you need to have Python 3.8 or higher, and the openai module installed. You also need to have a valid OpenAI API key, which you can obtain from the [OpenAI website](https://openai.com/blog/openai-api).

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/qxf2/openai-assistant-framework.git

2. **Install Dependencies**
    ```bash
    pip install -r requirements.txt

3. **Set Up API Keys**
    To run this project, you need to set the API_KEY environment variable to your OpenAI API key.
    ```bash
    export API_KEY=<your-key>

## Example Scripts
    There are two simple scripts which create OpenAI AI Assistants for performing data validation tasks - outlier detection and numerical validation. The scripts perform the required tasks such as creating an assistant, uploading a file, creating a thread, sending a message, creating a run, checking the run status, processing the assistant response, and deleting the thread.

### Features

This project has the following functionalities:

***AssistantManager***: A class for managing OpenAI assistants, which provides methods for creating, listing, retrieving, and deleting assistants using the OpenAI API. 
***FileManager***: A class for managing OpenAI files, which provides methods for uploading, listing, retrieving files using the OpenAI API.
***ThreadManager***: A class for managing OpenAI threads, which provides methods for creating, listing, retrieving, and deleting threads using the    OpenAI API.
***MessageManager***: A class for managing OpenAI messages, which provides methods for creating, listing, retrieving messages using the OpenAI API. It also provides a method for processing the assistant response and displaying it to the user.
***RunManager***: A class for managing OpenAI runs, which provides methods for creating, retrieving, and submitting tool outputs for runs using the OpenAI API. It also provides a method for checking the run status and handling the required actions from the user.
***api_exception_handler***: A module that defines custom exception classes and decorator functions for handling OpenAI API errors, such as BadRequestError, RateLimitError, AuthenticationError, APIError, etc.

## License ##
This project is licensed under the MIT License.
