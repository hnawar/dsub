# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Package marker file."""
import os

# VERSION is parsed here to decouple dsub's __init__ from the implementation
# of providers.
with open(os.path.join(os.path.dirname(__file__), 'VERSION'), 'r') as vf:
  __version__ = ''.join(l for l in vf.readlines() if not l.startswith('#'))
__version__ = __version__.strip()
