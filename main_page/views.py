import datetime

from django.shortcuts import render, HttpResponse, redirect
from .models import Category, Dishes, AboutUs, BlockOfInformation, Events, PhotoToGallery, CrewMember, \
    CustomerFeedback, HeroSection, ThisIsForTest, InformationInContactUs, Footer
from .forms import UserReservationForm, ContactUsForm
# Create your views here.


def main_page(request):
    """
    View function of the main page. Processed POST and GET requests.

    :param request: POST or GET request.
    :return: Render of the HTML-page with context.

    reservation - Form of model User Reservation.\n
    contact_us - Form of the model Contact Us.\n
    user_manager - Objects model 'UserManager' filtered by group 'manager'\n
    user_auth - Is user logged in or not.\n
    categories - Category model objects filtered by 'is_visible' marker.\n
    dishes - Dishes model objects filtered by 'is_visible' marker.\n
    specials - Dishes model objects filtered by 'is_special' marker.\n
    about_us - Object of the model 'About Us'\n
    blocks_with_info - All objects of the BlockOfInformation model.\n
    events - Events model objects filtered by date and time. If event date > than datetime.now,
    event will be filtered out.\n
    photo_in_gallery -
    crew_member - all objects model PhotoToGallery.
    testimonials - Objects model CustomerFeedback filtered by 'is_visible' marker.\n
    hero - Object of the model 'HeroSection'.\n
    reservation - form UserReservationForm.\n
    test - test feature.\n
    contact_us - form ContactUsForm.\n
    information_in_contact_us - object model InformationInContactUs.\n
    footer - object model Footer.\n
    """

    if request.method == 'POST':
        reservation = UserReservationForm(request.POST)
        contact_us = ContactUsForm(request.POST)
        if reservation.is_valid():
            reservation.save()
            return redirect('/')
        if contact_us.is_valid():
            contact_us.save()
            return redirect('/')

    user_manager = request.user.groups.filter(name='manager').exists()
    user_auth = request.user.is_authenticated
    categories = Category.objects.filter(is_visible=True)
    dishes = Dishes.objects.filter(is_visible=True)
    specials = Dishes.objects.filter(special=True)
    about_us = AboutUs.objects.get()
    blocks_with_info = BlockOfInformation.objects.all()
    events = Events.objects.filter(event_date_and_time__gt=datetime.datetime.now())
    photo_in_gallery = PhotoToGallery.objects.all()
    crew_member = CrewMember.objects.all()
    testimonials = CustomerFeedback.objects.filter(is_visible=True).all()
    hero = HeroSection.objects.all()
    reservation = UserReservationForm()
    test = ThisIsForTest.objects.get()
    contact_us = ContactUsForm()
    information_in_contact_us = InformationInContactUs.objects.get()
    footer = Footer.objects.get()

    data = {
        'categories': categories,
        'dishes': dishes,
        'specials': specials,
        'about_us': about_us,
        'blocks_with_info': blocks_with_info,
        'events': events,
        'photo_in_gallery': photo_in_gallery,
        'crew_member': crew_member,
        'testimonials': testimonials,
        'hero': hero,
        'reservation_form': reservation,
        'test': test,
        'contact_us': contact_us,
        'information_in_contact_us': information_in_contact_us,
        'footer': footer,
        'user_manager': user_manager,
        'user_auth': user_auth



    }
    return render(request, 'main_page.html', context=data)
