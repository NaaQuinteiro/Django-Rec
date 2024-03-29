# Generated by Django 5.0.3 on 2024-03-05 13:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('Suspense', 'Suspense'), ('Romance', 'Romance'), ('Ação', 'Ação')], max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Livros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GeneroLivro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fk_genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genero_genero', to='app.genero')),
                ('fk_livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='livro_genero', to='app.livros')),
            ],
        ),
    ]
