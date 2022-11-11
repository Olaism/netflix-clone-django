from django.contrib import admin

from .models import SubscriptionPlan

@admin.register(SubscriptionPlan)
class SubscriptionAdmin(admin.ModelAdmin):
    model = SubscriptionPlan
    list_display = ('subscription_plan', 'monthly_price', 
    'video_quality', 'video_resolution')
