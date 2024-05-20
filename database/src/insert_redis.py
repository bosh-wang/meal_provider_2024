import redis
import json
import psycopg2
from lib.iac_config_helper import IACConfigHelper
from lib.pg_helper import PGConnect
config_path = 'config/credential.yaml'
conn_config = IACConfigHelper.get_conn_info(config_path)
# 连接到 Redis，加入密码认证
pool = redis.ConnectionPool(
    host=conn_config['database']['redis']['host'], 
    port=conn_config['database']['redis']['port'], 
    db=0, 
    # password=conn_config['database']['redis']['password'],
    decode_responses=True)
redis_client = redis.Redis(connection_pool=pool)
# 连接到 PostgreSQL
pg_config = conn_config['database']["postgres"]
pg_connection = PGConnect(**pg_config)
pg_connection.connect()
conn = pg_connection.conn

# 定义一个函数来获取菜单数据
def get_menus(cursor):
    # 首先尝试从 Redis 获取数据
    menus = redis_client.get('menus')
    if menus:
        return json.loads(menus)
    
    # 如果 Redis 中没有数据，从数据库获取
    cursor.execute("SELECT * FROM menus")
    menu_data = cursor.fetchall()
    # 转换成 JSON 格式
    menus = json.dumps(menu_data)
    # 缓存到 Redis，并设置过期时间为 1 小时
    redis_client.setex('menus', 3600, menus)
    return menu_data

# 使用函数
menu_data = get_menus(conn.cursor())
print(menu_data)
