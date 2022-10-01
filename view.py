

def mode():
    choose_mode = input('What you want to do (1- add new employee; 2- find existing employee; 3- delete employer;)\n or any buttom for exit:')
    return choose_mode


def get_data():
    return input('Insert new employee(First name, Last name, Job title, Salary): ')

def say_done(boll):
    if boll:
        print('Done!')
    else:
        print('Something wrong!')

def find_empl():
    return input('Insert last name:')