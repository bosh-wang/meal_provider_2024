import logging
import os
import yaml

class IACConfigHelper:
    @staticmethod
    def get_conn_info(conn_file):
        with open(conn_file, "r") as file:
            conn_config = yaml.safe_load(file)

        return conn_config
