from lib.iac_config_helper import IACConfigHelper
from lib.pg_helper import PGConnect
from crud_pg import insert_data, create_table, update_date
from lib.json_helper import read_json

if __name__ == "__main__":
    config_path = "config/credential.yaml"
    conn_config = IACConfigHelper.get_conn_info(config_path)
    pg_config = conn_config["database"]["postgres"]
    pg_connection = PGConnect(**pg_config)
    pg_connection.connect()
    conn = pg_connection.conn
    cur = conn.cursor()
    # Check if the table exists
    print(conn)
    table_list = [
        "users",
        "employees",
        "restaurants",
        "restaurants_staffs",
        "restaurants_stands",
        "menus",
        "menus_items",
        "meals_ratings",
        "orders",
        "orders_items",
        "shopping_cart",
    ]
    # for table in table_list:
    # table = "orders_items"
    # sqlpath = f"database/sql/create/create_{table}_table.sql"
    # # Prepare to check if the table already exists
    # create_table(conn, sqlpath, table)
    # json_path = f"database/data/{table}.json"
    # insert_json = read_json(json_path)
    # print(type(insert_json))
    # insert_data(conn, insert_json, table)

    # update the column value
    # update_table = "restaurants"
    # json_path = f"database/data/{update_table}_new.json"
    # update_json = read_json(json_path)
    # update_columns = ["image_url"]
    # condition_column = "restaurant_id"
    # update_date(conn, update_table, update_json, update_columns, condition_column)
    # update the column value for the second time
    # update_table = "menus_items"
    # json_path = f"database/data/updated_menus_items_category_classified.json"
    # update_json = read_json(json_path)
    # print(update_json)
    # update_columns = ["category"]
    # condition_column = "item_name"
    # update_date(conn, update_table, update_json, update_columns, condition_column)

    # update the column pwd value of for pwd
    update_table = "users"
    json_path = f"database/data/{update_table}_with_hashed_passwords.json"
    update_json = read_json(json_path)
    update_columns = ["password_hash"]
    condition_column = "user_id"
    update_date(conn, update_table, update_json, update_columns, condition_column)
