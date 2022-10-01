from peewee import *

db = SqliteDatabase('database.db')


class Employee(Model):
    id = PrimaryKeyField(unique=True)
    first_name = CharField()
    last_name = CharField()
    job_title = CharField()
    salary = CharField()

    class Meta:
        database = db
        order_by = 'id'
        db_table = 'employers'


def insert_empl(data):
    with db:
        tmp = data.split()

        try:
            data_dict = [
                {'first_name': tmp[0].capitalize(), 'last_name': tmp[1].capitalize(), 'job_title': tmp[2],
                 'salary': tmp[3]}]
            Employee.insert_many(data_dict).execute()
            return True
        except:
            return False


def get_empl(data):
    with db:
        employers = Employee.get(Employee.last_name == data.capitalize())
        print(employers.id, employers.first_name, employers.last_name, employers.job_title, employers.salary)


def del_empl(data):
    with db:
        try:
            empl = Employee.get(Employee.last_name == data.capitalize())
            empl.delete_instance()
            print('Done')
        except:
            print('Cant find employer')
