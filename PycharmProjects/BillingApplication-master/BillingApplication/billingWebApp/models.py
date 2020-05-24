from django.db import models

class user(models.Model):
    userId=models.AutoField(primary_key=True)
    name=models.CharField(max_length=10)
    age=models.IntegerField(default=0)


    def __str__(self):
        return self.name

class gstSlab(models.Model):
    slabId=models.AutoField(primary_key=True)
    slabName=models.CharField(max_length=10)
    slabPercentage=models.IntegerField(default=0)

    def __str__(self):
        return self.slabName

class category(models.Model):
    categoryID=models.AutoField(primary_key=True)
    categoryName=models.CharField(max_length=10)
    gstSlab=models.ForeignKey(gstSlab,on_delete=models.CASCADE)

    def __str__(self):
        return self.categoryName

class item(models.Model):
    itemId=models.AutoField(primary_key=True)
    itemName=models.CharField(max_length=10)
    itemCostinINR=models.DecimalField(default=0,decimal_places=6,max_digits=12)
    categoryId=models.ForeignKey(category,on_delete=models.CASCADE)

    def __str__(self):
        return self.itemName

class order(models.Model):
    orderId=models.AutoField(primary_key=True)
    user=models.ForeignKey(user,on_delete=models.CASCADE)
    orderDate = models.DateTimeField
    orderMode=models.CharField(max_length=10)
    orderSource=models.CharField(max_length=10)

    def __str__(self):
        return self.orderId

class orderItem(models.Model):
    ordersItemId=models.AutoField(primary_key=True)
    order=models.ForeignKey(order,on_delete=models.CASCADE)
    item=models.ForeignKey(item,on_delete=models.CASCADE)

    def __str__(self):
        return self.ordersItemId

class payment(models.Model):
    paymentId=models.AutoField(primary_key=True)
    order=models.ForeignKey(order,on_delete=models.CASCADE)
    totalSubCost=models.DecimalField(default=0,decimal_places=6,max_digits=12)
    totalGST=models.DecimalField(default=0,decimal_places=6,max_digits=12)
    totalCost=models.DecimalField(default=0,decimal_places=6,max_digits=12)
    modeofPayment=models.CharField(max_length=10)
    status=models.CharField(max_length=10)

    def __str__(self):
        return self.paymentId



