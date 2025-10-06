
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.lines import Line2D
from matplotlib.axes import Axes
from typing import Optional, Tuple


def glow_line(
    x: np.ndarray,
    y: np.ndarray,
    main_line: Optional[Line2D] = None,
    glow_color: Optional[str] = None,
    glow_width: float = 3.0,
    glow_alpha: float = 0.5,
    glow_layers: int = 10,
    decay_function: Optional[callable] = None,
    alpha_mode: str = "uniform",
    colormap: Optional[str] = None,
    ax: Optional[Axes] = None,
    **plot_kwargs
) -> Tuple[Line2D, list]:
    """
    Создаёт линию с эффектом свечения.
    
    Parameters
    ----------
    x : np.ndarray
        Координаты X для линии
    y : np.ndarray
        Координаты Y для линии
    main_line: Optional[Line2D]
        Объект линия если уже создан и настроен и требуется применить градиент к ней
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
        где distance_ratio от 0 (центр) до 1 (край свечения)
    alpha_mode : str
        Режим изменения прозрачности: 'uniform', 'gradient', 'pulse'
    colormap : Optional[str]
        Цветовая схема для свечения (например, 'plasma', 'viridis')
    ax : Optional[Axes]
        Оси для построения. Если None, используются текущие оси
    **plot_kwargs
        Дополнительные аргументы для основной линии
        
    Returns
    -------
    Tuple[Line2D, list]
        Основная линия и список линий свечения
    """
    # Преобразуем входные данные в numpy массивы
    x = np.asarray(x)
    y = np.asarray(y)
    
    # Получаем текущие оси, если не переданы
    if ax is None:
        ax = plt.gca()
    
    # Строим основную линию
    if main_line is None:
        main_line, = ax.plot(x, y, **plot_kwargs)
    
    # Определяем цвет свечения
    if glow_color is None:
        glow_color = main_line.get_color()
    
    # Получаем базовую ширину линии
    base_linewidth = main_line.get_linewidth()
    zorder = main_line.get_zorder()
    
    # Создаем функцию затухания по умолчанию
    if decay_function is None:
        decay_function = _default_decay_functions()['gaussian']
    
    # Создаем слои свечения
    glow_lines = []
    
    for i in range(glow_layers):
        # Расчет параметров для текущего слоя
        layer_ratio = (i + 1) / glow_layers
        layer_width = base_linewidth + (glow_width * base_linewidth * layer_ratio)
        
        # Применяем функцию затухания
        decay_alpha = decay_function(layer_ratio)
        
        # Применяем режим изменения прозрачности
        alpha_multiplier = _calculate_alpha_mode(alpha_mode, i, glow_layers)
        
        layer_alpha = glow_alpha * decay_alpha * alpha_multiplier
        
        # Определяем цвет слоя
        layer_color = _get_layer_color(glow_color, colormap, layer_ratio)
        
        # Создаем слой свечения
        layer_line, = ax.plot(
            x, y,
            color=layer_color,
            alpha=layer_alpha,
            linewidth=layer_width,
            solid_capstyle='round',
            solid_joinstyle='round',
            zorder=zorder - i - 1  # Размещаем под основной линией
        )
        
        glow_lines.append(layer_line)
    
    return main_line, glow_lines


def _default_decay_functions() -> dict:
    """
    Возвращает словарь с предустановленными функциями затухания.
    
    Returns
    -------
    dict
        Словарь функций затухания
    """
    return {
        'linear': lambda r: 1.0 - r,
        'exponential': lambda r: np.exp(-3 * r),
        'gaussian': lambda r: np.exp(-2 * r**2),
        'quadratic': lambda r: (1 - r)**2,
        'cubic': lambda r: (1 - r)**3,
        'sine': lambda r: np.sin(np.pi * (1 - r) / 2),
    }


def _calculate_alpha_mode(mode: str, layer_index: int, total_layers: int) -> float:
    """
    Вычисляет множитель прозрачности в зависимости от режима.
    
    Parameters
    ----------
    mode : str
        Режим изменения прозрачности
    layer_index : int
        Индекс текущего слоя
    total_layers : int
        Общее количество слоев
        
    Returns
    -------
    float
        Множитель прозрачности
    """
    ratio = layer_index / (total_layers - 1) if total_layers > 1 else 0
    
    if mode == 'uniform':
        return 1.0
    elif mode == 'gradient':
        return 1.0 - ratio * 0.5  # Уменьшение до 50%
    elif mode == 'pulse':
        return 0.5 + 0.5 * np.sin(ratio * 2 * np.pi)
    else:
        return 1.0


def _get_layer_color(base_color: str, colormap: Optional[str], ratio: float) -> str:
    """
    Определяет цвет слоя в зависимости от цветовой схемы.
    
    Parameters
    ----------
    base_color : str
        Базовый цвет
    colormap : Optional[str]
        Название цветовой схемы
    ratio : float
        Соотношение от центра к краю (0-1)
        
    Returns
    -------
    str
        Цвет для текущего слоя
    """
    if colormap is None:
        return base_color
    
    try:
        cmap = plt.cm.get_cmap(colormap)
        # Инвертируем ratio, чтобы яркие цвета были в центре
        color_value = cmap(1.0 - ratio)
        return mcolors.to_hex(color_value)
    except (ValueError, AttributeError):
        # Если colormap не найден, возвращаем базовый цвет
        return base_color


# Экспортируем функции затухания для внешнего использования
def get_decay_functions() -> dict:
    """
    Возвращает доступные функции затухания для использования в glow_line.
    
    Returns
    -------
    dict
        Словарь с функциями затухания
        
    Examples
    --------
    >>> decay_funcs = get_decay_functions()
    >>> custom_decay = decay_funcs['exponential']
    >>> ax.glow_line(x, y, decay_function=custom_decay)
    """
    return _default_decay_functions()