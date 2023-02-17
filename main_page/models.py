from django.core.validators import RegexValidator
from django.db import models
from tinymce.models import HTMLField
import uuid
import os


class Category(models.Model):
    """
    The class is responsible for creating "Category" models In the database.

    name - Name of the category.\n
    position - Position of the category in menu.\n
    is_visible - Is category visible on the site or not.\n
    """
    name = models.CharField(unique=True, max_length=50, db_index=True)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('position', )


class Dishes(models.Model):
    """
    The class is responsible for creating "Dish" models In the database.

    name - Name of the dish.\n
    slug - Slug from the name.\n
    position - Position in the menu category.\n
    price - Price of the dish.\n
    description - Description of the dish.\n
    ingredients - Ingredients of the dish.\n
    is_visible - Is dish visible on the site or not.\n
    special - Is dish in 'special' dishes or not\n
    photo - Photo of the dish\n
    category - Category of the dish.\n
    """

    def get_file_name(self, filename: str) -> str:
        """
        Function for getting unique uuid-names for media files.

        :param filename: file original name.
        :return: New file name in uuid-4 format.
        """
        ext_of_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_of_file}'
        return os.path.join('dishes/', new_filename)

    name = models.CharField(unique=True, max_length=50, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    position = models.SmallIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(max_length=300, blank=True)
    ingredients = models.CharField(max_length=300)
    is_visible = models.BooleanField(default=True)
    special = models.BooleanField(default=False)
    photo = models.ImageField(upload_to=get_file_name, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('position', 'price', )
        index_together = (('id', 'slug'), )


class Events(models.Model):
    """
    The class is responsible for creating "Events" models In the database.

    title - Title of the event.\n
    event_description - Event description.\n
    event_date_and_time - Date and time of the event.\n
    event_price - Event entry price.\n
    photo - Photo to promotion.\n
    is_visible - Is event visible on site.\n
    """

    def get_file_name(self, filename: str) -> str:
        """
        Function for getting unique uuid-names for media files.

        :param filename: file original name.
        :return: New file name in uuid-4 format.
        """
        ext_of_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_of_file}'
        return os.path.join('events/', new_filename)

    title = models.CharField(unique=True, max_length=70, db_index=True)
    event_description = models.TextField(max_length=500)
    event_date_and_time = models.DateTimeField(help_text='Enter date and time of event')
    event_price = models.SmallIntegerField()
    photo = models.ImageField(upload_to=get_file_name, blank=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('event_date_and_time', )


class PhotoToGallery(models.Model):
    """
    The class is responsible for creating "Photo to gallery" models In the database.

    With this model we can download photos to the app and show them on site later.

    photo - Photo to the gallery.\n
    is_visible - Is photo visible in the gallery.\n
    """

    def get_file_name(self, filename: str) -> str:
        """
        Function for getting unique uuid-names for media files.

        :param filename: file original name.
        :return: New file name in uuid-4 format.
        """
        ext_of_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_of_file}'
        return os.path.join('photo/', new_filename)

    photo = models.ImageField(upload_to=get_file_name)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.photo}'

    class Meta:
        ordering = ('is_visible', )


class AboutUs(models.Model):
    """
    The class is responsible for creating "Photo to gallery" models In the database.

    header - Header of the About Us section.\n
    heading_text - Heading text of the About Us section.\n
    font_photo - Font photo of the section.\n
    video_url - URL-link to the video.\n
    """

    def get_file_name(self, filename: str) -> str:
        """
        Function for getting unique uuid-names for media files.

        :param filename: file original name.
        :return: New file name in uuid-4 format.
        """
        ext_of_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_of_file}'
        return os.path.join('about_us/', new_filename)

    header = models.CharField(max_length=80, help_text='Header text.')
    heading_text = models.TextField(max_length=700, help_text='Heading text')
    font_photo = models.ImageField(upload_to=get_file_name)
    video_url = models.URLField(help_text='Enter here link to the video.')


class BlockOfInformation(models.Model):
    """
    The class is responsible for creating "Block of information" models In the database.

    You can add any quantities of blocks, all they will be displayed on site.

    block_number - Number of block (visible part on site).\n
    block_title - Title of the block.\n
    block_text - Text inside the block.\n
    """

    block_number = models.SmallIntegerField()
    block_title = models.TextField(max_length=50)
    block_text = models.TextField(max_length=255)

    def __str__(self):
        return f'Block {self.block_number}'


class CrewMember(models.Model):
    """
    The class is responsible for creating "Crew member" models In the database.

    member_name - Name of the team member.\n
    member_description - Description of the team member.\n
    member_photo - Photo of the team member.\n
    twitter_link - Team member twitter link.\n
    facebook_link - Team member facebook link.\n
    instagram_link - Team member instagram link.\n
    linkedin_link - Team member linkedin link.\n
    """

    def get_file_name(self, filename: str) -> str:
        """
        Function for getting unique uuid-names for media files.

        :param filename: file original name.
        :return: New file name in uuid-4 format.
        """
        ext_of_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_of_file}'
        return os.path.join('member_photos/', new_filename)

    member_name = models.CharField(max_length=50)
    member_description = models.CharField(max_length=80)
    member_photo = models.ImageField(upload_to=get_file_name)
    twitter_link = models.URLField(help_text='Input here URL to Twitter account.')
    facebook_link = models.URLField(help_text='Input here URL to Facebook account.')
    instagram_link = models.URLField(help_text='Input here URL to Instagram account.')
    linkedin_link = models.URLField(help_text='Input here URL to LinkedIn account.')

    def __str__(self):
        return f'{self.member_name}'


class CustomerFeedback(models.Model):
    """
    The class is responsible for creating "Customer Feedback" models In the database.

    customer_name - Name of the customer.\n
    position - position.\n
    comment - Text of the comment.\n
    is_visible - Is comment visible on site.\n
    customer_photo - Photo of the customer.\n
    """

    def get_file_name(self, filename: str) -> str:
        """
        Function for getting unique uuid-names for media files.

        :param filename: file original name.
        :return: New file name in uuid-4 format.
        """
        ext_of_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_of_file}'
        return os.path.join('customer_feedback/', new_filename)

    customer_name = models.CharField(max_length=50)
    position = models.CharField(max_length=200)
    comment = models.TextField(max_length=200)
    is_visible = models.BooleanField(default=True)
    customer_photo = models.ImageField()


class HeroSection(models.Model):
    """
    The class is responsible for creating "Hero Section" models In the database.

    photo - Background photo.\n
    title - Title of the hero block.\n
    description - Description inside.\n
    """

    def get_file_name(self, filename: str) -> str:
        """
        Function for getting unique uuid-names for media files.

        :param filename: file original name.
        :return: New file name in uuid-4 format.
        """
        ext_of_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_of_file}'
        return os.path.join('hero/', new_filename)

    photo = models.ImageField(upload_to=get_file_name)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)


class UserReservation(models.Model):
    """
    The class is responsible for creating "User Reservation" models In the database, that will be used in forms on
    the site.

    mobile_re - regular expression for mobile phone validation.\n
    email_re - regular expression for email validation.\n
    name - Name of the customer.\n
    email - Customer's email.\n
    phone - Customer's phone.\n
    date_reservation - Date of table reservation.\n
    time_reservation - Time of table reservation.\n
    persons - How many persons.\n
    message - Additional message.\n
    date_of_the_request - Date and time when request was created.\n
    is_processed - Is request processed oe not.\n
    """

    mobile_re = RegexValidator(regex=r'^(\d{3}[- .]?){2}\d{4}$', message='Phone in format xxx xxx xxxx')
    email_re = RegexValidator(regex=r'^[a-zA-Z0-9]{1}[a-zA-Z0-9_]+(-{1})?[a-zA-Z0-9_]+@{1}([a-zA-Z0-9]+\.)+[a-z0-9]{1}'
                                    r'([a-z0-9-]*[a-z0-9])?$', message='Standard e-mail form')

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=63, validators=[email_re])
    phone = models.CharField(max_length=15, validators=[mobile_re])
    date_reservation = models.CharField(max_length=10)
    time_reservation = models.CharField(max_length=10)
    persons = models.PositiveSmallIntegerField()
    message = models.TextField(max_length=250, blank=True)
    date_of_the_request = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)

    class Meta:
        ordering = ('-date_of_the_request', )

    def __str__(self):
        return f'{self.name}, {self.phone}: {self.message}'


class ThisIsForTest(models.Model):
    """
    Test feature.
    """

    this_is_text = HTMLField(max_length=250)
    this_is_text_2 = HTMLField(max_length=250)
    this_is_text_3 = HTMLField(max_length=250)


class ContactUs(models.Model):
    """
    The class is responsible for creating "Contact Us" models In the database, that will be used in forms on
    the site.

    email_re - regular expression for email validation.\n
    name - Name of the customer.\n
    email - Customer's email.\n
    subject - Subject of the request.\n
    message - Additional message.\n
    date_of_the_request - Date and time when request was created.\n
    is_processed - Is request processed oe not.\n
    """

    email_re = RegexValidator(regex=r'^[a-zA-Z0-9]{1}[a-zA-Z0-9_]+(-{1})?[a-zA-Z0-9_]+@{1}([a-zA-Z0-9]+\.)+[a-z0-9]{1}'
                                    r'([a-z0-9-]*[a-z0-9])?$', message='Standard e-mail form')

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=63, validators=[email_re])
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=250, blank=True)
    date_of_the_request = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)

    class Meta:
        ordering = ('-date_of_the_request', )

    def __str__(self):
        return f'{self.name}, {self.email} - {self.subject}'


class InformationInContactUs(models.Model):
    """
    The class is responsible for creating "Information In Contact Us" models In the database.

    header - Header of the information.\n
    heading_text - Heading text.\n
    location - Location of the restaurant.\n
    open_hours - Open hours.\n
    email - Restaurant's email.\n
    call - Restaurant's phone number.\n
    phone_for_top_bar - Restaurant's phone number for top bar.\n
    open_hours_for_top_bar - Restaurant's open hours for top bar.\n
    """

    header = models.CharField(max_length=50)
    heading_text = HTMLField(max_length=250)
    location = HTMLField()
    open_hours = HTMLField()
    email = HTMLField()
    call = HTMLField()
    phone_for_top_bar = models.CharField(max_length=15)
    open_hours_for_top_bar = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.header}'


class Footer(models.Model):
    """
    The class is responsible for creating "Footer" models In the database.

    header - Header of the information.\n
    heading_text - Heading text.\n
    twitter - Twitter link.
    facebook - Facebook link.
    instagram - Instagram link.
    skype - Skype login.
    linked_in - Linkedin link.
    site_owner - Site owner.
    """

    header = HTMLField()
    heading_text = HTMLField(blank=True)
    twitter = models.CharField(max_length=500, blank=True)
    facebook = models.CharField(max_length=500, blank=True)
    instagram = models.CharField(max_length=500, blank=True)
    skype = models.CharField(max_length=500, blank=True)
    linked_in = models.CharField(max_length=500, blank=True)
    site_owner = HTMLField()

    def __str__(self):
        return f'{self.header} - {self.site_owner}'


