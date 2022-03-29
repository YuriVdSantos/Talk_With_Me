import pyttsx3 #importando biblioteca responsável pela fala do pc

fala = pyttsx3.init() #atribuindo inicialização para engine


while True:
    frase = input("Coloque a frase que deseja ouvir: ")

    fala.say(frase)  # mostrando a frase que o pc vai falar

    fala.runAndWait()  # vai executar e esperar