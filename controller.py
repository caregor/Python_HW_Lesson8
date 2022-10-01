import models
import view


def main():
    while True:
        mode = view.mode()

        match mode:
            case '1':
                data = view.get_data()
                ok = models.insert_empl(data)
                view.say_done(ok)
            case '2':
                find_person = view.find_empl()
                models.get_empl(find_person)
            case '3':
                 data = view.find_empl()
                 models.del_empl(data)
            case _:
                 break
