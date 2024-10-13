# from Traning_model.model import mind
# import requests
# from pprint import pprint
# import subprocess as sp
# import wikipedia
# import pywhatkit as kit
# import os
# import webbrowser
# import pyautogui
# from Head.Ear import listen
# from Head.Mouth import speak
#
# # Paths to commonly used apps
# paths = {
#     'notepad': "C:\\Program Files\\Notepad++\\notepad++.exe",
#     'discord': "C:\\Users\\ashut\\AppData\\Local\\Discord\\app-1.0.9003\\Discord.exe",
#     'calculator': "C:\\Windows\\System32\\calc.exe"
# }
#
#
# # Task functions
# def open_notepad():
#     webbrowser.open("https://onlinenotepad.org/notepad")
#
#
# def open_discord():
#     os.startfile(paths['discord'])
#
#
# def open_cmd():
#     os.system('start cmd')
#
#
# def open_camera():
#     sp.run('start microsoft.windows.camera:', shell=True)
#
#
# def open_calculator():
#     sp.Popen(paths['calculator'])
#
#
# def type_message():
#     speak("Please tell me what should I write.")
#     while True:
#         typequery = listen()
#         if typequery == 'exit typing':
#             break
#         else:
#             pyautogui.write(typequery)
#
#
# def find_my_ip():
#     ip_address = requests.get('https://api64.ipify.org?format=json').json()
#     return ip_address["ip"]
#
#
# def search_on_wikipedia(query):
#     results = wikipedia.summary(query, sentences=2)
#     return results
#
#
# def play_on_youtube(video):
#     kit.playonyt(video)
#
#
# def search_on_google(query):
#     kit.search(query)
#
#
# def send_whatsapp_message(number, message):
#     kit.sendwhatmsg_instantly(f"+91{number}", message)
#
#
# def get_latest_news(news_api_key):
#     try:
#         res = requests.get(
#             f"https://newsapi.org/v2/top-headlines?country=in&apiKey={news_api_key}&category=general").json()
#         articles = res["articles"]
#         news_headlines = [article["title"] for article in articles]
#         return news_headlines[:5]
#     except Exception as e:
#         return ["Error fetching news"]
#
#
# def get_random_joke():
#     headers = {'Accept': 'application/json'}
#     res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
#     return res["joke"]
#
#
# def get_random_advice():
#     res = requests.get("https://api.adviceslip.com/advice").json()
#     return res['slip']['advice']
#
#
# def get_weather_report(city):
#     # Using mock data for demonstration
#     res = {
#         "weather": [{"main": "Haze"}],
#         "main": {"temp": 26.95, "feels_like": 26.64},
#         "name": city
#     }
#     weather = res["weather"][0]["main"]
#     temperature = res["main"]["temp"]
#     feels_like = res["main"]["feels_like"]
#     return weather, f"{temperature}℃", f"{feels_like}℃"
#
#
# # Main brain function to handle user input
# def brain(text):
#     response = mind(text)
#
#     # Start listening for commands in a loop
#     while True:
#         query = listen().lower()
#
#         if 'open notepad' in query:
#             open_notepad()
#
#         elif 'open discord' in query:
#             open_discord()
#
#         elif 'open command prompt' in query or 'open cmd' in query:
#             open_cmd()
#
#         elif 'open camera' in query:
#             open_camera()
#
#         elif 'open calculator' in query:
#             open_calculator()
#
#         elif 'ip address' in query:
#             ip_address = find_my_ip()
#             speak(f'Your IP Address is {ip_address}.')
#
#         elif 'wikipedia' in query:
#             speak('What do you want to search on Wikipedia?')
#             search_query = listen().lower()
#             results = search_on_wikipedia(search_query)
#             speak(f"According to Wikipedia, {results}")
#
#         elif 'youtube' in query:
#             speak('What do you want to play on Youtube?')
#             video = listen().lower()
#             play_on_youtube(video)
#
#         elif 'search on google' in query or 'search' in query:
#             speak('What do you want to search on Google?')
#             query = listen().lower()
#             search_on_google(query)
#
#         elif 'send whatsapp message' in query:
#             speak('On what number should I send the message?')
#             number = input("Enter the number: ")
#             speak("What is the message?")
#             message = listen().lower()
#             send_whatsapp_message(number, message)
#             speak("I've sent the message.")
#
#         elif 'joke' in query:
#             joke = get_random_joke()
#             speak(joke)
#
#         elif 'advice' in query:
#             advice = get_random_advice()
#             speak(advice)
#
#         elif 'news' in query:
#             speak(f"I'm reading out the latest news headlines.")
#             news_api_key = "your_news_api_key"  # Replace with your actual News API Key
#             headlines = get_latest_news(news_api_key)
#             for headline in headlines:
#                 speak(headline)
#
#         elif 'weather' in query:
#             speak(f"Which city do you want the weather report for?")
#             city = listen().lower()
#             weather, temperature, feels_like = get_weather_report(city)
#             speak(f"The weather in {city} is {weather}. The temperature is {temperature}, but feels like {feels_like}.")
#
#         elif 'type' in query or 'type message' in query:
#             type_message()
#
#
# # Initial call to brain with starting message
# brain()
