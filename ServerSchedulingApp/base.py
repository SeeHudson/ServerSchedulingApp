import os
import django
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ServerSchedulingApp.settings')
django.setup()

from Scheduler.models import *
from django.core.management import call_command
from django.db import connection


def reset_app(app_name):
    # First, disable foreign key checks
    cursor = connection.cursor()
    if connection.vendor == 'sqlite':
        cursor.execute('PRAGMA foreign_keys = OFF;')
    elif connection.vendor == 'mysql':
        cursor.execute('SET FOREIGN_KEY_CHECKS = 0;')

    # Then, flush the database to drop all tables
    call_command('flush', interactive=False)

    # Finally, re-enable foreign key checks
    if connection.vendor == 'sqlite':
        cursor.execute('PRAGMA foreign_keys = ON;')
    elif connection.vendor == 'mysql':
        cursor.execute('SET FOREIGN_KEY_CHECKS = 1;')


def insert_data():
    # Create Restaurant
    restaurant = Restaurant.objects.create(restaurant_name='Grand Cafe', address='1234 Main St', city='San Francisco', zip='94111')

    # Create Users
    user1 = User.objects.create_user(username='employee_user1', password='BlahBlah', role='EMPLOYEE', first_name='John',
                                     last_name='Doe', restaurant=restaurant)

    user2 = User.objects.create_user(username='employee_user2', role='EMPLOYEE', first_name='Sophia',
                                     last_name='Curtis', restaurant=restaurant)
    user3 = User.objects.create_user(username='employee_user3', role='EMPLOYEE', first_name='Jaden',
                                     last_name='Wallace', restaurant=restaurant)
    user4 = User.objects.create_user(username='employee_user4', role='EMPLOYEE', first_name='Tiffany', last_name='Liu', restaurant=restaurant)
    user_manager = User.objects.create_user(username='manager_user', role='MANAGER', first_name='Alice',
                                            last_name='Smith', restaurant=restaurant)

    # Create Employee and Manager
    employee1 = Employee.objects.create(user=user1, score1=4, score2=3, score3=5, score4=2, score5=4, average_score=3.6)
    employee2 = Employee.objects.create(user=user2, score1=3, score2=4, score3=5, score4=3, score5=4, average_score=3.8)
    employee3 = Employee.objects.create(user=user3, score1=5, score2=4, score3=5, score4=4, score5=5, average_score=4.6)
    employee4 = Employee.objects.create(user=user4, score1=4, score2=5, score3=5, score4=4, score5=5, average_score=4.6)
    manager = Manager.objects.create(user=user_manager)

    # Create Shifts
    shift1 = Shift.objects.create(day='Mo', shift_type='Open')
    shift2 = Shift.objects.create(day='Mo', shift_type='Mid')
    shift3 = Shift.objects.create(day='Tu', shift_type='Open')
    shift4 = Shift.objects.create(day='Tu', shift_type='Mid')
    shift5 = Shift.objects.create(day='We', shift_type='Open')
    shift6 = Shift.objects.create(day='We', shift_type='Close')
    shift7 = Shift.objects.create(day='Th', shift_type='Open')
    shift8 = Shift.objects.create(day='Th', shift_type='Mid')
    shift9 = Shift.objects.create(day='Fr', shift_type='Open')

    # Assign Shifts to Employees
    EmployeeShift.objects.create(user=employee1, shift=shift1)
    EmployeeShift.objects.create(user=employee2, shift=shift1)
    EmployeeShift.objects.create(user=employee3, shift=shift1)
    EmployeeShift.objects.create(user=employee4, shift=shift2)
    EmployeeShift.objects.create(user=employee2, shift=shift2)
    EmployeeShift.objects.create(user=employee3, shift=shift2)
    EmployeeShift.objects.create(user=employee2, shift=shift3)
    EmployeeShift.objects.create(user=employee4, shift=shift4)
    EmployeeShift.objects.create(user=employee1, shift=shift5)
    EmployeeShift.objects.create(user=employee4, shift=shift6)
    EmployeeShift.objects.create(user=employee1, shift=shift7)
    EmployeeShift.objects.create(user=employee4, shift=shift8)
    EmployeeShift.objects.create(user=employee2, shift=shift9)


def delete_user(username):
    # Find the user you want to delete
    user = User.objects.filter(username=username).first()

    if user:
        # Delete the user
        user.delete()


if __name__ == '__main__':
    reset_app('Scheduler')
    insert_data()

    # For testing
    # delete_user('employee_user')
    # delete_user('manager_user')
