# robosys_ROS2
![test](https://github.com/Kenzo-Fujisaki/robosys_ROS2/actions/workflows/test.yml/badge.svg)

本リポジトリは2022年度ロボットシステム学課題2で作成したおみくじができるROS2パッケージです。

---

## 実行方法
  ```
  $ ros2 launch robosys_ROS2 omikuji.launch.py
  ```

---

## 実行結果
![ロボシス課題2](https://user-images.githubusercontent.com/85381022/210080607-9b6f2ae1-989f-4029-9da9-cf444abd38a4.png)

---

## トピックの説明
* `/number`
    * `fortune.py`にてランダム生成される数字を格納し、`result.py`に格納された数字を渡す。
    * メッセージの型は16ビットの符号付き整数

---


## 動作確認済み環境
* OS: Ubuntu 20.04 LTS, Ubuntu 22.04 LTS
* ROS: foxy

---

## ライセンス

  * このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
  * このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
      * [ryuichiueda/my_slides robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)
  * © 2022 Kenzo Fujisaki