# Generated by Django 4.0.5 on 2022-11-17 10:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('local', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=200)),
                ('data', models.DateField(default=django.utils.timezone.now)),
                ('foto', models.ImageField(upload_to='static/images')),
            ],
        ),
        migrations.CreateModel(
            name='InteresseCarona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('aniversario', models.DateField(default=django.utils.timezone.now, verbose_name='aniversario')),
                ('carona', models.CharField(max_length=80, verbose_name='carona')),
                ('curso', models.CharField(max_length=200, verbose_name='curso')),
                ('foto', models.ImageField(upload_to='static/images')),
                ('interesse1', models.CharField(max_length=200, verbose_name='interesse1')),
                ('interesse2', models.CharField(max_length=200, verbose_name='interesse2')),
                ('interesse3', models.CharField(max_length=200, verbose_name='interesse3')),
                ('nome', models.CharField(blank=True, max_length=200, unique=True, verbose_name='nome')),
                ('ponto_de_encontro', models.CharField(max_length=200, verbose_name='ponto_encontro')),
                ('periodo', models.IntegerField(default=0, verbose_name='periodo')),
                ('webmail', models.EmailField(max_length=200, unique=True, verbose_name='webmail')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
