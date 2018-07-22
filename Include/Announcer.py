import win32com.client
from multiprocessing import Process as Pc


def speak(string, number=1):
    spk = win32com.client.Dispatch("SAPI.SpVoice")
    for i in range(number):
        spk.Speak(string)


def speak_thread(string, number=1):
    Pc(target=speak, args=(string, number)).start()
