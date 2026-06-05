import win32com.client
import time

print("Connecting to Skype")

skype = win32com.client.Dispatch("Skype4COM.Skype")
skype.Attach()

print("Connected to Skype")

chat = skype.ActiveChat

# Fake login message
chat.SendMessage("Logged in offline mode")

print("Listening for messages")

last_message = ""

while True:
    try:
        messages = chat.Messages
        if messages.Count > 0:
            msg = messages[messages.Count]
            if msg.Body != last_message and msg.FromHandle != skype.CurrentUserHandle:
                last_message = msg.Body
                print("You typed: ", msg.Body)

                # Echo reply
                chat.SendMessage("[Echo] " + msg.Body)

        time.sleep(1)

    except Exception as e:
        print("Error: ", e)
        time.sleep(2)
