import pyttsx3

engine=pyttsx3.init()
engine.say("hello i am new college assistant how may i help you")

voice=engine.getProperty('voices')
engine.setProperty('voices',voice[1].id)
engine.runAndWait()
