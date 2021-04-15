<img width="318" alt="スクリーンショット 2019-12-29 18 38 53" src="https://user-images.githubusercontent.com/56011102/71576357-bea48180-2b33-11ea-8105-b3872e445de2.png">

# これは何か

草APIサービスである Pixela を Google Analytics API と連携させて

blog の PV数を GitHub 草風に表示させました。

# 実行

```
python3 google_analytics_access.py
```

# セットアップ

1. PixelaでユーザーとIDを作成
https://pixe.la/

2. 対象blogにGoogleAnalyticsを導入
https://analytics.google.com/analytics/web/provision/#/provision

3. GoogleAnalytics APIを利用してjsonファイルをDL
https://developers.google.com/analytics/devguides/reporting/core/v4/quickstart/service-py?hl=ja

4. 以下の依存パッケージをインストールしておきます。

- google-api-python-client
- oauth2client
- requests
- python-dotenv

```
pip3 install google-api-python-client oauth2client requests python-dotenv
```

5. cron

```
# crontab -e
0 2 * * * cd /opt/wp-pixela && python3 google_analytics_access.py
```

6. htmlに貼り付け

```
<iframe src="https://pixe.la/v1/users/<ユーザー名>/graphs/<グラフID>?mode=short"></iframe>
```

---

詳細については下記blogを参照

[Pixelaという草APIサービスを利用して、WordPressのPV数をGitHub風に草生やしてサイドバーに表示させたい(丁寧に)](https://suwa3.netlify.app/post/2019-12-28-pixela%E3%81%A8%E3%81%84%E3%81%86%E8%8D%89api%E3%82%B5%E3%83%BC%E3%83%93%E3%82%B9%E3%82%92%E5%88%A9%E7%94%A8%E3%81%97%E3%81%A6wordpress%E3%81%AEpv%E6%95%B0%E3%82%92github%E9%A2%A8%E3%81%AB-2/)

ツールチップを表示させたい場合はこちらを参照

[Pixelaでツールチップを表示させてみる](https://wp.suwa3.me/2019/12/29/pixela%e3%81%a7%e3%83%84%e3%83%bc%e3%83%ab%e3%83%81%e3%83%83%e3%83%97%e3%82%92%e8%a1%a8%e7%a4%ba%e3%81%95%e3%81%9b%e3%81%a6%e3%81%bf%e3%82%8b/)

