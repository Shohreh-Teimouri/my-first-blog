# Generated by Django 3.2.13 on 2022-05-20 19:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_post_visit_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostViewWithUniqueUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_views', to='blog.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_view', to=settings.AUTH_USER_MODEL)),
                ('viewers', models.ManyToManyField(editable=False, related_name='view_visitor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
