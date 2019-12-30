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

4. cron

```
# crontab -e
0 2 * * * cd /opt/wp-pixela && python3 google_analytics_access.py
```

5. htmlに貼り付け

```
<iframe src="https://pixe.la/v1/users/<ユーザー名>/graphs/<グラフID>?mode=short"></iframe>
```

---

詳細については下記blogを参照

[Pixelaという草APIサービスを利用して、WordPressのPV数をGitHub風に草生やしてサイドバーに表示させたい(丁寧に)](https://wp.suwa3.me/2019/12/28/pixela%e3%81%a8%e3%81%84%e3%81%86%e8%8d%89api%e3%82%b5%e3%83%bc%e3%83%93%e3%82%b9%e3%82%92%e5%88%a9%e7%94%a8%e3%81%97%e3%81%a6%e3%80%81wordpress%e3%81%aepv%e6%95%b0%e3%82%92github%e9%a2%a8%e3%81%ab-2/)

ツールチップを表示させたい場合はこちらを参照

[Pixelaでツールチップを表示させてみる](https://wp.suwa3.me/2019/12/29/pixela%e3%81%a7%e3%83%84%e3%83%bc%e3%83%ab%e3%83%81%e3%83%83%e3%83%97%e3%82%92%e8%a1%a8%e7%a4%ba%e3%81%95%e3%81%9b%e3%81%a6%e3%81%bf%e3%82%8b/)

