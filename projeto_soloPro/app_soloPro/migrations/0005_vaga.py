# Generated by Django 4.2.3 on 2023-08-29 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_soloPro', '0004_candidato'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vaga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=100)),
                ('atuacao', models.CharField(max_length=100)),
                ('contato', models.IntegerField(default=0)),
            ],
        ),
    ]