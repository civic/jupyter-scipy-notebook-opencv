jupyter-scipy-notebook-opencv
================================

jupyter/scipy-notebookにopencvを入れたローカル作業用jupyterコンテナ。

ビルド
-----

```
$ docker build --pull --rm -t jupyter-scipy-notebook-opencv .
```

実行
-----

```
$ ./start-jupyter.sh
```

ブラウザでlocalhost:8888をひらく。


機能拡張
---------

support.pyというモジュールを追加してある。

opencvで生成したイメージオブジェクト(numpy.array)を画像として表示する関数を実装してある。

```
from support import cv_img

img = cv.imread('example.png')
cv_img(img)

```
もしくはマジックコマンド %cv_imgも使用可能になる。

```
import support

img = cv.imread('example.png')
%cv_img img
```

