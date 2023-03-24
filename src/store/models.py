from django.db import models

class StoreStatus(models.Model):
  store_id = models.IntegerField(primary_key=True)
  timestamp_utc = models.DateTimeField()
  status = models.CharField(max_length=10)

class BusinessHours(models.Model):
  store_id = models.ForeignKey("StoreStatus", on_delete=models.CASCADE)
  dayOfWeek = models.IntegerField()
  start_time_local = models.DateTimeField()
  end_time_local = models.DateTimeField()

class Timezone(models.Model):
  store_id = models.ForeignKey("StoreStatus", on_delete=models.CASCADE)
  timezone_str = models.CharField(max_length=100)