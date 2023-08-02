# dkreem Voice Assistant

dkreem Voice Assistant is a simple Python-based voice assistant that uses the OpenAI GPT-3.5 API for natural language processing and the `speech_recognition` and `pyttsx3` libraries for speech recognition and text-to-speech conversion, respectively. This README file provides an overview of the dkreem Voice Assistant, explains its features, and offers instructions on how to run the code.

## Features

The dkreem Voice Assistant offers the following features:

1. **Speech Recognition:** The assistant captures the user's voice input through the device's microphone using the `speech_recognition` library.

2. **OpenAI GPT-3.5 API Integration:** The user's voice input is processed using the GPT-3.5 API from OpenAI to generate AI-generated responses.

3. **Text-to-Speech Conversion:** The AI-generated responses are converted to speech using the `pyttsx3` library, allowing the assistant to respond audibly.

4. **Error Handling:** The script includes basic error handling for cases where the speech recognition service fails to understand the user's input or when there are request errors with the GPT-3.5 API.

## How to Run the Code

To run the dkreem Voice Assistant, follow these steps:

1. **Install Dependencies:** Ensure you have the necessary libraries installed. You can install them using pip:

   ```
   pip install openai
   ```
   ```
   pip install speechrecognition
   ```
   ```
   pip install pyttsx3
   ```

2. **OpenAI API Key:** Replace `"..."` in `openai.api_key = "..."` with your actual OpenAI GPT-3.5 API key. If you don't have an API key, you can sign up for access on the [OpenAI website](https://beta.openai.com/signup/).

3. **Run the Script:** Save the code in a Python file (e.g., `dkreem_assistant.py`). Run the script by executing the following command in the terminal:

   ```
   python dkreem_assistant.py
   ```

4. **Interact with the Assistant:** The dkreem Voice Assistant will prompt you to say something. Speak your query into the microphone. The assistant will process your input using the GPT-3.5 API and respond audibly through text-to-speech.

5. **Continuous Interaction:** The script runs in an infinite loop, allowing you to have multiple interactions with the AI assistant. To exit the loop and stop the assistant, terminate the script manually (e.g., press `Ctrl + C` in the terminal).

## Note

Please note that this implementation is a basic demonstration of a voice assistant and does not include advanced features such as intent recognition, multilingual support, or external skill integration. Additionally, the OpenAI GPT-3.5 API and other third-party services require internet connectivity for the assistant to function properly.

## Contributions

We welcome contributions to enhance the dkreem Voice Assistant's functionality and capabilities. If you have any suggestions, bug fixes, or new features to add, please feel free to submit a pull request.

## License

The dkreem Voice Assistant is open-source software licensed under the [MIT License](LICENSE).

## Acknowledgments

- The dkreem Voice Assistant utilizes the OpenAI GPT-3.5 API, which is made possible by OpenAI.
- Special thanks to the developers of the `speech_recognition` and `pyttsx3` libraries for providing the speech recognition and text-to-speech functionalities, respectively.

## Contact

If you have any questions or feedback, please don't hesitate to contact us at [contact@dkreem.com](mailto:contact@dkreem.com).

Thank you for using dkreem Voice Assistant!
