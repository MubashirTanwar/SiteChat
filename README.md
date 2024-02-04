# SiteChat - Turn your static site into brains of a chat engine

## Project Description
This project is a generative AI chatbot that specializes in extracting and comprehending information from small websites. It allows users to upload multiple URLs, trains on the content of those pages, and enables them to ask questions or make queries related to the site's content. The chatbot leverages Python with Langchain and Streamlit to provide an interactive and user-friendly experience.

## Overview
- Training: The chatbot processes the website using Langchain and UnstructuredURLLoader to extract textual data and generate a knowledge base.
- Chat Interface: Users can initiate conversations with the chatbot by asking questions or making inquiries within the scope of the Website Text Contents.
- Responses: The chatbot uses generative AI to provide meaningful responses based on the trained knowledge base.
- User-Friendly: The project is built with a user-friendly interface using Streamlit for easy interaction.

## Tech Stack
- **Langchain**: Langchain is used for natural language processing (NLP) tasks, including text extraction and understanding.
- **Streamlit**: Streamlit is the framework used for creating a user-friendly web interface for the chatbot.
- **Generative AI**: The project incorporates generative AI techniques to generate responses based on the content of the PDFs.
- **Python**: The project is primarily developed in Python.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/MubashirTanwar/SiteChat.git
    cd SiteChat
    ```

2. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Streamlit app:**

    ```bash
    streamlit run app.py
    ```

4. **Interact with SiteChat through the Streamlit app.**

## Usage

1. Open the Streamlit app in your web browser using the localhost port provided.
2. Enter your questions in the text input field to interact with SiteChat.

## Configuration

- Create an '.env' file and add your OpenAI API key
- Configure language models and chat parameters in the `get_conversation_chain` function in the `app.py` file.
- Adjust the Streamlit app layout and styling as needed for your preferences.

## Contributing

If you'd like to contribute to SiteChat, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.

## Acknowledgments

- Thanks to the developers of Streamlit, LangChain, OpenAI, and other libraries used in this project.
- Inspired by the need for a chat-based NLP assistant for site handholding.

Feel free to customize this README according to your specific project details and requirements.