# Web Spider 

## 环境
### Linux数据库配置
1. 数据库安装
    ```bash
    # yum -y install mariadb mariadb-server
    ```
2. 密码设置  
+ 执行`mysql_secure_installation`进行相关配置
+ 首先是设置密码，会提示先输入密码:
    ```bash
    # Enter current password for root (enter for none):<–初次运行直接回车
    # 设置密码
    # Set root password? [Y/n] <– 是否设置root用户密码，输入y并回车或直接回车
    # New password: <– 设置root用户的密码
    # Re-enter new password: <– 再输入一次你设置的密码
    ``` 

3. 配置MariaDB远程连接
    ```bash
    # mysql -uroot -p // 登录数据库
    # GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'password' WITH GRANT OPTION;  // 将password换成密码
    # flush privileges; 
    ```
    最后重启数据库




## 使用
## 感谢
