# Tweet Console Dummy

[TweetConsole](http://www.forest.impress.co.jp/docs/review/20100518_367685.html)の`/t`と`/txt`だけを実装した。

## 使用法
1. Python 2.7とtweepyを何らかの手段でインストールする
2. `python twtcnsldmy.py /t a`でAuth URLが表示されるので、ブラウザで開いて、表示されたPINコードを入力する
3. `python twtcnsldmy.py /t text`で`text`をツイート、`python twtcnsldmy.py /txt n file`で`file`の`n`行目をツイート
