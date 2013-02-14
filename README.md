# nose-xvfb

This plugin provides a virtual X display to run tests through xvfb X server.
It might be useful when running interface tests, avoiding visible pop-up windows and providing a sensible speedup.

To use it, install the package and run `nosetests` along with the flag `--with-xvfb`

## Dependences

- nose
- xvfbwrapper

It requires the _xvfb_ executable already installed within the system. It can be usually found in the `xorg-server-xvfb` package.

## Usage

	nosetests --with-xvfb
