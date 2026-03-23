from django.db import models


class Car(models.Model):
    serial_number = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    colour = models.CharField(max_length=50)

    year = models.IntegerField()
    car_for_sale = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"


class Customer(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state_province = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Salesperson(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)

class Mechanic(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)


# service types and their rates
class Service(models.Model):
    service_name = models.CharField(max_length=100)
    hourly_rate = models.FloatField()


class Parts(models.Model):

    part_number = models.CharField(max_length=50)
    description = models.TextField()
    purchase_price = models.FloatField()
    retail_price = models.FloatField()


class SalesInvoice(models.Model):
    invoice_number = models.CharField(max_length=100)
    date = models.DateField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    salesperson = models.ForeignKey(Salesperson, on_delete=models.CASCADE)

    def __str__(self):
        return self.invoice_number


class ServiceTicket(models.Model):
    service_ticket_number = models.CharField(max_length=100)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_received = models.DateField()
    comments = models.TextField()
    date_returned = models.DateField(null=True, blank=True)


class ServiceMechanic(models.Model):
    service_ticket = models.ForeignKey(ServiceTicket, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    mechanic = models.ForeignKey(Mechanic, on_delete=models.CASCADE)

    hours = models.FloatField()
    comment = models.TextField()
    rate = models.FloatField()


