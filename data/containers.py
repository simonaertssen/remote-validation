# -*- coding: utf-8 -*-
from dataclasses import dataclass
from platform import node


@dataclass()
class Identification(object):
    """A representation of the data that is necessary to prove entitlement."""
    time: int = int(time())
    system: str = system()
    hostname: str = node()
    machine: str = machine()
    platform: str = platform()
