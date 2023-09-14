from django.shortcuts import render,redirect
from .models import User,Product_mst,Product_sub_cat

# Create your views here.

def index(request):
    return render(request,'index.html')

def register(request):
    if request.method == "POST":
        try:
            User.objects.get(email = request.POST['email'])
            msg = 'email is already register '
        except:
          if request.POST['password'] == request.POST['cpassword']:
                User.objects.create(
                usertype = request.POST['usertype'],
                name= request.POST['name'],
                email= request.POST['email'],
                mobile= request.POST['mobile'],
                gender= request.POST['gender'],
                password = request.POST['password'],
                
                )
                msg = " your data is registerd "
                return render(request,'register.html',{'msg':msg})
          else:
                msg=" password and confirme password is not mached"
                return render(request,'register.html',{'msg':msg})


            
    
    return render(request,'register.html')

def login(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			if user.password==request.POST['password']:
				if user.usertype=="Admin":
					request.session['email']=user.email
					request.session['name']=user.name
					return render(request,'admin.html')
				else:
					request.session['email']=user.email
					request.session['name']=user.name
					return render(request,'productmanager.html')
			else:
				msg="Incorrect Password"
				return render(request,'login.html',{'msg':msg})
		except:
			msg="Email Not Registered"
			return render(request,'login.html',{'msg':msg})
	else:
		return render(request,'login.html')
	
def logout(request):
	try:
		del request.session['email']
		del request.session['name']
		return redirect(request,'index.html')
	except:
		return render(request,'index.html')
	

def add_product(request):
	if request.method == "POST":
		try:
			Product_mst.objects.get(id=request.POST['id'])
			msg = 'the id is already exist '
			return render(request,'add_product.html',{'msg':msg})
		
		except:
			
			Product_mst.objects.create(
				id = request.POST['id'],
				product_brand = request.POST['product_brand']
			)
			msg = 'your product data add successfully'
			return render(request, 'add_product.html',{'msg':msg})
	else:
		return render(request,'add_product.html')
	
def add_detail(request):
	if request.method == "POST":
		try:
			Product_sub_cat.objects.get( pname= request.POST['pname'])
			msg="Product Details Alredy Exist"
			return render(request,'add_product_d.html',{'msg':msg})
		except:
			
			Product_sub_cat.objects.create(
				pname=request.POST['pname'],
				product_price=request.POST['product_price'],
				product_img=request.POST['product_image'],
				product_model=request.POST['product_model'],
				product_ram=request.POST['product_ram']
			)
			msg="Product Sub Details Add Successfully"
			return render(request,'add_product_d.html',{'msg':msg})
	else:
		return render(request,'add_product_d.html')
def view_product(request):
	products = Product_sub_cat.objects.all()
	return render(request,'view-product.html',{'products':products})

def edit_product(request,pk):
	products=Product_sub_cat.objects.get(pk=pk)
	if request.method == "POST":
		products.pname = request.POST['pname']
		products.product_price = request.POST['product_price']
		products.product_model= request.POST['product_model']
		products.product_ram = request.POST['Product_ram']

		try:
			products.product_img = request.FILES['product_img']

		except:
				
				pass	
		products.save()
		msg = "product edited"
		return render(request,'edit-product.html',{'msg':msg,'products':products})
	else:
		return render(request,'edit-product.html',{'products':products})
	

def delete_product(request,pk):
	products = Product_sub_cat.objects.get(pk= pk)
	products.delete()
	return redirect('view-product')

def edit_product(request,pk):
	products = Product_sub_cat.objects.get(pk = pk)
	if request.method == 'POST':
		products.pname = request.POST['pname']
		products.product_price = request.POST['product_price']
		products.product_model = request.POST['product_model']
		products.product_ram = request.POST['product_ram']
		try:
			products.product_img = request.FILES['prouduct_img']
		except:
			pass

		products.save()
		msg = 'product successfully edited'
		return render(request,'edit-product.html',{'msg':msg},{'products':products})
	else:
		return render(request,'edit-product.html',{'products':products})
		