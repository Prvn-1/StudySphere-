from django.conf import settings
from django.db import models

CATEGORY_CHOICES = [
    ('Notes', 'Notes'),
    ('Lab Programs', 'Lab Programs'),
    ('Question Papers', 'Question Papers'),
    ('Mini Projects', 'Mini Projects'),
    ('other','Other'),
]

STATUS_CHOICES = [('pending','Pending'), ('approved','Approved'), ('rejected','Rejected')]

class Resource(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    college = models.CharField(max_length=200)
    department = models.CharField(max_length=150)
    semester = models.IntegerField(null=True, blank=True)
    file = models.FileField(upload_to='resources/')
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    download_count = models.IntegerField(default=0)

    def average_rating(self):
        ratings = self.ratings.all()
        if not ratings:
            return 0
        return sum(r.stars for r in ratings) / ratings.count()

    def __str__(self):
        return self.title

class Rating(models.Model):
    resource = models.ForeignKey(Resource, related_name='ratings', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stars = models.IntegerField()  # validate 1-5
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('resource', 'user')
