"""
Пример использования кастомных методов EleganPlot.

Демонстрирует новую систему расширения с gradient_plot и другими методами.
"""

import numpy as np
import eleganplot as eplt

# Создаём данные для примеров
x = np.linspace(0, 4 * np.pi, 100)
y1 = np.sin(x) * np.exp(-x/8)
y2 = np.cos(x) * np.exp(-x/8)
y3 = np.sin(x/2) + 0.1 * np.random.randn(100)

# Пример 1: Градиентная заливка
fig, axes = eplt.subplots(2, 2, figsize=(12, 8))

# Простой gradient_plot
axes[0, 0].gradient_plot(x, y1, fill_color='blue', alpha_coef=0.8)
axes[0, 0].set_title('Gradient Plot - Синий градиент')

# Gradient_plot с кастомными параметрами
axes[0, 1].gradient_plot(x, y2, fill_color='red', alpha_coef=0.6, 
                        gradient_to_min=True, gradient_steps=50)
axes[0, 1].set_title('Gradient Plot - Красный до минимума')

# Несколько линий
axes[1, 0].multi_line(x, [y1, y2], 
                     labels=['Sin', 'Cos'], 
                     colors=['purple', 'orange'])
axes[1, 0].set_title('Multi Line Plot')

# Доверительная полоса (если scipy доступна)
try:
    y_mean = np.sin(x/2)
    y_std = np.abs(0.2 * np.sin(x))
    axes[1, 1].confidence_band(x, y_mean, y_std, confidence=0.95)
    axes[1, 1].set_title('Confidence Band')
except ImportError:
    # Fallback если scipy недоступна
    axes[1, 1].plot(x, y3)
    axes[1, 1].set_title('Simple Plot (scipy not available)')

plt.tight_layout()
plt.show()

# Пример 2: Создание собственного кастомного метода
@eplt.custom_axes_method("rainbow_plot")
def rainbow_plot(ax, x, y, **kwargs):
    """Создаёт линию с радужными цветами."""
    import matplotlib.pyplot as plt
    from matplotlib.colors import rainbow
    
    # Разбиваем данные на сегменты
    n_segments = len(x) - 1
    colors = rainbow(np.linspace(0, 1, n_segments))
    
    lines = []
    for i in range(n_segments):
        x_seg = x[i:i+2]
        y_seg = y[i:i+2]
        line = ax._ax.plot(x_seg, y_seg, color=colors[i], **kwargs)[0]
        lines.append(line)
    
    return lines

# Применяем новый метод к классу
from eleganplot.utils.decorators import apply_custom_methods
apply_custom_methods(eplt.axes().__class__)

# Используем новый метод
fig, ax = eplt.subplots()
x_rainbow = np.linspace(0, 2*np.pi, 50)
y_rainbow = np.sin(x_rainbow)

ax.rainbow_plot(x_rainbow, y_rainbow, linewidth=3)
ax.set_title('Кастомный Rainbow Plot')
plt.show()

print("Доступные кастомные методы:")
for name, description in eplt.method_registry.list_methods().items():
    print(f"  {name}: {description}")
