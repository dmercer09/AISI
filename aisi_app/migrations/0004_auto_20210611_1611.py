# Generated by Django 2.2 on 2021-06-11 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aisi_app', '0003_auto_20210611_0319'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aisi_post',
            old_name='content',
            new_name='message',
        ),
        migrations.AlterField(
            model_name='aisi_post',
            name='poster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_posts', to='aisi_app.User'),
        ),
    ]
