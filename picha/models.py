from django.db import models
import datetime as dt

# Create your models here.

class Location(models.Model):
    location = models.CharField(max_length=30)
    
    class Meta:
        ordering = ('location',)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    # def update_location(self, update):
    #     self.photo_location = update
    #     self.save()

    # @classmethod
    # def get_location_id(cls, id):
    #     locate = Location.objects.get(pk = id)
    #     return locate


class Category(models.Model):
    picture_category = models.CharField(max_length=30)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    # def __str__(self):
    #     return self.category

    # def update_category(self, update):
    #     self.photo_category = update
    #     self.save()

    # @classmethod
    # def get_category_id(cls, id):
    #     category = Category.objects.get(pk = id)
    #     return category

    # @classmethod
    # def todays_picha(cls,date):
    #     today =dt.date.today()
    #     picha=cls.objects.filter(pub_date__date=today)
    #     return picha

    # @classmethod
    # def days_picha(cls,date):
    #     picha = cls.objects.filter(pub_date__date = date)
    #     return picha

    # def __str__(self):
    #     return self.photo_category

class Image(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length =50)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,)
    category = models.ManyToManyField(Category)
    pub_date = models.DateTimeField(auto_now_add=True)
    picha_image = models.ImageField(upload_to = 'images/')
    
    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(title__icontains=search_term)
        return images
    
    @classmethod
    def update_image_by_id(cls,id):
        image = cls.objects.update(id=id)
        return image
    
    @classmethod
    def search_by_location(cls,search_term):
        image = Image.objects.filter(location__id=search_term).all()
        return image
    
    @classmethod
    def get_all_images(cls):
        images = cls.objects.all()
        return images
    
    @classmethod
    def get_image_by_id(cls,id):
        image = cls.objects.filter(id=id)
        return image
    
    @classmethod
    def delete_image_by_id(cls,id):
        image = cls.objects.remove(id=id)
        return image

    def save_image(self):
            self.save()

    def delete_image(self):
        self.delete()

    # def __str__(self):
    #     return self.image_name