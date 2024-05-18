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
    restaurant = Restaurant.objects.create(restaurant_name='Grand Cafe', address='1234 Main St', city='San Francisco',
                                           zip='94111')
    # Create Users
    user1 = User.objects.create_user(username='JDoe@gmail.com', password='BlahBlah', role='EMPLOYEE', first_name='John',
                                     last_name='Doe', restaurant=restaurant, email='JDoe@gmail.com')
    user1.phone = '2621948562'
    user1.save()

    user2 = User.objects.create_user(username='SCurtis@gmail.com', password='BlahBlah', role='EMPLOYEE',
                                     first_name='Sophia',
                                     last_name='Curtis', restaurant=restaurant, email='SCurtis@gmail.com')
    user2.phone = '2623746502'
    user2.save()

    user3 = User.objects.create_user(username='JadenW@gmail.com', password='BlahBlah', role='EMPLOYEE',
                                     first_name='Jaden',
                                     last_name='Wallace', restaurant=restaurant, email='JadenW@gmail.com')
    user3.phone = '2625057683'
    user3.save()

    user4 = User.objects.create_user(username='TiffLiu@gmail.com', password='BlahBlah', role='EMPLOYEE',
                                     first_name='Tiffany',
                                     last_name='Liu', restaurant=restaurant, email='TiffLiu@gmail.com')
    user4.phone = '2623342845'
    user4.save()

    user5 = User.objects.create_user(username='MJohnson@gmail.com', password='BlahBlah', role='EMPLOYEE',
                                     first_name='Michael',
                                     last_name='Johnson', restaurant=restaurant, email='MJohnson@gmail.com')
    user5.phone = '2623374812'
    user5.save()

    user6 = User.objects.create_user(username='LCarter@gmail.com', password='BlahBlah', role='EMPLOYEE',
                                     first_name='Liam',
                                     last_name='Carter', restaurant=restaurant, email='LCarter@gmail.com')
    user6.phone = '262665830'
    user6.save()

    user7 = User.objects.create_user(username='EClark@gmail.com', password='BlahBlah', role='EMPLOYEE',
                                     first_name='Emma',
                                     last_name='Clark', restaurant=restaurant, email='EClark@gmail.com')
    user7.phone = '2623846222'
    user7.save()

    user_manager = User.objects.create_user(username='ASmith@gmail.com', password='BAS', role='MANAGER',
                                            first_name='Alice',
                                            last_name='Smith', restaurant=restaurant, email='ASmith@gmail.com')
    user_manager.phone = '2623985760'
    user_manager.save()

    # Create Employee and Manager
    employee1 = Employee.objects.create(user=user1, score1=4, score2=3, score3=5, score4=2, score5=4, average_score=3.6)
    employee2 = Employee.objects.create(user=user2, score1=3, score2=4, score3=5, score4=3, score5=4, average_score=3.8)
    employee3 = Employee.objects.create(user=user3, score1=5, score2=4, score3=5, score4=4, score5=5, average_score=4.6)
    employee4 = Employee.objects.create(user=user4, score1=4, score2=5, score3=5, score4=4, score5=5, average_score=4.6)
    employee5 = Employee.objects.create(user=user5, score1=3, score2=4, score3=5, score4=3, score5=4, average_score=3.8)
    employee6 = Employee.objects.create(user=user6, score1=5, score2=4, score3=5, score4=4, score5=5, average_score=4.6)
    employee7 = Employee.objects.create(user=user7, score1=4, score2=5, score3=5, score4=4, score5=5, average_score=4.6)
    manager = Manager.objects.create(user=user_manager)
    #
    # # Create Shifts
    # shift1 = Shift.objects.create(day='Mo', shift_type='Open')
    # shift2 = Shift.objects.create(day='Mo', shift_type='Mid')
    # shift3 = Shift.objects.create(day='Tu', shift_type='Open')
    # shift4 = Shift.objects.create(day='Tu', shift_type='Mid')
    # shift5 = Shift.objects.create(day='We', shift_type='Open')
    # shift6 = Shift.objects.create(day='We', shift_type='Close')
    # shift7 = Shift.objects.create(day='Th', shift_type='Open')
    # shift8 = Shift.objects.create(day='Th', shift_type='Mid')
    # shift9 = Shift.objects.create(day='Fr', shift_type='Open')

    # # Assign Shifts to Employees
    # EmployeeShift.objects.create(user=employee1, shift=shift1)
    # EmployeeShift.objects.create(user=employee2, shift=shift1)
    # EmployeeShift.objects.create(user=employee3, shift=shift1)
    # EmployeeShift.objects.create(user=employee4, shift=shift2)
    # EmployeeShift.objects.create(user=employee2, shift=shift2)
    # EmployeeShift.objects.create(user=employee3, shift=shift2)
    # EmployeeShift.objects.create(user=employee2, shift=shift3)
    # EmployeeShift.objects.create(user=employee4, shift=shift4)
    # EmployeeShift.objects.create(user=employee1, shift=shift5)
    # EmployeeShift.objects.create(user=employee4, shift=shift6)
    # EmployeeShift.objects.create(user=employee1, shift=shift7)
    # EmployeeShift.objects.create(user=employee4, shift=shift8)
    # EmployeeShift.objects.create(user=employee2, shift=shift9)



    # Create Availability for Employees
    availabilities = [
        # Availability(employee=employee1, day='Tu', shift_type='Open'),
        # Availability(employee=employee1, day='Tu', shift_type='Mid'),
        # Availability(employee=employee1, day='Tu', shift_type='Close'),
        # Availability(employee=employee1, day='We', shift_type='Open'),
        # Availability(employee=employee1, day='We', shift_type='Mid'),
        # Availability(employee=employee1, day='We', shift_type='Close'),
        # Availability(employee=employee1, day='Th', shift_type='Open'),
        # Availability(employee=employee1, day='Th', shift_type='Mid'),
        # Availability(employee=employee1, day='Th', shift_type='Close'),
        # Availability(employee=employee1, day='Fr', shift_type='Open'),
        # Availability(employee=employee1, day='Fr', shift_type='Mid'),
        # Availability(employee=employee1, day='Fr', shift_type='Close'),
        # Availability(employee=employee1, day='Sa', shift_type='Open'),
        # Availability(employee=employee1, day='Sa', shift_type='Mid'),
        # Availability(employee=employee1, day='Sa', shift_type='Close'),
        # Availability(employee=employee1, day='Su', shift_type='Open'),
        # Availability(employee=employee1, day='Su', shift_type='Mid'),
        # Availability(employee=employee1, day='Su', shift_type='Close'),
        Availability(employee=employee2, day='Mo', shift_type='Open'),
        Availability(employee=employee2, day='Mo', shift_type='Mid'),
        Availability(employee=employee2, day='Mo', shift_type='Close'),
        Availability(employee=employee2, day='Tu', shift_type='Open'),
        Availability(employee=employee2, day='Tu', shift_type='Mid'),
        Availability(employee=employee2, day='Tu', shift_type='Close'),
        Availability(employee=employee2, day='We', shift_type='Open'),
        Availability(employee=employee2, day='We', shift_type='Mid'),
        Availability(employee=employee2, day='We', shift_type='Close'),
        Availability(employee=employee2, day='Th', shift_type='Open'),
        Availability(employee=employee2, day='Th', shift_type='Mid'),
        Availability(employee=employee2, day='Th', shift_type='Close'),
        Availability(employee=employee2, day='Fr', shift_type='Open'),
        Availability(employee=employee2, day='Fr', shift_type='Mid'),
        Availability(employee=employee2, day='Fr', shift_type='Close'),
        Availability(employee=employee2, day='Sa', shift_type='Open'),
        Availability(employee=employee2, day='Sa', shift_type='Mid'),
        Availability(employee=employee2, day='Sa', shift_type='Close'),
        Availability(employee=employee2, day='Su', shift_type='Open'),
        Availability(employee=employee2, day='Su', shift_type='Mid'),
        Availability(employee=employee2, day='Su', shift_type='Close'),
        Availability(employee=employee3, day='Mo', shift_type='Open'),
        Availability(employee=employee3, day='Mo', shift_type='Mid'),
        Availability(employee=employee3, day='Mo', shift_type='Close'),
        Availability(employee=employee3, day='Tu', shift_type='Open'),
        Availability(employee=employee3, day='Tu', shift_type='Mid'),
        Availability(employee=employee3, day='Tu', shift_type='Close'),
        Availability(employee=employee3, day='We', shift_type='Open'),
        Availability(employee=employee3, day='We', shift_type='Mid'),
        Availability(employee=employee3, day='We', shift_type='Close'),
        Availability(employee=employee3, day='Th', shift_type='Open'),
        Availability(employee=employee3, day='Th', shift_type='Mid'),
        Availability(employee=employee3, day='Th', shift_type='Close'),
        Availability(employee=employee3, day='Fr', shift_type='Open'),
        Availability(employee=employee3, day='Fr', shift_type='Mid'),
        Availability(employee=employee3, day='Fr', shift_type='Close'),
        Availability(employee=employee3, day='Sa', shift_type='Open'),
        Availability(employee=employee3, day='Sa', shift_type='Mid'),
        Availability(employee=employee3, day='Sa', shift_type='Close'),
        Availability(employee=employee3, day='Su', shift_type='Open'),
        Availability(employee=employee3, day='Su', shift_type='Mid'),
        Availability(employee=employee3, day='Su', shift_type='Close'),
        Availability(employee=employee4, day='Mo', shift_type='Open'),
        Availability(employee=employee4, day='Mo', shift_type='Mid'),
        Availability(employee=employee4, day='Mo', shift_type='Close'),
        Availability(employee=employee4, day='Tu', shift_type='Open'),
        Availability(employee=employee4, day='Tu', shift_type='Mid'),
        Availability(employee=employee4, day='Tu', shift_type='Close'),
        Availability(employee=employee4, day='We', shift_type='Open'),
        Availability(employee=employee4, day='We', shift_type='Mid'),
        Availability(employee=employee4, day='We', shift_type='Close'),
        Availability(employee=employee4, day='Th', shift_type='Open'),
        Availability(employee=employee4, day='Th', shift_type='Mid'),
        Availability(employee=employee4, day='Th', shift_type='Close'),
        Availability(employee=employee4, day='Fr', shift_type='Open'),
        Availability(employee=employee4, day='Fr', shift_type='Mid'),
        Availability(employee=employee4, day='Fr', shift_type='Close'),
        Availability(employee=employee4, day='Sa', shift_type='Open'),
        Availability(employee=employee4, day='Sa', shift_type='Mid'),
        Availability(employee=employee4, day='Sa', shift_type='Close'),
        Availability(employee=employee4, day='Su', shift_type='Open'),
        Availability(employee=employee4, day='Su', shift_type='Mid'),
        Availability(employee=employee4, day='Su', shift_type='Close'),
        Availability(employee=employee5, day='Mo', shift_type='Open'),
        Availability(employee=employee5, day='Mo', shift_type='Mid'),
        Availability(employee=employee5, day='Mo', shift_type='Close'),
        Availability(employee=employee5, day='Tu', shift_type='Open'),
        Availability(employee=employee5, day='Tu', shift_type='Mid'),
        Availability(employee=employee5, day='Tu', shift_type='Close'),
        Availability(employee=employee5, day='We', shift_type='Open'),
        Availability(employee=employee5, day='We', shift_type='Mid'),
        Availability(employee=employee5, day='We', shift_type='Close'),
        Availability(employee=employee5, day='Th', shift_type='Open'),
        Availability(employee=employee5, day='Th', shift_type='Mid'),
        Availability(employee=employee5, day='Th', shift_type='Close'),
        Availability(employee=employee5, day='Fr', shift_type='Open'),
        Availability(employee=employee5, day='Fr', shift_type='Mid'),
        Availability(employee=employee5, day='Fr', shift_type='Close'),
        Availability(employee=employee5, day='Sa', shift_type='Open'),
        Availability(employee=employee5, day='Sa', shift_type='Mid'),
        Availability(employee=employee5, day='Sa', shift_type='Close'),
        Availability(employee=employee5, day='Su', shift_type='Open'),
        Availability(employee=employee5, day='Su', shift_type='Mid'),
        Availability(employee=employee5, day='Su', shift_type='Close'),
        Availability(employee=employee6, day='Mo', shift_type='Open'),
        Availability(employee=employee6, day='Mo', shift_type='Mid'),
        Availability(employee=employee6, day='Mo', shift_type='Close'),
        Availability(employee=employee6, day='Tu', shift_type='Open'),
        Availability(employee=employee6, day='Tu', shift_type='Mid'),
        Availability(employee=employee6, day='Tu', shift_type='Close'),
        Availability(employee=employee6, day='We', shift_type='Open'),
        Availability(employee=employee6, day='We', shift_type='Mid'),
        Availability(employee=employee6, day='We', shift_type='Close'),
        Availability(employee=employee6, day='Th', shift_type='Open'),
        Availability(employee=employee6, day='Th', shift_type='Mid'),
        Availability(employee=employee6, day='Th', shift_type='Close'),
        Availability(employee=employee6, day='Fr', shift_type='Open'),
        Availability(employee=employee6, day='Fr', shift_type='Mid'),
        Availability(employee=employee6, day='Fr', shift_type='Close'),
        Availability(employee=employee6, day='Sa', shift_type='Open'),
        Availability(employee=employee6, day='Sa', shift_type='Mid'),
        Availability(employee=employee6, day='Sa', shift_type='Close'),
        Availability(employee=employee6, day='Su', shift_type='Open'),
        Availability(employee=employee6, day='Su', shift_type='Mid'),
        Availability(employee=employee6, day='Su', shift_type='Close'),
        Availability(employee=employee7, day='Mo', shift_type='Open'),
        Availability(employee=employee7, day='Mo', shift_type='Mid'),
        Availability(employee=employee7, day='Mo', shift_type='Close'),
        Availability(employee=employee7, day='Tu', shift_type='Open'),
        Availability(employee=employee7, day='Tu', shift_type='Mid'),
        Availability(employee=employee7, day='Tu', shift_type='Close'),
        Availability(employee=employee7, day='We', shift_type='Open'),
        Availability(employee=employee7, day='We', shift_type='Mid'),
        Availability(employee=employee7, day='We', shift_type='Close'),
        Availability(employee=employee7, day='Th', shift_type='Open'),
        Availability(employee=employee7, day='Th', shift_type='Mid'),
        Availability(employee=employee7, day='Th', shift_type='Close'),
        Availability(employee=employee7, day='Fr', shift_type='Open'),
        Availability(employee=employee7, day='Fr', shift_type='Mid'),
        Availability(employee=employee7, day='Fr', shift_type='Close'),
        Availability(employee=employee7, day='Sa', shift_type='Open'),
        Availability(employee=employee7, day='Sa', shift_type='Mid'),
        Availability(employee=employee7, day='Sa', shift_type='Close'),

    ]

    Availability.objects.bulk_create(availabilities)


def delete_user(username):
    # Find the user you want to delete
    user = User.objects.filter(username=username).first()

    if user:
        # Delete the user
        user.delete()


def refresh_data():
    # Delete existing data in the correct order
    EmployeeShift.objects.all().delete()
    Shift.objects.all().delete()
    Employee.objects.all().delete()
    Manager.objects.all().delete()
    User.objects.all().delete()
    Restaurant.objects.all().delete()

    # Insert new data
    insert_data()


if __name__ == '__main__':
    reset_app('Scheduler')
    refresh_data()
