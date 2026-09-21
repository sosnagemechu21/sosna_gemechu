from django.shortcuts import render

def home(request):
    projects = [
        {
            'name': 'Web2Gram',
            'url': 'https://web2gram.pro.et/',
            'description': 'Telegram × AI information filtering',
            'image': 'https://image.thum.io/get/width/1200/crop/800/https://web2gram.pro.et/'
        },
        {
            'name': 'FocusLoop',
            'url': 'https://addisverse.pro.et/',
            'description': 'digital wellness / distraction control',
            'image': 'https://image.thum.io/get/width/1200/crop/800/https://addisverse.pro.et/'
        },
        {
            'name': 'Medstar',
            'url': 'https://medstarinternalspecialityclinic.vercel.app/en',
            'description': 'healthcare web platform',
            'image': 'https://image.thum.io/get/width/1200/crop/800/https://medstarinternalspecialityclinic.vercel.app/en'
        },
        {
            'name': 'Gara Media',
            'url': 'https://gara-media.vercel.app/',
            'description': 'A modern media application built with a focus on seamless user experience',
            'image': 'https://image.thum.io/get/width/1200/crop/800/https://gara-media.vercel.app/'
        }
    ]
    
    context = {
        'projects': projects,
    }
    return render(request, 'portfolio/index.html', context)
