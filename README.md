Melon
-----

Melon – **M**ultimedia- & **E**ntertainment **L**inking and **O**peration **N**ode – is a daemon that allows linking media devices (e.g. Sonos, Televisions) and operating them through one API

## Requirements

- WiFi
- A Raspberry Pi Zero W / A / A+ / B / B + with an LIRCd-compatible IrDA transmitter
- Raspbian on its microSD card
- A GitHub account

## Installation

On your Raspberry:

```bash
$ aptitude install python3 python3-pip python3-dev python3-spidev
$ pip3 install gunicorn falcon ujson
$ # For controlling Samsung TVs:
$ pip3 install samsungctl
$ # For controlling Sonos speakers:
$ pip3 install soco
$ # For controlling Philips Hue:
$ pip3 install phue
$ cd /opt
$ git clone https://github.com/mrusme/melon.git
$ ln -s /opt/melon/init.d/melon /etc/init.d/melon
$ update-rc.d melon defaults
```

Melon will now be run automatically every time your Raspberry starts.

## Running manually

```bash
$ cd melon/
$ ./melon.sh
```

## Configuration

### Port (on boot)

You can change the port by creating a file named `/etc/melon` and adding the following content to it:

```bash
export PORT=1337
```

The init.d-script will look for the file and in case it was found source it.

### Port (manually)

```bash
PORT=1337 ./melon.sh
```

## API

TODO

## "Let me tell you..."

Sure, [tell me](https://twitter.com/intent/tweet?text=@mrusme%20regarding%20Melon,%20let%20me%20tell%20you%20that...)!
