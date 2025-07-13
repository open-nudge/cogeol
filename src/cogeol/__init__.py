# SPDX-FileCopyrightText: © 2025 open-nudge <https://github.com/open-nudge>
# SPDX-FileContributor: szymonmaszke <github@maszke.co>
#
# SPDX-License-Identifier: Apache-2.0

"""`cogeol` lets you to obtain the supported Python versions.

This module provides functionalities to get the latest supported Python
versions from the endoflife.date API. The function caches the result
for `24` hours (by default) to avoid making multiple requests to the
API and to improve performance.

This module will likely be used with `cog` to automate the generation
of supported Python versions in the project (e.g. in `pyproject.toml`
or source code).

- See [endoflife/python](https://endoflife.date/python) for
    more information about the API.
- See [cog repo](https://github.com/nedbat/cog) for
    more information about the cog tool.

See [`pyproject.toml`](https://github.com/open-nudge/cogeol/blob/main/pyproject.toml)
of this project for examples of how to use this module with cog.

"""

from __future__ import annotations

from importlib.metadata import version

from . import error
from ._versions import scientific, versions

__version__ = version("cogeol")
"""Current cogeol version."""

del version

__all__: list[str] = [
    "__version__",
    "error",
    "scientific",
    "versions",
]
