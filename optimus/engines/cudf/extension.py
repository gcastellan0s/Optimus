import ujson

import numpy as np
import pandas as pd

from optimus.engines.base.extension import BaseExt
from optimus.helpers.columns import parse_columns
from optimus.helpers.json import json_converter
from cudf.core import DataFrame



def ext(self: DataFrame):
    class Ext(BaseExt):

        def __init__(self, df):
            super().__init__(df)



        @staticmethod
        def profile(columns, lower_bound, upper_bound):
            """

            :param lower_bound:
            :param upper_bound:
            :param columns:
            :return:
            """
            df = self[lower_bound:upper_bound]
            # columns = parse_columns(df, columns)
            # result = {}

            columns = parse_columns(df, columns)
            # print(df)
            result = {"sample": {"columns": [{"title": col_name} for col_name in df.cols.select(columns).cols.names()],
                                 "value": df.rows.to_list(columns)}}

            # df = df.dropna()
            df = self
            for col_name in columns:
                if df[col_name].dtype == np.float64 or df[col_name].dtype == np.int64:
                    result.update(df.cols.hist(col_name))
                else:
                    # df[col_name] = df[col_name].astype("str").dropna()
                    # print("asdfakshdf")
                    result.update(df.cols.frequency(col_name))
            return result

        @staticmethod
        def cache():
            pass

        @staticmethod
        def sample(n=10, random=False):
            pass

        @staticmethod
        def pivot(index, column, values):
            pass

        @staticmethod
        def melt(id_vars, value_vars, var_name="variable", value_name="value", data_type="str"):
            pass

        @staticmethod
        def query(sql_expression):
            pass

        @staticmethod
        def partitions():
            pass

        @staticmethod
        def partitioner():
            pass

        @staticmethod
        def repartition(partitions_number=None, col_name=None):
            pass

        @staticmethod
        def show():
            df = self
            return df

        @staticmethod
        def debug():
            pass

        @staticmethod
        def create_id(column="id"):
            pass

    return Ext(self)


DataFrame.ext = property(ext)