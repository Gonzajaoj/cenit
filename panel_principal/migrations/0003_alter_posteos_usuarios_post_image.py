# Generated by Django 4.0.6 on 2023-12-08 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel_principal', '0002_alter_comentarios_usuarios_comment_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posteos_usuarios',
            name='post_image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
