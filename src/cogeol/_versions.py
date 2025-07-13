# SPDX-FileCopyrightText: © 2025 open-nudge <https://github.com/open-nudge>
# SPDX-FileContributor: szymonmaszke <github@maszke.co>
#
# SPDX-License-Identifier: Apache-2.0

"""Get the latest Python versions from the endoflife.date API.

This module provides a function to get the latest Python versions from the
endoflife.date API. The function caches the result for 24 hours (by default)
to avoid making too many requests to the API and to speed up the results.

This module will likely be used with `cog` to automate the generation
of supported Python versions in the project (e.g. in `pyproject.toml`
or source code).

- See https://endoflife.date/python for more information about the API.
- See https://github.com/nedbat/cog for more information about the cog tool.

See [python-template](https://github.com/nosludge/python-template/blob/main/pyproject.toml)
for an example of how to use this module with cog.

"""

from __future__ import annotations

import functools
import json
import pathlib
import tempfile
import time
import urllib.request

from . import error


@functools.cache
def versions(
    *, cache_duration: int | None = 24 * 60 * 60
) -> list[dict[str, str | bool]]:
    """Return Python versions from the endoflife.date API.

    The result is cached for 24 hours by default to avoid making too many
    requests to the API and to speed up the results returning.

    See [the API response format](https://endoflife.date/api/python.json)
    for more information about the data returned by the API.

    __Example__:

    ```python
    import cogeol

    # Get the latest Python versions
    for version in cogeol.versions(cache=0):
        print(f"Python version: {version['cycle']}")

    # Cached response returned from tmp file
    print(cogeol.versions()[0])  # Get the last version:
    ```

    Args:
        cache_duration:
            The number of seconds after which the cache should be invalidated.
            If `None`, the cache will not be invalidated, use `0` to always
            invalidate the cache.
            Default: 24 hours (24 * 60 * 60 seconds).

    Returns:
        A list of dictionaries containing metadata about Python versions.
    """
    if cache_duration is not None and cache_duration < 0:
        raise error.CacheDurationNegativeError(cache_duration)

    tempdir = pathlib.Path(tempfile.gettempdir())
    eol_cache = tempdir / "python-eol.json"
    if eol_cache.exists() and (
        cache_duration is None
        or eol_cache.stat().st_mtime < time.time() - cache_duration
    ):
        with eol_cache.open("r") as f:
            return json.load(f)

    request = urllib.request.Request(
        "https://endoflife.date/api/python.json",
        headers={"Accept": "application/json"},
    )

    with urllib.request.urlopen(request) as response:  # noqa: S310
        data = json.loads(response.read().decode("utf-8"))

    with eol_cache.open("w") as f:
        json.dump(data, f)

    return data


def scientific(
    *, cache_duration: int | None = 24 * 60 * 60
) -> list[dict[str, str | bool]]:
    """Return __the last three__ Python versions from the endoflife.date API.

    Functions the same as `versions` but returns only the latest `3` versions
    according to
    [Scientific Python SPEC0](https://scientific-python.org/specs/spec-0000/)

    __Example__:

    ```python
    import cogeol

    # Last three Python versions, starting from the latest one
    for version in cogeol.scientific():
        print(f"Python version: {version['cycle']}")
    ```

    Args:
        cache_duration:
            The number of seconds after which the cache should be invalidated.
            If `None`, the cache will not be invalidated, use `0` to always
            invalidate the cache.
            Default: 24 hours (24 * 60 * 60 seconds).

    Returns:
        A list of dictionaries containing metadata about last `3` Python
        versions.
    """
    scientific_python_versions = 3
    return versions(cache_duration=cache_duration)[:scientific_python_versions]
