from django.db import models

STATUS_CHOICES = (
    ('pending', 'Kutilmoqda'),
    ('approved', 'Qabul qilindi'),
    ('rejected', 'Rad etildi'),
)

status = models.CharField(
    max_length=20,
    choices=STATUS_CHOICES,
    default='pending'
)

class Direction(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class TimeSlot(models.Model):
    time = models.CharField(max_length=50)  # masalan: 09:00 - 11:00

    def __str__(self):
        return self.time


class Application(models.Model):
    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_contacted = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name
class Application(models.Model):

    STATUS_CHOICES = (
        ('pending', 'Kutilmoqda'),
        ('approved', 'Qabul qilindi'),
        ('rejected', 'Rad etildi'),
    )

    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
