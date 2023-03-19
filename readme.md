[flask參考資料](https://www.maxlist.xyz/2020/05/01/flask-list/)
docker build -t {mage_name} {current_folder}
docker image build -t dockerfile_flask .


指令參數講解：
-d 背景執行
-p 將主機 80 port 與 container的 8888 port 綁定
–name 為 container 命名
docker run -d -p 80:8888 --name flask dockerfile_flask

[github action參考資料](https://www.ruanyifeng.com/blog/2019/09/getting-started-with-github-actions.html)