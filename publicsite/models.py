from django.db import models
from django.utils.text import slugify
class PartnerShop(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=140, unique=True, blank=True)
    tagline = models.CharField(max_length=180, blank=True)
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to="partner_shops/", blank=True, null=True)
    food_categories = models.CharField(max_length=250, blank=True, help_text="Separate categories with commas")
    phone = models.CharField(max_length=40, blank=True)
    email = models.EmailField(blank=True)
    operating_hours = models.CharField(max_length=180, blank=True)
    service_area = models.CharField(max_length=180, blank=True)
    app_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)
    class Meta:
        ordering = ["display_order", "name"]
    def save(self, *args, **kwargs):
        if not self.slug:
            root = slugify(self.name) or "partner-shop"
            candidate, n = root, 2
            while PartnerShop.objects.filter(slug=candidate).exclude(pk=self.pk).exists():
                candidate, n = f"{root}-{n}", n+1
            self.slug = candidate
        super().save(*args, **kwargs)
    def __str__(self): return self.name
