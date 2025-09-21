"""
Коллекция кастомных методов для EleganAxes.

Этот модуль содержит готовые кастомные методы, которые можно легко
добавить к осям через систему декораторов.
"""

import numpy as np
from typing import Optional, Tuple, Any
from matplotlib.lines import Line2D
from matplotlib.image import AxesImage

from .decorators import custom_axes_method, method_registry
from .gradient import gradient_fill
from .glow import glow_line


@custom_axes_method("gradient_plot")
def gradient_plot_method(
    self, 
    x, 
    y, 
    fill_color: Optional[str] = None,
    alpha_coef: float = 1.0,
    gradient_to_min: bool = False,
    gradient_steps: int = 100,
    **kwargs
) -> Tuple[Line2D, AxesImage]:
    """
    Строит линию с градиентной заливкой под ней.
    
    Parameters
    ----------
    x : array-like
        Координаты X
    y : array-like
        Координаты Y  
    fill_color : Optional[str]
        Цвет заливки. Если None, используется цвет линии
    alpha_coef : float
        Коэффициент прозрачности градиента
    gradient_to_min : bool
        Градиент до минимума осей (вместо минимума данных)
    gradient_steps : int
        Количество шагов в градиенте
    **kwargs
        Дополнительные аргументы для plot()
        
    Returns
    -------
    Tuple[Line2D, AxesImage]
        Линия и градиентное изображение
        
    Examples
    --------
    >>> fig, ax = eleganplot.subplots()
    >>> x = np.linspace(0, 10, 100)
    >>> y = np.sin(x)
    >>> line, gradient = ax.gradient_plot(x, y, fill_color='red', alpha_coef=0.7)
    """
    return gradient_fill(
        x=x,
        y=y, 
        fill_color=fill_color,
        ax=self._ax,
        alpha_coef=alpha_coef,
        gradient_to_min=gradient_to_min,
        gradient_steps=gradient_steps,
        **kwargs
    )


@custom_axes_method("glow_line")
def glow_line_method(
    self, 
    x, 
    y, 
    glow_color: Optional[str] = None,
    glow_width: float = 3.0,
    glow_alpha: float = 0.5,
    glow_layers: int = 10,
    decay_function: Optional[callable] = None,
    alpha_mode: str = "uniform",
    colormap: Optional[str] = None,
    **kwargs
) -> Tuple[Line2D, list]:
    """
    Строит линию с эффектом свечения.
    
    Parameters
    ----------
    x : array-like
        Координаты X
    y : array-like
        Координаты Y  
    glow_color : Optional[str]
        Цвет свечения. Если None, используется цвет основной линии
    glow_width : float
        Ширина свечения (множитель относительно основной линии)
    glow_alpha : float
        Базовая прозрачность свечения
    glow_layers : int
        Количество слоев свечения
    decay_function : Optional[callable]
        Функция затухания f(distance_ratio) -> alpha_multiplier
    alpha_mode : str
        Режим изменения прозрачности: 'uniform', 'gradient', 'pulse'
    colormap : Optional[str]
        Цветовая схема для свечения (например, 'plasma', 'viridis')
    **kwargs
        Дополнительные аргументы для основной линии
        
    Returns
    -------
    Tuple[Line2D, list]
        Основная линия и список линий свечения
        
    Examples
    --------
    >>> fig, ax = eleganplot.subplots()
    >>> x = np.linspace(0, 10, 100)
    >>> y = np.sin(x)
    >>> main_line, glow_lines = ax.glow_line(x, y, glow_color='cyan', glow_width=5.0)
    
    >>> # Использование кастомной функции затухания
    >>> custom_decay = lambda r: np.exp(-5 * r**3)
    >>> main_line, glow_lines = ax.glow_line(x, y, decay_function=custom_decay)
    
    >>> # Использование цветовой схемы
    >>> main_line, glow_lines = ax.glow_line(x, y, colormap='plasma', alpha_mode='gradient')
    """
    return glow_line(
        x=x,
        y=y, 
        glow_color=glow_color,
        glow_width=glow_width,
        glow_alpha=glow_alpha,
        glow_layers=glow_layers,
        decay_function=decay_function,
        alpha_mode=alpha_mode,
        colormap=colormap,
        ax=self._ax,
        **kwargs
    )