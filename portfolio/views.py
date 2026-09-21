from django.shortcuts import render

def home(request):
    projects = [
        {
            'name': 'Web2gram',
            'url': 'https://web2gram.pro.et/',
            'description': 'A modern web application demonstrating strong frontend and backend integration.',
            'image': 'https://image.thum.io/get/width/1200/crop/800/https://web2gram.pro.et/'
        },
        {
            'name': 'Medstar Internal Speciality Clinic',
            'url': 'https://medstarinternalspecialityclinic.vercel.app/en',
            'description': 'A professional clinic website with clean UI, responsive design, and robust functionality.',
            'image': 'https://image.thum.io/get/width/1200/crop/800/https://medstarinternalspecialityclinic.vercel.app/en'
        },
        {
            'name': 'Addisverse',
            'url': 'https://addisverse.pro.et/',
            'description': 'An innovative platform showing advanced web development capabilities.',
            'image': 'https://image.thum.io/get/width/1200/crop/800/https://addisverse.pro.et/'
        },
        {
            'name': 'Gara Media',
            'url': 'https://gara-media.vercel.app/',
            'description': 'A modern media application built with a focus on seamless user experience.',
            'image': 'https://image.thum.io/get/width/1200/crop/800/https://gara-media.vercel.app/'
        }
    ]
    
    context = {
        'projects': projects,
    }
    return render(request, 'portfolio/index.html', context)
