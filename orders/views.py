from django.shortcuts import render

from .forms import OrderForm


def create_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            if order.is_pending:
                return render(request, "orders/order_fail.html")
            return render(request, "orders/order_success.html")
        return render(request, "orders/order_create.html", {"form": form})
    form = OrderForm()
    return render(request, "orders/order_create.html", {"form": form})

