from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Sum, Avg
from .models import Category, Supplier, Item
from .forms import CategoryForm, SupplierForm, ItemForm

# --- Dashboard ---
@login_required
def dashboard(request):
    total_stock = Item.objects.aggregate(total_stock=Sum('stock'))['total_stock'] or 0
    total_value = Item.objects.aggregate(total_value=Sum('price'))['total_value'] or 0
    avg_price = Item.objects.aggregate(avg_price=Avg('price'))['avg_price'] or 0
    low_stock_items = Item.objects.filter(stock__lt=5)

    context = {
        'total_stock': total_stock,
        'total_value': total_value,
        'avg_price': avg_price,
        'low_stock_items': low_stock_items,
    }
    return render(request, 'dashboard.html', context)

# --- Login Custom ---
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# --- Logout ---
def logout_view(request):
    logout(request)
    return redirect('login')

# --- CRUD Category ---
@login_required
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'categories/category_list.html', {'categories': categories})

@login_required
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm()
    return render(request, 'categories/category_form.html', {'form': form, 'title': 'Add New Category'})

@login_required
def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'categories/category_form.html', {'form': form, 'title': 'Edit Category'})

@login_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('categories')
    return render(request, 'categories/category_confirm_delete.html', {'category': category})

# --- CRUD Supplier ---
@login_required
def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'suppliers/supplier_list.html', {'suppliers': suppliers})

@login_required
def supplier_create(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('suppliers')
    else:
        form = SupplierForm()
    return render(request, 'suppliers/supplier_form.html', {'form': form, 'title': 'Add New Supplier'})

@login_required
def supplier_edit(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            return redirect('suppliers')
    else:
        form = SupplierForm(instance=supplier)
    return render(request, 'suppliers/supplier_form.html', {'form': form, 'title': 'Edit Supplier'})

@login_required
def supplier_delete(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        supplier.delete()
        return redirect('suppliers')
    return render(request, 'suppliers/supplier_confirm_delete.html', {'supplier': supplier})

# --- CRUD Item ---
@login_required
def item_list(request):
    items = Item.objects.select_related('category', 'supplier')
    return render(request, 'items/item_list.html', {'items': items})

@login_required
def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('items')
    else:
        form = ItemForm()
    return render(request, 'items/item_form.html', {'form': form, 'title': 'Add New Item'})

@login_required
def item_edit(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('items')
    else:
        form = ItemForm(instance=item)
    return render(request, 'items/item_form.html', {'form': form, 'title': 'Edit Item'})

@login_required
def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('items')
    return render(request, 'items/item_confirm_delete.html', {'item': item})

# --- Low Stock Page ---
@login_required
def low_stock_page(request):
    low_stock_items = Item.objects.filter(stock__lt=5)
    return render(request, 'low_stock/low_stock.html', {'items': low_stock_items})

# --- Summary Page ---
@login_required
def summary_page(request):
    total_stock = Item.objects.aggregate(total_stock=Sum('stock'))['total_stock'] or 0
    total_value = Item.objects.aggregate(total_value=Sum('price'))['total_value'] or 0
    avg_price = Item.objects.aggregate(avg_price=Avg('price'))['avg_price'] or 0

    context = {
        'total_stock': total_stock,
        'total_value': total_value,
        'avg_price': avg_price,
    }
    return render(request, 'summary/summary.html', context)

# --- Profile Page ---
@login_required
def profile(request):
    return render(request, 'profile/profile.html')
