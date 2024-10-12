import asyncio
import threading
import os
import edge_tts
import pygame

VOICE = "en-AU-WilliamNeural"
BUFFER_SIZE = 1024

def remove_file(file_path):
    max_attempts = 3
    attempts = 0
    while attempts < max_attempts:
        try:
            os.remove(file_path)
            break
        except Exception as e:
            print(f"Error removing file: {e}")
            attempts += 1

async def amain(TEXT, output_file) -> None:
    try:
        cm_txt = edge_tts.Communicate(TEXT, VOICE)
        await cm_txt.save(output_file)
        thread = threading.Thread(target=play_audio, args=(output_file,))
        thread.start()  # Start the audio playing thread
        thread.join()   # Wait for the thread to finish
    except Exception as e:
        print(f"Error: {e}")
    finally:
        remove_file(output_file)

def play_audio(file_path):
    try:
        pygame.init()
        pygame.mixer.init()
        sound = pygame.mixer.Sound(file_path)
        sound.play()
        while pygame.mixer.get_busy():
            pygame.time.delay(10)  # Delay to prevent busy looping
        pygame.quit()
    except Exception as e:
        print(f"Error playing audio: {e}")

def speak(TEXT, output_file=None):
    if output_file is None:
        output_file = os.path.join(os.getcwd(), "output.wav")  # Correct output file path
    asyncio.run(amain(TEXT, output_file))

# Call the speak function
speak("Welcome to the world of Jarvis")
