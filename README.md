# iFairyServer
    iFairy的后台
    github地址：https://github.com/MandaJC/iFairyServer
    pip配置：django、pillow、django、djangorestframework、markdown、django-filter、pymysql、django-qiniu-storage
    修改restframework下renderers.py的JSONRenderer类中charset = 'utf-8'
    本地启动：python manage.py runserver 本地ip:8000
    手机要连同一路由器，安卓中HTTPPath的IP改为本地IP
    云端：已实现，项目部署在腾讯云，图片部署在七牛云，安卓中IP也预设为为云端IP，不需要进行任何修改
    有问题请联系：
    QQ：781913861
    邮箱：lyzwjaa@163.com
    联系人：曾雯嘉
----
## 文件说明
### iFairyServer：
    settings：配置文件，整个项目的根本，包括数据库配置、资源位置配置、模块依赖配置等
    urls：一级接口
    wsgi：云端用gunicorn可以后台运行服务器，24小时开启服务器的接触
---
### Article：
    admin：后台管理界面
    models：数据结构 Article、Like、Collect、Comment
    serilizers：rest框架便捷处理数据结构 ArticleSerializer、CollectSerializer、CommentSerializer
    urls：二级接口
    views：逻辑代码 处理网络请求、数据库操作
---
### Column：
    admin：后台管理界面
    models：数据结构 Column、Like、Dislike、
    serilizers：rest框架便捷处理数据结构 ColumnSerializer
    urls：二级接口
    views：逻辑代码 处理网络请求、数据库操作
---
### regNlog：
    admin：后台管理界面
    models：数据结构 Person
    serilizers：rest框架便捷处理数据结构 PersonSerializer
    urls：二级接口
    views：逻辑代码 处理网络请求、数据库操作
---
### 其他：
    框架文件，尽量不要修改
