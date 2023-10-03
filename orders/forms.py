from django import forms
from customers.models import Customer
from .models import Order


class OrderForm(forms.Form):
    email = forms.EmailField(max_length=255, label="E-Mail")
    robot_serial = forms.CharField(max_length=5, min_length=5, label="Серийный номер Робота")

    def save(self):
        customer = Customer.objects.create(email=self.cleaned_data['email'])

        order = Order(
            customer=customer,
            robot_serial=self.cleaned_data['robot_serial'].upper(),
        )
        if not order.is_exist_robot():
            order.is_pending = True

        order.save()

        return order

