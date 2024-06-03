import { Routes } from '@angular/router';
import { HomeComponent } from './component/pages/home/home.component';
import { FoodPageComponent } from './component/pages/food-page/food-page.component';
import { CartPageComponent } from './component/pages/cart-page/cart-page.component';
import { RestaurantPageComponent } from './component/pages/restaurant-page/restaurant-page.component';
import { LoginComponent } from './component/pages/login/login.component';
import { OrderListComponent } from './component/pages/order-list/order-list.component';
import { OrderAdminComponent } from './component/pages/order-admin/order-admin.component';
import { OrderDashboardComponent } from './component/pages/order-dashboard/order-dashboard.component';
import { OrderHRComponent } from './component/pages/order-hr/order-hr.component';
export const routes: Routes = [
  { path: '', component: HomeComponent },

  { path: 'search/:searchTerm', component: HomeComponent },

  { path: 'food-search/:food-searchTerm', component: RestaurantPageComponent },

  { path: 'tag/:tag', component: HomeComponent },

  { path: 'restaurant-tag/:tag-type', component: HomeComponent },

  { path: 'restaurant/:id', component: RestaurantPageComponent },

  { path: 'food/:food-id', component: FoodPageComponent },

  { path: 'cart-page', component: CartPageComponent },

  { path: 'header', component: HomeComponent },
  { path: 'dashboard', component: OrderDashboardComponent },
  { path: 'profile', component: HomeComponent },
  { path: 'login', component: LoginComponent },
  { path: 'order', component: OrderDashboardComponent },
  { path: 'orderadmin', component: OrderAdminComponent },
  { path: 'orderhr', component: OrderHRComponent },
  { path: 'feedback', component: HomeComponent },
  { path: 'logout', component: HomeComponent },
  { path: 'campus-menu', component: HomeComponent },

  { path: 'campus/:campus-name', component: HomeComponent },
];
