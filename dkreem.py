import openai
import speech_recognition as sr
import pyttsx3

# Set up OpenAI GPT-3.5 API
openai.api_key = "..."

def dkreem_assistant():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something...")
        audio = recognizer.listen(source)

    try:
        user_input = recognizer.recognize_google(audio).lower()
        print("User: " + user_input)

        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=user_input,
            max_tokens=150,
            temperature=0.7,
        )

        ai_response = response.choices[0].text.strip()
        print("dkreem: " + ai_response)

        engine = pyttsx3.init()
        engine.say(ai_response)
        engine.runAndWait()

    except sr.UnknownValueError:
        print("dkreem: Sorry, I didn't catch that. Could you please repeat?")
        engine = pyttsx3.init()
        engine.say("Sorry, I didn't catch that. Could you please repeat?")
        engine.runAndWait()

    except sr.RequestError as e:
        print("dkreem: Oops! There was an error with the speech recognition service. {0}".format(e))
        engine = pyttsx3.init()
        engine.say("Oops! There was an error with the speech recognition service.")
        engine.runAndWait()

if __name__ == "__main__":
    while True:
        dkreem_assistant()
