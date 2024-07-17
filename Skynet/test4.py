import YouTubeMusicAPI
import pyttsx3
import pvporcupine
import struct
import pyaudio
import pymorphy2
import sys
import vosk
import sounddevice as sd
import queue
import speech_recognition as sr
import datetime
import time
import os
import webbrowser
from pyowm import OWM
from pyowm.utils.config import get_default_config
import rem
h1 = ['привет', 'добрый день', 'добрый вечер', 'доброе утро']
br = ['хватит', 'пока', 'закройся', 'спокойной', 'ночи']
tm = ['время', 'времени']
datar = ['дата', 'число', 'даты', 'дату', 'датой', 'дате']
music=['включи']
prog=['программу']
good=['молодец', 'спасибо']
youtube=['ютуб']
sh=['поиск', 'поиска', 'найти', 'найди']
wt=['погода', 'погоду']
tw=['москва', 'санкт','петербург', 'санкт-петербург', 'ростов', 'на', 'дону', 'ростов-на-дону', 'дорохов', 'петрищев']
lg=['английская', 'английской', 'раскладка', 'раскладке']
sm=['напоминание']
music_search=['музыка', 'музыку']
h2=['hello']
br2=['break', 'goodbye']
tm2=['time']
datar2=['date']
music2=['music']
good2=['well', 'thanks']
youtube2=['youtube']
sh2=['searching']
r = sr.Recognizer()
engine = pyttsx3.init()
print("Skynet к Вашим услугам")
engine.say("Скайнэт к Вашим услугам")
engine.runAndWait()
model_ru = vosk.Model("model-small ru")
model_en = vosk.Model("model-small en")
samplerate = 16000
device = 1
q = queue.Queue()
def recognize_number():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Говорите")
        audio = r.listen(source)
    try:
        number = r.recognize_google(audio, language="ru-RU")
        print(number)
        return number
    except sr.UnknownValueError:
        return "Не удалось распознать речь"
    except sr.RequestError as e:
        print("Ошибка сервиса распознавания речи; {0}".format(e))
def q_callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

def listen(qe):
    with sd.RawInputStream(samplerate=samplerate, blocksize=8000, device=device, dtype='int16', channels=1,
                           callback=q_callback):
        rec = vosk.KaldiRecognizer(model_ru, samplerate)
        while qe:
            m = []
            data = q.get()
            if rec.AcceptWaveform(data):
                text = rec.Result()
                txt = text.split()
                for j in range(len(txt)):
                    if txt[j] != '{' and txt[j] != '"text"' and txt[j] != '}' and txt[j] != ':':
                        m.append(txt[j])
                for k in range(len(m)):
                    m[k] = m[k].replace('"', '')
                for i in range(len(m)):
                    for j in range(len(m)):
                        if i != j:
                            if m[i] == m[j]:
                                m[j] = ''
                return m
def sound_and_text(text_to_speech):
    engine.say(text_to_speech)
    engine.runAndWait()
def contains_russian_letters(string):
    russian_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    for char in string:
        if char.lower() in russian_letters:
            return True
    return False
keyword_path = 'Sky-Net_en_windows_v2_2_0.ppn'
access_key = 'EOFYtgI9KTqgFhzVxsCg2siqvbaw3FMdEdFwR14o+U6ZOL/Jv5qvMg=='
porcupine = pvporcupine.create(keyword_paths=[keyword_path], access_key=access_key)
sample_rate = porcupine.sample_rate
chunk_size = porcupine.frame_length
# Создание экземпляра PyAudio
pa = pyaudio.PyAudio()
stream = pa.open(rate=sample_rate, channels=1, format=pyaudio.paInt16, input=True,
                 output=False, frames_per_buffer=chunk_size)
# Запуск потока
stream.start_stream()
xz=0
while True:
    while True:
        g=True
        r=True
        while stream.is_active():
            if xz!=0:
                import rem_man
                cc = True
                rem_man.remind_man(cc)
            in_data=stream.read(chunk_size)
            pcm = struct.unpack_from("h" * chunk_size, in_data)
            keyword_index = porcupine.process(pcm)
            if keyword_index >= 0:
                print("Да, создатель")
                engine = pyttsx3.init()
                engine.say("Да, создатель")
                engine.runAndWait()
                break
        while True:
            filename="C:\\Users\\ВАЛЕРА\\PycharmProjects\\Skynet\\reminder.txt"
            import rem_man
            cc=True
            rem_man.remind_man(cc)
            g=True
            r=True
            qe=True
            m_ru=listen(qe)
            if m_ru!=['']:
                print(" ".join(m_ru))
            for i in m_ru:
                if 'спасибо' in m_ru and 'пока' in m_ru:
                    print('Не за что, создатель. До скорой встречи!')
                    engine = pyttsx3.init()
                    engine.say('Не за что, создатель. До скорой встречи!')
                    engine.runAndWait()
                    exit()
                if i in h1:
                    print("Доброго времени суток, создатель")
                    engine = pyttsx3.init()
                    engine.say("Доброго времени суток, создатель")
                    engine.runAndWait()
                    break
                if i in br:
                    print("Всего доброго, создатель")
                    engine = pyttsx3.init()
                    engine.say("Всего доброго, создатель")
                    engine.runAndWait()
                    exit()
                if i in tm:
                    print("Сейчас: " + datetime.datetime.now().strftime("%H:%M"))
                    engine = pyttsx3.init()
                    engine.say("Сейчас: " + datetime.datetime.now().strftime("%H:%M"))
                    engine.runAndWait()
                    break
                if i in datar:
                    print("Сегодня: " + str(datetime.date.today().strftime("%d.%m.%Y")))
                    engine = pyttsx3.init()
                    engine.say("Сегодня: " + str(datetime.date.today().strftime("%d.%m.%Y")))
                    engine.runAndWait()
                    break
                if m_ru[0] in music and m_ru[1] in prog:
                    import open_app
                    open_app.opena()
                    break
                if i in good:
                    print("Всегда к Вашим услугам")
                    engine = pyttsx3.init()
                    engine.say("Всегда к Вашим услугам")
                    engine.runAndWait()
                    g=False
                    break
                if i in youtube:
                    print("Включаю")
                    engine = pyttsx3.init()
                    engine.say("Включаю")
                    engine.runAndWait()
                    opera = 'C:/Users/ВАЛЕРА/AppData/Local/Programs/Opera/launcher.exe %s'
                    webbrowser.get(opera).open("https://www.youtube.com")
                    break
                if m_ru[0]=='включи' and m_ru[1]=='музыку':
                    engine = pyttsx3.init()
                    engine.say("Говорите")
                    engine.runAndWait()
                    txt=recognize_number()
                    query: str = txt
                    result = YouTubeMusicAPI.Search(query)
                    if result:
                        print(result.get('trackUrl'))
                        webbrowser.open(result.get('trackUrl'))
                    else:
                        print("No Result Found")
                    break
                if i in sh:
                    if 'поиск' in m_ru:
                        m_ru.remove('поиск')
                    if 'найди' in m_ru:
                        m_ru.remove('найди')
                    if 'найти' in m_ru:
                        m_ru.remove('найти')
                    if 'мне' in m_ru:
                        m_ru.remove('мне')
                    print('Ваш запрос: ' + " ".join(m_ru))
                    sound_and_text('Ваш запрос: ' + " ".join(m_ru))
                    print('Правильно?')
                    sound_and_text('Правильно?')
                    while True:
                        jk=True
                        vn=recognize_number()
                        if vn=='да':
                            k=" ".join(m_ru)
                            webbrowser.open(
                                f'https://yandex.ru/search/?text={k}&clid=9403&search_source=dzen_desktop_safe&lr=213')
                            break
                        if vn=='нет':
                            while True:
                                print('Скажите ваш запрос (без слов "поиск", "найти", "найди"):')
                                sound_and_text('Скажите ваш запрос')
                                hg=recognize_number()
                                if hg=='':
                                    print('Повторите запрос')
                                    continue
                                if hg!='':
                                    print('Ваш запрос: ' + hg)
                                    sound_and_text('Ваш запрос: ' + hg)
                                    print('Правильно?')
                                    sound_and_text('Правильно?')
                                    while True:
                                        jk=True
                                        vn = recognize_number()
                                        if vn == 'да':
                                            k=hg
                                            webbrowser.open(f'https://yandex.ru/search/?text={k}&clid=9403&search_source=dzen_desktop_safe&lr=213')
                                            jk=False
                                            break
                                        if vn=='нет':
                                            print('Ещё раз')
                                            break
                                    if jk==False:
                                        break
                        if jk==False:
                            break
                if "английской" in m_ru or "английская" in m_ru and ("раскладка" in m_ru or "раскладке" in m_ru):
                    print('English keyboard has been turned on')
                    engine = pyttsx3.init()
                    voices = engine.getProperty('voices')
                    en_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
                    engine.setProperty('voice', en_voice_id)
                    engine.say('English keyboard has been turned on')
                    engine.runAndWait()
                    r = False
                    break
                if ('ближайшее' in m_ru or 'ближайший' in m_ru or 'ближайшие' in m_ru) and (
                        'напоминание' not in m_ru or 'напоминанием' not in m_ru or 'запоминанием' not in m_ru or 'упоминанием' not in m_ru) and len(m_ru) != 2:
                    break
                if ('ближайшее' in m_ru or 'ближайший' in m_ru or 'ближайшие' in m_ru) and (
                        'напоминание' in m_ru or 'напоминанием' in m_ru or 'запоминанием' or m_ru or 'упоминанием' in m_ru) and len(m_ru)==2:
                    cc = True
                    bn = rem_man.remind_man(cc)
                    if bn == None:
                        print('Запланированных задач нет')
                        sound_and_text('Запланированных задач нет')
                        break
                    else:
                        ga = 0
                        dv=[]
                        for i in range(len(bn[0])):
                            if '@' in bn[0][i]:
                                ga = i
                                break
                        if ga != 0:
                            sa = bn[1][-1]
                            kj=bn[0]
                            kj = kj.replace(sa, '')
                            kj = kj.replace('Напоминание', 'напоминание')
                            print('Ближайшее '+ kj[3:])
                            sound_and_text('Ближайшее '+ kj[3:])
                        if ga==0:
                            kj=bn[0]
                            kj=kj.replace('Напоминание', 'напоминание')
                            print('Ближайшее '+ kj[3:])
                            sound_and_text('Ближайшее ' + kj[3:])
                        break
                elif i in sm:
                    qe=False
                    rem.remind(i)
                qe=True
                if i in wt:
                    ww=[]
                    for j in m_ru:
                        config_dict = get_default_config()
                        config_dict['language'] = 'ru'
                        morph = pymorphy2.MorphAnalyzer()
                        word=j
                        parsedword = morph.parse(word)[0]
                        if "PREP" in parsedword.tag and j in tw:
                            ww.append(j)
                            continue
                        if "PREP" in parsedword.tag and j not in tw:
                            continue
                        parsed_word = morph.parse(word)[0]
                        cases = ["nomn", "gent", "datv", "accs", "ablt", "loct"]
                        u = []
                        for case in cases:
                            inflected_word = parsed_word.inflect({case})
                            if inflected_word is not None:
                                u.append(inflected_word.word)
                        if len(u)==0 and j in tw:
                            ww.append(j)
                            continue
                        if len(u)==0 and j not in tw:
                            continue
                        else:
                            if j in tw and j=='дону':
                                ww.append(u[2])
                        if u[0] in tw:
                            ww.append(u[0])
                    if len(ww)==0:
                        print('Повторите запрос')
                        engine = pyttsx3.init()
                        engine.say('Повторите запрос')
                        engine.runAndWait()
                    else:
                        place=ww[0]
                        vil=False
                        if ('дорохов' in ww):
                            place='Дорохово'
                        if ('петрищев' in ww):
                            place='Петрищево'
                            vil=True
                        if ('санкт' in ww and 'петербург' in ww) or ('санкт-петербург' in ww):
                            place='Санкт-Петербург'
                        if ('ростов' in ww and 'на' in ww and 'дону' in ww) or ('ростов-на-дону' in ww):
                            place='Ростов-на-Дону'
                        country = 'RU'
                        country_and_place = place + ", " + country
                        owm = OWM('386be372473f69f15991d1a053f1614c')
                        mgr = owm.weather_manager()
                        observation = mgr.weather_at_place(country_and_place)
                        w = observation.weather
                        status = w.detailed_status
                        w.wind()
                        humidity = w.humidity
                        temp = w.temperature('celsius')['temp']
                        if place!='Ростов-на-Дону' and place!='Санкт-Петербург' and vil==False:
                            print("В городе " + str(place).capitalize() + " сейчас " + str(status) +
                                  "\nТемпература " + str(
                                round(temp)) + " градусов по цельсию" +
                                  "\nВлажность составляет " + str(humidity) + "%" +
                                  "\nСкорость ветра " + str(w.wind()['speed']) + " метров в секунду")
                            engine = pyttsx3.init()
                            engine.say("В городе " + str(place).capitalize() + " сейчас " + str(status) +
                                  "\nТемпература " + str(
                                round(temp)) + " градусов по цельсию" +
                                  "\nВлажность составляет " + str(humidity) + "%" +
                                  "\nСкорость ветра " + str(w.wind()['speed']) + " метров в секунду")
                            engine.runAndWait()
                        if place == 'Ростов-на-Дону' or place == 'Санкт-Петербург' and vil == False:
                            print("В городе " + str(place) + " сейчас " + str(status) +
                                  "\nТемпература " + str(
                                round(temp)) + " градусов по цельсию" +
                                  "\nВлажность составляет " + str(humidity) + "%" +
                                  "\nСкорость ветра " + str(w.wind()['speed']) + " метров в секунду")
                            engine = pyttsx3.init()
                            engine.say("В городе " + str(place) + " сейчас " + str(status) +
                                       "\nТемпература " + str(
                                round(temp)) + " градусов по цельсию" +
                                       "\nВлажность составляет " + str(humidity) + "%" +
                                       "\nСкорость ветра " + str(w.wind()['speed']) + " метров в секунду")
                            engine.runAndWait()
                        if place != 'Ростов-на-Дону' and place != 'Санкт-Петербург' and vil == True:
                            print("В деревне " + str(place).capitalize() + " сейчас " + str(status) +
                                  "\nТемпература " + str(
                                round(temp)) + " градусов по цельсию" +
                                  "\nВлажность составляет " + str(humidity) + "%" +
                                  "\nСкорость ветра " + str(w.wind()['speed']) + " метров в секунду")
                            engine = pyttsx3.init()
                            engine.say("В деревне " + str(place).capitalize() + " сейчас " + str(status) +
                                  "\nТемпература " + str(
                                round(temp)) + " градусов по цельсию" +
                                  "\nВлажность составляет " + str(humidity) + "%" +
                                  "\nСкорость ветра " + str(w.wind()['speed']) + " метров в секунду")
                            engine.runAndWait()
            if g==False:
                break
            if r==False:
                break
        if g == False:
            xz=1
            continue
        if r == False:
            break
    while True:
        r = True
        keyword_path = 'Sky-Net_en_windows_v2_2_0.ppn'
        access_key = 'EOFYtgI9KTqgFhzVxsCg2siqvbaw3FMdEdFwR14o+U6ZOL/Jv5qvMg=='
        porcupine = pvporcupine.create(keyword_paths=[keyword_path], access_key=access_key)
        sample_rate = porcupine.sample_rate
        chunk_size = porcupine.frame_length
        # Создание экземпляра PyAudio
        pa = pyaudio.PyAudio()
        stream = pa.open(rate=sample_rate, channels=1, format=pyaudio.paInt16, input=True,
                         output=False, frames_per_buffer=chunk_size)
        stream.start_stream()
        while stream.is_active():
            in_data=stream.read(chunk_size)
            pcm = struct.unpack_from("h" * chunk_size, in_data)
            keyword_index = porcupine.process(pcm)
            if keyword_index >= 0:
                print("Yes, creator")
                engine = pyttsx3.init()
                engine.say("Yes, creator")
                engine.runAndWait()
                break
        with sd.RawInputStream(samplerate=samplerate, blocksize=8000, device=device, dtype='int16', channels=1,
                               callback=q_callback):
            rec_en = vosk.KaldiRecognizer(model_en, samplerate)
            while True:
                g = True
                m = []
                m_ru = []
                m_en = []
                data = q.get()
                if rec_en.AcceptWaveform(data):
                    text_en = rec_en.Result()
                    txt_en = text_en.split()
                    for j in range(len(txt_en)):
                        if txt_en[j] != '{' and txt_en[j] != '"text"' and txt_en[j] != '}' and txt_en[j] != ':':
                            m_en.append(txt_en[j])
                    for k in range(len(m_en)):
                        m_en[k] = m_en[k].replace('"', '')
                    for i in range(len(m_en)):
                        for j in range(len(m_en)):
                            if i != j:
                                if m_en[i] == m_en[j]:
                                    m_en[j] = ''
                    print(m_en)
                    k = " ".join(m_en)
                    print(" ".join(m_en))
                    for i in m_en:
                        if i in h2:
                            print("Good day, creator")
                            engine = pyttsx3.init()
                            engine.say("Good day, creator")
                            engine.runAndWait()
                            break
                        if i in br2:
                            print("All the best, creator")
                            engine = pyttsx3.init()
                            engine.say("All the best, creator")
                            engine.runAndWait()
                            exit()
                        if i in tm2:
                            print("Now: " + str(time.localtime().tm_hour) + ":" + str(time.localtime().tm_min))
                            engine = pyttsx3.init()
                            engine.say("Now: " + str(time.localtime().tm_hour) + ":" + str(time.localtime().tm_min))
                            engine.runAndWait()
                            break
                        if i in datar2:
                            print("Now: " + str(datetime.date.today()))
                            engine = pyttsx3.init()
                            engine.say("Now: " + str(datetime.date.today()))
                            engine.runAndWait()
                            break
                        if i in music2:
                            print("Turning on")
                            engine = pyttsx3.init()
                            engine.say("Turning on")
                            engine.runAndWait()
                            os.startfile('C:/Users/ВАЛЕРА/Desktop/Яндекс.Музыка - Ярлык.lnk')
                            break
                        if i in good2:
                            print("Always at your service")
                            engine = pyttsx3.init()
                            engine.say("Always at your service")
                            engine.runAndWait()
                            g = False
                            break
                        if i in youtube2:
                            print("Turning on")
                            engine = pyttsx3.init()
                            engine.say("Turning on")
                            engine.runAndWait()
                            opera = 'C:/Users/ВАЛЕРА/AppData/Local/Programs/Opera/launcher.exe %s'
                            webbrowser.get(opera).open("https://www.youtube.com")
                            break
                        if i in sh2:
                            m_en.remove(i)
                            k = " ".join(m_en)
                            webbrowser.open(f'https://yandex.ru/search/?text={k}&clid=9403&search_source=dzen_desktop_safe&lr=213')
                        if "russian" in m_en and "keyboard" in m_en:
                            print("Русская раскладка включена")
                            engine = pyttsx3.init()
                            voices = engine.getProperty('voices')
                            en_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0'
                            engine.setProperty('voice', en_voice_id)
                            engine.say('Русская раскладка включена')
                            engine.runAndWait()
                            r = False
                            g = False
                            break
                    if g == False:
                        break
        if r == False:
            break
