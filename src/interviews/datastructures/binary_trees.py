"""Binary trees."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Generic
from typing import Optional
from typing import TypeVar

# Key type, we only support int or strings (easier for our implementation)
K = TypeVar("K", int, str)

# Value type, could be anything
V = TypeVar("V")


@dataclass
class Node(Generic[K, V]):
    """A single node in a binary tree.

    Key is immutable while value can be changed, eventually set to None.
    """

    __slots__ = ["_key", "value", "left_child", "right_child"]

    _key: K
    value: Optional[V]

    left_child: Optional[Node[K, V]]
    right_child: Optional[Node[K, V]]

    def __init__(
        self,
        key: K,
        value: Optional[V] = None,
        left_child: Optional[Node[K, V]] = None,
        right_child: Optional[Node[K, V]] = None,
    ) -> None:
        """Build a new node.

        Args
            key: the key for this node
            value: the value of this node (optional)
            left_child: the left node (optional)
            right_child: the right node (optional)
        """
        self._key = key
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

    @property
    def key(self) -> K:
        """Returns the key for this node."""
        return self._key


@dataclass
class BinaryTree(Generic[K, V]):
    """A Binary tree."""

    root: Optional[Node[K, V]] = None

    def is_empty(self) -> bool:
        """Checks that this binary tree has at least one node."""
        return self.root is None
