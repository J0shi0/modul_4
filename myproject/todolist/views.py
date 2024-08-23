from django.shortcuts import render


def base(requests):
    return render(requests, template_name='base.html')


def about_us(requests):
    return render(requests, template_name='about_us.html')
