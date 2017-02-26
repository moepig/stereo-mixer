# coding: UTF-8

import spidev #https://github.com/doceme/py-spidev
import RPi.GPIO as GPIO
import sys
import argparse

# バスを開く
spi = spidev.SpiDev()
spi.open(0,0)


def init():
  write({1:100, 2:100, 3:100, 4:100})

# ボリュームファイルからの読み込み
# return Dictionary channel:volume
def read():
  f = open('mixer.vol', 'r')
  lines = map(lambda x: x.split(',') ,f.readlines())
  
  volume_dict = {}
  for line in lines:
    dict[line[0]]=line[1]
  
  f.close()
  
  return volume_dict


# ボリュームファイルへの書き込み
# 書き込み形式 channel,volume\n ...
def write(volume):
  
  f = open('mixer.vol', 'w')
  
  for i in range(1, volume_dict.size()):
    f.write(i + ',' + volume[i])
  
  f.close()


# SPIで送信
def send(channel, volume):

  chip_address = channel - 1
  vol = int(95/100 * volume) << 1
  
  for i in range(0,1):
    select = i << 4
    spi.xfer([chip_address + select, vol])


# ボリュームを変える
def setvolume(channel, volume):
  send(channel,volume)
  volume_dict = read()
  volume_dict[channel] = volume
  write(volume_dict)


if __name__ == '__main__':
  parser = argparse.ArgumentParser(description=u'ボリュームをSPI通信で変える')
  parser.add_argument("mode", help = u'get: ボリュームを得る  set: ボリュームを設定')
  parser.add_argument("--channel")
  parser.add_argument("--volume")
  args = parser.parse_args()
  
  if args.mode == 'get':
    volumes = read()
    for item in volumes.items():
      print item[0] + ',' + item[1]
  
  elif args.mode == 'set':
    if args.channel and args.volume:
      setvolume(args.channel, args.volume)
    else:
      print u'引数が不足しています'