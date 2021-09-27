#!/usr/bin/env python

from html import unescape
import logging
import re

import click
import latex2mathml.converter


def convert_inline(m):
    """Convert a block of LaTeX to MathML (inline mode)"""
    contents = m.group(1)
    s = latex2mathml.converter.convert(contents)
    return s

def convert_block(m):
    """Convert a block of LaTeX to MathML (display mode)"""
    contents= m.group(1)
    s = latex2mathml.converter.convert(contents,display="block")
    return s

def fixstb(s):
    """Fix HTML issues created by the Sakai to Brightspace conversion.
    
    Namely, text between dollar signs ($...$) is converted to MathML in inline mode
    (not block mode, which is Brightspace's default)    
    """
    s = unescape(s)
    s = re.sub('\$\$(.*?)\$\$',convert_block,s)
    s = re.sub('\$(.*?)\$',convert_inline,s)
    s = unescape(s)
    s = s.replace('<mi>ℤ</mi>','<mi mathvariant="double-struck">Z</mi>')
    return s


# cli helper
def set_log_level(ctx, param, value):
    """Set the logging level"""
    levels = {
        'verbose': logging.INFO,
        'debug' : logging.DEBUG
    }
    if value:
        logging.basicConfig(level=levels[param.name])


@click.command(
    help="""Fix HTML issues created by the Sakai to Brightspace conversion.
    
    INPUT can be a file, or - or empty for stdin.
    """
)
@click.argument('input',type=click.File('rb'),default="-")
@click.option('--debug',
    help="Print lots of debugging statements",
    is_flag=True,
    expose_value=False,
    callback=set_log_level)
@click.option('--verbose',
    help="Be verbose",
    is_flag=True,
    expose_value=False,
    callback=set_log_level)
def cli(input):
    logging.info("Hello, world!")
    text = input.read().decode()
    logging.debug(f"{text=}")
    print(fixstb(text))


if __name__ == '__main__':
    cli()