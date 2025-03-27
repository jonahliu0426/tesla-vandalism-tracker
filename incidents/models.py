from django.db import models

class Incident(models.Model):
    """
    latitude and longitude: Coordinates for map placement.
    time: When the incident occurred.
    location: Text description of the location.
    image and video: Optional evidence files.
    status: Indicates if the suspect is arrested (“Closed”) or not (“Open”).
    description: Additional details.
    """
    latitude = models.FloatField()
    longitude = models.FloatField()
    time = models.DateTimeField()
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='incident_images/', blank=True, null=True)
    video = models.FileField(upload_to='incident_videos/', blank=True, null=True)
    status = models.CharField(max_length=100, choices=[('open', 'Open'), ('closed', 'Closed')], default='open')
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Incident at {self.location} on {self.time}"