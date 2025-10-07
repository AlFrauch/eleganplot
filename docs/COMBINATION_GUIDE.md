# Руководство по комбинированию методов EleganPlot

![Пример комбинирования методов](images/demo_output.png)

## Быстрый старт

### Базовое комбинирование glow_line + gradient_plot

```python
import eleganplot as eplt
import numpy as np

fig, ax = eplt.subplots()
x = np.linspace(0, 4*np.pi, 200)
y = np.sin(x) * np.exp(-x/8)

# 1. Сначала gradient_plot для заливки
line, gradient = ax.gradient_plot(
    x, y, 
    fill_color='cyan', 
    alpha_coef=0.3,
    linewidth=0  # Скрываем линию gradient_plot
)

# 2. Затем glow_line для свечения
main_line, glow_lines = ax.glow_line(
    x, y,
    glow_color='cyan',
    glow_width=3.0,
    glow_alpha=0.8,
    linewidth=2
)
```

## Принципы комбинирования

### 1. Порядок имеет значение
- **Z-order**: Методы, вызванные позже, рисуются поверх
- **Рекомендуемый порядок**: заливка → свечение → основная линия

### 2. Управление видимостью
```python
# Скрыть основную линию gradient_plot
ax.gradient_plot(x, y, linewidth=0)

# Сделать прозрачным
ax.gradient_plot(x, y, alpha_coef=0.3)
```

### 3. Цветовая гармония
```python
# Одинаковые цвета для согласованности
color = 'cyan'
ax.gradient_plot(x, y, fill_color=color, linewidth=0)
ax.glow_line(x, y, glow_color=color)

# Или дополняющие цвета
ax.gradient_plot(x, y, fill_color='blue', linewidth=0)
ax.glow_line(x, y, glow_color='cyan')
```

## Популярные комбинации

### Мягкое свечение с заливкой
```python
# Заливка
ax.gradient_plot(x, y, fill_color='blue', alpha_coef=0.2, linewidth=0)
# Мягкое свечение
ax.glow_line(x, y, glow_color='blue', glow_width=2.0, glow_alpha=0.5)
```

### Яркое неоновое свечение
```python
ax.set_facecolor('black')  # Тёмный фон
ax.gradient_plot(x, y, fill_color='cyan', alpha_coef=0.4, linewidth=0)
ax.glow_line(x, y, glow_color='cyan', glow_width=4.0, glow_alpha=0.9, 
             glow_layers=15, alpha_mode='gradient')
```

### Многослойные эффекты
```python
# Широкая заливка
ax.gradient_plot(x, y, fill_color='purple', alpha_coef=0.1, linewidth=0)
# Основное свечение
ax.glow_line(x, y, glow_color='magenta', glow_width=3.0, glow_alpha=0.6)
# Тонкое внутреннее свечение
ax.glow_line(x, y, glow_color='white', glow_width=1.0, glow_alpha=0.8, glow_layers=5)
```

## Комбинирование с другими методами

### Несколько линий
```python
# Данные
y1 = np.sin(x)
y2 = np.cos(x) + 0.5

# Первая линия
ax.gradient_plot(x, y1, fill_color='red', alpha_coef=0.3, linewidth=0)
ax.glow_line(x, y1, glow_color='red', glow_width=2.5)

# Вторая линия
ax.gradient_plot(x, y2, fill_color='blue', alpha_coef=0.3, linewidth=0)
ax.glow_line(x, y2, glow_color='blue', glow_width=2.5)
```

### С доверительными интервалами
```python
# Основная линия с эффектами
ax.gradient_plot(x, y_mean, fill_color='green', alpha_coef=0.4, linewidth=0)
ax.glow_line(x, y_mean, glow_color='green', glow_width=2.0)

# Доверительная область (если метод доступен)
ax.fill_between(x, y_mean - y_std, y_mean + y_std, alpha=0.2, color='green')
```

### С аннотациями
```python
# Эффекты
ax.gradient_plot(x, y, fill_color='orange', alpha_coef=0.3, linewidth=0)
main_line, glow_lines = ax.glow_line(x, y, glow_color='orange', glow_width=3.0)

# Аннотации
peak_idx = np.argmax(y)
ax.annotate(f'Максимум: {y[peak_idx]:.2f}', 
           xy=(x[peak_idx], y[peak_idx]),
           xytext=(10, 10), textcoords='offset points',
           bbox=dict(boxstyle='round,pad=0.3', facecolor='orange', alpha=0.7),
           arrowprops=dict(arrowstyle='->', color='orange'))
```

## Создание кастомных комбинированных методов

### Простой комбинированный метод
```python
@eplt.custom_axes_method("glow_gradient")
def glow_gradient(ax, x, y, color='cyan', **kwargs):
    """Комбинация gradient_plot + glow_line."""
    # Заливка
    line, grad = ax.gradient_plot(x, y, fill_color=color, 
                                 alpha_coef=0.3, linewidth=0)
    # Свечение
    main, glow = ax.glow_line(x, y, glow_color=color, 
                             glow_width=3.0, **kwargs)
    return {'gradient': (line, grad), 'glow': (main, glow)}

# Применить к классу
from eleganplot.utils.decorators import apply_custom_methods
apply_custom_methods(eplt.axes().__class__)

# Использовать
ax.glow_gradient(x, y, color='cyan', glow_alpha=0.8)
```

### Продвинутый метод с настройками
```python
@eplt.custom_axes_method("neon_plot")
def neon_plot(ax, x, y, color='cyan', intensity='medium', **kwargs):
    """Неоновый эффект с разными уровнями интенсивности."""
    
    settings = {
        'soft': {'grad_alpha': 0.2, 'glow_width': 2.0, 'glow_alpha': 0.5},
        'medium': {'grad_alpha': 0.4, 'glow_width': 3.0, 'glow_alpha': 0.7},
        'bright': {'grad_alpha': 0.6, 'glow_width': 4.0, 'glow_alpha': 0.9}
    }
    
    config = settings.get(intensity, settings['medium'])
    
    # Применяем эффекты
    ax.gradient_plot(x, y, fill_color=color, 
                    alpha_coef=config['grad_alpha'], linewidth=0)
    return ax.glow_line(x, y, glow_color=color,
                       glow_width=config['glow_width'],
                       glow_alpha=config['glow_alpha'],
                       **kwargs)
```

## Оптимизация производительности

### Для больших данных
```python
# Уменьшите количество шагов градиента
ax.gradient_plot(x, y, gradient_steps=50)  # вместо 100

# Уменьшите количество слоёв свечения  
ax.glow_line(x, y, glow_layers=8)  # вместо 10+
```

### Для интерактивных графиков
```python
# Используйте более простые эффекты
ax.gradient_plot(x, y, alpha_coef=0.3, linewidth=0)
ax.glow_line(x, y, glow_layers=6, glow_width=2.0)
```

## Примеры применения

### Научные графики
- Основная линия с доверительными интервалами
- Мягкое свечение для выделения трендов
- Градиентная заливка для области неопределённости

### Презентации
- Яркие неоновые эффекты на тёмном фоне
- Контрастные цвета для разных серий данных
- Комбинирование с аннотациями

### Художественная визуализация
- Многослойные эффекты с разными цветами
- Цветовые схемы (colormap) для свечения
- Экспериментальные комбинации эффектов

## Полезные советы

1. **Тестируйте на тёмном фоне**: `ax.set_facecolor('black')`
2. **Сохраняйте ссылки на объекты** для дальнейшего управления
3. **Используйте согласованную цветовую палитру**
4. **Экспериментируйте с параметрами** для достижения нужного эффекта
5. **Создавайте переиспользуемые методы** для часто используемых комбинаций

Смотрите `examples/combination_methods_example.py` для полных рабочих примеров!





