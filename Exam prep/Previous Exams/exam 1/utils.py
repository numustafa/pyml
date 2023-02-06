#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json
from pathlib import Path


def load_diamonds(filepath: str='./data/diamonds.json'):
    data = json.loads(Path(filepath).read_text())
    for i,d in enumerate(data['data']):
        data['data'][i] = tuple(d)
        
    return data
    