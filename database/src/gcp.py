from google.cloud import storage
import os
from google.oauth2 import service_account
from lib.json_helper import read_json, write_json


def upload_images_to_bucket(key_path, folder_path, project, bucket_name) -> str:
    # 初始化 GCP Storage 客戶端
    credentials = service_account.Credentials.from_service_account_file(key_path)
    client = storage.Client(credentials=credentials, project=project)
    bucket = client.get_bucket(bucket_name)
    # 遍歷資料夾中的所有檔案
    if filename.endswith(".png") or filename.endswith(".jpg"):  # 假設只上傳 PNG 和 JPG 檔案
        blob = bucket.blob(filename)
        blob.upload_from_filename(os.path.join(folder_path, filename))
        # 設置 blob 為公開
        blob.make_public()
        return blob.public_url

        # 儲存 URL 到資料庫
        # store_url_in_db(blob.public_url, filename)


if __name__ == "__main__":
    key_path = "config/meal_provider_system.json"
    folder_path = "database/data/pic/restaurants"
    project = "cloudnative"
    bucket_name = "meal_provider_system"
    # json_file_path = "database/data/menus_items.json"
    # url_file_path = "database/data/menus_items_image_url.json"
    # menu_items = read_json(json_file_path)

    # # 建立一個以 item_name 為鍵，item_id 為值的字典
    # item_list = [
    #     {"item_id": item["item_id"], "item_name": item["item_name"], "image_url": None}
    #     for item in menu_items
    # ]
    # for filename in os.listdir(folder_path)[1:]:
    #     image_url = upload_images_to_bucket(key_path, folder_path, project, bucket_name)
    #     item_name = filename.rsplit(".", 1)[0]
    #     for item in item_list:
    #         if item["item_name"] == item_name:
    #             item["image_url"] = image_url
    #             print(item)
    #             break
    # write_json(url_file_path, item_list)

    json_file_path = "database/data/restaurants.json"
    rest_items = read_json(json_file_path)
    for filename in os.listdir(folder_path):
        rest_name = filename.rsplit(".", 1)[0]
        image_url = upload_images_to_bucket(key_path, folder_path, project, bucket_name)
        for rest in rest_items:
            if rest["name"] == rest_name:
                rest["image_url"] = image_url
                break
    write_json("database/data/restaurants_new.json", rest_items)
    # print(rest_items)
