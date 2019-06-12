from django.urls import path
from myapp import views


urlpatterns = [
    path('home/',views.homepage,name='homepage'),
	path('gallery/',views.gallery,name='gallery'),
	path('signin/',views.signin,name='signin'),
	path('signup/',views.signup,name='signup'),
	path('about/',views.about,name='About'),
	path('contact/',views.contact,name='Contact'),
	path('custom/',views.custom,name='Custom'),
	path('login/',views.login_form,name='Form'),
]
