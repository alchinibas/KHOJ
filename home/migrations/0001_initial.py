# Generated by Django 3.0.5 on 2020-11-16 10:34

from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields
import home.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('desc', models.TextField()),
                ('report_date', models.DateTimeField(auto_now_add=True)),
                ('read', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='indexing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=255)),
                ('site_id', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='search_text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_text', models.CharField(max_length=255)),
                ('visit_couont', models.IntegerField(default=0)),
                ('priority', models.FloatField(default=1.0)),
            ],
        ),
        migrations.CreateModel(
            name='SiteDetail',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('site', djongo.models.fields.EmbeddedField(model_container=home.models.Site)),
                ('title', models.CharField(default='', max_length=255)),
                ('desc', models.CharField(default='', max_length=400)),
                ('domain', models.CharField(default='.com', max_length=20)),
                ('display', models.BooleanField(default=True)),
                ('visit_count', models.IntegerField(default=0)),
                ('priority', models.FloatField(default=1.0)),
                ('indexed', models.BooleanField(default=False)),
                ('words_links', models.CharField(default='-', max_length=255)),
                ('icon', models.CharField(default='/favicon.ico', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SiteRank',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('site', djongo.models.fields.EmbeddedField(model_container=home.models.Site)),
                ('rank', models.FloatField(default=1.0)),
            ],
        ),
        migrations.CreateModel(
            name='sites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField(default='')),
                ('title', models.CharField(default='', max_length=255)),
                ('desc', models.CharField(default='', max_length=400)),
                ('domain', models.CharField(default='.com', max_length=20)),
                ('display', models.BooleanField(default=True)),
                ('visit_count', models.IntegerField(default=0)),
                ('priority', models.FloatField(default=1.0)),
                ('indexed', models.BooleanField(default=False)),
                ('words_links', models.CharField(default='', max_length=255)),
                ('icon', models.CharField(default='/favicon.ico', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='uncrawled',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('url', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='KeyExtract',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('key', djongo.models.fields.EmbeddedField(model_container=home.models.Key)),
                ('original', djongo.models.fields.ArrayField(model_container=home.models.Original, null=True)),
                ('file', djongo.models.fields.ArrayReferenceField(on_delete=django.db.models.deletion.CASCADE, to='home.SiteDetail')),
            ],
        ),
        migrations.CreateModel(
            name='Index',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('key', djongo.models.fields.EmbeddedField(model_container=home.models.Key)),
                ('sites', djongo.models.fields.ArrayReferenceField(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.SiteDetail')),
            ],
        ),
    ]
