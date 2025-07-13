# SPDX-FileCopyrightText: © 2025 open-nudge <https://github.com/open-nudge>
# SPDX-FileContributor: szymonmaszke <github@maszke.co>
#
# SPDX-License-Identifier: Apache-2.0

"""`cogeol` exceptions."""

from __future__ import annotations


class CogeolError(Exception):
    """Base exception for cogeol."""


class CacheDurationNegativeError(CogeolError):
    """Raised when the provided cache duration is negative."""

    def __init__(self, cache_duration: int) -> None:
        """Initialize the exception.

        Args:
            cache_duration:
                The cache duration that was negative.

        """
        super().__init__(
            f"cache_duration must be `None` or a positive integer, got '{cache_duration}'"
        )
