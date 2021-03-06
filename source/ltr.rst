レベルテスト報告
================

レベルテスト報告 (Level Test Report) は実施したテストの結果の概要を記述する文書です。また結果の評価と提案事項も記載します。

レベルテスト報告はレベルテストの実施が1件完了するたびに作成します。

記法
----

.. rst:directive:: .. ieee829:ltr:: id

   レベルテスト報告のセクションを作成します。セクションには ``id`` で文書識別番号を設定します。たとえば ``id`` に 1 を指定すると、このセクションに ``LTR-1`` というユニークなIDが付与されます。

   ``:title``
      文書のタイトルを指定します。指定しない場合はIDがタイトルになります。

.. rst:role:: ieee829:ltr

   レベルテスト報告を参照します。``:ieee829:ltr:`1``` で ``LTR-1`` を参照します。

作成例
------

参考
   http://www.qbook.jp/qptemplate/testieee829s/9

サンプル::

   .. ieee829:ltr:: 1
      :title: レベルテスト報告 作成例

   概要
   ====

   対象範囲
   --------

   参考資料
   --------

   詳細
   ====

   テスト結果の概要
   ----------------

   詳細テスト結果
   --------------

   判定理由
   --------

   総合評価・推奨事項
   ------------------

   一般
   ====

   用語集
   ------

   改訂履歴
   --------
