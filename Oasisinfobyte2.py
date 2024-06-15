import speech_recognition as sr
import datetime
import webbrowser

def respond(text):
    print(text)

def get_time():
    now = datetime.datetime.now()
    respond(f"The current time is {now.hour} hours and {now.minute} minutes.")

def get_date():
    now = datetime.datetime.now()
    respond(f"Today's date is {now.day} {now.month} {now.year}.")

def search_web(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

def main():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print(f"You said: {text}")

        if "hello" in text.lower():
            respond("Hello! How can I assist you today?")
        elif "time" in text.lower():
            get_time()
        elif "date" in text.lower():
            get_date()
        else:
            search_web(text)

    except sr.UnknownValueError:
        print("Sorry, I didn't understand what you said.")
    except sr.RequestError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()