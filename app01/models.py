from django.db import models

# ��
class Book(models.Model):
    title = models.CharField(max_length=32)
    publish_date = models.DateField(auto_now_add=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    memo = models.TextField(null=True)
    # �������������publish
    publisher = models.ForeignKey(to="Publisher",on_delete=models.CASCADE)
    # ������Զ����author
    author = models.ManyToManyField(to="Author")

    def __str__(self):
        return "<Book object: {} {}>".format(self.id, self.title)


# ������
class Publisher(models.Model):
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)

    def __str__(self):
        return "<Publisher object: {} {}>".format(self.id, self.name)


# ����
class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    phone = models.CharField(max_length=11)

    def __str__(self):
        return "<Author object: {} {}>".format(self.id, self.name)