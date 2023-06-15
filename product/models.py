from django.core.validators import MinValueValidator
from django.db import models
from django.shortcuts import resolve_url
# Create your models here.
class Product(models.Model): # 열에 들어감
    name = models.CharField(max_length=20)
    price = models.IntegerField(validators=[MinValueValidator(0)])
    # price = models.PositiveIntegerField(0)


    # 빈칸으로 두면 아까 media 폴더 만들어 둔 곳에 올라감
    # 뭐 쓰면  media/product_images/ 이렇게 들어감
    # Y는 소문자로 하면 yy, 날짜안에 이미지가 들어감
    image = models.ImageField(upload_to='product_images/%Y/%m/%d', null=True, blank=True) # 값이 없거나 비어있어도 허락한다는 것


    def __str__(self):
        return f'{self.name} : {self.price}'

    def get_absolute_url(self): # 모델 하나를 구하는 절대 주소
        return resolve_url('product:detail', pk=self.id)