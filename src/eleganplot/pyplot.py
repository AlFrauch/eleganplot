"""Модуль pyplot для EleganPlot в стиле matplotlib.pyplot.

Предоставляет функции figure и axes с автоматическим применением тем EleganPlot.
"""

from __future__ import annotations

from typing import Any

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from matplotlib.colors import LinearSegmentedColormap

from .theme import apply_theme
from .utils.decorators import apply_custom_methods


class EleganAxes:
    """Обёртка для matplotlib.axes.Axes с дополнительными методами EleganPlot."""
    
    def __init__(self, ax: Axes):
        """Инициализация обёртки для осей.
        
        Args:
            ax: Объект matplotlib.axes.Axes для обёртки
        """
        self._ax = ax
        # Применяем тему при создании
        apply_theme()
    
    def plot(self, *args, **kwargs):
        """Рисует линии и/или маркеры с применением темы EleganPlot.
        
        Args:
            *args: Позиционные аргументы для matplotlib.axes.Axes.plot()
            **kwargs: Именованные аргументы для matplotlib.axes.Axes.plot()
            
        Returns:
            Результат вызова matplotlib.axes.Axes.plot()
        """
        # Обычный plot без дополнительной логики
        # Кастомные методы теперь доступны отдельно (например, gradient_plot)
        return self._ax.plot(*args, **kwargs) 
    
    def __getattr__(self, name):
        """Делегирует все остальные атрибуты и методы оригинальному объекту Axes."""
        return getattr(self._ax, name)
    
    def __setattr__(self, name, value):
        """Устанавливает атрибуты."""
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            setattr(self._ax, name, value)
    
    def __repr__(self):
        """Представление объекта."""
        return f"EleganAxes({self._ax!r})"


def figure(*args, **kwargs) -> Figure:
    """Создаёт новую фигуру с применением текущей темы EleganPlot.
    
    Параметры те же, что у matplotlib.pyplot.figure().
    Автоматически применяет текущую тему перед созданием фигуры.
    
    Returns:
        Figure: Объект фигуры matplotlib с применённой темой
    """
    # Применяем текущую тему перед созданием фигуры
    apply_theme()
    
    # Создаём фигуру с переданными параметрами
    fig = plt.figure(*args, **kwargs)
    
    return fig


def axes(*args, **kwargs) -> EleganAxes:
    """Создаёт новые оси с применением текущей темы EleganPlot.
    
    Параметры те же, что у matplotlib.pyplot.axes().
    Автоматически применяет текущую тему перед созданием осей.
    
    Returns:
        EleganAxes: Обёртка для объекта осей matplotlib с дополнительными методами
    """
    # Применяем текущую тему перед созданием осей
    apply_theme()
    
    # Создаём оси с переданными параметрами
    ax = plt.axes(*args, **kwargs)
    
    # Возвращаем обёртку с дополнительными методами
    return EleganAxes(ax)


def subplots(*args, **kwargs) -> tuple[Figure, EleganAxes | Any]:
    """Создаёт фигуру и оси с применением текущей темы EleganPlot.
    
    Параметры те же, что у matplotlib.pyplot.subplots().
    Автоматически применяет текущую тему перед созданием.
    
    Returns:
        tuple: (Figure, EleganAxes) или (Figure, array of EleganAxes)
    """
    # Применяем текущую тему перед созданием
    apply_theme()
    
    # Создаём фигуру и оси с переданными параметрами
    fig, ax = plt.subplots(*args, **kwargs)
    
    # Обёртываем оси в EleganAxes
    if isinstance(ax, Axes):
        # Одиночные оси
        wrapped_ax = EleganAxes(ax)
    else:
        # Массив осей - обёртываем каждую
        wrapped_ax = np.array([[EleganAxes(axis) for axis in row] if hasattr(row, '__iter__') else EleganAxes(row) 
                              for row in ax] if ax.ndim > 1 else [EleganAxes(axis) for axis in ax])
    
    return fig, wrapped_ax


def gradient_subplots(
    figsize: tuple[float, float] = (8, 5),
    dpi: int | None = None,
    gradient_colors: tuple[str, str] = ("#00080a", "#042628"),
    axes_position: tuple[float, float, float, float] = (0.12, 0.12, 0.75, 0.75),
    nx: int = 512,
    ny: int = 64,
    **kwargs
) -> tuple[Figure, EleganAxes]:
    """Создаёт фигуру с градиентным фоном и оси для построения графиков.
    
    Эта функция создает фигуру с красивым градиентным фоном и возвращает
    основную ось с прозрачным фоном для рисования графиков поверх градиента.
    
    Parameters
    ----------
    figsize : tuple[float, float], optional
        Размер фигуры (ширина, высота) в дюймах, по умолчанию (8, 5)
    dpi : int | None, optional
        Разрешение фигуры в точках на дюйм, по умолчанию None
    gradient_colors : tuple[str, str], optional
        Цвета для градиента (начальный, конечный), по умолчанию ("#00080a", "#042628")
    axes_position : tuple[float, float, float, float], optional
        Позиция осей в формате [left, bottom, width, height] в относительных координатах,
        по умолчанию (0.12, 0.12, 0.75, 0.75)
    nx : int, optional
        Разрешение градиента по горизонтали, по умолчанию 512
    ny : int, optional
        Разрешение градиента по вертикали, по умолчанию 64
    **kwargs
        Дополнительные аргументы для matplotlib.pyplot.figure()
    
    Returns
    -------
    tuple[Figure, EleganAxes]
        Кортеж из объекта фигуры и обёрнутых осей для построения графиков
        
    Examples
    --------
    >>> import eleganplot as eplt
    >>> fig, ax = eplt.gradient_subplots(dpi=200)
    >>> ax.plot([1, 2, 3], [1, 4, 2])
    >>> eplt.show()
    
    С кастомными цветами градиента:
    >>> fig, ax = eplt.gradient_subplots(
    ...     gradient_colors=("#1a0033", "#330066"),
    ...     figsize=(10, 6)
    ... )
    """
    # Применяем текущую тему
    apply_theme()
    
    # Создаём параметры для фигуры
    fig_kwargs = {'figsize': figsize}
    if dpi is not None:
        fig_kwargs['dpi'] = dpi
    fig_kwargs.update(kwargs)
    
    # Создаём фигуру
    fig = plt.figure(**fig_kwargs)
    
    # --- Фоновая ось (вся фигура) с градиентом ---
    ax_bg = fig.add_axes([0, 0, 1, 1], zorder=0)
    ax_bg.axis('off')
    
    # Создаём градиентный массив
    grad = np.linspace(0, 1, nx)
    grad = np.tile(grad, (ny, 1))  # 2D полотно
    
    # Создаём цветовую карту из двух цветов
    cmap = LinearSegmentedColormap.from_list("gradient_bg", gradient_colors)
    
    # Применяем градиент к фоновой оси
    ax_bg.imshow(
        grad, 
        aspect='auto', 
        cmap=cmap, 
        extent=[0, 1, 0, 1], 
        transform=fig.transFigure
    )
    
    # --- Основная ось поверх с прозрачным фоном ---
    ax = fig.add_axes(axes_position, zorder=1, facecolor='none')
    
    # Возвращаем обёрнутые оси
    return fig, EleganAxes(ax)


def gca() -> EleganAxes:
    """Получает текущие оси с применением темы.
    
    Returns:
        EleganAxes: Обёртка для текущих активных осей
    """
    apply_theme()
    return EleganAxes(plt.gca())


def gcf() -> Figure:
    """Получает текущую фигуру с применением темы.
    
    Returns:
        Figure: Текущая активная фигура
    """
    apply_theme()
    return plt.gcf()


def show(*args, **kwargs) -> None:
    """Отображает все фигуры."""
    plt.show(*args, **kwargs)


def close(*args, **kwargs) -> None:
    """Закрывает фигуру(ы)."""
    plt.close(*args, **kwargs)


def savefig(*args, **kwargs) -> None:
    """Сохраняет текущую фигуру."""
    plt.savefig(*args, **kwargs)


# Автоматически применяем кастомные методы к EleganAxes при импорте модуля
def _initialize_custom_methods():
    """Инициализирует кастомные методы для EleganAxes."""
    try:
        # Импортируем кастомные методы (это автоматически их регистрирует)
        from .utils import custom_methods
        from .utils.decorators import method_registry
        
        # Применяем зарегистрированные методы к классу через оба реестра
        apply_custom_methods(EleganAxes)
        method_registry.apply_to_class(EleganAxes)
    except ImportError:
        # Если кастомные методы недоступны, продолжаем без них
        pass


# Инициализируем при импорте
_initialize_custom_methods()
