from Productos.models import *
from Usuarios.models import *


class Cart(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now_add=True)
    off_code = models.CharField(max_length=200)
    min_amount = models.IntegerField(default=0)
    discount = models.FloatField(default=0)
    payed = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user} - {str(self.date)}'

    def amount(self) -> float:
        total = 0
        articles = Article.objects.filter(cart=self)
        for article in articles:
            total += article.subtotal()
            return total

    @property
    def num_products(self) -> int:
        articles = Article.objects.filter(cart=self)
        return len(articles)


class Article(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.cart.__str__() + " / " + self.product.__str__()

    def subtotal(self) -> float:
        self.product.price * self.quantity


class InfoShip(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    def __str__(self):
        return self.cart.__str__()
