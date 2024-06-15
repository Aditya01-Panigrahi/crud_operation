from django.shortcuts import render

# Create your views here.
# views.py

def service_page(request):
    context = {
        'services': [
            {'name': 'Web Development', 'description': 'Building modern and responsive web applications.'},
            {'name': 'SEO Optimization', 'description': 'Improving your website visibility on search engines.'},
            {'name': 'Digital Marketing', 'description': 'Creating effective online marketing strategies.'},
            # Add more services as needed
        ]
    }
    return render(request, 'application/service_page.html', context)

