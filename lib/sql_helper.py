import os


def readsqlfile(sqlFileName_str: str):
    sql_file_str = os.path.join(os.getcwd(), sqlFileName_str)
    with open(sql_file_str, "r") as r:
        sqltxt = r.read()
    return sqltxt
