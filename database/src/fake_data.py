from openai import OpenAI
import json
from lib.iac_config_helper import IACConfigHelper
# 你的 OpenAI API 金鑰


def query_openai(api_key,prompt):
    try:
        # 使用 OpenAI 的 `gpt-4` 模型發送請求

        # 設定 OpenAI API 金鑰
        # openai.api_key = api_key
        client = OpenAI(
            api_key=api_key,  # this is also the default, it can be omitted
        )
        response = client.chat.completions.create(
            model="gpt-4",
            prompt=prompt,
            max_tokens=4800,
        )
        # 將回應保存為 JSON
        response_json = json.dumps(response, ensure_ascii=False, indent=4)
        
        # 寫入檔案
        with open('response.json', 'w', encoding='utf-8') as file:
            file.write(response_json)
        
        print("JSON file has been saved.")
        return response_json
    except Exception as e:
        print(f"An error occurred: {e}")
def read_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        response_json = json.load(file)
    return response_json

if __name__ == "__main__":
    config_path = 'config/credential.yaml'
    conn_config = IACConfigHelper.get_conn_info(config_path)
    api_key = conn_config['key']['open_api']
    restaurants = read_json('database/data/restaurants.json')
    menus = read_json('database/data/menus_items.json')
    menu_value = []
    for menus in menus:
        menu_value.append({'item_name':menus['item_name'],'item_description':menus['description']}) 
    # print(menu_value[:1])
    print(len(menu_value))
    unique_list = []
    for item in menu_value:
        if item not in unique_list:
            unique_list.append(item)
    print(len(unique_list))
    # print(unique_list[2])
    for menu in unique_list[151:161]:
        print("可以請你幫我依照下面菜品文字，產出圖片")
        print(menu)
    # from openai import OpenAI
    # client = OpenAI(api_key=api_key)

    # response = client.images.generate(
    # model="dall-e-3",
    # prompt=f"""可以請你幫我依照下面菜品文字，產出圖片
    # {menu_value}""",
    # size="1024x1024",
    # quality="standard",
    # n=1,
    # )
    # image_url = response.data[0].url
    # print(image_url)
    # for menu in menu_value[:1]:
    #     prompt = f"""
    #     菜單項目資訊:
    #     {menu}
    #     可以請你幫我依照 menu_value 依照每個菜品品項的名字和菜單描述每家品牌餐廳名和特性，產出圖片，並依照回傳圖片
        
    #     """
        
    
    #     response_json = query_openai(api_key,prompt)
