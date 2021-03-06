# Generated by Django 4.0.4 on 2022-05-12 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('list', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listitem',
            old_name='added_by',
            new_name='added_to',
        ),
        migrations.AlterField(
            model_name='list',
            name='contributors',
            field=models.ManyToManyField(related_name='contributors', to='accounts.account'),
        ),
        migrations.AlterField(
            model_name='list',
            name='list_items',
            field=models.ManyToManyField(blank=True, related_name='items', to='list.listitem'),
        ),
        migrations.AlterField(
            model_name='listitem',
            name='deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='listitem',
            name='setted_done_by',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='checker', to='accounts.account'),
        ),
    ]
