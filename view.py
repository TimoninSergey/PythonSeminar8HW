import model  #Зачем? из нее вроде ничего не имортится, да и нельзя связывать модел и вью. Оставил на всякий случай.

def input_class():
    return input('С каким классом работаем? ').upper()

def input_subject():
    return input('Какой предмет? ').lower()

def who_answer():
    return input('Кто будет отвечать? ')

def what_mark():
    return input('На какую оценку ответил? ')

def list_of_child(journal: dict):
    for i, child in enumerate(journal, 1):
        print(f'{i}. {child:20} {journal.get(child)}')

def student_check():
    print('Такого ученика нет, для продолжения перезапустите программу.')

def mark_check():
    print('Оценка должна быть от 1 до 5, для продолжения перезапустите программу.')

def mark_deleting():
    return input('Сохранить оценку? ').lower()