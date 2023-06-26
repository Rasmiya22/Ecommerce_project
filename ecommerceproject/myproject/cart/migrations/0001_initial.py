# Generated by Django 4.2.1 on 2023-06-16 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ecommerceapp', '0003_alter_category_image_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_id', models.CharField(blank=True, max_length=250)),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'cart',
                'ordering': ['date_added'],
            },
        ),
        migrations.CreateModel(
            name='cartitem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('cart2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cart')),
                ('product2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerceapp.product')),
            ],
            options={
                'db_table': 'cartitem',
            },
        ),
    ]
