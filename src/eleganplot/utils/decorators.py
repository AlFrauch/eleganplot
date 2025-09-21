"""
Система декораторов для расширения функциональности EleganAxes.

Позволяет легко добавлять кастомные методы к осям через декораторы.
"""

from functools import wraps
from typing import Callable, Dict, Any, Optional
import inspect


# Реестр кастомных методов
_CUSTOM_METHODS: Dict[str, Callable] = {}


def custom_axes_method(
    name: Optional[str] = None, 
    override_existing: bool = False
) -> Callable:
    """
    Декоратор для регистрации кастомных методов EleganAxes.
    
    Parameters
    ----------
    name : Optional[str]
        Имя метода. Если None, используется имя функции
    override_existing : bool
        Разрешить ли переопределение существующих методов
        
    Returns
    -------
    Callable
        Декорированная функция
        
    Examples
    --------
    >>> @custom_axes_method()
    >>> def gradient_plot(ax, x, y, **kwargs):
    ...     from .gradient import gradient_fill
    ...     return gradient_fill(x, y, ax=ax._ax, **kwargs)
    
    >>> @custom_axes_method("fancy_scatter")
    >>> def custom_scatter(ax, x, y, **kwargs):
    ...     return ax._ax.scatter(x, y, **kwargs)
    """
    def decorator(func: Callable) -> Callable:
        method_name = name or func.__name__
        
        if method_name in _CUSTOM_METHODS and not override_existing:
            raise ValueError(
                f"Метод '{method_name}' уже зарегистрирован. "
                f"Используйте override_existing=True для переопределения."
            )
        
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            # Передаём self (EleganAxes) как первый аргумент
            return func(self, *args, **kwargs)
        
        # Добавляем docstring информацию
        if func.__doc__:
            wrapper.__doc__ = func.__doc__
        else:
            wrapper.__doc__ = f"Кастомный метод {method_name} для EleganAxes"
        
        # Регистрируем метод
        _CUSTOM_METHODS[method_name] = wrapper
        
        return func
    
    return decorator


def register_method(axes_class, method_name: str, method_func: Callable) -> None:
    """
    Регистрирует метод в классе осей.
    
    Parameters
    ----------
    axes_class
        Класс осей для регистрации
    method_name : str
        Имя метода
    method_func : Callable
        Функция метода
    """
    setattr(axes_class, method_name, method_func)


def get_registered_methods() -> Dict[str, Callable]:
    """
    Возвращает все зарегистрированные кастомные методы.
    
    Returns
    -------
    Dict[str, Callable]
        Словарь зарегистрированных методов
    """
    return _CUSTOM_METHODS.copy()


def apply_custom_methods(axes_class) -> None:
    """
    Применяет все зарегистрированные кастомные методы к классу осей.
    
    Parameters
    ----------
    axes_class
        Класс осей для применения методов
    """
    for method_name, method_func in _CUSTOM_METHODS.items():
        register_method(axes_class, method_name, method_func)


class MethodRegistry:
    """
    Реестр методов для более продвинутого управления кастомными методами.
    """
    
    def __init__(self):
        self._methods: Dict[str, Dict[str, Any]] = {}
    
    def register(
        self, 
        name: str, 
        func: Callable, 
        description: str = "",
        category: str = "general"
    ) -> None:
        """
        Регистрирует метод с дополнительными метаданными.
        
        Parameters
        ----------
        name : str
            Имя метода
        func : Callable
            Функция метода
        description : str
            Описание метода
        category : str
            Категория метода
        """
        self._methods[name] = {
            'function': func,
            'description': description,
            'category': category,
            'signature': inspect.signature(func)
        }
    
    def get_method(self, name: str) -> Optional[Callable]:
        """Получает метод по имени."""
        method_info = self._methods.get(name)
        return method_info['function'] if method_info else None
    
    def list_methods(self, category: Optional[str] = None) -> Dict[str, str]:
        """
        Возвращает список методов с описаниями.
        
        Parameters
        ----------
        category : Optional[str]
            Фильтр по категории
            
        Returns
        -------
        Dict[str, str]
            Словарь {имя_метода: описание}
        """
        result = {}
        for name, info in self._methods.items():
            if category is None or info['category'] == category:
                result[name] = info['description']
        return result
    
    def apply_to_class(self, axes_class) -> None:
        """Применяет все методы к классу."""
        for name, info in self._methods.items():
            register_method(axes_class, name, info['function'])


# Глобальный реестр для удобства
method_registry = MethodRegistry()
