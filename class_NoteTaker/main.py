import json
from datetime import datetime
import speech_recognition as sr

# Made purely so that all words that are said my lecturer online are written
# into a json file and i can read it later.

r = sr.Recognizer()
run = True
data = {}
with open("/home/mark/programs/python_programs/class_NoteTaker/notepad.json", 'r') as f:
    data = json.load(f)

while run:
    with sr.Microphone() as source:
        print("Working")
        audio_text = r.listen(source)
        print("Done")
        try:
            text = r.recognize_google(audio_text)
            print(json.dumps(data, indent=4))
            # Create Json file
            now = datetime.now()
            timestamp = datetime.timestamp()
            data["Notes"].append({
                str(timestamp): text
            })

            with open("notepad.json", w) as outfile:
                outfile.write(json.dumps(data, indent=4))
        except KeyboardInterrupt:
            print("Stopping")
        except:
            print("Error")
            run = False
