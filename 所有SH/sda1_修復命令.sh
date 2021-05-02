#!/bin/bash
sudo umount /dev/sda1 
sudo ntfsfix /dev/sda1 
sudo mount /dev/sda1

