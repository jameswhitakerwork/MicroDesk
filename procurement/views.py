from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import *
from .forms import PRForm, PRAjaxForm, PRCreateFormSet, PRCreateForm, \
    SignatureForm
from filters import PRFilter
import django_tables2 as tables
from django_tables2.utils import A
from jsignature.utils import draw_signature
from django.forms.models import inlineformset_factory

# Tables


class PRTable(tables.Table):
    no = tables.Column(accessor='pr_no')
    link = tables.LinkColumn(
        'pr_view',
        args=[A('pk')],
        orderable=False,
        text='View'
    )

    class Meta:
        model = PurchaseRequest
        fields = ['pr_no', 'pr_creator', 'pr_requisitioner', 'pr_department']
        attrs = {'class': 'paleblue'}


# Views

@login_required
def index(request):
    return render(request, 'hr/index.html', {})


@login_required
def pr_list(request):
    prs = PurchaseRequest.objects.all()
    table = PRTable(prs)
    f = PRFilter(request.GET, queryset=PurchaseRequest.objects.all())

    return render(
        request,
        'procurement/pr_list.html',
        {'prs': prs, 'table': table, 'f': f}
    )


@login_required
def view_signature(request):
    print request.POST
    form = SignatureForm(request.POST or None)
    print form
    if form.is_valid():
        print 'valid form'
        print form.cleaned_data.get('signature')
        signature = form.cleaned_data.get('signature')
        if signature:
            print 'signature found'
            # as an image
            signature_picture = draw_signature(signature)
            print signature_picture
            j = JSignatureModel()
            j.signature = signature
            j.save()

            return render(
                request,
                'hr/signature_form.html',
                {
                    'signature': signature,
                    'form': form
                }
            )
    print 'form not valid'
    return render(
        request,
        'hr/signature_form.html',
        {
            'form': form
        }
    )


def test_signature(request):
    return render(request, 'hr/signature_form.html', {})


class PRCreate(CreateView):
    template_name = 'hr/generic_form.html'
    form_class = PRForm
    success_url = '/procurement'
    exclude = ['pr_no', ]
    formset = PRCreateFormSet

def pr_create(request, object_id=False):
    LinkFormSet = inlineformset_factory(
        PurchaseRequest,
        PurchaseItem,
        extra=5,
        form=PRAjaxForm,
        can_delete=False
    )
    if object_id:
        pr = PurchaseRequest.objects.get(pk=object_id)
    else:
        pr = PurchaseRequest()
    if request.method == "POST":
        f = PRAjaxForm(request.POST, request.FILES, instance=pr)
        fs = LinkFormSet(request.POST, instance=pr)
        if fs.is_valid() and f.is_valid():
            f.save()
            fs.save()
            return HttpResponse('success')
    else:
        f = PRAjaxForm(instance=pr)
        fs = LinkFormSet(instance=pr)
    return render_to_response('procurement/pr_form.html', {'fs': fs, 'f': f, 'pr':pr})


class PRList(ListView):
    model = PurchaseRequest

class PurchaseRequestCreate(CreateView):
    template_name = 'procurement/pr_create.html'
    model = PurchaseRequest
    form_class = PRAjaxForm
    
    def get_success_url(self):
        return reverse('pr_view', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        data = super(PurchaseRequestCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['purchaseitems'] = PRCreateFormSet(self.request.POST)
        else:
            data['purchaseitems'] = PRCreateFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        purchaseitems = context['purchaseitems']
        form.instance.pr_creator = self.request.user
        self.object = form.save()

        if purchaseitems.is_valid():
            purchaseitems.instance = self.object
            purchaseitems.save()
        return super(PurchaseRequestCreate, self).form_valid(form)


class PurchaseRequestUpdate(UpdateView):
    template_name = 'procurement/pr_create.html'
    model = PurchaseRequest
    form_class = PRAjaxForm


class PurchaseRequestView(DetailView):
    model = PurchaseRequest
    template = 'procurement/pr_view.html'


class PurchaseItemUpdate(UpdateView):
    template_name = 'procurement/item_update.html'
    model = PurchaseItem
    form_class = PRCreateForm

    def get_success_url(self):
        return reverse('pr_view', args=(self.object.pr.id,))


def purchase_request_view(request, pk):
    context_dict = {}
    pr = PurchaseRequest.objects.get(id=pk)
    item_set = PurchaseItem.objects.filter(pr=pk)
    context_dict['pr'] = pr
    context_dict['item_set'] = item_set
    return render(request, 'procurement/pr_view.html', context_dict)


@login_required
def add_signature(request, pk, sig_type):
    if not request.user.has_perm('can_confirm_need'):
        messages.warning(request, "You are not authorized to sign this document.")
        return HttpResponseRedirect(reverse('pr_view', args=(pk,)))
    print sig_type
    form = SignatureForm(request.POST or None)
    if form.is_valid():
        print 'valid form'
        signature = form.cleaned_data.get('signature')
        if signature:
            print 'signature found'
            # as an image
            signature_picture = draw_signature(signature)
            j = JSignatureModel()
            j.user = request.user
            j.signature = signature
            j.save()
            pr = PurchaseRequest.objects.get(pk=pk)
            print sig_type
            if sig_type == 'request':
                pr.sig1 = j
            elif sig_type == 'confirm_need':
                pr.sig2 = j
            elif sig_type == 'funds_available':
                pr.sig3 = j
            elif sig_type == 'approve':
                pr.sig4 = j
            pr.save()
            print pr.sig1

            return HttpResponseRedirect(reverse('pr_view', args=(pk,)))
    else:
        return render(
            request,
            'procurement/signature_form.html',
            {
                'form': form,
                'pk': pk,
                'sig_type': sig_type,
            }
        )


def dashboard(request):
    return render(request, 'procurement/dashboard.html', {})
