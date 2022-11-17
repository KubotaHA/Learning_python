#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import python_learning

class Test_python_learning(unittest.TestCase):
    def test_multiplication_01(self):
        self.assertEqual(
            # テスト対象の実行結果
            python_learning.multiplication(6, 3),
            # 期待する値
            18
        )

    def test_division_01(self):
        self.assertEqual(
            # テスト対象の実行結果
            python_learning.division(6, 3),
            # 期待する値
            2
        )

    def test_division_02(self):
            # 例外のテスト
            with self.assertRaises(ZeroDivisionError):
                # テスト対象の実行(異常系)
                python_learning.division(6, 0)

    # def test_addition_01(self):
    #     self.assertEqual(
    #         # テスト対象の実行
    #         python_learning.addition(6, 3),
    #         # 期待する値
    #         9
    #     )

    # def test_subtraction_01(self):
    #     self.assertEqual(
    #         # テスト対象の実行
    #         python_learning.subtraction(6, 3),
    #         # 期待する値
    #         3
    #     )


if __name__ == "__main__":
    unittest.main()