import { OrderItem } from "./Orderitem";
export class Order_employee {
    order_id!: string;
    order_date!: string;
    items!: OrderItem[];
    total_price!: number;
    order_status! : string;
    paid !: boolean;
  };
  class OrderItems {
    name!: string;
    quantity!: number;
    price!: number;
}
export class Order{
  order_id !: string;
  orderNumber !: number;
  date !: string;
  user_id!: string;
  items!:OrderItems[];
  totalAmount!: number;
  order_status!: string
}