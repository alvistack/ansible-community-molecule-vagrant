# !/usr/bin/env python
import site
import sys

import setuptools

# See https://github.com/pypa/pip/issues/7953
site.ENABLE_USER_SITE = "--user" in sys.argv[1:]


if __name__ == "__main__":
    setuptools.setup(
        name="molecule_vagrant",
        version="0.6.3",
        include_package_data=True,
        packages=["molecule_vagrant"],
        install_requires=[
            "molecule>=3.2.0a0",
            "pyyaml>=5.1,<6",
            "selinux",
        ],
    )
