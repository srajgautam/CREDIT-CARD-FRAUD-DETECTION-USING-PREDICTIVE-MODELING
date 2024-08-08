"""leveraging_product_characteristics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from Remote_User import views as remoteuser
from creditcard_fraud import settings
from Service_Provider import views as serviceprovider
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', remoteuser.login, name="login"),


    path('Register1/', remoteuser.Register1, name="Register1"),

    path('Recommend/(?P<pk>\d+)/', remoteuser.Recommend, name="Recommend"),
    path('Review/(?P<pk>\d+)/', remoteuser.Review, name="Review"),
    path('Search_Products/', remoteuser.Search_Products, name="Search_Products"),
    path('View_All_Product_Details/', remoteuser.View_All_Product_Details, name="View_All_Product_Details"),
    path('View_Product_Reviews/', remoteuser.View_Product_Reviews, name="View_Product_Reviews"),
    path('ratings/(?P<pk>\d+)/', remoteuser.ratings, name="ratings"),
    path('dislikes/(?P<pk>\d+)/', remoteuser.dislikes, name="dislikes"),
    path('likes/(?P<pk>\d+)/', remoteuser.likes, name="likes"),
    path('ViewTrending/', remoteuser.ViewTrending, name="ViewTrending"),
    path('ViewYourProfile/', remoteuser.ViewYourProfile, name="ViewYourProfile"),
    path('purchase/(?P<pk>\d+)/', remoteuser.purchase, name="purchase"),
    path('View_Product_Recommends/', remoteuser.View_Product_Recommends, name="View_Product_Recommends"),
    path('View_All_Collusion_Sellers/', remoteuser.View_All_Collusion_Sellers, name="View_All_Collusion_Sellers"),
    path('View_Account_Details/', remoteuser.View_Account_Details, name="View_Account_Details"),


    path('Add_Products/', serviceprovider.Add_Products, name="Add_Products"),
    path('serviceproviderlogin/',serviceprovider.serviceproviderlogin, name="serviceproviderlogin"),
    path('View_Remote_Users/',serviceprovider.View_Remote_Users,name="View_Remote_Users"),
    path('ViewTrendings/',serviceprovider.ViewTrendings,name="ViewTrendings"),
    path('charts/(?P<chart_type>\w+)', serviceprovider.charts,name="charts"),
    path('dislikeschart/(?P<dislike_chart>\w+)', serviceprovider.dislikeschart,name="dislikeschart"),
    path('confirmstatus/(?P<pk>\d+)/', serviceprovider.confirmstatus,name='confirmstatus'),
    path('likeschart/(?P<like_chart>\w+)', serviceprovider.likeschart,name="likeschart"),
    path('View_Products_Details/',serviceprovider.View_Products_Details, name='View_Products_Details'),
    path('viewallpostsreviews/', serviceprovider.viewallpostsreviews, name='viewallpostsreviews'),
    path('View_Recommended_Products/', serviceprovider.View_Recommended_Products, name='View_Recommended_Products'),
    path('View_Purchased_Details/', serviceprovider.View_Purchased_Details, name='View_Purchased_Details'),
    path('View_Purchased_Status/', serviceprovider.View_Purchased_Status, name='View_Purchased_Status'),
    path('View_CreditCard_Frauds/', serviceprovider.View_CreditCard_Frauds, name='View_CreditCard_Frauds'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

