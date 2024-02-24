from django.shortcuts import render
# from django.db.models.functions import datetime
import datetime
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CustomerForm
from .models import Customer



class CustomerCreateView(CreateView):
    template_name = 'asbook.customer/create_customer.html'
    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy('home_page')
    # permission_required = 'customer.add_customer'

    def form_valid(self, form):
        if form.is_valid():
            new_customer = form.save()

            get_message = f'Clientul cu numele {new_customer.first_name} {new_customer.last_name} a fost inregistrat'

            # HistoryCustomer.objects.create(message=get_message,
            #                               created_at=datetime.datetime.now(),
            #                               active=True,
            #                               user_id=self.request.user.id)

        return redirect('list-of-customers')


from django.shortcuts import redirect
