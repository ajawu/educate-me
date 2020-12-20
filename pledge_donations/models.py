from django.db import models
from django.conf import settings


class Contact(models.Model):
    contact_name = models.CharField(max_length=150)
    contact_email = models.EmailField(blank=False)
    message_title = models.CharField(max_length=200)
    message = models.TextField()
    has_reached_out = models.BooleanField(default=False)


class Books(models.Model):
    name = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='books/')
    total_donated = models.IntegerField(default=0)
    grade_level = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='events/', default='default.png')
    slug = models.SlugField(max_length=200)
    description = models.CharField(max_length=400)
    venue_state = models.CharField(max_length=20)
    venue_lga = models.CharField(max_length=100)
    venue_street_address = models.CharField(max_length=300)
    volunteers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='events', blank=True)
    books = models.ManyToManyField(Books, related_name='events', blank=True)
    event_time = models.DateTimeField(auto_now_add=True)
    donation_amount = models.DecimalField(decimal_places=2, max_digits=20, blank=True)
    donation_goal = models.DecimalField(decimal_places=2, max_digits=20, blank=True)
    volunteer_goal = models.IntegerField(default=0, blank=True)
    book_goal = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.name


class Donations(models.Model):
    donor = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    amount = models.DecimalField(decimal_places=2, blank=True, max_digits=20)
    event = models.ForeignKey(Event,
                              related_name='donations',
                              on_delete=models.DO_NOTHING)
    donation_time = models.DateTimeField(auto_now_add=True, blank=False)
    donation_type = models.CharField(blank=False, max_length=5)
    books = models.ForeignKey(Books, related_name='donations', on_delete=models.DO_NOTHING, null=True)
    fulfilled = models.BooleanField(default=False)
    item_count = models.IntegerField(default=1)

    def __str__(self):
        return self.donor.username + '-' + str(self.id)


class Subscription(models.Model):
    email = models.EmailField(blank=False, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True, blank=True)
