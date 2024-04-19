from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0016_test_order'),
        ('sslcommerz', '0004_payment_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='test_order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='doctor.test_order'),
        ),
    ]
