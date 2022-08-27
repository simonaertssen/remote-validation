# -*- coding: utf-8 -*-
from requests import Response, get

from data.containers import Identification


class Client(object):
    """A representation of a program requesting remote validation."""

    def __init__(self, url: str = "www.localhost:5000") -> None:
        """Store variables of the client machine."""
        self.url: str = url

    def knock(self, id: Identification) -> Response:
        """Send identification to a url."""
        return get(url=self.url, data=id(), verify=False)

    # def persist(self, id: Identification) -> None:
