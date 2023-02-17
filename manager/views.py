from django.shortcuts import render, redirect
from main_page.models import UserReservation, ContactUs
from django.contrib.auth.decorators import login_required, user_passes_test
from main_page.models import InformationInContactUs, Footer
# Create your views here.


def is_manager(user):
    """
    Checked if user have group 'manager' in his group list.\n
    
    :param user: Session user unit.
    :return: True or False.
    """
    return user.groups.filter(name='manager').exists()


@login_required(login_url='login/')
@user_passes_test(is_manager)
def manager_page(request):
    """
    View function of the manager page. Processed GET requests.
    Access guaranteed only for user's from 'manager' group.

    information_in_contact_us - Object model InformationInContactUs.\n
    footer - Footer object model.\n
    user_auth - Is user authenticated or not.\n

    :param request: GET request.
    :return: Render of the HTML-page with context.
    
    """
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
    """
    View function of the reservation page. Processed GET requests.
    Access guaranteed only for user's from 'manager' group.

    lst - User Reservation objects filtered by is_processed marker.\n
    information_in_contact_us - Object model InformationInContactUs.\n
    footer - Footer object model.\n
    user_auth - Is user authenticated or not.\n

    :param request: GET request.
    :return: Render of the HTML-page with context.

    """
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
    """
    Change UserReservation variable is_processed status to True.
    Access guaranteed only for user's from 'manager' group.
    
    :param request: GET request.
    :param pk: Primary Key.
    :return: Redirect to the reservations_list.
    """
    UserReservation.objects.filter(pk=pk).update(is_processed=True)
    return redirect('manager:reservations_list')


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def contact_list(request):
    """
    View function of the contact page. Processed GET requests.
    Access guaranteed only for user's from 'manager' group.

    all_contacts - User ContactUs objects filtered by is_processed marker.\n
    information_in_contact_us - Object model InformationInContactUs.\n
    footer - Footer object model.\n
    user_auth - Is user authenticated or not.\n

    :param request: GET request.
    :return: Render of the HTML-page with context.

    """
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
    """
    Change ContactUs variable is_processed status to True.
    Access guaranteed only for user's from 'manager' group.

    :param request: GET request.
    :param pk: Primary Key.
    :return: Redirect to the reservations_list.
    """
    ContactUs.objects.filter(pk=pk).update(is_processed=True)
    return redirect('manager:contact_list')
