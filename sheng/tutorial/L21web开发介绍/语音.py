import pyttsx3
# 初始化， 必须要有奥
engine = pyttsx3.init()
engine.say('hello')
# 注意，没有本句话是没有声音的
engine.runAndWait()
