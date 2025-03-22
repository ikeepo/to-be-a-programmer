# TA-Lib
[This](https://github.com/TA-Lib/ta-lib-python/issues/566) module now requires the TA-Lib C library to be installed.
1. [Install](https://ta-lib.org/install/#linux-build-from-source) [ta-lib](https://github.com/TA-Lib/ta-lib)
2. Intall [ta-lib-python]
# Error
### /usr/bin/ld: cannot find -lta-lib
The installed C version talib is called libra_lib.so, so make a soft link `sudo ln -s /usr/lib/libta_lib.so /usr/lib/libta-lib.so`.
这是因为用了旧版本C ta-lib和新版本Python ta-lib导致；
### ImportError: libta_lib.so.0: cannot open shared object file: No such file or directory
安装配置问题；
```
make clean
./configure --prefix=/usr --enable-shared
make
sudo make install
```
上述方法无效：
```
sudo nvim /etc/ld.so.conf
# add
include /usr/local/lib
sudo ldconfig
```
