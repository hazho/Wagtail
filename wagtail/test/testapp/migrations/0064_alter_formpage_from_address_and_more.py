# Generated by Django 4.0.3 on 2022-03-28 09:18

from django.db import migrations, models
import wagtail.contrib.forms.models


class Migration(migrations.Migration):

    dependencies = [
        ("tests", "0063_jsonblockcountsstreammodel_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="formpage",
            name="from_address",
            field=models.EmailField(
                blank=True, max_length=255, verbose_name="from address"
            ),
        ),
        migrations.AlterField(
            model_name="formpage",
            name="to_address",
            field=models.CharField(
                blank=True,
                help_text="Optional - form submissions will be emailed to these addresses. Separate multiple addresses by comma.",
                max_length=255,
                validators=[wagtail.contrib.forms.models.validate_to_address],
                verbose_name="to address",
            ),
        ),
        migrations.AlterField(
            model_name="formpagewithcustomformbuilder",
            name="from_address",
            field=models.EmailField(
                blank=True, max_length=255, verbose_name="from address"
            ),
        ),
        migrations.AlterField(
            model_name="formpagewithcustomformbuilder",
            name="to_address",
            field=models.CharField(
                blank=True,
                help_text="Optional - form submissions will be emailed to these addresses. Separate multiple addresses by comma.",
                max_length=255,
                validators=[wagtail.contrib.forms.models.validate_to_address],
                verbose_name="to address",
            ),
        ),
        migrations.AlterField(
            model_name="formpagewithcustomsubmission",
            name="from_address",
            field=models.EmailField(
                blank=True, max_length=255, verbose_name="from address"
            ),
        ),
        migrations.AlterField(
            model_name="formpagewithcustomsubmission",
            name="to_address",
            field=models.CharField(
                blank=True,
                help_text="Optional - form submissions will be emailed to these addresses. Separate multiple addresses by comma.",
                max_length=255,
                validators=[wagtail.contrib.forms.models.validate_to_address],
                verbose_name="to address",
            ),
        ),
        migrations.AlterField(
            model_name="formpagewithcustomsubmissionlistview",
            name="from_address",
            field=models.EmailField(
                blank=True, max_length=255, verbose_name="from address"
            ),
        ),
        migrations.AlterField(
            model_name="formpagewithcustomsubmissionlistview",
            name="to_address",
            field=models.CharField(
                blank=True,
                help_text="Optional - form submissions will be emailed to these addresses. Separate multiple addresses by comma.",
                max_length=255,
                validators=[wagtail.contrib.forms.models.validate_to_address],
                verbose_name="to address",
            ),
        ),
        migrations.AlterField(
            model_name="formpagewithredirect",
            name="from_address",
            field=models.EmailField(
                blank=True, max_length=255, verbose_name="from address"
            ),
        ),
        migrations.AlterField(
            model_name="formpagewithredirect",
            name="to_address",
            field=models.CharField(
                blank=True,
                help_text="Optional - form submissions will be emailed to these addresses. Separate multiple addresses by comma.",
                max_length=255,
                validators=[wagtail.contrib.forms.models.validate_to_address],
                verbose_name="to address",
            ),
        ),
        migrations.AlterField(
            model_name="jadeformpage",
            name="from_address",
            field=models.EmailField(
                blank=True, max_length=255, verbose_name="from address"
            ),
        ),
        migrations.AlterField(
            model_name="jadeformpage",
            name="to_address",
            field=models.CharField(
                blank=True,
                help_text="Optional - form submissions will be emailed to these addresses. Separate multiple addresses by comma.",
                max_length=255,
                validators=[wagtail.contrib.forms.models.validate_to_address],
                verbose_name="to address",
            ),
        ),
    ]
