#!/usr/bin/python -u

"""
Copyright 2017, JacksGong(https://jacksgong.com)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import subprocess
import os
from os import remove, rename
from os.path import exists

from webpc.helper import size_diff, print_process, resource_path


FNULL = open(os.devnull, 'w')


class Converter:
    swap_webp_path = None
    command_prefix = list()

  