# Django Blog (ch6-blog)

一個使用 Django 建立的簡易部落格專案。

## 功能

- 文章列表頁
- 文章詳細頁
- Django Admin 後台管理
- 作者與文章的一對多關係（Many-to-One）
  - 一位作者可擁有多篇文章
  - 一篇文章只屬於一位作者

## 專案結構

- `django_project/`：Django 專案設定
- `blog/`：Blog app（models、views、tests、migrations）
- `templates/`：模板（`base.html`、`home.html`、`post_detail.html`）
- `static/`：靜態資源（CSS）

## 環境需求

- Python 3.13+
- Django（已安裝於虛擬環境）

## 快速開始

1. 進入專案目錄

```powershell
cd c:\Users\user\Desktop\blog
```

2. 啟用虛擬環境

```powershell
.\.venv\Scripts\Activate.ps1
```

3. 套用資料庫遷移

```powershell
python manage.py migrate
```

4. 建立管理員帳號（可選）

```powershell
python manage.py createsuperuser
```

5. 啟動開發伺服器

```powershell
python manage.py runserver
```

6. 開啟網站

- 前台首頁：http://127.0.0.1:8000/
- 後台管理：http://127.0.0.1:8000/admin/

## 如何新增不同作者

### 方式一：Django Admin（建議）

1. 進入 `/admin/`
2. 在 `Authors` 新增多位作者
3. 在 `Posts` 新增文章並選擇對應作者

### 方式二：Django Shell

```powershell
python manage.py shell
```

```python
from blog.models import Author, Post

alice = Author.objects.create(first_name="Alice", last_name="Chen", email="alice@example.com")
bob = Author.objects.create(first_name="Bob", last_name="Lin", email="bob@example.com")

Post.objects.create(title="Alice 第一篇", body="內容...", author=alice)
Post.objects.create(title="Bob 第一篇", body="內容...", author=bob)
```

## 測試

```powershell
python manage.py test blog
```

## GitHub

此專案已可推送至 GitHub 倉庫。

如果你修改了程式碼，可用以下流程更新：

```powershell
git add .
git commit -m "your message"
git push
```
