import json
from difflib import get_close_matches

podcasts = json.load(open("podcast_list.json"))


def retrive_definition(word):
    word = word.lower()
    if word in podcasts:
        return podcasts[word]
    elif word.title() in podcasts:
        return podcasts[word.title()]
    elif word.upper() in podcasts:
        return podcasts[word.upper()]
    elif len(get_close_matches(word, podcasts.keys(), n=4, cutoff=0.3)) > 0:
        from main import speak, take_user_input
        speak("Did you mean %s instead? Yes or No?: " % get_close_matches(word, podcasts.keys(), n=4, cutoff=0.3)[0])
        query = take_user_input().lower()
        if query == "yes":
            return podcasts[get_close_matches(word, podcasts.keys(), n=4, cutoff=0.3)[0]]
        elif query == "no":
            speak("Would you like to try again?")
            query = take_user_input().lower()
            if query == "yes":
                from main import podcast
                podcast()
            elif query == "no":
                from main import speak
                speak("The Podcast Doesn't Exist.")
    else:
        from main import speak
        speak("The Podcast Doesn't Exist.")
        return None
