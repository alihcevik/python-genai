# Copyright 2025 Google LLC
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
#

"""Tool decorator for automatic schema generation."""

from typing import Any, Callable, Optional, TypeVar

F = TypeVar('F', bound=Callable[..., Any])

def tool(
    func: Optional[F] = None,
    *,
    name: Optional[str] = None,
    description: Optional[str] = None,
) -> Any:
    """Decorator to mark a function as a tool and optionally customize its schema.

    Usage:
    
    @tool
    def my_func(x: int) -> str:
        '''Docstring here.'''
        return str(x)
        
    @tool(name="custom_name", description="Custom description")
    def another_func(x: int) -> str:
        return str(x)
    """
    def decorator(f: F) -> F:
        f._tool_name = name
        f._tool_description = description
        return f

    if func is not None:
        return decorator(func)
    return decorator
