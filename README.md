# robosys_ROS2
![test](https://github.com/Kenzo-Fujisaki/robosys_ROS2/actions/workflows/test.yml/badge.svg)

本リポジトリは2022年度ロボットシステム学の課題2で作成したROS2パッケージです。

本パッケージでは以下のようにおみくじを引くことが出来ます。

<img src = "https://user-images.githubusercontent.com/85381022/210080607-9b6f2ae1-989f-4029-9da9-cf444abd38a4.png" width = "60%">

---

## パッケージの概要


<img src = "https://user-images.githubusercontent.com/85381022/210123489-5712bc3c-f106-4918-a483-27f1c106e08b.png" width = "40%">

* `fortune`: 1-100の間の数をランダム生成
* `result`: `fortune`でランダム生成された数字を受け取り、番号に対応したおみくじを表示
* `/number`
    * `fortune`にてランダム生成される数字を格納し、`result`に格納された数字を渡す。
    * メッセージの型は16ビットの符号付き整数

---

## 実行方法
  ```
  $ ros2 launch robosys_ROS2 omikuji.launch.py
  ```

---

## 動作確認済み環境
* OS: Ubuntu 20.04 LTS, Ubuntu 22.04 LTS
* ROS: foxy, humble

---

## ライセンス

  * このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
  * このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
      * [ryuichiueda/my_slides robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)
  * © 2022 Kenzo Fujisaki