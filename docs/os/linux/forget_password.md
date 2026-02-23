# Password Recovery

## 本地服务器忘记密码

```shell
# 修改BIOS强制进入GRUB
Esc --> Boot --> Boot Logo Display --> Disabled --> F10 

# 重启
开机第一时间一直按住shift --> Advanced options for Ubuntu  --> (recovery mode)  --> root - Drop to root shell prompt --> mount -o remount,rw / --> ls /home --> passwd user_name --> reboot
```
