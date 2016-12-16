import os
import yaml

import jinja2
from jinja2 import Template

latex_jinja_env = jinja2.Environment(
	block_start_string = '\BLOCK{',
	block_end_string = '}',
	variable_start_string = '\VAR{',
	variable_end_string = '}',
	comment_start_string = '\#{',
	comment_end_string = '}',
	line_statement_prefix = '%%',
	line_comment_prefix = '%',
	trim_blocks = True,
	autoescape = False,
	loader = jinja2.FileSystemLoader(os.path.abspath('.'))
)

def load_config():
    config = {}

    with open('menu.yaml', 'r') as f:
        for doc in yaml.load_all(f):
            for k, v in doc.items():
                config[k] = v

    return config

def compile_template(context):
    template = latex_jinja_env.get_template('menu.jinja.tex')
    return template.render(context)

config = load_config()
template = compile_template(config)

with open('menu.tex', 'w') as f:
    f.write(template)
