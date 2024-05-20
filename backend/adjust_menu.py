import pandas as pd
import json

fast_food = {
    "Restaurant": ["Tasty Burgers","Tasty Burgers", "Pizza Palace", "Pizza Palace"],
    "Items": ["Classic Burger","Cheeseburger", "Pepperoni Pizza", "Margherita Pizza"],
    "Price": [8.99,9.99, 11.99, 10.99]
}
df_menu = pd.DataFrame(fast_food)

# 读取 order.json 文件并解析数据
with open('adjust_menu.json', 'r') as f:
    adj_data = json.load(f)
# 解析 order.json 中的数据
add_del = adj_data['add_del']
Restaurant = adj_data['restaurant']
Item = adj_data['items'][0]['name']
price = adj_data['items'][0]['price']

if add_del == 'add':
    df_menu.loc[len(df_menu.index)] = [Restaurant, Item,price]
elif add_del == 'del':
    for index, row in df_menu.iterrows():
        if row['Restaurant'] == Restaurant and row['Items'] == Item:
            ind = index
    df_menu = df_menu.drop(index = ind)
else: #adj
    for index, row in df_menu.iterrows():
        if row['Restaurant'] == Restaurant and row['Items'] == Item:
            ind = index
            print(ind)
    df_menu.loc[ind,'Price'] = price
print(df_menu)
restaurants = []
for name, group in df_menu.groupby("Restaurant"):
    items = [{"name": row["Items"], "price": row["Price"]} for idx, row in group.iterrows()]
    restaurants.append({"name": name, "items": items})
print(restaurants)
