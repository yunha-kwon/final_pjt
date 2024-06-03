from django.db import models

# Create your models here.
class DepositProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True)
    kor_co_nm = models.TextField()
    fin_prdt_nm = models.TextField()
    etc_note = models.TextField()
    join_deny = models.IntegerField()
    join_member = models.TextField()
    join_way = models.TextField()
    spcl_cnd = models.TextField()
    isFavorite= models.BooleanField(default=False)   


class DepositOptions(models.Model):
    product = models.ForeignKey(DepositProducts, on_delete=models.CASCADE, related_name='deposit_options')
    fin_prdt_cd = models.TextField()
    intr_rate_type_nm = models.CharField(max_length=100, null=True)
    intr_rate = models.FloatField(null=True, default=-1)
    intr_rate2 = models.FloatField(null=True,default=-1)
    save_trm = models.IntegerField()


class SaveProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True)
    kor_co_nm = models.TextField()
    fin_prdt_nm = models.TextField()
    etc_note = models.TextField()
    join_deny = models.IntegerField()
    join_member = models.TextField()
    join_way = models.TextField()
    spcl_cnd = models.TextField()
    max_limit = models.IntegerField()


class SaveOptions(models.Model):
    product = models.ForeignKey(SaveProducts, on_delete=models.CASCADE, related_name='save_options')
    fin_prdt_cd = models.TextField()
    intr_rate_type_nm = models.CharField(max_length=100, null=True)
    intr_rate = models.FloatField(null=True, default=-1)
    intr_rate2 = models.FloatField(null=True,default=-1)
    rsv_type = models.CharField(max_length=100, null=True) # 적립 유형
    rsrv_type_nm = models.CharField(max_length=100, null=True) # 적립 유형명
    save_trm = models.IntegerField()

class Anonymous(models.Model):
    gen_one = models.BooleanField(default=False)
    gen_two = models.BooleanField(default=False)
    age_one = models.BooleanField(default=False)
    age_two = models.BooleanField(default=False)
    age_thr = models.BooleanField(default=False)
    age_fou = models.BooleanField(default=False)
    age_fiv = models.BooleanField(default=False)
    age_six = models.BooleanField(default=False)
    sal_one = models.BooleanField(default=False)
    sal_two = models.BooleanField(default=False)
    sal_thr = models.BooleanField(default=False)
    sal_fou = models.BooleanField(default=False)
    sal_fiv = models.BooleanField(default=False)
    sal_six = models.BooleanField(default=False)
    whl_one = models.BooleanField(default=False)
    whl_two = models.BooleanField(default=False)
    whl_thr = models.BooleanField(default=False)
    whl_fou = models.BooleanField(default=False)
    whl_five = models.BooleanField(default=False)
    whl_six = models.BooleanField(default=False)
    ten_one = models.BooleanField(default=False)
    ten_two = models.BooleanField(default=False)
    ten_thr = models.BooleanField(default=False)

    def __str__(self):
        return f"User {self.id}"