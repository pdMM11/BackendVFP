# Generated by Django 3.0.3 on 2020-04-14 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InhibitorAntibody',
            fields=[
                ('idsubstance', models.IntegerField(db_column='idSubstance', primary_key=True, serialize=False)),
                ('type', models.CharField(blank=True, db_column='Type', max_length=45, null=True)),
                ('repository', models.CharField(blank=True, db_column='Repository', max_length=45, null=True)),
                ('id_repository', models.CharField(blank=True, db_column='ID_Repository', max_length=45, null=True)),
            ],
            options={
                'verbose_name_plural': 'Inihitors / Antibodies',
                'db_table': 'inhibitor_antibody',
                'managed': False,
            },
        ),
    ]
