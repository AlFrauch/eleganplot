"""
Пример использования gradient_subplots для создания графиков с градиентным фоном.
"""

import numpy as np
import eleganplot as eplt

# Генерируем данные
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Простое использование с настройками по умолчанию
fig, ax = eplt.gradient_subplots(dpi=200)
ax.plot(x, y, linewidth=2, label='sin(x)')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('График с градиентным фоном')
ax.legend()
ax.grid(True, alpha=0.3)

eplt.savefig('examples/gradient_background_default.png', dpi=200, bbox_inches='tight')
eplt.show()

# Пример с кастомными цветами градиента
fig, ax = eplt.gradient_subplots(
    figsize=(10, 6),
    dpi=200,
    gradient_colors=("#1a0033", "#330066"),  # Фиолетовый градиент
)

# Рисуем несколько кривых
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) * np.cos(x)

ax.plot(x, y1, linewidth=2, label='sin(x)', color='#FF6B9D')
ax.plot(x, y2, linewidth=2, label='cos(x)', color='#FFA07A')
ax.plot(x, y3, linewidth=2, label='sin(x)*cos(x)', color='#98FB98')

ax.set_xlabel('X', fontsize=12)
ax.set_ylabel('Y', fontsize=12)
ax.set_title('Триганометрические функции на градиентном фоне', fontsize=14)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

eplt.savefig('examples/gradient_background_custom.png', dpi=200, bbox_inches='tight')
eplt.show()

# Пример с другими цветами (зелёный градиент)
fig, ax = eplt.gradient_subplots(
    figsize=(8, 5),
    dpi=200,
    gradient_colors=("#002200", "#004400"),
    axes_position=(0.15, 0.15, 0.7, 0.7),  # Кастомная позиция осей
)

# Экспоненциальный график
y = np.exp(-x/5) * np.sin(2*x)
ax.plot(x, y, linewidth=3, color='#00FF88', label='Затухающая синусоида')
ax.fill_between(x, y, alpha=0.3, color='#00FF88')

ax.set_xlabel('Время', fontsize=12)
ax.set_ylabel('Амплитуда', fontsize=12)
ax.set_title('Затухающая синусоида', fontsize=14, pad=20)
ax.legend(fontsize=11)
ax.grid(True, alpha=0.2, linestyle='--')

eplt.savefig('examples/gradient_background_green.png', dpi=200, bbox_inches='tight')
eplt.show()

print("✓ Примеры графиков с градиентным фоном созданы успешно!")

