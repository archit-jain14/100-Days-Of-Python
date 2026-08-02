import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
names = ["Rahul", "Rohan", "Priya", "Amit", "Neha"]

for name in names:
    shoutout = f"Shoutout to {name}"
    print(shoutout)
    speaker.Speak(shoutout)
