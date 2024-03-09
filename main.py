from imports import *
from helpers import *

openai.api_key = "your-api-key"

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            greetMe()

            while True:
                query = takeCommand().lower()
                if 'translate' in query:
                    query = query.replace("jarvis","")
                    query = query.replace("translate","")
                    translate_and_speak(query)
                elif "hello" in query:
                    speak("Hello mam, how are you ?")
                elif "i am fine" in query:
                    speak("That's great, mam")
                elif "how are you" in query:
                    speak("Perfect, mam")
                elif "thank you" in query:
                    speak("You are welcome, mam")
                elif "google" in query:
                    import wikipedia as googleScrap
                    query = query.replace("jarvis","")
                    query = query.replace("google search","")
                    query = query.replace("google","")
                    print("This is your query: ", query) 
                    speak("This is what I found on google")
                    try:
                        pywhatkit.search(query)
                        result = googleScrap.summary(query,1)
                        speak(result)
                    except:
                        speak("No speakable output available")
                elif "youtube" in query:
                    speak("This is what I found for your search!") 
                    query = query.replace("youtube search","")
                    query = query.replace("youtube","")
                    query = query.replace("jarvis","")
                    web  = "https://www.youtube.com/results?search_query=" + query
                    print("This is your query: ", query) 
                    webbrowser.open(web)
                    pywhatkit.playonyt(query)
                    speak("Done, Mam")
                elif "wikipedia" in query:
                    speak("Searching from Wikipedia....")
                    query = query.replace("wikipedia", "").replace("search wikipedia", "").replace("jarvis", "").strip()
                    print("This is your query:", query)
                    try:
                        results = wikipedia.summary(query, sentences=2)
                        speak("According to Wikipedia..")
                        print(results)
                        speak(results)
                    except wikipedia.DisambiguationError as e:
                        speak("Your search query matched multiple articles on Wikipedia. Please be more specific.")
                    except Exception as e:
                        speak("Sorry, I couldn't find any information on Wikipedia for your search.")
                elif "weather" in query:
                    query = query.replace("jarvis","")
                    query = query.replace("what is the","")
                    query = query.replace("weather","")
                    query = query.replace("in","")
                    city = query.strip() # This assumes that the city is the remaining part of the query
                    print("City: ", city)
                    weather_info = get_weather(city)
                    speak(weather_info)
                elif "the time" in query:
                    query = query.replace("jarvis","")
                    query = query.replace("what is","")
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"Mam, the time is {strTime}")
                elif "open" in query:   #EASY METHOD
                    query = query.replace("open","")
                    query = query.replace("jarvis","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")  
                elif "internet speed" in query:
                    query = query.replace("jarvis","")
                    query = query.replace("what is the","")
                    wifi  = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
                    download_net = wifi.download()/1048576
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is ",download_net)
                    speak(f"Wifi download speed is {download_net}")
                    speak(f"Wifi Upload speed is {upload_net}")
                elif "play a game" in query:
                    query = query.replace("jarvis","")
                    game_play()
                elif "generate text" in query:
                    query = query.replace("jarvis","")
                    speak("What should I generate?")
                    prompt = takeCommand().lower()  # Assuming takeCommand() gets user input
                    generated_text = generate_response(prompt)
                    print(generated_text)
                    speak(generated_text)
                elif "tired" in query:
                    speak("Playing your favourite songs, mam")
                    a = (1,2,3) # You can choose any number of songs (I have only choosen 3)
                    b = random.choice(a)
                    if b==1:
                        webbrowser.open("youtube-link-to-your-favourite-song-1")
                    elif b==2:
                        webbrowser.open("youtube-link-to-your-favourite-song-2")
                    else:
                        webbrowser.open("youtube-link-to-your-favourite-song-3")
                elif "screenshot" in query:
                     import pyautogui #pip install pyautogui
                     im = pyautogui.screenshot()
                     im.save("ss.jpg")
                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")
                elif "go to sleep" in query:
                    speak("Ok mam, You can call me anytime. Goodbye!")
                    break
                elif "finally sleep" in query:
                    speak("Going to sleep,mam")
                    exit()
