from django.shortcuts import render ,get_object_or_404
from datarepo.models import Home  
# Create your views here. 




def pages_list(request):
    all_homes = Home.objects.all()
    final = []
    for temp_home in all_homes:
        dict = {
            'name' : temp_home.slug
        }
        final.append(dict)
    return {'main_menu_list':final }
    
    
def home(request ,slug=None):
    if slug is None:
        initial_item = get_object_or_404(Home, slug='home')

        page_data = {
            "image": initial_item.image.url,
            "title": initial_item.title,
            "description": initial_item.description,
            "button_text": initial_item.button_text,
            "button_link": initial_item.button_link
        }
        return render(request, "home.html", context=page_data)
    else:
        try:
            page_info = Home.objects.get(slug=slug)
            page_data = {
                "image" : page_info.image.url,
                "title" : page_info.title,
                "description" : page_info.description,
                "button_text" : page_info.button_text,
                "button_link" : page_info.button_link
            }
            return render(request, "home.html",context=page_data) 
        except Home.DoesNotExist:
            return render(request, "not_found.html")
        
   