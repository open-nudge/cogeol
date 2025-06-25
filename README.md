<!--
SPDX-FileCopyrightText: © 2025 open-nudge <https://github.com/open-nudge>
SPDX-FileContributor: szymonmaszke <github@maszke.co>

SPDX-License-Identifier: Apache-2.0
-->

# cogeol

<!-- mkdocs remove start -->

<!-- vale off -->

<!-- pyml disable-num-lines 30 line-length-->

<p align="center">
    <em>Align with supported Python versions - automated with endoflife.date</em>
</p>

<div align="center">

<a href="https://pypi.org/project/cogeol">![PyPI - Python Version](https://img.shields.io/pypi/v/cogeol?style=for-the-badge&label=release&labelColor=grey&color=blue)
</a>
<a href="https://pypi.org/project/cogeol">![Python Version from PEP 621 TOML](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Fopen-nudge%2Fcogeol%2Fmain%2Fpyproject.toml&style=for-the-badge&label=python&labelColor=grey&color=blue)
</a>
<a href="https://opensource.org/licenses/Apache-2.0">![License](https://img.shields.io/badge/License-Apache_2.0-blue?style=for-the-badge)
</a>
<a>![Coverage Hardcoded](https://img.shields.io/badge/coverage-100%25-green?style=for-the-badge)
</a>
<a href="https://scorecard.dev/viewer/?uri=github.com/open-nudge/cogeol">![OSSF-Scorecard Score](https://img.shields.io/ossf-scorecard/github.com/open-nudge/cogeol?style=for-the-badge&label=OSSF)
</a>

</div>

<p align="center">
✨ <a href="#features">Features</a>
🚀 <a href="#quick-start">Quick start</a>
📚 <a href="https://open-nudge.github.io/cogeol">Documentation</a>
🤝 <a href="#contribute">Contribute</a>
👍 <a href="https://github.com/open-nudge/cogeol/blob/main/ADOPTERS.md">Adopters</a>
📜 <a href="#legal">Legal</a>
</p>
<!-- vale on -->

______________________________________________________________________

<!-- mkdocs remove end -->

## Features

__cogeol__ is a library which allows you to:

- __Works with any file format__ (e.g. updating Python versions in CI/CD tests)
- __No need to track Python EOL dates__ — cogeol does it for you
- __Align with [Scientific Python SPEC0](https://scientific-python.org/specs/spec-0000/)__:
    `cogeol` will allow you to align your project to the three latest
    supported Python versions
- __Caching__: retrieves data from https://endoflife.date/
    and stores it locally to minimize network requests
- __Based on [cog](https://github.com/nedbat/cog)__: Manage versions of Python
    by statically generated code (see examples below!)

## Quick start

### Installation

```sh
> pip install cogeol
```

### Usage

> [!TIP]
> Check out the [documentation](https://open-nudge.github.io/cogeol)
> for all available functionalities and public-facing API.

1. Open `pyproject.toml` of your project
    and find __necessary to have `requires-python` field__.
1. Update it as follows (__comments are crucial!__):

```toml
# [[[cog
# import cog
# import cogeol
#
# cycle = cogeol.scientific()[-1]["cycle"]
# cog.out(f'requires-python = ">={cycle}"')
# ]]]
requires-python = ">=3.9"
# [[[end]]]
```

Now run the following from the command line:

```sh
> cog -c -r pyproject.toml
```

__Now your `requires-python` field will be updated to the
latest supported Python version!__

For example (Python `3.11` is the latest supported version
at the time of writing):

```toml
# [[[cog
# import cog
# import cogeol
#
# cycle = cogeol.scientific()[-1]["cycle"]
# cog.out(f'requires-python = ">={cycle}"')
# ]]]
requires-python = ">=3.11"
# [[[end]]] (sum: uZEo+p96oZ)
```

> [!NOTE]
> Please notice a checksum, which verifies consistency
> of the changes at each run

### Examples

<details>
  <summary><b><big>Specifying Python version classifiers</big></b> (click me)</summary>
&nbsp;

You can automate the classifiers in your `pyproject.toml` file like this:

```toml
# [[[cog
# import cog
# import cogeol
#
# for version in reversed(cogeol.scientific()):
#     cycle = version["cycle"]
#     cog.outl(f'  "Programming Language :: Python :: {cycle}",')
# ]]]
"Programming Language :: Python :: 3.11",
# [[[end]]]
```

Now run the following from the command line:

```sh
> cog -c -r pyproject.toml
```

and you should see the following (__notice all versions are present!__):

```toml
# [[[cog
# import cog
# import cogeol
#
# for version in reversed(cogeol.scientific()):
#     cycle = version["cycle"]
#     cog.outl(f'  "Programming Language :: Python :: {cycle}",')
# ]]]
"Programming Language :: Python :: 3.11",
"Programming Language :: Python :: 3.12",
"Programming Language :: Python :: 3.13",
# [[[end]]] (sum: FeG7grp2Dw)
```

</details>

<details>
  <summary><b><big>Caching</big></b> (click me)</summary>
&nbsp;

Let's assume you have the following code snippet in `github-workflow.yml`:

```yaml
...
jobs:
  tests-reusable:
    strategy:
      matrix:
        python:
          #
          #           DO NOT EDIT UNTIL end marker
          #
          # [[[cog
          # import cog
          # import cogeol
          #
          # for version in reversed(cogeol.scientific()):
          #     cycle = version['cycle']
          #     cog.outl(f'          - "{cycle}"')
          # ]]]
          - "3.11"
          # [[[end]]] (sum: l3d2zGv79j)
```

in addition to your code in `pyproject.toml` using `cogeol`.

Now, if you run:

```sh
> cog -c -r pyproject.toml github-workflow.yml
```

The following will happen:

- Both files will be updated with appropriate Python versions
- __Only one call to [End of Life Date](https://endoflife.date) will be made__
    (the results are cached on disk)

Next time you run the same command, the results will be read from the cache

</details>

<details>
  <summary><b><big>Advanced</big></b> (click me)</summary>
&nbsp;

For more examples check out this project's:

- `pyproject.toml` file
    (see [here](https://github.com/open-nudge/cogeol/blob/main/pyproject.toml))
- Tests of the last three versions in GitHub Actions workflow
    (see [here](https://github.com/open-nudge/cogeol/blob/main/.github/workflows/tests-reusable.yml))

</details>

<!-- md-dead-link-check: off -->

<!-- mkdocs remove start -->

## Contribute

We welcome your contributions! Start here:

- [Code of Conduct](/CODE_OF_CONDUCT.md)
- [Contributing Guide](/CONTRIBUTING.md)
- [Roadmap](/ROADMAP.md)
- [Changelog](/CHANGELOG.md)
- [Report security vulnerabilities](/SECURITY.md)
- [Open an Issue](https://github.com/open-nudge/cogeol/issues)

## Legal

- This project is licensed under the _Apache 2.0 License_ - see
    the [LICENSE](/LICENSE.md) file for details.
- This project is copyrighted by _open-nudge_ - the
    appropriate copyright notice is included in each file.

<!-- mkdocs remove end -->

<!-- md-dead-link-check: on -->
