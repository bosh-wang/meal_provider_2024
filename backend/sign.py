import pandas as pd
import json

data = {'customer_ID': ['312706006','311706006'],
        'pwd': ['Accc1234','Vcde1575']}
member_df = pd.DataFrame(data)
member_df =member_df.sort_values(by=['customer_ID'],ascending=True)
print("資料庫內資料:\n",member_df)


def sign_up():
    with open('signin.json', 'r') as f:
        sign_in_data = json.load(f)
    cID = sign_in_data['customer_ID']
    passw = sign_in_data['pwd']
    member_df.loc[len(member_df.index)] = [cID,passw]
    print(member_df)
    print("註冊成功")
def sign_in():
    with open('signin.json', 'r') as f:
        sign_in_data = json.load(f)
    cID = sign_in_data['customer_ID']
    passw = sign_in_data['pwd']
    p = False
    for index, row in member_df.iterrows():
        if row['customer_ID'] == cID and row['pwd'] == passw:
            print('登入成功')
            p=True
        elif row['customer_ID'] == cID and row['pwd'] != passw:
            print('帳號或密碼錯誤')
            p=True
    if p == False:
        print('請先註冊')
# sign_in()
sign_up()