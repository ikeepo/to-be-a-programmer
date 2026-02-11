# Linux
# `Could not create MokListRT: Volume Full`
```
Could not create MokListRT: Volume Full
Could not create MokListXRT: Volume Full
Could not create SbatLevelRT: Volume Full
Could not create MokListTrustedRT: Volume Full
Something has gone seriously wrong: import_mok_state() failed: Volume Full
```
- `UEFI MOK `

Unified Extensible Firmware Interface,BIOS 的继任者，硬件初始化；
UEFI固件读取主板里的启动项Boot Entries，找到对应的EFI文件（比如grubx64.efi），如果Secure Boot开启，就检查这个EFI文件是否有受信任的签名。通过GRUB启动Linux内核vmlinuuz，然后挂在initrd，进入系统。
对与ROG主板，进入F2，找到EZ Mode/Advanced Mode,设置Boot Mode(UEFI),SecureBoot(disabled),FastBoot(disabled),SATA mode(AHCI).

虽然设置了Secure Boot是disabled，但是还是一样的问题，这是因为如果有残留的Key，ROG的系统会认为是启动了Secure，所以要先在Key Management / Clear Secure Boot Keys，然后再启动。
# 挂载剩余空间
```
sudo vgdisplay ubuntu-vg
sudo lvcreate -L 400G -n data ubuntu-vg
sudo mkfs.ext4 /dev/ubuntu-vg/data
sudo mkdir /mnt/data
sudo mount /dev/ubuntu-vg/data /mnt/data
# sudo nano /etc/fstab 
/dev/ubuntu-vg/data  /mnt/data  ext4  defaults  0 2

df -h /mnt/data

```
