Edit server.py to use correct hardware, plug in USB speak and run:

```
aplay -L
```

Example result:
> hw:CARD=UACDemoV10,DEV=0

```
aplay air_can.wav -Dhw:UACDemoV10
```

```
pip3 install -r requirements.txt
```

```
sudo cp air-can.service /etc/systemd/system/air-can.service
sudo systemctl enable air-can.service
sudo systemctl start air-can.service
```

```
sudo apt-get install ffmpeg
```

Send an http GET request to hostname:8080/sound to activate.
