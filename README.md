# dkreem Voice Assistant

dkreem Voice Assistant is a Python-based voice assistant that utilizes the OpenAI GPT-3.5 API, various libraries, and external services to provide an interactive and customizable voice experience for users. This README file explains the key features and advantages of the dkreem Voice Assistant and provides instructions on how to run the code.

## Advantages

The dkreem Voice Assistant offers the following advantages:

1. **User Interface and Feedback:** The assistant comes with a graphical user interface (GUI) built using `tkinter`, allowing users to interact with the assistant intuitively. The GUI displays the user's query and the AI's response, providing visual feedback during the listening, processing, and speaking stages.

2. **Customizable Voice and Speech:** Users can choose from different voices for the AI response using the `pyttsx3` library. The assistant offers a dropdown menu with available voices, enabling users to personalize the assistant's voice to their preference.

3. **Intent Recognition:** The assistant implements intent recognition through a simple rule-based approach. It identifies user intentions, such as greetings or questions, to provide relevant context to the AI model. This improves the quality of responses from the GPT-3.5 API.

4. **Multilingual Support:** The assistant supports multiple languages by leveraging the `langdetect` and `googletrans` libraries. It detects the language of the user's input and translates non-English queries to English before sending them to the GPT-3.5 API.

5. **Conversation History and Context:** The assistant maintains a conversation history using a list, allowing for a more coherent and natural conversation flow. It utilizes the last three interactions as context when communicating with the GPT-3.5 API.

6. **Error Handling Improvement:** The assistant provides informative and user-friendly error handling for various scenarios, such as API connection errors, speech recognition errors, and request errors. It offers suggestions or prompts when user input is not recognized correctly or errors occur.

7. **Offline Mode:** The current implementation does not include an offline mode. Internet connectivity is required for the assistant to interact with external services like GPT-3.5 and the OpenWeatherMap API.

8. **Skill Integration:** The assistant showcases skill integration by fetching weather data from the OpenWeatherMap API based on the user's query containing the keyword "weather."

9. **Keyword Triggering:** The assistant responds differently based on specific keywords, such as "weather" and "time," providing specialized responses for these queries.

10. **User Authentication:** The current implementation does not include user authentication to personalize the assistant's responses based on individual user profiles.

11. **Volume Control and Mute Option:** Users can mute the assistant's voice by including the keyword "mute" in their query. It sets the volume to 0.0 when "mute" is detected.

12. **Natural Language Understanding (NLU):** The assistant uses spaCy for named entity recognition (NER) to extract named entities from the user's input and incorporate them into the AI's response.

13. **Continual Learning:** The current implementation does not explicitly include mechanisms for continual learning and updating the AI model with new data.

14. **Privacy and Data Protection:** The assistant addresses privacy and data protection concerns by informing users about data collection during the session only. It saves the last three interactions in a text file but does not persistently store user data beyond the current session.

## How to Run the Code

To run the dkreem Voice Assistant, follow these steps:

1. Make sure you have Python installed on your system (Python 3.x recommended).

2. Install required dependencies by running the following command in the terminal:

   ```
   pip install openai 
   ```
   ```
   pip install speech_recognition 
   ```
   ```
   pip install pyttsx3 
   ```
   ```
   pip install tkinter
   ```
   ```
   pip install langdetect 
   ```
   ```
   pip install googletrans
   ```
   ```
   pip install requests
   ```
   ```
   pip install spacy
   ```
3. Replace the placeholders "YOUR_OPENAI_API_KEY" and "YOUR_OPENWEATHERMAP_API_KEY" in the code with your actual API keys from OpenAI and OpenWeatherMap, respectively.

4. Save the code in a Python file (e.g., `dkreem_v3.py`).

5. Run the script by executing the following command in the terminal:

   ```
   python dkreem_v3.py
   ```

6. The dkreem Voice Assistant GUI window will appear. Interact with the assistant by speaking queries into the microphone.

7. The assistant will respond to your queries using AI-generated responses and may provide additional information based on keywords and named entities detected.

8. To quit the assistant, close the GUI window.

Please note that the assistant requires an active internet connection to interact with the GPT-3.5 and OpenWeatherMap APIs. The conversation history is saved temporarily during the session and will not persist beyond the current session to ensure privacy and data protection.
