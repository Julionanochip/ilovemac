# Generated by Django 5.1.2 on 2024-11-01 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comparamac', '0003_rename_nanomeme_notebook_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='notebook',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='imagens/'),
        ),
    ]