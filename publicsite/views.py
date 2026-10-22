from django.conf import settings
from django.shortcuts import get_object_or_404, render
from .models import PartnerShop
def home(request):
    shops = PartnerShop.objects.filter(is_active=True)
    return render(request,"publicsite/home.html",{"shops":shops,"featured_shops":shops.filter(app_featured=True)[:6],"app_url":getattr(settings,"AIRXPRESS_APP_URL","https://web-production-81fc2.up.railway.app/")})
def partners(request):
    return render(request,"publicsite/partners.html",{"shops":PartnerShop.objects.filter(is_active=True),"app_url":getattr(settings,"AIRXPRESS_APP_URL","https://web-production-81fc2.up.railway.app/")})
def partner_detail(request,slug):
    shop=get_object_or_404(PartnerShop,slug=slug,is_active=True)
    return render(request,"publicsite/partner_detail.html",{"shop":shop,"app_url":getattr(settings,"AIRXPRESS_APP_URL","https://web-production-81fc2.up.railway.app/")})
def drivers(request): return render(request,"publicsite/info.html",{"heading":"Become a delivery driver","intro":"Interested in delivering with AirXpress Eats? Contact operations to learn about application and verification.","email":"modise.ofentse100@gmail.com","kind":"driver"})
def partner_with_us(request): return render(request,"publicsite/info.html",{"heading":"Partner with AirXpress Eats","intro":"We are building a network of local food businesses. Tell our team about your business and service area.","email":"modise.ofentse100@gmail.com","kind":"partner"})
def contact(request): return render(request,"publicsite/contact.html")
