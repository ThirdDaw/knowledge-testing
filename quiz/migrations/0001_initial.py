# Generated by Django 3.2.7 on 2021-09-12 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Category')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('url', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Test')),
                ('time', models.PositiveIntegerField()),
                ('url', models.SlugField(max_length=160, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.category', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Test',
                'verbose_name_plural': 'Tests',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Question')),
                ('image', models.ImageField(blank=True, null=True, upload_to='questions/', verbose_name='Image')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.test', verbose_name='Test')),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Article')),
                ('text', models.TextField(verbose_name='Text')),
                ('url', models.SlugField(max_length=160, unique=True)),
                ('date_pub', models.DateTimeField(auto_now_add=True)),
                ('tags', models.ManyToManyField(blank=True, related_name='articles', to='quiz.Tag')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
                'ordering': ['-date_pub'],
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Answer')),
                ('image', models.ImageField(blank=True, null=True, upload_to='answers/', verbose_name='Image')),
                ('is_right', models.BooleanField(verbose_name='Right')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.question', verbose_name='Question')),
            ],
            options={
                'verbose_name': 'Answer',
                'verbose_name_plural': 'Answers',
            },
        ),
    ]
