# print Poem
print(''' if the text is long then we can use like 
      this also . we can use single quotes to print the 
      large text ''')


# using external module (i am using text to speach converter)
import pyttsx3
engine = pyttsx3.init()
engine.say(" enter the text ")
engine.runAndWait()
