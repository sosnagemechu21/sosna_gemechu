from django.shortcuts import render

def home(request):
    projects = [
        {
            'name': 'Web2gram',
            'url': 'https://web2gram.pro.et/',
            'description': 'A modern web application demonstrating strong frontend and backend integration.'
        },
        {
            'name': 'Medstar Internal Speciality Clinic',
            'url': 'https://medstarinternalspecialityclinic.vercel.app/en',
            'description': 'A professional clinic website with clean UI, responsive design, and robust functionality.'
        },
        {
            'name': 'Addisverse',
            'url': 'https://addisverse.pro.et/',
            'description': 'An innovative platform showing advanced web development capabilities.'
        }
    ]
    
    context = {
        'projects': projects,
    }
    return render(request, 'portfolio/index.html', context)
