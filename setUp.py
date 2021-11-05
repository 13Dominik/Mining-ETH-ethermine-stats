#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
miner_address = os.environ.get("miner_address", "default")

if miner_address == "default":
    raise Exception("Missing Miner address!")
