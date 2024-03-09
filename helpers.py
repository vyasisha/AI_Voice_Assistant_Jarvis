from imports import *
from main import engine

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding...")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query


def generate_response(prompt):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=4000,
        temperature=0.5
    )
    return response.choices[0].text.strip()


def greetMe():
    hour  = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning,mam")
    elif hour >12 and hour<=18:
        speak("Good Afternoon ,mam")

    else:
        speak("Good Evening,mam")

    speak("I am Jarvis, an AI Voice assistant. Please tell me, How can I help you mam?")


def game_play():
    speak("Lets Play ROCK PAPER SCISSORS !!")
    print("LETS PLAYYYYYYYYYYYYYY")
    i = 0
    Me_score = 0
    Com_score = 0
    while(i<5):
        choose = ("rock","paper","scissors") #Tuple
        com_choose = random.choice(choose)
        query = takeCommand().lower()
        if (query == "rock"):
            if (com_choose == "rock"):
                speak("ROCK")
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            elif (com_choose == "paper"):
                speak("paper")
                Com_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            else:
                speak("Scissors")
                Me_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")

        elif (query == "paper" ):
            if (com_choose == "rock"):
                speak("ROCK")
                Me_score += 1
                print(f"Score:- ME :- {Me_score+1} : COM :- {Com_score}")

            elif (com_choose == "paper"):
                speak("paper")
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            else:
                speak("Scissors")
                Com_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")

        elif (query == "scissors" or query == "scissor"):
            if (com_choose == "rock"):
                speak("ROCK")
                Com_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            elif (com_choose == "paper"):
                speak("paper")
                Me_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            else:
                speak("Scissors")
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
        i += 1
    print(f"FINAL SCORE :- ME :- {Me_score} : COM :- {Com_score}")
    if Me_score > Com_score:
        speak("Congratulations mam!, You won!")
    elif Me_score == Com_score:
        speak("Hurray! it's a tie!")
    else:
        speak("Oh! i won, Congrats to me! lol!")


def get_weather(city):
    api_key = "b977345bf10ea32346053de5a7f55568"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    print("HTTP Status Code: ", response.status_code)
    data = response.json()
    print("Response Data: ", data)
    if data["cod"] == 200:
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        return f"The weather in {city} is {weather_description}. The temperature is {temperature}°C with humidity {humidity}% and wind speed {wind_speed} m/s."
    else:
        return "Unable to fetch weather information."
    

def translate_and_speak(query):
    speak("SURE MAM")
    print(googletrans.LANGUAGES)  
    
    speak("Choose the language in which you want to translate")
    b = input("To_Lang :- ")
    translator = Translator()   
    text_to_translate = translator.translate(query, src='auto', dest= b)
    text = text_to_translate.text
    try: 
        speak_gl = gTTS(text=text, lang=b, slow=False)
        speak_gl.save("voice.mp3")
        playsound("voice.mp3")
        time.sleep(5)
        os.remove("voice.mp3")
    except Exception as e:
        print("Unable to translate:", e)
