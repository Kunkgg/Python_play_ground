from __future__ import annotations

from typing import List

import attr


@attr.frozen
class Configuration:
    @attr.frozen
    class Files:
        input_dir: str
        output_dir: str

    files: Files

    @attr.frozen
    class Parameters:
        patterns: List[str]

    parameters: Parameters


def configuration_from_dict(details):
    files = Configuration.Files(
        input_dir=details["files"]["input-dir"],
        output_dir=details["files"]["output-dir"],
    )
    parameters = Configuration.Paraneters(
        patterns=details["parameters"]["patterns"])
    return Configuration(
        files=files,
        parameters=parameters,
    )


json_config = """
{
    "files": {
        "input-dir": "inputs",
        "output-dir": "outputs"
    },
    "parameters": {
        "patterns": [
            "*.txt",
            "*.md"
        ]
    }
}
"""

ini_config = """
[files]
input-dir = inputs
output-dir = outputs

[parameters]
patterns = ['*.txt', '*.md']
"""

yaml_config = """
files:
  input-dir: inputs
  output-dir: outputs
parameters:
  patterns:
  - '*.txt'
  - '*.md'
"""

toml_config = """
[files]
input-dir = "inputs"
output-dir = "outputs"

[parameters]
patterns = [ "*.txt", "*.md",]
"""
