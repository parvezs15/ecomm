import django.core.management.base
from faker import Faker

from app.models import Teacher  # Replace 'app' with your app name


class Command(django.core.management.base.BaseCommand):
    help = 'Insert fake data into the Teacher model'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Number of fake records to create
        num_records = 10

        for _ in range(num_records):
            Teacher.objects.create(
                name=fake.name(),
                email=fake.unique.email(),
                phone=fake.phone_number(),
                biography=fake.text(max_nb_chars=200),
                subjects=", ".join(fake.words(nb=3)),  # Random subjects
                profile_picture=None  # Set to None or upload a default image
            )

        self.stdout.write(self.style.SUCCESS(f'{num_records} fake teacher records inserted successfully!'))
