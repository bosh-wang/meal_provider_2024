from lib.json_helper import read_json, write_json

# image_url_json = read_json('database/data/menus_items_image_url.json')
# new_list = {}
# for item in image_url_json:
#     if item['image_url'] is not None:
#         new_list[item['item_name']] = item['image_url']

# print(new_list)
# write_json('database/data/menus_items_non_dp_image_url.json',new_list)
mapping_data = read_json("database/data/menus_items_non_dp_image_url.json")
menu_items = read_json("database/data/menus_items.json")
for item in menu_items:
    if item["item_name"] in mapping_data:
        item["image_url"] = mapping_data[item["item_name"]]
    else:
        print(f"Error: {item['item_name']} not found.")
write_json("database/data/menus_items_new.json", menu_items)
