# Stubs for galaxy.tools.deps.resolvers.unlinked_tool_shed_packages (Python 3.4)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from .galaxy_packages import BaseGalaxyPackageDependencyResolver
from ..resolvers import Dependency

class UnlinkedToolShedPackageDependencyResolver(BaseGalaxyPackageDependencyResolver):
    dict_collection_visible_keys = ...  # type: Any
    resolver_type = ...  # type: str
    preferred_owners = ...  # type: Any
    select_by_owner = ...  # type: Any
    def __init__(self, dependency_manager, **kwds) -> None: ...

class CandidateDependency(Dependency):
    dict_collection_visible_keys = ...  # type: Any
    dependency_type = ...  # type: str
    @property
    def exact(self): ...
    dependency = ...  # type: Any
    path = ...  # type: Any
    owner = ...  # type: Any
    def __init__(self, dependency, path, owner: Any = ...) -> None: ...
    def shell_commands(self, requirement): ...
