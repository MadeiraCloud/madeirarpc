#!/usr/bin/env/python
"""
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

import distutils.core

distutils.core.setup(
    name = "madeirarpc",
    version = "0.1",
    packages = ["madeirarpc"],
    author = "Peng Zhao",
    author_email = "peng@mc2.io",
    url = "https://github.com/MadeiraCloud/madeira-rpc",
    license = "http://www.apache.org/licenses/LICENSE-2.0",
    description = "MadeiraRPC is a fork of TornadoRPC, with bug fixes and feature patch"
)
