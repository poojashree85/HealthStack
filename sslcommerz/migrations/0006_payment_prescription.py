from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0043_merge_20220918_0018'),
        ('sslcommerz', '0005_payment_test_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='prescription',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='doctor.prescription'),
        ),
    ]
