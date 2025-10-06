import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.patches import Polygon
from typing import Optional, Tuple
from matplotlib.axes import Axes
from matplotlib.lines import Line2D
from matplotlib.image import AxesImage


def gradient_fill(
    x: np.ndarray, 
    y: np.ndarray,
    line: Optional[Line2D] = None,
    fill_color: Optional[str] = None, 
    ax: Optional[Axes] = None,
    alpha_coef: float = 1.0, 
    gradient_to_min: bool = False, 
    gradient_steps: int = 100,
    autoscale: bool = False,
    **plot_kwargs
) -> Tuple[Line2D, AxesImage]:
    """
    Создаёт линию с градиентной заливкой под ней.

    Parameters
    ----------
    x : np.ndarray
        Координаты X для линии
    y : np.ndarray  
        Координаты Y для линии
    line: Optional[Line2D]
        Объект линия если уже создан и настроен и требуется применить градиент к ней
    fill_color : Optional[str]
        Цвет для заливки. Если None, будет использован цвет линии
    ax : Optional[Axes]
        Оси для построения. Если None, используются текущие оси
    alpha_coef : float
        Коэффициент прозрачности градиента (по умолчанию 1.0)
    gradient_to_min : bool
        Если True, градиент идёт до минимального значения Y на осях
    gradient_steps : int
        Количество шагов в градиенте (по умолчанию 100)
    **plot_kwargs
        Дополнительные аргументы для matplotlib.plot()

    Returns
    -------
    Tuple[Line2D, AxesImage]
        Кортеж из объекта линии и градиентного изображения
    """
    # Преобразуем входные данные в numpy массивы
    x = np.asarray(x)
    y = np.asarray(y)
    
    # Получаем текущие оси, если не переданы
    if ax is None:
        ax = plt.gca()

    # Строим основную линию
    if line is None:
        line, = ax.plot(x, y, **plot_kwargs)

    # Определяем цвет заливки
    if fill_color is None:
        fill_color = line.get_color()

    # Получаем параметры линии для согласованности
    zorder = line.get_zorder()
    line_alpha = line.get_alpha()
    line_alpha = 1.0 if line_alpha is None else line_alpha

    # Создаём градиентный массив
    gradient_array = _create_gradient_array(
        fill_color, 
        alpha_coef * line_alpha, 
        gradient_steps
    )

    # Определяем границы для градиента
    x_bounds, y_bounds = _calculate_bounds(x, y, ax, gradient_to_min)

    # Создаём градиентное изображение
    gradient_image = ax.imshow(
        gradient_array, 
        aspect='auto', 
        extent=[*x_bounds, *y_bounds],
        origin='lower', 
        zorder=zorder - 1  # Размещаем под линией
    )

    # Создаём маску для обрезки градиента по контуру данных
    clip_path = _create_clip_path(x, y, x_bounds, y_bounds)
    ax.add_patch(clip_path)
    gradient_image.set_clip_path(clip_path)

    # Автоматически подстраиваем масштаб
    ax.autoscale(autoscale)
    
    return line, gradient_image


def _create_gradient_array(
    color: str, 
    max_alpha: float, 
    steps: int
) -> np.ndarray:
    """
    Создаёт массив градиента для заливки.
    
    Parameters
    ----------
    color : str
        Цвет в формате matplotlib
    max_alpha : float
        Максимальная прозрачность
    steps : int
        Количество шагов градиента
        
    Returns
    -------
    np.ndarray
        Массив градиента размером (steps, 1, 4) в формате RGBA
    """
    gradient = np.empty((steps, 1, 4), dtype=float)
    rgb = mcolors.to_rgb(color)
    
    # Устанавливаем RGB компоненты
    gradient[:, :, :3] = rgb
    
    # Создаём линейный градиент альфа-канала
    gradient[:, :, 3] = np.linspace(0, max_alpha, steps)[:, None]
    
    return gradient


def _calculate_bounds(
    x: np.ndarray, 
    y: np.ndarray, 
    ax: Axes, 
    gradient_to_min: bool
) -> Tuple[Tuple[float, float], Tuple[float, float]]:
    """
    Вычисляет границы для градиента.
    
    Parameters
    ----------
    x : np.ndarray
        Координаты X
    y : np.ndarray
        Координаты Y
    ax : Axes
        Объект осей
    gradient_to_min : bool
        Использовать ли минимум осей вместо минимума данных
        
    Returns
    -------
    Tuple[Tuple[float, float], Tuple[float, float]]
        ((x_min, x_max), (y_min, y_max))
    """
    x_min, x_max = float(x.min()), float(x.max())
    y_min, y_max = float(y.min()), float(y.max())
    
    if gradient_to_min:
        y_min = ax.get_ylim()[0]
    
    return (x_min, x_max), (y_min, y_max)


def _create_clip_path(
    x: np.ndarray, 
    y: np.ndarray, 
    x_bounds: Tuple[float, float], 
    y_bounds: Tuple[float, float]
) -> Polygon:
    """
    Создаёт путь обрезки для градиента.
    
    Parameters
    ----------
    x : np.ndarray
        Координаты X линии
    y : np.ndarray
        Координаты Y линии
    x_bounds : Tuple[float, float]
        Границы по X
    y_bounds : Tuple[float, float]
        Границы по Y
        
    Returns
    -------
    Polygon
        Полигон для обрезки градиента
    """
    x_min, x_max = x_bounds
    y_min, _ = y_bounds
    
    # Создаём замкнутый контур: начало -> линия данных -> конец -> обратно
    path_points = np.column_stack([x, y])
    closed_path = np.vstack([
        [x_min, y_min],  # Начальная точка на базовой линии
        path_points,     # Точки данных
        [x_max, y_min],  # Конечная точка на базовой линии
        [x_min, y_min]   # Замыкание контура
    ])
    
    return Polygon(
        closed_path, 
        facecolor='none', 
        edgecolor='none', 
        closed=True
    )
