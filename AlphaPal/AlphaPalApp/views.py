from django.shortcuts import render, redirect
from .models import Client, AlphaReportTable, Transaction, Account
from .forms import ClientForm, TransactionForm, AccountForm
from django.contrib.auth.decorators import login_required
#from .decorators import allowed_users


# Create your views here.

def home(request):
    return render(request, 'AlphaPalApp/home.html')

@login_required(login_url='login')
def loansafe(request):
    return render(request, 'AlphaPalApp/loansafe.html')


@login_required(login_url='login')
#@allowed_users(allowed_roles=['Admin'])
def process(request):
    user = Client.objects.all()
    context = {'user': user}
    return render(request, 'AlphaPalApp/process.html', context)


@login_required(login_url='login')
def transaction(request):
    form = TransactionForm()

    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'AlphaPalApp/transaction.html', context)


@login_required(login_url='login')
def summary(request):
    tran = Transaction.objects.all()
    context = {'tran': tran}
    return render(request, 'AlphaPalApp/summary.html', context)


@login_required(login_url='login')
def detail(request, pk):
    det = Client.objects.filter(client_id=pk)
    many = Account.objects.filter(client=pk)
    context = {'det': det, 'many': many}
    return render(request, 'AlphaPalApp/detail.html', context)


@login_required(login_url='login')
def createform(request):
    form = ClientForm()

    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('process')

    context = {'form': form}
    return render(request, 'AlphaPalApp/createform.html', context)


@login_required(login_url='login')
def update(request, pk):
    order = Client.objects.get(client_id=pk)
    form = ClientForm(instance=order)

    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES, instance=order)
        if form.is_valid():
            form.save()
            return redirect('process')

    context = {'form': form}

    return render(request, 'AlphaPalApp/update.html', context)


@login_required(login_url='login')
def delete(request, pk):
    mainns = Client.objects.get(client_id=pk)
    if request.method == 'POST':
        mainns.delete()
        return redirect('process')

    context = {'mainns': mainns}
    return render(request, 'AlphaPalApp/delete.html', context)

@login_required(login_url='login')
def createaccount(request):
    form = AccountForm()

    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'AlphaPalApp/createaccount.html', context)
