=======================
Shaw, Heiu-Jou (邵揮洲)
=======================

.. image:: https://travis-ci.org/nmshaw000/nmshaw.png?branch=master
   :target: https://travis-ci.org/nmshaw000/nmshaw

Shaw, Heiu-Jou (邵揮洲) Professor Personal Website


=======================
如何在Windows系統上開發
=======================


第一次安裝
----------

1. 安裝 Cygwin_ （ `64位元安裝檔 <https://www.cygwin.com/setup-x86_64.exe>`_ ）

   安裝時，請將 **Python** 以及 **Devel** 選成 *Install* （不要選 *Default* ）

2. 安裝須花頗多時間，完成後，在桌面建立一個 Cygwin Terminal 的捷徑。

3. 點擊捷徑進入 Cygwin Terminal，進入後先檢查 Python_ 以及 git_ 是否安裝成功。

   先檢查 Python_ ：

   .. code-block:: bash

     $ python -V

   如果成功會看到 Python_ 的版本號碼。

   接著檢查 git_ ：

   .. code-block:: bash

     $ git --version

   如果成功會看到 git_ 的版本號碼。
   接著設定user名稱跟email：

   .. code-block:: bash

     $ git config --global user.name "nmshaw000"
     $ git config --global user.email "nmshaw@mail.ncku.edu.tw"

   或

   .. code-block:: bash

     $ git config --global user.name "NFChen"
     $ git config --global user.email "an94.design@gmail.com"

   請依照自己的帳號及email做設定。

4. 安裝 pip_ [2]_ ：

   .. code-block:: bash

     $ easy_install-2.7 pip

   移除有問題的套件：

   .. code-block:: bash

     $ pip uninstall stgit
     $ pip uninstall bzr-fastimport

5. 進入D槽，建立github資料夾：

   .. code-block:: bash

     $ cd /cygdrive/d/
     $ mkdir github

6. 進入剛剛建立的github資料夾，把網站原始碼從GitHub上clone下來：

   .. code-block:: bash

     $ cd /cygdrive/d/github/
     $ git clone https://github.com/nmshaw000/nmshaw.git

7. 進入原始碼目錄，用 pip_ 安裝需要的 Python 套件：

   .. code-block:: bash

     $ cd /cygdrive/d/github/nmshaw
     $ pip install -r requirements.txt

8. 安裝 pelican plugin：

   .. code-block:: bash

     $ cd /cygdrive/d/github/nmshaw
     $ make download

9. 產生 JavaScript 及 CSS 檔

   .. code-block:: bash

     $ cd /cygdrive/d/github/nmshaw
     $ make js
     $ make scss

10. 產生整個網站：

    .. code-block:: bash

      $ cd /cygdrive/d/github/nmshaw
      $ make

    用瀏覽器打開 `http://localhost:8000/ <http://localhost:8000/>`_
    可看產生的網站。


日常開發
--------

進入原始碼目錄修改或新增檔案，完成後

.. code-block:: bash

  $ cd /cygdrive/d/github/nmshaw
  $ make
  # 此時打開瀏覽器(chrome, firefox, ...)，拜訪網址：
  # http://localhost:8000/
  # 確認是否正確。

  # 觀看還未加入的修改
  $ git status
  # 加入修改
  $ git add {{檔案名稱}}
  # 確認修改
  $ git commit -m "此處填寫做了何種修改"
  # 整合別人的修改
  $ git pull
  # 上傳修改到GitHub
  $ git push
  # 接著git會問帳號密碼，請輸入你的帳號密碼


參考
----

.. [1] `7. 附录：轻量级标记语言 — GotGitHub <http://www.worldhello.net/gotgithub/appendix/markups.html>`_
       (`GitHub <https://github.com/gotgit/gotgithub/blob/master/appendix/markups.rst>`__)
       |`Quick reStructuredText <http://docutils.sourceforge.net/docs/user/rst/quickref.html>`_

.. [2] `python - Installing Pip-3.2 on Cygwin - Stack Overflow <http://stackoverflow.com/a/30685412>`_

.. [3] | `邵揮洲 - Google search <https://www.google.com/search?q=%E9%82%B5%E6%8F%AE%E6%B4%B2>`_
       | `邵揮洲 - DuckDuckGo search <https://duckduckgo.com/?q=%E9%82%B5%E6%8F%AE%E6%B4%B2>`_
       | `邵揮洲 - Ecosia search <https://www.ecosia.org/search?q=%E9%82%B5%E6%8F%AE%E6%B4%B2>`_
       | `邵揮洲 - Qwant search <https://www.qwant.com/?q=%E9%82%B5%E6%8F%AE%E6%B4%B2>`_
       | `邵揮洲 - Bing search <https://www.bing.com/search?q=%E9%82%B5%E6%8F%AE%E6%B4%B2>`_
       | `邵揮洲 - Yahoo search <https://search.yahoo.com/search?p=%E9%82%B5%E6%8F%AE%E6%B4%B2>`_
       | `邵揮洲 - Baidu search <https://www.baidu.com/s?wd=%E9%82%B5%E6%8F%AE%E6%B4%B2>`_
       | `邵揮洲 - Yandex search <https://www.yandex.com/search/?text=%E9%82%B5%E6%8F%AE%E6%B4%B2>`_
       | `Heiu-Jou Shaw - Google search <https://www.google.com/search?q=Heiu-Jou+Shaw>`_
       | `Heiu-Jou Shaw - DuckDuckGo search <https://duckduckgo.com/?q=Heiu-Jou+Shaw>`_
       | `Heiu-Jou Shaw - Ecosia search <https://www.ecosia.org/search?q=Heiu-Jou+Shaw>`_
       | `Heiu-Jou Shaw - Qwant search <https://www.qwant.com/?q=Heiu-Jou+Shaw>`_
       | `Heiu-Jou Shaw - Bing search <https://www.bing.com/search?q=Heiu-Jou+Shaw>`_
       | `Heiu-Jou Shaw - Yahoo search <https://search.yahoo.com/search?p=Heiu-Jou+Shaw>`_
       | `Heiu-Jou Shaw - Baidu search <https://www.baidu.com/s?wd=Heiu-Jou+Shaw>`_
       | `Heiu-Jou Shaw - Yandex search <https://www.yandex.com/search/?text=Heiu-Jou+Shaw>`_

.. [4] `Bulma: a modern CSS framework based on Flexbox <http://bulma.io/>`_

.. _Cygwin: https://www.cygwin.com/
.. _Python: https://www.python.org/
.. _git: https://git-scm.com/
.. _pip: https://pypi.python.org/pypi/pip
