import model
import view

def start():
    model.set_class(view.input_class())
    model.set_subject(view.input_subject())
    model.open_file()
    student = ''
    while True:
        journal = model.get_journal()
        view.list_of_child(journal)
        student = view.who_answer()
        if student == 'exit':
            break
        elif student not in journal:
            view.student_check()
            break
        mark = int(view.what_mark())
        if mark < 1 or mark > 5:
            view.mark_check()
            break
        model.student_mark(student, mark)
        save_mark = view.mark_deleting()
        if save_mark == 'нет':
            model.delete_mark(student)
    model.save_file()