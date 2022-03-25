"""
練習：2022年3月25日

1つのテストケースは
M（カードの素数の種類の数）
P_1 N_1 （素数、カード枚数）
……
P_M N_M

Test Set 1 はカード枚数が高々10枚なのでビット全探索。GCJの小規模問題はとりあえず全探索。これを書けるのも実装能力がそこそこ要るだろう。
練習なので後で書くかも。
"""

"""
Test Set 2 は?
カード枚数が高々100枚。全探索は当然無理。
当然素数であることは使うはず。目標スコアを決めたら、素因数分解により、積のカードは一意に定まる。
それで和が条件を満たしてたら使える。
……でもこれだとうーん。二分探索は使えないし。
目標スコアの全探索? 2から499が1枚ずつあったら目標スコアが2^95 種類あって死亡よ。
あ、逆に目標スコアを和の方から見るのか。和にならなきゃいけないから目標スコアは高々499*100 = 50000で、
これを全探索は間に合うはず。
factorize, 499より上が含まれてたら不可、種類と枚数が出せなかったら不可、出せたら和から引いて一致判定。
OK〜〜〜
"""

"""
Test Set 3 は?
カード枚数が高々10^15 枚。
"""
