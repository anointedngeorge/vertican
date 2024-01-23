# Generated by Django 4.2.9 on 2024-01-23 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0006_rename_widgettitle_footerwidgets_widgetid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menusmodel',
            name='link',
            field=models.CharField(blank=True, choices=[('/', 'Index'), ('/estates', 'Show Estates'), ('/listing', 'LISTING'), ('/detail', 'DETAIL'), ('/testimonal', 'TESTIMONAL'), ('/contact copy', 'CONTACT COPY'), ('/television', 'TELEVISION'), ('/base', 'BASE'), ('/about', 'ABOUT'), ('/agent_detail', 'AGENT DETAIL'), ('/downloads', 'DOWNLOADS'), ('/property_details', 'PROPERTY DETAILS'), ('/ourservices', 'OURSERVICES'), ('/blog', 'BLOG'), ('/agency_detail', 'AGENCY DETAIL'), ('/property_details copy', 'PROPERTY DETAILS COPY'), ('/index_property', 'INDEX PROPERTY'), ('/agent', 'AGENT'), ('/blog_detail', 'BLOG DETAIL'), ('/property', 'PROPERTY'), ('/agency', 'AGENCY'), ('/index', 'INDEX'), ('/contact', 'CONTACT')], max_length=250, null=True, verbose_name='Website page'),
        ),
    ]
