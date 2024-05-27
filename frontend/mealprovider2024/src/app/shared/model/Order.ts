import { OrderItem } from "./Orderitem";
export class Order {
    order_id!: string;
    orderNumber!: number;
    date!: string;
    items!: OrderItem[];
    totalAmount!: number;
    order_status! : string;
  }