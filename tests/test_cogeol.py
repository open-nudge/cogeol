# SPDX-FileCopyrightText: © 2025 open-nudge <https://github.com/open-nudge>
# SPDX-FileContributor: szymonmaszke <github@maszke.co>
#
# SPDX-License-Identifier: Apache-2.0

"""Test the functions of the cogeol module."""

from __future__ import annotations

import pytest

import cogeol


@pytest.mark.parametrize("cache_duration", (3600, 0, None))
def test_version(cache_duration: None | int) -> None:
    """Test the version function of the cogeol module.

    Args:
        cache_duration:
            The number of seconds after which the cache should be invalidated.

    """
    versions = cogeol.versions(cache_duration=cache_duration)
    assert versions[0]["cycle"] > versions[1]["cycle"]  # pyright: ignore[reportOperatorIssue]


def test_incorrect_cache_duration() -> None:
    """Test the `version` function with an incorrect value."""
    with pytest.raises(cogeol.error.CacheDurationNegativeError):
        _ = cogeol.versions(cache_duration=-1)


@pytest.mark.parametrize("cache_duration", (3600, 0, None))
def test_scientific(cache_duration: None | int) -> None:
    """Test the scientific versioning (Scientific Python SPEC0).

    Read more here: https://scientific-python.org/specs/spec-0000/

    Args:
        cache_duration:
            The number of seconds after which the cache should be invalidated.

    """
    scientific_python_versions = 3
    length = len(cogeol.scientific(cache_duration=cache_duration))
    assert length == scientific_python_versions
