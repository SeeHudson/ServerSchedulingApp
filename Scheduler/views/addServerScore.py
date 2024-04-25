from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from Scheduler.models import Employee, User


class addServerScore(View):
    def get(self, request):
        current_user = request.user
        allUsers = User.objects.all()
        restaurant_name = request.session.get('restaurant_name')
        context = {
            'restaurant_name': restaurant_name,
            'userList': allUsers,
        }
        if request.method == 'GET':
            return render(request, "Scheduler/addServerScore.html", context)

    def post(self, request):
        current_user = request.user
        employee_id = request.POST.get('employee_score')
        new_score = int(request.POST.get('averagescore'))

        # Retrieve the selected employee
        selected_employee = Employee.objects.get(pk=employee_id)

        # Get the current scores for the selected employee
        scores = [selected_employee.score1, selected_employee.score2, selected_employee.score3,
                  selected_employee.score4, selected_employee.score5]

        # Update the scores list with the new score and remove the oldest score if there are already 5 scores
        if len(scores) >= 5:
            scores.pop(0)  # Remove the oldest score
        scores.append(new_score)  # Add the new score

        # Calculate the average score
        if len(scores) > 0:
            average_score = sum(scores) / len(scores)
        else:
            average_score = "No scores entered"

        # Update the scores and average score for the selected employee
        selected_employee.score1, selected_employee.score2, selected_employee.score3, \
            selected_employee.score4, selected_employee.score5 = scores
        selected_employee.average_score = average_score
        selected_employee.save()

        # Update context with the latest scores and average score
        allUsers = User.objects.all()
        restaurant_name = request.session.get('restaurant_name')
        context = {
            'restaurant_name': restaurant_name,
            'userList': allUsers,
        }

        # Render the template with updated context
        return render(request, "Scheduler/addServerScore.html", context)