from django.urls import path
from customer import views 
urlpatterns = [
    path("register/",views.SignUpView.as_view(),name="signup"),
    path("signin",views.SignInView.as_view(),name="signin"),
    path("home",views.IndexView.as_view(),name="index"),
    path("products/<int:id>",views.ProductDetailView.as_view(),name="product-detail"),
    path("products/<int:id>/carts/add",views.AddtoCartView.as_view(),name="cart-add"),
    path("customer/carts/all",views.CartlistView.as_view(),name="cart-list"),
    path("customer/carts/<int:id>/change",views.CartRemoveView.as_view(),name="cart-change"),
    path("orders/add/<int:id>",views.MakeorderView.as_view(),name="create-order"),
    path("orders/all",views.MyorderView.as_view(),name="placed-orders"),
    path("orders/<int:id>/cancell",views.CancellorderView.as_view(),name="cancelled"),
    path("offer/all",views.OfferView.as_view(),name="offer"),

]
#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