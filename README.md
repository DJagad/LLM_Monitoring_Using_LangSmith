# LLM Monitoring Application using LangSmith

## Overview

This application is designed to run and monitor large language models (LLMs) using LangSmith, a platform built for creating production-grade LLM applications. LangSmith provides comprehensive tools for debugging, testing, evaluating, and monitoring LLM chains and intelligent agents across various frameworks, including integration with LangChain.

The `app.py` provided in this repository is a simple script to demonstrate how to utilize the LangSmith and LangChain frameworks to process queries against an OpenAI model. The script sets up an environment to use OpenAI's GPT-3.5-turbo model to answer a question based on a given context.

## Features

- **LLM Integration**: Utilizes OpenAI's GPT-3.5-turbo for generating responses.
- **Environment Configuration**: Manages sensitive data like API keys using environment variables.
- **Chain Execution**: Implements a chain of operations from prompting to model invocation and parsing the output.
- **Tracing and Monitoring**: Enabled tracing for deeper insights and monitoring of the query handling process.

## Prerequisites

Before you run the application, ensure you have the following prerequisites installed on your system:

- Python 3.9 or later
- pip (Python package installer)

## Installation

To set up the environment and run the application, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://your-repository-url.git
   cd your-repository-directory
   ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
3. **Setup environment variables**:

    **Create a .env file in the root directory and populate it with your OpenAI and LangChain API keys**:
    ```bash
    OPENAI_API_KEY=your_openai_api_key_here
    LANGCHAIN_PROJECT_NAME=name_of_the_project
    LANGCHAIN_API_KEY=your_langchain_api_key_here
    ```

## Usage
**Run the application using the following command**:

```bash
python app.py
```

The script will prompt the OpenAI model using a predefined question and context and output the model's response to the console.

## Contributing
**Contributions are welcome! If you have improvements or bug fixes**:

```bash
Fork the repository.
Create a new branch (git checkout -b feature/your_feature).
Make your changes.
Commit your changes (git commit -am 'Add some feature').
Push to the branch (git push origin feature/your_feature).
Create a new Pull Request.
```

## License
**This project is licensed under the MIT License - see the LICENSE file for details.**

## Support
**If you encounter any issues or require assistance, please submit an issue on the repository issue tracker.**

**By utilizing LangSmith with LangChain in this application, developers can build robust and scalable LLM applications with enhanced capabilities for real-world deployment.**