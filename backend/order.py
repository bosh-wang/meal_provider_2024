import pandas as pd
import json

data = {'order_number': [1001],
        'time': ['2024.02.05 12:23:02'],
        'customer_ID': ['311120202'],
        'restaurant': ['KFC'],
        'order_items': ['fry chicken'],
        'total_price':[300]}
 
orders_df = pd.DataFrame(data)
print(orders_df)

# 读取 order.json 文件并解析数据
with open('order.json', 'r') as f:
    order_data = json.load(f)

# 获取新的订单编号
new_order_number = str(int(orders_df['order_number'].iloc[-1]) + 1).zfill(3)
print(new_order_number)
# 解析 order.json 中的数据
customer_ID = order_data['customer_ID']
restaurant = order_data['restaurant']
order_items = order_data['items']
# 仅提取项目名称
item_names = ', '.join(item['name'] for item in order_items)
total_price = sum(item['price'] for item in order_items)

# 构建新的订单数据并添加到 DataFrame 中
orders_df.loc[len(orders_df.index)] = [new_order_number, pd.Timestamp.now().tz_localize('UTC'),customer_ID, restaurant,item_names,total_price]
# new_order = {'order_number': new_order_number, 'customer_ID': customer_ID, 'time': '2024.5.5 12:30', 'restaurant': restaurant, 'order_items': order_items, 'total_price': total_price}
# orders_df.insert('order_number': new_order_number, 'customer_ID': customer_ID, 'time': '2024.5.5 12:30', 'restaurant': restaurant, 'order_items': order_items, 'total_price': total_price)

# 打印 DataFrame
print("DataFrame:")
print(orders_df)

# 将 DataFrame 转换为 JSON 格式并打印
json_output = orders_df.tail(1).to_json(orient='records', indent=4)
print("\nJSON output:")
print(json_output)

# # 将 JSON 输出保存到文件中
# with open('orders_output.json', 'w') as f:
#     f.write(json_output)