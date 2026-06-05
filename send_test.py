import Skype4Py

skype = Skype4Py.Skype()
skype.Attach()

chat = skype.Chat("test_chat")
chat.SendMessage("Hello")

raw_input("Press enter to exit")
