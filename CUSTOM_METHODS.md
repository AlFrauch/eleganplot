# Система Кастомных Методов EleganPlot

EleganPlot теперь предоставляет мощную систему для добавления собственных методов к осям. Это позволяет легко расширять функциональность библиотеки без изменения основного кода.

## Быстрый старт

### Использование готовых методов

```python
import eleganplot as eplt
import numpy as np

# Создаём данные
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

# Создаём график с градиентной заливкой
fig, ax = eplt.subplots()
line, gradient = ax.gradient_plot(x, y, fill_color='blue', alpha_coef=0.7)
plt.show()
```

### Доступные готовые методы

- **`gradient_plot(x, y, ...)`** - Линия с градиентной заливкой
- **`smooth_line(x, y, ...)`** - Сглаженная линия через точки
- **`confidence_band(x, y_mean, y_std, ...)`** - Линия с доверительной полосой
- **`multi_line(x, y_data, ...)`** - Несколько линий на одних осях

## Создание собственных методов

### Простой способ - декоратор

```python
from eleganplot import custom_axes_method
from eleganplot.utils.decorators import apply_custom_methods

@custom_axes_method("my_plot")
def my_custom_plot(ax, x, y, style='fancy', **kwargs):
    \"\"\"Мой кастомный метод построения графиков.\"\"\"
    if style == 'fancy':
        # Ваша логика здесь
        return ax._ax.plot(x, y, marker='o', linestyle='--', **kwargs)
    else:
        return ax._ax.plot(x, y, **kwargs)

# Применяем к классу EleganAxes
apply_custom_methods(eplt.axes().__class__)

# Теперь можно использовать
fig, ax = eplt.subplots()
ax.my_plot(x, y, style='fancy', color='red')
```

### Продвинутый способ - через реестр

```python
from eleganplot import method_registry

def advanced_plot(ax, x, y, **kwargs):
    \"\"\"Продвинутый метод построения.\"\"\"
    # Ваша сложная логика
    return ax._ax.plot(x, y, **kwargs)

# Регистрируем с метаданными
method_registry.register(
    name="advanced_plot",
    func=advanced_plot,
    description="Продвинутый метод для сложных графиков",
    category="advanced"
)

# Применяем к классу
method_registry.apply_to_class(eplt.axes().__class__)
```

## Параметры gradient_fill

Обновлённая функция `gradient_fill` теперь поддерживает:

- **`fill_color`** - Цвет заливки (по умолчанию цвет линии)
- **`alpha_coef`** - Коэффициент прозрачности (0-1)
- **`gradient_to_min`** - Градиент до минимума осей (вместо данных)
- **`gradient_steps`** - Количество шагов в градиенте

```python
# Пример с разными параметрами
fig, axes = eplt.subplots(1, 3, figsize=(15, 5))

# Стандартный градиент
axes[0].gradient_plot(x, y, fill_color='blue')

# Полупрозрачный градиент до минимума осей
axes[1].gradient_plot(x, y, fill_color='red', alpha_coef=0.5, gradient_to_min=True)

# Грубый градиент с малым количеством шагов
axes[2].gradient_plot(x, y, fill_color='green', gradient_steps=20)
```

## Структура проекта

```
src/eleganplot/
├── utils/
│   ├── decorators.py      # Система декораторов
│   ├── custom_methods.py  # Готовые кастомные методы
│   └── gradient.py        # Улучшенная gradient_fill
└── pyplot.py              # Основной модуль с автоинициализацией
```

## Лучшие практики

1. **Именование**: Используйте описательные имена методов
2. **Документация**: Всегда добавляйте docstring к методам
3. **Параметры**: Первым параметром должен быть `ax` (объект EleganAxes)
4. **Возвращаемые значения**: Возвращайте matplotlib объекты для дальнейшей работы
5. **Обработка ошибок**: Добавляйте проверки входных данных

## Примеры использования

Смотрите файл `examples/custom_methods_example.py` для полных примеров использования всех возможностей системы кастомных методов.
