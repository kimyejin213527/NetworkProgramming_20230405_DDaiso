from django.core.validators import MinValueValidator
from django.db import models
from django.shortcuts import resolve_url


class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField(validators=[MinValueValidator(0)]) #positiveIntegerField()
    image = models.ImageField(upload_to='product_images/%Y/%m/%d/', null=True, blank=True)

    def __str__(self):
        return f'{self.name}:{self.price}원'

    def get_absolute_url(self): #모델 하나를 구하는 절대 주소
        return resolve_url('product:detail',pk=self.id)

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  #1:N 관계
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.contents}'
    class Meta:
        ordering = ['-updated_at']  #수정된 날짜, 시간 역순 (최신순)