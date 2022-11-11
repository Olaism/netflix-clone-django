from django.db import models

VIDEO_QUAL_CHOICES = (
    ('good', 'good'),
    ('better','better'),
    ('best', 'best'),
)

VIDEO_RES_CHOICES = (
    ('480p', '480p'),
    ('720p', '720p'),
    ('1080p', '1080p'),
    ('4K+HDR', '4K+HDR'),
)

class SubscriptionPlan(models.Model):
    subscription_plan = models.CharField(max_length=255)
    monthly_price = models.DecimalField(max_digits=7, decimal_places=2)
    video_quality = models.CharField(
        max_length=6,
        choices=VIDEO_QUAL_CHOICES,
    )
    video_resolution = models.CharField(
        max_length=6,
        choices=VIDEO_RES_CHOICES,
    )

    def __str__(self):
        return f"{self.subscription_plan} #{self.monthly_price}"
