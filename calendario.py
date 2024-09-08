import requests
from icalendar import Calendar
from datetime import datetime
import pytz
import time
import pywhatkit as kit
import pyautogui
import emoji

feed_url = '  '# URL do feed iCal

def get_events():
    response = requests.get(feed_url)
    calendar = Calendar.from_ical(response.content)
    events = []

    now = datetime.now(pytz.utc)  # Obtém a data e hora atual no UTC

    for component in calendar.walk():
        if component.name == "VEVENT":
            start_time = component.get('dtstart').dt
            if start_time >= now:  # Filtra eventos a partir da data atual
                summary = component.get('summary')
                description = component.get('description', 'Sem descrição')
                events.append((start_time, summary, description))
    
    return events

def format_event(event):
    start_time, summary, description = event
    local_time = start_time.astimezone()
    return f"Evento: {summary} em {local_time.strftime('%d/%m/%Y às %I:%M %p')} - Descrição: {description}"

events = get_events()


def send_whatsapp_message(message, phone_number):
    now = time.localtime()  # Atualiza a obtenção da hora atual
    hour = now.tm_hour
    minute = now.tm_min + 1  # Envia a mensagem com um atraso de 1 minuto
    kit.sendwhatmsg(phone_number, message, hour, minute)

# Lista de números de telefone
phone_numbers = [
    "99999999", 
    "99999999", 
    "99999999", 

    # Adicione mais números conforme necessário
]

# whatsapp
for event in events:
    message = format_event(event)
    confirm = '!!!!!GENTILEZA CONFIRMAR RECEBIMENTO DO AGENDAMENTO!!!!'
    for number in phone_numbers:
        send_whatsapp_message(message, number)
        time.sleep(5)  # Aguarda 5 segundos entre o envio para números diferentes 
        pyautogui.click(-763, 980)  # Ajuste as coordenadas conforme necessário *instruções abaixo*
        pyautogui.press('Enter')
        time.sleep(2)
        pyautogui.write(confirm)
        time.sleep(2)
        pyautogui.press('Enter')



#Rode esse script para pegar a localização da aba de digitar a msg no whatsapp
#import pyautogui
#import time

#time.sleep(4)
#x= pyautogui.position()
#print(x)
