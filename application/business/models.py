from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



#Product 

class Product(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Status(models.Model):
    type=models.CharField(max_length=20)

    def __str__(self):
        return f"{self.type}"

#Orders
class Order(models.Model):
    companyName = models.ForeignKey(Company, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    state=models.CharField(max_length=30)
    city=models.CharField(max_length=40)
    landmark=models.CharField(max_length=100)
    area=models.CharField(max_length=50)
    pincode=models.IntegerField(
         validators=[
            MinValueValidator(100000),  # Minimum allowed value
            MaxValueValidator(999999),  # Maximum allowed value
        ]
    )
    houseName = models.CharField(max_length=100)
    #added from Customer track views
    customerId=models.IntegerField()
    status=models.ForeignKey(Status, on_delete=models.CASCADE)
    dateTime=models.CharField(max_length=40)


    def __str__(self):
        return f"Order for {self.quantity} {self.product} from {self.companyName}"




class ItemList(models.Model):
      material=models.CharField(max_length=200)
      price=models.CharField(max_length=10)
      ItemImage=models.ImageField(upload_to='ItemImage/')

      def __str__(self):
          return f"{self.material}---{self.price}"   





