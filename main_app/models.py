from django.db import models
# Import the reverse function
from django.urls import reverse

# Create your models here.

class Stablizer(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('stablizers_detail', kwargs={'pk': self.id})



class Keyboard(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    switches = models.TextField(max_length=250)


	  # Add this method
    def get_absolute_url(self):

	# detail is the url name of the page you want to go to
	#kwargs are if there are any params in the route
	# path('cats/<int:cat_id>/', views.cats_detail, name='detail'),
        return reverse('detail', kwargs={'keyboard_id': self.id})

PROFILES = (
    ('C', 'Cherry'),
    ('O', 'OEM'),
    ('X', 'XDA')
)

class Keycap(models.Model):
    date = models.DateField()
    profile = models.CharField(
        max_length=1,
        # create a select menu, the value of the select item
        # will be the first letter, and whats between the tags,
        # what the user see will be second item in the tuple (Breakfast)
        choices=PROFILES,
        default=PROFILES[0][0]
    )
    # Create a cat_id FK lowercase singular of your related model
    # inside postgres the column will have _id attached so cat_id
    keyboard = models.ForeignKey(Keyboard, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.get_profile_display()} on {self.date}"
