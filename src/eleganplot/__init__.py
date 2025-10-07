
"""
EleganPlot - Элегантные графики для Python.

Библиотека для создания красивых и стильных графиков на основе matplotlib
с поддержкой тем и кастомных методов визуализации.
"""

from .theme import Theme, get_current_theme, list_themes, set_current_theme, apply_theme
from .pyplot import figure, axes, subplots, gradient_subplots, gca, gcf, show, close, savefig
from .utils.gradient import gradient_fill
from .utils.decorators import custom_axes_method, method_registry

__all__ = [
    # Основные функции pyplot
    "figure",
    "axes", 
    "subplots",
    "gradient_subplots",
    "gca",
    "gcf",
    "show",
    "close",
    "savefig",
    
    # Система тем
    "Theme",
    "get_current_theme",
    "set_current_theme", 
    "apply_theme",
    "list_themes",
    
    # Кастомные функции
    "gradient_fill",
    
    # Система расширения
    "custom_axes_method",
    "method_registry",
    
    "__version__",
]

__version__ = "0.1.0"
