from django.db import models


class Supplier(models.Model):
    name            =       models.CharField(max_length=30, unique=True)
    phone           =       models.CharField(max_length=16, unique=True)
    address         =       models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Rate(models.Model):
    supplier        =       models.ForeignKey(Supplier, on_delete=models.CASCADE)
    rate            =       models.FloatField()
    start_date      =       models.DateField()

    def __str__(self):
        return str(self.supplier) + '_' + str(self.rate)

class Service(models.Model):
    supplier        =       models.ForeignKey(Supplier, on_delete=models.CASCADE)
    date            =       models.DateField()
    quantity        =       models.FloatField()
    rate            =       models.ForeignKey(Rate, on_delete=models.CASCADE)
    remark          =       models.CharField(max_length=100, blank = True, null=True)

    supplier.unique_for_date = "date"

    def __str__(self):
        return str(self.supplier) + '_' + str(self.date)

class Bill(models.Model):
    supplier        =       models.ForeignKey(Supplier, on_delete=models.CASCADE)
    start_date      =       models.DateField()
    end_date        =       models.DateField()
    amount          =       models.FloatField()

    def __str__(self):
        return str(self.supplier) + '_' + str(self.start_date)

class Payment(models.Model):
    bill            =       models.ForeignKey(Bill, on_delete=models.CASCADE)
    amount          =       models.FloatField()
    payment_date    =       models.DateField()
    remaining_amt   =       models.FloatField(null=True, default=0)
    remark          =       models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.bill) + '_' + str(self.payment_date)