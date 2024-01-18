# Generated by Django 4.2.1 on 2024-01-18 02:51

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import frontend.models.front_agent
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutModel',
            fields=[
                ('created', models.DateField(auto_created=True, default=django.utils.timezone.now, editable=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('about', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('site_logo', models.ImageField(blank=True, null=True, upload_to='contact')),
                ('site_title', models.CharField(blank=True, max_length=250, null=True)),
                ('site_subtitle', models.CharField(blank=True, default='', max_length=250)),
            ],
            options={
                'verbose_name': 'About',
                'verbose_name_plural': 'About',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('created', models.DateField(auto_created=True, default=django.utils.timezone.now, editable=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('icon', models.CharField(max_length=150)),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('link', models.CharField(blank=True, default='', max_length=150)),
                ('position', models.CharField(choices=[('left', 'left'), ('right', 'right')], max_length=150)),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='BranchModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('image', models.ImageField(upload_to='contact')),
                ('address', models.CharField(blank=True, max_length=250, null=True)),
                ('tel', models.CharField(blank=True, max_length=250, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Branch',
                'verbose_name_plural': 'Branches',
            },
        ),
        migrations.CreateModel(
            name='Downloads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='contact')),
            ],
            options={
                'verbose_name_plural': 'Downloads',
            },
        ),
        migrations.CreateModel(
            name='FrontEndAgent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=250, null=True)),
                ('last_name', models.CharField(blank=True, max_length=250, null=True)),
                ('role', models.CharField(blank=True, max_length=250, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, upload_to='frontend/agent', validators=[frontend.models.front_agent.validate_square_image])),
                ('facebook_url', models.CharField(blank=True, default='#', max_length=250)),
                ('twitter_url', models.CharField(blank=True, default='#', max_length=250)),
                ('linkedin_url', models.CharField(blank=True, default='#', max_length=250)),
                ('instagram_url', models.CharField(blank=True, default='#', max_length=250)),
            ],
            options={
                'verbose_name': 'Front End Agent',
                'verbose_name_plural': 'Front End Agents',
            },
        ),
        migrations.CreateModel(
            name='MenusModel',
            fields=[
                ('created', models.DateField(auto_created=True, default=django.utils.timezone.now, editable=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('link', models.CharField(blank=True, max_length=250, null=True)),
                ('has_children', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Menu',
                'verbose_name_plural': 'Menus',
            },
        ),
        migrations.CreateModel(
            name='ServicesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('subtitle', models.CharField(blank=True, max_length=250, null=True)),
                ('descriptions', models.TextField()),
                ('icon', models.CharField(choices=[('fa-gear', 'Gear'), ('fa-building-o', 'Building'), ('fa-home', 'Home')], max_length=300, null=True)),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.CreateModel(
            name='SettingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tel', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=300, null=True)),
                ('site_title', models.CharField(blank=True, max_length=255, null=True)),
                ('site_logo', models.ImageField(blank=True, null=True, upload_to='setting')),
                ('site_subtitle', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('description_title', models.CharField(max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('aboutus', models.TextField(blank=True, null=True)),
                ('footer_section', models.CharField(blank=True, max_length=255, null=True)),
                ('facebook', models.CharField(blank=True, max_length=255, null=True)),
                ('twitter', models.CharField(blank=True, max_length=255, null=True)),
                ('youtube', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Setting',
                'verbose_name_plural': 'Settings',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, null=True)),
                ('subtitle', models.CharField(max_length=250, null=True)),
                ('alt', models.CharField(default='1.jpg', max_length=250)),
                ('image', models.ImageField(upload_to='slider')),
                ('is_media_file_online', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(choices=[(1, 'Is Active'), (0, 'Not Active')], default=False, help_text='Set one to true')),
                ('is_showed', models.BooleanField(choices=[(1, 'Show Slider'), (0, "Don't Show Slider")], default=True, help_text='Tell if to show on the website')),
            ],
            options={
                'verbose_name': 'Slider',
                'verbose_name_plural': 'Sliders',
            },
        ),
        migrations.CreateModel(
            name='Television',
            fields=[
                ('created', models.DateField(auto_created=True, default=django.utils.timezone.now, editable=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('youtube', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Television',
                'verbose_name_plural': 'Televisions',
            },
        ),
        migrations.CreateModel(
            name='YoutubeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('link', models.CharField(blank=True, max_length=250, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Youtube Link',
                'verbose_name_plural': 'Youtube Links',
            },
        ),
        migrations.CreateModel(
            name='MenuChildModel',
            fields=[
                ('created', models.DateField(auto_created=True, default=django.utils.timezone.now, editable=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('link', models.CharField(blank=True, max_length=250, null=True)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu', to='frontend.menusmodel')),
            ],
            options={
                'verbose_name': 'Menu Child',
                'verbose_name_plural': 'Menu Children',
            },
        ),
        migrations.CreateModel(
            name='DownloadContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('link', models.URLField(blank=True, max_length=250, null=True)),
                ('download', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='downloads', to='frontend.downloads')),
            ],
        ),
    ]
