#!/usr/bin/env python
import pandas as pd

# df1データフレームの例
data = {
    "CLASS": ["Straight", "Straight", "Straight", "Straight", "Straight", "B_Only", "B_Only", "B_Only", "B_Only", "B_Only", "B_Only", "B_Only", "Straight", "Straight", "Straight", "Straight", "B_Only", "B_Only", "B_Only", "B_Only"],
    "OPE_NAME": ["JIK-VM", "JIK-SAL", "JIK-VM2", "JIK-VMH2", "JIK-VMHA", "JIK-VM", "JIK-SAL", "JIK-VM2", "JIK-VMH2", "JIK-VMHA", "JIK-FULL", "JIK-MMJ", "JIK-VM", "JIK-SAL", "JIK-VM2", "JIK-VMH2", "JIK-VM", "JIK-SAL", "JIK-VM2", "JIK-VMH2"],
    "HIST_CD": ["ST", "ST", "ST", "ST", "DF", "ST", "ST", "ST", "ST", "ST", "ST", "ST", "BA", "BA", "BA", "BA", "BA", "BA", "BA", "BA"],
    "QTY": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    "SUB": [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
    "GOMI": [41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60],
    "NO_GOMI": [61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
    "CG": [81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
}

df1 = pd.DataFrame(data)

# 必要なカラムの初期化
items = ["yield"] * 4 + ["GOMI", "NO_GOMI", "CG"]
ope_names = ["JIK-VM", "JIK-SAL", "JIK-VM2", "JIK-VMH2", "JIK-VMHA", "JIK-VMHA", "JIK-VMHA"]
作業数 = []
対象数 = []

# 分岐処理
for item, ope_name in zip(items, ope_names):
    if item == "yield":
        作業数.append(df1[(df1["OPE_NAME"] == ope_name) & (df1["HIST_CD"] == "ST")]["QTY"].values[0])
        対象数.append(df1[(df1["OPE_NAME"] == ope_name) & (df1["HIST_CD"] == "BA")]["SUB"].values[0])
    elif item == "GOMI":
        作業数.append(df1[(df1["OPE_NAME"] == ope_name) & (df1["HIST_CD"] == "DF")]["QTY"].values[0])
        対象数.append(df1[(df1["OPE_NAME"] == ope_name) & (df1["HIST_CD"] == "DF")]["GOMI"].values[0])
    elif item == "NO_GOMI":
        作業数.append(df1[(df1["OPE_NAME"] == ope_name) & (df1["HIST_CD"] == "DF")]["QTY"].values[0])
        対象数.append(df1[(df1["OPE_NAME"] == ope_name) & (df1["HIST_CD"] == "DF")]["NO_GOMI"].values[0])
    elif item == "CG":
        作業数.append(df1[(df1["OPE_NAME"] == ope_name) & (df1["HIST_CD"] == "DF")]["QTY"].values[0])
        対象数.append(df1[(df1["OPE_NAME"] == ope_name) & (df1["HIST_CD"] == "DF")]["CG"].values[0])

# 新しいデータフレームを作成
df2 = pd.DataFrame({
    "ITEM": items,
    "OPE_NAME": ope_names,
    "作業数": 作業数,
    "対象数": 対象数
})

# 結果を表示
print(df2)
