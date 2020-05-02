# -*- coding: utf-8 -*-
import click
from bse import config
from typing import Dict
from ._root import cmd_root


@cmd_root.command(name='config')
@click.pass_obj
def cmd_config(obj: Dict[str, str]) -> int:
    """Get configuration options"""
    conf = config.new(obj)
    click.echo(conf.json())
    return 0
