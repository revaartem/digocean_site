from django.contrib import admin
from .models import Category, Dishes, Events, PhotoToGallery, AboutUs, \
    BlockOfInformation, CrewMember, CustomerFeedback, HeroSection, \
    UserReservation, ThisIsForTest, ContactUs, InformationInContactUs, Footer


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Registering category in admin section, added some visible and edition filters.
    """
    list_display = ['name', 'position', 'is_visible']
    list_editable = ['position', 'is_visible']


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    """
    Registering category in admin section, added some visible and edition filters.
    """
    list_display = ['title', 'event_description', 'event_date_and_time', 'event_price', 'is_visible']
    list_editable = ['event_date_and_time', 'event_price', 'is_visible']


@admin.register(Dishes)
class DishesAdmin(admin.ModelAdmin):
    """
    Registering category in admin section, added some visible and edition filters.
    Set prepopulated field Slug.
    """
    list_filter = ('category', 'position', )
    list_display = ['name', 'position', 'is_visible', 'price', 'photo', 'category']
    list_editable = ['position', 'is_visible', 'price']
    prepopulated_fields = {'slug': ('name', ), }


@admin.register(PhotoToGallery)
class PhotoToGalleryAdmin(admin.ModelAdmin):
    """
    Registering category in admin section, added some visible and edition filters.
    """
    list_display = ['photo', 'is_visible']
    list_editable = ['is_visible', ]


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    """
    Registering category in admin section, added some visible and edition filters.
    """
    list_display = ['header', 'heading_text', 'font_photo']
    list_editable = ['heading_text']


@admin.register(BlockOfInformation)
class BlockOfInformationAdmin(admin.ModelAdmin):
    """
    Registering category in admin section, added some visible and edition filters.
    """
    list_display = ['block_number', 'block_title', 'block_text']
    list_editable = ['block_title', 'block_text']


@admin.register(CrewMember)
class CrewMemberAdmin(admin.ModelAdmin):
    """
    Registering category in admin section, added some visible and edition filters.
    """
    list_display = ['member_name', 'member_description', 'member_photo']
    list_editable = ['member_description', ]


@admin.register(CustomerFeedback)
class CustomerFeedbackAdmin(admin.ModelAdmin):
    """
    Registering category in admin section, added some visible and edition filters.
    """
    list_display = ['customer_name', 'position', 'comment', 'is_visible', 'customer_photo']
    list_editable = ['comment', 'is_visible']


@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    """
    Registering category in admin section, added some visible and edition filters.
    """
    list_display = ['title', 'description', 'photo']
    list_editable = ['description', 'photo']


# Register other models without extra-settings.
admin.site.register(UserReservation)
admin.site.register(ThisIsForTest)
admin.site.register(ContactUs)
admin.site.register(InformationInContactUs)
admin.site.register(Footer)
