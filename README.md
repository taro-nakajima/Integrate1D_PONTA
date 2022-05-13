# Integrate1D_PONTA
Integrating peak intensity measured at PONTA

## How to use
python Integrate1D_PONTA.py _(list file name)_ _(output file name)_

## parameters in the list file
- skip line :
ファイルの冒頭でスキップする行数。PONTAのデータファイルの場合は「33」にする。
- index of x  (column number 0,1,2,3...) :
スキャン変数の列番号。ゼロから始まることに注意。PONTAのデータの場合は通常「1」にする。
- index of F(x) : 強度の列番号。PONTAのデータの場合、角度スキャンだと「4」、hklスキャンだと「6」となる。
- index of Err of F(x) : エラーの列番号。PONTAの場合、データファイルにエラーの列はなく、カウント数のルートがエラーとなる。その場合はこのパラメーターを「-1」など負の値にしておく。（この場合、強度が0カウントだったらエラーは1となるようにしてある）
- index of T or H.: 温度もしくは磁場のデータ列番号。PONTAのデータでは「35」のことが多いが、使用オプションによって変わることがあるので各自確認すること。
- Initial run number : スキャン番号の初期値（特に計算には用いられず、表示用）
- Run number interval : スキャン番号の間隔。例えば一連の温度スキャンで100, 102, 104, 106....番のデータを積分したいときは initialが100で、intervalが2。
- Number of points used for background estimation : バックグラウンド推定に使うデータ点数。例えば「３」と入れておくと、下の「x range for integration」の範囲に収まっているデータについて、右端から３点、左端から３点のデータを平均して、その間を線形補間するバックグラウンドを定義し、積分強度から差し引いてくれる。バックグラウンドの差引を行わない場合は「-1」などの負の値を入れておく。 
- x range for integration : 数値積分の範囲。
