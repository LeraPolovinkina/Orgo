# Generated by Django 3.2.7 on 2022-05-27 16:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('faq', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FaqFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155, verbose_name='Name')),
                ('email', models.EmailField(blank=True, max_length=155, null=True, verbose_name='Email')),
                ('phone', models.CharField(max_length=10, verbose_name='Phone')),
                ('title', models.CharField(max_length=155, verbose_name='Subject')),
                ('message', models.TextField(verbose_name='Your Message')),
                ('checked', models.BooleanField(default=False, verbose_name='Checked')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
            ],
            options={
                'verbose_name': 'Вопрос к нам',
                'verbose_name_plural': 'Вопросы к нам',
            },
        ),
    ]
