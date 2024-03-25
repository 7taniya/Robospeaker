import pyttsx3

if __name__ == '__main__':
    print("Welcome to Robospeaker 2.O created by Taniya")

    engine = pyttsx3.init()
    #This line initializes a text-to-speech engine.
    # The init() function initializes the text-to-speech engine
    # with the default settings. It returns an instance of the pyttsx3.
    # Engine class, which you can use to control and
    # interact with the text-to-speech engine.

    while True:
        x = input("Enter what you want me to speak: ")

        if x == "q":
            break

        engine.say(x)
        engine.runAndWait()

        #After initializing the engine, you can use it to
        # convert text (x in this case) to speech using the say method.
        # The runAndWait method is then called to wait for the speech to be
        # completed before proceeding with the next line of code.
        #So, the initialization step is necessary to set up the text-to-speech
        # engine before using it to convert text into spoken words.


        #Think of this as setting up a robot speaker.
        # You're creating a robot (named 'engine') that can talk,
        # and you're giving it the basic instructions on how to start.
        #So, in simple terms, these lines help you use a tool (pyttsx3)
        # to make your computer say things out loud.
        # The engine = pyttsx3.init() line is like turning on the talking robot,
        # and the engine.say(x) line is like telling the robot what to say.

