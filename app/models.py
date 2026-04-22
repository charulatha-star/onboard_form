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

    # Add company contact fields
        
    contact_name = models.CharField(max_length=255, null=True, blank=True)
    contact_phone = models.CharField(max_length=10, null=True, blank=True)
    contact_email = models.EmailField(null=True, blank=True)

    contact_designation = models.CharField(max_length=255, null=True, blank=True)
    contact_country = models.CharField(max_length=100, null=True, blank=True)
    contact_zipcode = models.CharField(max_length=20, null=True, blank=True)

    contact_address = models.CharField(max_length=300, null=True, blank=True)

    contact_signature = models.FileField(upload_to="signatures/",null=True,blank=True)

    contact_is_active = models.BooleanField(default=True)

    # Add company address fields
    company_address_line1=models.CharField(max_length=300, null=True, blank=True)
    company_address_line2=models.CharField(max_length=200, null=True, blank=True)
    company_country = models.CharField(max_length=50,choices=COUNTRY, null=True, blank=True)
    company_zipcode = models.CharField(max_length=10, null=True, blank=True)



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
    
# Create a table for signin

class SignIn(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.email
    

# Campaign model 

class Campaign(models.Model):

    STATUS = [('Draft','Draft'),('Live','Live'),('Paused','Paused'),('Completed','Completed'), ('Active', 'Active')]

    # Campaign Info
    campaign_id = models.CharField(max_length=20, unique=True, blank=True)
    client_campaign_id = models.CharField(max_length=50, null=True, blank=True)

    reporting_id = models.CharField(max_length=20, null=True, blank=True)
    purchase_order_id = models.CharField(max_length=50, null=True, blank=True)

    campaign_name = models.CharField(max_length=255)
    client_name = models.CharField(max_length=255)

    # Dates
    start_date = models.DateField()
    end_date = models.DateField()

    # Details
    subagency = models.CharField(max_length=255, null=True, blank=True)
    brand = models.CharField(max_length=255, null=True, blank=True)

    website_url = models.URLField(null=True, blank=True)

    status = models.CharField(max_length=20, choices=STATUS, default="Draft")

    is_active = models.BooleanField(default=True)

    #created_on = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):

        if not self.campaign_id:
            last = Campaign.objects.all().order_by('id').last()

            if last:
                last_id = int(last.campaign_id[4:])
                self.campaign_id = f"CMP-{last_id + 1:04d}"
            else:
                self.campaign_id = "CMP-0001"

        super().save(*args, **kwargs)


    def __str__(self):
        return self.campaign_name