
1，windows下注意apache、mod_wsgi的vc编译版本一致


2，请用 pip install 安装whl文件


3，版本一致的apache以及whl文件在当前目录下，如有需要请自行安装（二者均为VC9编译，apache版本24以及python版本27，二者均为32位）


4，httpd.conf文件添加以下代码：

        ----------------以下为配置文件----------------------------------------------------
        LoadModule wsgi_module "d:/python27/lib/site-packages/mod_wsgi/server/mod_wsgi.pyd" (路径为你的python路径)
        WSGIPythonHome "d:/python27"                                                        (路径为你的python路径)


        <VirtualHost *:80>
            DocumentRoot C:\Users\sunzhiming\Desktop\blueprint                               （你的app的根目录）
            WSGIScriptAlias /  C:\Users\sunzhiming\Desktop\blueprint\app.wsgi                 （wsgi文件路径）
            <Directory 'C:\Users\sunzhiming\Desktop\blueprint'>                               （你的app的根目录）
                AllowOverride AuthConfig FileInfo
                Require all granted
                Order allow,deny
                Allow from all
            </Directory>
        </VirtualHost>

        -----------------------------------------------------------------------------------


5，wsgi配置见文件app.wsgi


6，如果用apache启动网站服务，读写本地文件必须使用绝对路径


7，启动apache服务，直接 cmd httpd.exe







