from clean_blogs.models import SocialUrl

def contact_urls(request):
    objs = SocialUrl.objects.all()
    url_dict = {}
    for id in range(len(objs)):
        url_dict[f'{objs[id].name}'] = objs[id].url
    return url_dict