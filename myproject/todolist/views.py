from django.shortcuts import render


def base(requests):
    return render(requests, template_name='C:/Users/joji/PycharmProjects/ToDoList/myproject/todolist/templates/base'
                                          '.html')


def about_us(requests):
    return render(requests, template_name='C:/Users/joji/PycharmProjects/ToDoList/myproject/todolist/templates'
                                          '/about_us.html')
