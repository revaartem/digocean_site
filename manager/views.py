from django.shortcuts import render, redirect
from main_page.models import UserReservation, ContactUs
from django.contrib.auth.decorators import login_required, user_passes_test
from main_page.models import InformationInContactUs, Footer
# Create your views here.


def is_manager(user):
    return user.groups.filter(name='manager').exists()

@login_required(login_url='login/')
@user_passes_test(is_manager)
def manager_page(request):
    user_auth = request.user.is_authenticated
    information_in_contact_us = InformationInContactUs.objects.get()
    footer = Footer.objects.get()
    return render(request, 'manager_main_page.html', context={
        'information_in_contact_us': information_in_contact_us,
        'footer': footer,
        'user_auth': user_auth,
    })


@login_required(login_url='login/')
@user_passes_test(is_manager)
def reservation_list(request):
    user_auth = request.user.is_authenticated
    lst = UserReservation.objects.filter(is_processed=False)
    information_in_contact_us = InformationInContactUs.objects.get()
    footer = Footer.objects.get()
    return render(request, 'reservations_list.html', context={
        'lst': lst,
        'information_in_contact_us': information_in_contact_us,
        'footer': footer,
        'user_auth': user_auth,
    })


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def update_reservation(request, pk):
    UserReservation.objects.filter(pk=pk).update(is_processed=True)
    return redirect('manager:reservations_list')


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def contact_list(request):
    user_auth = request.user.is_authenticated
    all_contacts = ContactUs.objects.filter(is_processed=False)
    information_in_contact_us = InformationInContactUs.objects.get()
    footer = Footer.objects.get()
    return render(request, 'contact_list.html', context={
        'all_contacts': all_contacts,
        'information_in_contact_us': information_in_contact_us,
        'footer': footer,
        'user_auth': user_auth,
    })


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def update_contact(request, pk):
    ContactUs.objects.filter(pk=pk).update(is_processed=True)
    return redirect('manager:contact_list')
