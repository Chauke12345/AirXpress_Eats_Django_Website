from django.urls import path
from . import views
app_name="publicsite"
urlpatterns=[
 path("",views.home,name="home"),
 path("shops/",views.partners,name="partners"),
 path("shops/<slug:slug>/",views.partner_detail,name="partner_detail"),
 path("drivers/",views.drivers,name="drivers"),
 path("partner-with-us/",views.partner_with_us,name="partner_with_us"),
 path("contact/",views.contact,name="contact"),
 path("refund-policy/", views.refund_policy, name="refund_policy"),
]
