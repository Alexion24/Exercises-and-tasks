import random

answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да',
           'Можешь быть уверен в этом', 'Мне кажется - да', 'Вероятнее всего',
           'Хорошие перспективы', 'Знаки говорят - да', 'Да',
           'Пока неясно, попробуй снова', 'Спроси позже',
           'Лучше не рассказывать', 'Сейчас нельзя предсказать',
           'Сконцентрируйся и спроси опять', 'Даже не думай',
           'Мой ответ - нет', 'По моим данным - нет', '	Перспективы не очень хорошие',
           'Весьма сомнительно']


def answer():
    return random.choice(answers)


def answer_for_continue(final_answer):
    return final_answer == 'да' or final_answer == 'нет'


def ask_name():
    print('Привет! Я магический шар и я знаю ответ на любой ваш вопрос.\n')
    print('Как я могу к вам обращаться?')
    name = input()
    print(f'Привет, {name}!')


def ask_question():
    print('Что бы вы хотели узнать?')
    input()
    print(answer())


def ask_user_for_continue():
    while True:
        print('Хочешь задать ещё вопрос? да/нет')
        final_answer = input()
        if not answer_for_continue(final_answer):
            print('Ввведи "да" или "нет", я верю, что у тебя получится!')
        if final_answer.lower() == 'да':
            ask_question()
        if final_answer.lower() == 'нет':
            print('Возвращайся если возникнут вопросы!')
            break


ask_name()
ask_question()
ask_user_for_continue()
