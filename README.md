# WorkplaceFirstAidAssistant

A RAG-based LLM chatbot specializing in workplace first aid information

This README provides a guide to set up and use a specialized chatbot that leverages Retrieval-Augmented Generation (RAG) to provide information about workplace first aid programs, drawing from OSHA guidelines.

## Introduction

This project implements a chatbot that specializes in workplace first aid information. It uses a Large Language Model (LLM) combined with a Retrieval-Augmented Generation (RAG) system to provide accurate and relevant information based on OSHA's "Fundamentals of a Workplace First-Aid Program" document.

## Features

- Utilizes the Zephyr 7B model for natural language processing
- Implements RAG for enhanced accuracy and relevance of responses
- Provides information on workplace first aid programs, procedures, and legal requirements
- Offers a user-friendly interface powered by Gradio

## Prerequisites

Before you start using this chatbot, make sure you have the following:

- Python 3.7 or higher
- pip (Python package manager)

## Installation

1. Clone this repository:
   git clone https://github.com/yourusername/WorkplaceFirstAidAssistant.git
   cd WorkplaceFirstAidAssistant

2. Install the required packages:
   pip install -r requirements.txt

## Usage

To run the chatbot locally:

1. Execute the following command in your terminal:
   python app.py

2. Open your web browser and navigate to the local URL provided in the terminal output (typically http://127.0.0.1:7860).

3. Start interacting with the chatbot by asking questions about workplace first aid programs.

## Customization

You can customize the chatbot by modifying the following in `app.py`:

- Change the `system_message` to alter the chatbot's persona or specialization
- Modify the `examples` list to add or change the suggested questions
- Adjust the RAG parameters in the `search_documents` method to fine-tune retrieval

## Disclaimer

This chatbot provides educational information on workplace first-aid. It is not a substitute for professional medical advice, training, or local regulations. Always seek professional medical guidance and adhere to relevant laws.

## Contributing

If you wish to contribute:

1. Fork this repository
2. Create a new branch (git checkout -b feature/AmazingFeature)
3. Commit your changes (git commit -m 'Add some AmazingFeature')
4. Push to the branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

## Contact

For any questions or feedback, please reach out to [your-email@example.com].
