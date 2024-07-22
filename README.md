# Zephyr Flying Instructor Chatbot

A specialized LLM chatbot designed to help you learn about flying airplanes

## Introduction

This project implements a chatbot using the Zephyr 7B model, specifically tailored to assist users in learning about flying airplanes. Whether you're a complete novice or looking to expand your aviation knowledge, this chatbot serves as your virtual flying instructor.

## Features

- Utilizes the Zephyr 7B model for natural language processing
- Specialized in providing information about flying airplanes
- User-friendly interface powered by Gradio

## Prerequisites

- Python 3.7+
- pip (Python package manager)
- A Hugging Face account (for deployment)

## Installation

1. Clone the repository:
   git clone https://github.com/yourusername/ZephyrFlyingInstructor.git
   cd ZephyrFlyingInstructor

2. Install required packages:
   pip install -r requirements.txt

## Usage

1. Run the chatbot locally:
   python app.py

2. Open your web browser and navigate to the provided local URL.

3. Start asking questions about flying airplanes!

## How It Works

The chatbot is initialized with the following system message:

"I want to learn how to fly an airplane."

This specialized prompt ensures that the Zephyr 7B model focuses its vast knowledge on the subject of flying airplanes. You can ask questions about:

- Basic flight principles
- Aircraft controls and instruments
- Pre-flight procedures
- Navigation techniques
- Aviation regulations
- And much more!

## Customization

While the chatbot is pre-configured for flying instruction, you can modify the system message in `app.py` to explore other aviation-related topics:

system_message = "I want to learn about aircraft maintenance."

## Deployment

To deploy on Hugging Face Spaces:

1. Log into your Hugging Face account
2. Create a new Space, selecting Gradio as the SDK
3. Upload the `app.py` and `requirements.txt` files

## Contributing

Contributions to enhance the chatbot's aviation knowledge or improve its functionality are welcome. Please fork the repo and submit a pull request with your changes.

## Contact

For questions or to share your experiences learning about flying with this chatbot, contact: turna.fardousi@gmail.com

## Disclaimer

This chatbot provides educational information about flying airplanes. It is not a substitute for professional flight instruction. Always consult certified flight instructors and follow proper aviation regulations for actual flight training.
