# Generated by Django 5.0.3 on 2024-05-20 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoption', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adoptionrequest',
            name='status',
            field=models.CharField(choices=[('applied', 'Applied'), ('reviewed', 'Reviewed'), ('interviewed', 'Home Visited'), ('approved', 'Approved'), ('paid', 'Paid'), ('adopted', 'Adopted')], default='applied', max_length=25),
        ),
    ]
