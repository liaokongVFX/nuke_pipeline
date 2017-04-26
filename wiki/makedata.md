##项目数据产生及使用流程图

![](pipeline.png)

####详细说明：
* 共有3个数据库：**progressData(项目进度数据库)、readData(daliy数据库)、userIpData(数据库)**。
* 当制作人员启动TrayReminder时，会自动发送该人员对应的<font color=red>user_name(制作人员)、ip</font>到**userIpData**数据库中。
* 分配镜头插件会将<font color=red>project(项目)、shot_name(镜头名)、grade(镜头难度等级)、artist(分配到的制作人员)、frame_len(镜头帧数)、date(日期)</font>写入**progressData**数据库中。
* 在制作人员完成镜头，使用渲染输出模板渲染完镜头后会自动将<font color=red>file_name(输出的镜头文件名)、shot_name(镜头名)、day(日)</font>分别写入**progressData**和**readData**数据库中。
* 当每天总监检查完镜头后，会把<font color=red>project、user_name(制作人员)、frame_len、pass_value(是否通过)、feed_back(反馈)、year(年)、month(月)、day(日)、date(日期)</font>分别写入**progressData**和**readData**数据库中。
* daliyPanel会从**readData**数据库中获取数据，将<font color=red>project、shot_name、file_name、user_name、frame_len、pass_value、feed_back、date</font>数据展示出来。
* ProgressPanel会从**progressData**数据库中获取数据，将<font color=red>project、shot_name、frame_len、grade、artist、user_name、pass_value、client_feed_back、date</font>数据展示出来。
* 当修改EditPanel(ProgressPanel的编辑面板)数据时，数据会实时存回**progressData**数据库，并且在artist(分配到的制作人员)被修改时会自动发送气泡提示给该对应的制作人员。

####后期数据利用
积累的数据可以再去做好多事，比如生成每个月整个公司的项目情况数据报表、生成员工画像。
比如通过生成的统计图表可以很清楚的反应每个员工工作效率，如果公司有员工等级标准，可以非常客观的根据用户画像对每个员工进行等级划分。如果是绩效公司，可以根据对应的绩效公式每月自动生成该月的员工工资等等。
数据库如果放在云端还可以实现多地协同工作，每个地方的人都可以实时看到整个项目的进度和每个镜头的反馈。
