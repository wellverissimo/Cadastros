# Generated by Django 4.2 on 2023-04-24 23:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CadastroClientes', '0005_profissoes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profissoes',
            new_name='Profissao',
        ),
        migrations.AlterModelOptions(
            name='profissao',
            options={'verbose_name_plural': 'Profissões'},
        ),
    ]
