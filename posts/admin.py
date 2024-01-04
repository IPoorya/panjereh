from django.contrib import admin
from .models import ApartmentRent, ApartmentSell


@admin.register(ApartmentSell)
class ApartmentSellAdmin(admin.ModelAdmin):
    list_display = ['token', 'title', 'meterage', 'province', 'city',  "created_at"]
    readonly_fields = ["timestamp", "created_at", "token"]

    fieldsets = [
        ('post info',
         {
             "fields": ["owner", "token", "title", "description",
                        "created_at", "timestamp", "visible"]}),
        ('price',
         {
             "fields": ["total_price", "price_per_meter"]}),
        ("building info",
         {
             "fields": ["meterage", "room", "build", 
                        "floor", "total_floors", "unit_per_floor", 
                        "elevator", "parking", "storage"]}),
        ("location",
         {
             "fields": ["province", "city", "neighbourhood", 
                        "location"]}),
        ("photos",
         {
             "fields": ["photo_0", "photo_1", "photo_2", 
                        "photo_3", "photo_4", "photo_5", 
                        "photo_6", "photo_7", "photo_8", 
                        "photo_9",]}),
    ]

    # add_fieldsets = [
    #     (
    #         None,
    #         {
    #             "classes": ["wide"],
    #             "fields": ["owner", "title", "description",
    #                        "visible", "total_price", "price_per_meter",
    #                        "meterage", "room", "build",
    #                        "floor", "total_floors", "unit_per_floor",
    #                        "elevator", "parking", "storage",
    #                        "province", "city", "neighbourhood",
    #                        "location", "photo_0", "photo_1",
    #                        "photo_2", "photo_3", "photo_4",
    #                        "photo_5", "photo_6", "photo_7",
    #                        "photo_8","photo_9",],
    #         },
    #     ),
    # ]




@admin.register(ApartmentRent)
class ApartmentRentAdmin(admin.ModelAdmin):
    list_display = ['token', 'title', 'meterage', 'province', 'city',  "created_at"]
    readonly_fields = ["timestamp", "created_at", "token"]

    fieldsets = [
        ('post info',
         {
             "fields": ["owner", "token", "title", "description",
                        "created_at", "timestamp", "visible"]}),

        ('low-deposite',
            {
                "fields": ["low_deposite", "high_rent"]}),
            ('high-deposite',
            {
                "fields": ["high_deposite", "low_rent"]}),

        
        ("building info",
         {
             "fields": ["meterage", "room", "build", 
                        "floor", "total_floors", "unit_per_floor", 
                        "elevator", "parking", "storage"]}),
        ("location",
         {
             "fields": ["province", "city", "neighbourhood", 
                        "location"]}),
        ("photos",
         {
             "fields": ["photo_0", "photo_1", "photo_2", 
                        "photo_3", "photo_4", "photo_5", 
                        "photo_6", "photo_7", "photo_8", 
                        "photo_9",]}),
    ]

    # add_fieldsets = [
    #     (
    #         None,
    #         {
    #             "classes": ["wide"],
    #             "fields": ["owner", "title", "description",
    #                        "visible", "low_deposite", "high_rent",
    #                        "high_deposite", "low_rent",
    #                        "meterage", "room", "build",
    #                        "floor", "total_floors", "unit_per_floor",
    #                        "elevator", "parking", "storage",
    #                        "province", "city", "neighbourhood",
    #                        "location", "photo_0", "photo_1",
    #                        "photo_2", "photo_3", "photo_4",
    #                        "photo_5", "photo_6", "photo_7",
    #                        "photo_8","photo_9",],
    #         },
    #     ),
    # ]

# admin.site.register(ApartmentSell)
# admin.site.register(ApartmentRent)
