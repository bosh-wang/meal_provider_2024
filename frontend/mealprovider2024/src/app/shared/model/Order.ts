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
export class Order_HR {
  customer_id !:string;
  order_id!: string;
  order_date!: string;
  total_price!: number;
  paid !: boolean;
};
export class Order_Kitchen {
  customer_id !:string;
  order_id!: string;
  order_date!: string;
  confirmed_date !: string;
  prepared_date !: string;
  completed_date !: string;
  canceled_date !: string;
  items!:OrderItem[];
  order_status!: string
  total_price!: number;
  paid !: boolean;
};