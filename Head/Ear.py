import os
import speech_recognition as sr
from mtranslate import translate
from colorama import Fore, Style, init

init(autoreset=True)


def translate_if_needed(text, lang_code):
    """Translate text only if it's Tamil, otherwise return the original text."""
    if lang_code == "ta":
        return translate(text, "en")  # Translate Tamil to English
    return text  # No translation for English text


def detect_and_translate_text(recognizer, audio):
    """Detect the spoken language and translate it to English if necessary."""
    try:
        # Recognize the speech, first trying Tamil and then English
        tamil_text = recognizer.recognize_google(audio, language="ta-IN")
        print(Fore.LIGHTYELLOW_EX + f"Detected (Tamil): {tamil_text}")

        # Translate Tamil to English
        translated_text = translate_if_needed(tamil_text, "ta")
        print(Fore.LIGHTCYAN_EX + f"Translated to English: {translated_text}")

    except sr.UnknownValueError:
        # If Tamil recognition fails, try English
        try:
            english_text = recognizer.recognize_google(audio, language="en-IN")
            print(Fore.LIGHTYELLOW_EX + f"Detected (English): {english_text}")
            # No need to translate if it's already in English
            translated_text = translate_if_needed(english_text, "en")
            print(Fore.LIGHTCYAN_EX + f"Final Text: {translated_text}")

        except sr.UnknownValueError:
            print(Fore.RED + "Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(Fore.RED + f"Could not request results from Google Speech Recognition service; {e}")


def listen():
    """Main function to listen for speech and handle recognition and translation."""
    recognizer = sr.Recognizer()

    # Adjust recognizer settings
    recognizer.dynamic_energy_threshold = False
    recognizer.energy_threshold = 35000
    recognizer.dynamic_energy_adjustment_damping = 0.03
    recognizer.dynamic_energy_ratio = 1.9
    recognizer.pause_threshold = 0.8  # Increased to give more time between pauses
    recognizer.operation_timeout = None  # No timeout for recognition operation

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            print(Fore.LIGHTBLUE_EX + "I am Listening....", flush=True)
            try:
                # Listen with no timeout, to avoid timing out too early
                audio = recognizer.listen(source, timeout=None)
                print(Fore.LIGHTGREEN_EX + "Got it, now recognizing...")

                # Detect the spoken language and translate if needed
                detect_and_translate_text(recognizer, audio)

            except sr.WaitTimeoutError:
                print(Fore.RED + "Listening timed out. Please try again.")
            except sr.RequestError as e:
                print(Fore.RED + f"Could not request results from Google Speech Recognition service; {e}")
            except Exception as e:
                print(Fore.RED + f"An error occurred: {e}")

            # Clear the terminal after each recognition attempt
            os.system('cls' if os.name == 'nt' else 'clear')


# Main entry point
if __name__ == "__main__":
    # Start listening for speech input in the main thread
    listen()
