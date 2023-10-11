1、安装新库: python3 -m pip install numpy==1.24.3 (可以不指定安装的版本号，即会默认安装最新的版本）


2、查看是否有库可以进行更新: pip list --outdated


3、升级单个库，或批量升级库
升级单个库：python3 -m pip install --upgrade library_name==版本号 (可以不指定安装的版本号，即会默认安装最新的版本）
批量升级：需要先安装pip-review。 
#python3 -m pip-review：检查哪些库需要更新
#python3 -m pip-review --auto：自动更新所有库
#python3 -m pip-review --interactive：手动更新库
                                                        
全部升级：python3 -m pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U （谨慎使用）
升级pip本身：python3 -m pip install --upgrade pip (pip是python包管理器的缩写，用于管理模块，库，软件包等等工具）

                                              
4、卸载库：python3 -m pip uninstall numpy

                                              
5、查看库
查看单个库的信息：python3 -m pip show matplotlib
查看已安装的所有库的版本：python3 -m pip list
查看可更新的库：python3 -m pip list --outdated

                                              
                                              

