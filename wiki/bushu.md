## 部署

1. 安装MongoDB

2. 根据自身情况修改plugin->configure->configure.py中的配置

(artists_ip有两种获取方式，默认开启的是手动书写人员以及对应的ip，第二种方式人员和对应的ip是通过TrayReminder获取的，缺点是在ProgressPanel面板的分配人员显示的是对应人员电脑的用户名)

3. 拷贝plugin中的文件到nuke插件目录下

4. 根据自身情况修改start_mongodb.bat,并运行

5. 安装TrayReminder所需的第三方库：PyQt4、Win32

6. 设置TrayReminder->config.py中的nuke插件根目录

7. 运行TrayReminder文件夹下的App_MainWindow.py文件(可以自行打包该独立程序。)