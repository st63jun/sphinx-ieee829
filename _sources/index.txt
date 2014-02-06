Sphinx IEEE829 Extensions
=========================

ソフトウェアテストの文書の標準規格であるIEEE829 [#]_ についての文書と、IEEE829に準拠した文書を作成・管理しやすくするための Sphinx [#]_ の拡張プラグインについてのドキュメントです。

素人が調べながら書いているので不適切な部分があるかもしれません。間違い等があればご指摘いただけると幸いです。

ソースコード
   https://github.com/st63jun/sphinx-ieee829

IEEE829について
===============

IEEE829はソフトウェアのテストの各工程で作成する文書の標準規格です。以下の9の文書から構成されています。各文書の目的はWikipedia [#]_ を参考に記述しています。

.. toctree::
   :maxdepth: 1
   :numbered:

   mtp
   ltp
   ltd
   ltc
   ltpr
   ltl
   ar
   ltr
   mtr

開発者はこれらの標準に則ってテスト仕様を書くこともできますし、IEEE829を土台にして独自に様式を作成することもできます。

拡張プラグインについて
======================

``extensions/ieee829.py`` が拡張プラグインのソースコードです。、IEEE829文書の作成のためのディレクティブやロールをサポートする ``ieee829`` というドメインを新たに追加します。

このプラグインは（今のところ）以下の機能を持っています。

* 文書識別番号の設定
* 文書識別番号によるクロスリファレンス (例: :ieee829:mtp:`9999`)

参考資料
========

.. [#] `IEEE829-1998 Standard for Software and System Test Documentation <http://dx.doi.org/10.1109/IEEESTD.1998.88820>`_
.. [#] http://sphinx-doc.org/
.. [#] https://en.wikipedia.org/wiki/IEEE_829
