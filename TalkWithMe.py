import pyttsx3 #importando biblioteca responsável pela fala do pc
import speech_recognition as sr #importar biblioteca responsável pelo reconhecimento de voz

fala = pyttsx3.init() #atribuindo inicialização para engine

escreva = input("Você quer digitar e eu falo? [S/N] ")

def reconhecer_fala():   #definindo o que o programa vai fazer caso o usuário digite 'N ou n'
    microfone = sr.Recognizer() #Habilita o microfone
    with sr.Microphone() as source:        
        microfone.adjust_for_ambient_noise(source)#Reducao de ruido disponivel na speech_recognition        
        print("Diga alguma coisa: ")        
        audio = microfone.listen(source) #guarda o audio falado na variavel 'audio', o audio é finalizado nas pausas grandes
        try:
            frase = microfone.recognize_google(audio,language='pt-BR') #audio sera interpretado na lingua portuguesa            
            print("Você disse: " + frase)        
        except:
            print("Não entendi o que você disse!")
        return frase


if escreva == "S" or escreva == "s":
    while True:
        frase = input("Coloque a frase que deseja ouvir: ")

        fala.say(frase)  # mostrando a frase que o pc vai falar

        fala.runAndWait()  # vai executar e esperar

else:
    while True:

        fala.say("Agora você pode falar, e eu, escreverei o que falar.")
        fala.runAndWait()
        reconhecer_fala()
        

