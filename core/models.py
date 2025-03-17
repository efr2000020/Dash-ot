from django.db import models

from django.db import models

class Node(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Sensor(models.Model):
    node = models.ForeignKey(Node, related_name="sensors", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.node.name} - {self.name}"

class Actuator(models.Model):
    node = models.ForeignKey(Node, related_name="actuators", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.node.name} - {self.name}"

