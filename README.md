# CompileHub

# Code Execution Web App

This is a simple Flask-based web application that allows users to execute code written in different programming languages (Python, C, C++, and Java) directly from a web interface.

## Features

- Executes Python, C, C++, and Java code dynamically.
- Provides output or error messages from the code execution.
- Uses temporary files to store code before execution.
- Designed as a web service with Flask.

## Requirements

Before running the application, ensure that you have the following installed:

- **Python** (preferably Python 3.6+)
- **Flask**: A lightweight Python web framework.
  - Install it using pip:
    ```bash
    pip install flask
    ```

- **Compilers** (for C, C++, and Java):
  - **GCC** (for C programming)
  - **G++** (for C++ programming)
  - **Javac** (for Java programming)

### Install GCC, G++, and Javac:

- **On Ubuntu/Debian**:
  ```bash
  sudo apt update
  sudo apt install gcc g++ openjdk-11-jdk
