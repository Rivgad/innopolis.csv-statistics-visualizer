from app.tests.result import IsAplicableResult, Result
from app.tests.statistical_test import StatisticalTest


import pandas as pd
from scipy import stats


from typing import List


class MannWhitneyUTest(StatisticalTest):
    def _is_applicable(
        self, dataframe: pd.DataFrame, columns: List[str]
    ) -> IsAplicableResult:
        if (dataframe[columns[0]].dtype not in ["object", "bool"]) and (
            dataframe[columns[1]].dtype not in ["object", "bool"]
        ):
            return (True, None)
        else:
            return (
                False,
                "Mann–Whitney U test requires two numerical variables. Please select other variables or a test.",
            )

    def _compute(self, dataframe: pd.DataFrame, columns: List[str]) -> Result:
        df = dataframe.dropna(subset=columns)

        stat, pvalue = stats.mannwhitneyu(df[columns[0]], df[columns[1]])
        return Result(statistic=stat, pvalue=pvalue)
