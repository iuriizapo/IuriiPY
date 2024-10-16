def proverka_sobaka(a):    # Функция проверки электронного адреса на
    a = a.lower()          # наличие "@" и оканчания ".com"/".ru"/".net"
    b = list(a)
    sobaka = 0
    for i in b:
        if i == '@':
            sobaka += 1

    domen = 0
    if b[-3:] == ['.', 'r', 'u']:
        domen += 1
    elif b[-4:] == ['.', 'n', 'e', 't'] or b[-4:] == ['.', 'c', 'o', 'm']:
        domen += 1

    if sobaka == 1 and domen == 1:
        result = True
    else:
        result = False
    return result

def send_email(message, recipient,*, sender = "university.help@gmail.com"):
    if proverka_sobaka(recipient) == True and proverka_sobaka(sender) == True:
        if recipient != sender:
            if sender != "university.help@gmail.com":
                print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, 'на адрес', recipient)
            else:
                print("Письмо успешно отправлено с адреса", sender, 'на адрес', recipient)

        else:
            print("Нельзя отправить письмо самому себе!")
    else:
        print('Невозможно отправить письмо с адреса ', sender, 'на адрес ', recipient)


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
