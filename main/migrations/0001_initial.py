# Generated by Django 4.1 on 2022-11-13 00:07

from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agreement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('dir', models.CharField(default='agreements/', max_length=256)),
                ('file', models.FileField(upload_to=main.models.rename_file)),
                ('about', models.TextField()),
            ],
            options={
                'verbose_name': 'Termo',
                'verbose_name_plural': 'Termos',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Docs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_documento', models.CharField(max_length=256)),
                ('arquivo', models.FileField(upload_to='files/documentos/')),
                ('sobre', models.TextField()),
            ],
            options={
                'verbose_name': 'Documento',
                'verbose_name_plural': 'Documentos',
                'ordering': ['nome_documento'],
            },
        ),
        migrations.CreateModel(
            name='Fabricante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fabricante', models.CharField(max_length=100)),
                ('imagem_logo', models.ImageField(upload_to='images/fabricantes/')),
                ('sobre', models.TextField()),
            ],
            options={
                'verbose_name': 'Fabricante',
                'verbose_name_plural': 'Fabricantes',
                'ordering': ['fabricante'],
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_produto', models.CharField(max_length=256)),
                ('codigo_de_barra', models.PositiveBigIntegerField()),
                ('preco', models.FloatField()),
                ('gramatura', models.FloatField()),
                ('imagem_produto', models.ImageField(upload_to='images/produtos/')),
                ('sobre', models.TextField()),
                ('fabricante', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.fabricante')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
                'ordering': ['nome_produto'],
            },
        ),
    ]
