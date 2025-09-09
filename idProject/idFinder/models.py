from django.db import models

class FoundID(models.Model):
    name_on_id = models.CharField(max_length=100)
    location_found = models.CharField(max_length=200)
    date_found = models.DateField()
    image = models.ImageField(upload_to='found_ids/')
    contact = models.CharField(max_length=100, blank=True)
    approved = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name_on_id} - {self.location_found}"
    
class LostIDReport(models.Model):
    name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=20)
    last_seen_location = models.CharField(max_length=200)
    contact_info = models.CharField(max_length=150, blank=True, help_text="Optional phone/email")
    reported_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.id_number}"
