from django.db import models

class Client(models.Model):

    # Dropdown Choices
    PAYMENT_TYPE = [('Prepaid', 'Prepaid'),('Postpaid', 'Postpaid')]
    PAYMENT_TERM = [('15 Days', '15 Days'),('30 Days', '30 Days'),('45 Days', '45 Days')]
    BILLING_CURRENCY = [('INR', 'INR'),('USD', 'USD')]
    COUNTRY = [('India', 'India'),('USA', 'USA'),('UK', 'UK'),('Chinese', 'Chinese') ]


    # Basic Fields
    client_id = models.CharField(max_length=20, unique=True, blank=True)
    reporting_id = models.CharField(max_length=20, blank=True, null=True)

    name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=10)
    email = models.EmailField()

    # Address
    address_line1 = models.CharField(max_length=300)
    address_line2 = models.CharField(max_length=200, blank=True, null=True)

    country = models.CharField(max_length=50,choices=COUNTRY)

    zipcode = models.CharField(max_length=10)

    # Payment
    payment_type = models.CharField(max_length=20,choices=PAYMENT_TYPE)

    payment_term = models.CharField(max_length=20,choices=PAYMENT_TERM)

    billing_currency = models.CharField(max_length=10,choices=BILLING_CURRENCY)

    # Tax
    gst_no = models.CharField(max_length=20, blank=True, null=True)
    cin_no = models.CharField(max_length=30, blank=True, null=True)

    # Status
    is_domestic = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    created_on = models.DateTimeField(auto_now_add=True)

    # Wallet
    '''
    wallet_available_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_credited_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_debited_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    topup_wallet_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    '''


    def save(self, *args, **kwargs):

        if not self.client_id:
            last = Client.objects.all().order_by('id').last()

            if last:
                last_id = int(last.client_id[3:])
                self.client_id = f"CLI{last_id + 1:04d}"
            else:
                self.client_id = "CLI0001"

        super().save(*args, **kwargs)


    def __str__(self):
        return self.name