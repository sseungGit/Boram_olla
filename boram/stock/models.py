from django.db import models

# Create your models here.

# 임시로 만든 멤버 테이블 필요없으면 삭제
class Member(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    passwd = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    reg_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member'