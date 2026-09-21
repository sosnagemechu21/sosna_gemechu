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
            'url': '#',
            'description': 'digital wellness / distraction control',
            'image': 'https://picsum.photos/seed/focusloop/1200/800'
        },
        {
            'name': 'Libria',
            'url': '#',
            'description': 'AI-powered study companion',
            'image': 'https://picsum.photos/seed/libria/1200/800'
        },
        {
            'name': 'Medstar',
            'url': 'https://medstarinternalspecialityclinic.vercel.app/en',
            'description': 'healthcare web platform',
            'image': 'https://image.thum.io/get/width/1200/crop/800/https://medstarinternalspecialityclinic.vercel.app/en'
        }
    ]
    
    context = {
        'projects': projects,
    }
    return render(request, 'portfolio/index.html', context)
