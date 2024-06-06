from django.db import models

# Create your models here.

class DepositProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True)
    kor_co_nm = models.TextField()
    fin_prdt_nm = models.TextField()
    join_deny = models.IntegerField(default=0)
    join_way = models.TextField(default=None)
    spcl_cnd = models.TextField(default=None)

class DepositOptions(models.Model):
    product = models.ForeignKey(DepositProducts,on_delete=models.CASCADE)
    fin_prdt_cd = models.TextField()
    intr_rate_type_nm = models.CharField(max_length=100, default=None)
    intr_rate = models.FloatField(default=0, null=True)
    intr_rate2 = models.FloatField(default=0, null=True)
    save_trm = models.IntegerField(default=0, null=True)
    
class SavingProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True)
    kor_co_nm = models.TextField()
    fin_prdt_nm = models.TextField()
    join_deny = models.IntegerField(default=0)
    join_way = models.TextField(default=None)
    spcl_cnd = models.TextField(default=None)
    
class SavingOptions(models.Model):
    product = models.ForeignKey(SavingProducts,on_delete=models.CASCADE)
    fin_prdt_cd = models.TextField()
    intr_rate_type_nm = models.CharField(max_length=100, default=None)
    intr_rate = models.FloatField(default=0, null=True)
    intr_rate2 = models.FloatField(default=0, null=True)
    save_trm = models.IntegerField(default=0, null=True)
    rsrv_type_nm = models.TextField(default=None)
    
class LoanProducts(models.Model):
    fin_prdt_cd = models.TextField()
    cb_name = models.TextField()
    fin_co_no = models.TextField()
    kor_co_nm = models.TextField()
    fin_prdt_nm = models.TextField()
    crdt_prdt_type = models.IntegerField()
    join_way = models.TextField(default=None)

class LoanOptions(models.Model):
    product = models.ForeignKey(LoanProducts,on_delete=models.CASCADE)
    crdt_lend_rate_type_nm = models.TextField()
    crdt_grad_1 = models.FloatField(default=0, null=True)
    crdt_grad_4 = models.FloatField(default=0, null=True)
    crdt_grad_5 = models.FloatField(default=0, null=True)
    crdt_grad_6 = models.FloatField(default=0, null=True)
    crdt_grad_10 = models.FloatField(default=0, null=True)
    crdt_grad_11 = models.FloatField(default=0, null=True)
    crdt_grad_12 = models.FloatField(default=0, null=True)
    crdt_grad_13 = models.FloatField(default=0, null=True)
    crdt_grad_avg = models.FloatField(default=0, null=True)