#!/usr/bin/env python

"""
Copyright (c) Build Your Own Arch Linux Repository developers
See the file 'LICENSE' for copying permission
"""

import os

from utils.process import git_remote_path


# Bot version (<major>.<minor>.<month>.<monthly commit>)
# To get the monthly commit, you need to execute
# git rev-list --count HEAD --since="last month"
VERSION = "1.0.7.95"

# Upstream repository
UPSTREAM_REPOSITORY = "https://github.com/unix-development/build-your-own-archlinux-repository"

# Current repository
CURRENT_REPOSITORY = "https://" + git_remote_path().rstrip(".git")

# Check if it's upstream repository
IS_DEVELOPMENT = (CURRENT_REPOSITORY is UPSTREAM_REPOSITORY)

# Define if it's Travis-CI
IS_TRAVIS = ("TRAVIS" in os.environ and os.environ["TRAVIS"] != "")

# Content allowed in repository.json
ALLOWED_CONFIGS = ("database", "url", "github.token", "ssh.port", "ssh.user", "ssh.host", "ssh.path")

# Alias configs for repository.json
ALIAS_CONFIGS = ("db", "url", "github_token", "ssh_port", "ssh_user", "ssh_host", "ssh_path")
