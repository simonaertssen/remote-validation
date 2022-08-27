# -*- coding: utf-8 -*-
import platform
import time


class Client(object):
    """A representation of a program requesting remote validation."""
    data: dict = {}

    def __init__(self) -> None:
        """Store variables of the client machine."""
        self.data['system'] = platform.system()
        self.data['hostname'] = platform.node()
        self.data['machine'] = platform.machine()
        self.data['platform'] = platform.platform()

    def query(self) -> None:
        """Send the data."""
        self.data['unixtime'] = int(time.time())

        print(self.data)
