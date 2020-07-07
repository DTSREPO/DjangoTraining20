from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # context = {'name': 'Md. Firoz Mahmud', 'age': 30, 'marks': 70, 'rolls': [1, 3, 4, 5]}
    return render(request, 'index.html')


def about(request):
    context = {
        'name': 'Md. Firoz Mahmud',
        'district': 'Narail',
        'result': {
            'bangla': 80,
            'math': 90,
            'english': 30,
            'physics': [54, 56, 44, 66]
        }
    }
    return render(request, 'student.html', context)


def blog(request):
    context = {
        'students': [
            {
                'name': 'Md Firoz Mahmud',
                'roll': 1,
            },
            {
                'name': 'Md Firoz',
                'roll': 2,
            }
        ]
    }
    return render(request, 'blog.html', context)


def support(request):
    context = {
        'students': [
            {
                'class1': [
                    {
                        'name': 'Md. Firoz Mahmud',
                        'roll': 1
                    },
                    {
                        'name': 'Zabber Mahmud',
                        'roll': 2
                    },
                ],
                'class2': [
                    {
                        'name': 'Ayaan Mahmud',
                        'roll': 1
                    },

                    {
                        'name': 'Mohin',
                        'roll': 2,
                    },

                    {
                        'name': 'Kalam Mahmud',
                        'roll': 3
                    },

                ]
            }
        ]
    }

    return render(request, 'support.html', context)


def contact(request):
    return render(request, 'contact.html')
