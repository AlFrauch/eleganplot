"""
Утилиты EleganPlot.

Содержит вспомогательные функции и системы расширения.
"""

from .gradient import gradient_fill
from .glow import glow_line, get_decay_functions
from .decorators import custom_axes_method, method_registry

__all__ = [
    "gradient_fill",
    "glow_line",
    "get_decay_functions",
    "custom_axes_method", 
    "method_registry",
]
