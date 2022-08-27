# -*- coding: utf-8 -*-
from client.client import Client
from data.containers import Identification


def main():
    c = Client(None)
    c.knock(Identification())


if __name__ == "__main__":
    main()
