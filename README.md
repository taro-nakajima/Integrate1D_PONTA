# Integrate1D_PONTA
Integrating peak intensity measured at PONTA

## How to use
python Integrate1D_PONTA.py _(list file name)_ _(output file name)_

## parameters in the list file
- skip line
ファイルの冒頭でスキップする行数。PONTAのデータファイルの場合は「33」にする。
- index of x  (column number 0,1,2,3...)
積分変数の列番号。ゼロから始まることに注意。PONTAのデータの場合は通常「1」にする。

6     # index of F(x)
-1     # index of Err of F(x). If the error of F(x) is sqrt(F(x)), put a negative value.
35     # index of T or H.
96     # Initial run number
2     # Run number interval
-1    # Number of points used for background estimation (negative value for integration without BG subtraction.) 
0.488 0.512    # x range for integration
