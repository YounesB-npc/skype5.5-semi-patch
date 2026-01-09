import Skype4Py

skype = Skype4Py.Skype()
skype.Attach()

chat = skype.Chat("test_chat")
chat.SendMessage("Hello from Python")

raw_input("Press Enter to exit...")
