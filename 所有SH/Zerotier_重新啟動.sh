#!/bin/bash
sudo systemctl stop zerotier-one.service
sudo systemctl start zerotier-one.service
echo "按Q退出狀態檢視"
sudo systemctl status zerotier-one.service
