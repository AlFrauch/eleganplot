#!/usr/bin/env python3
"""
Быстрая демонстрация gradient_subplots
"""

import sys
sys.path.insert(0, 'src')  # Для работы без установки

import numpy as np
import eleganplot as eplt

print("🎨 Демонстрация gradient_subplots")
print("=" * 50)

# Генерируем данные
x = np.linspace(0, 10, 100)
y = np.sin(x)

print("\n1. Создание графика с градиентным фоном...")
fig, ax = eplt.gradient_subplots(dpi=150)
ax.plot(x, y, linewidth=2, label='sin(x)', color='#00aaff')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Demo: Gradient Background')
ax.legend()
ax.grid(True, alpha=0.3)
print("   ✓ График создан")

# Сохраняем
output_file = 'examples/demo_output.png'
fig.savefig(output_file, dpi=150, bbox_inches='tight')
print(f"   ✓ Сохранено в: {output_file}")

print("\n2. Параметры вызова:")
print("   fig, ax = eplt.gradient_subplots(dpi=150)")

print("\n3. Возвращаемые значения:")
print(f"   fig: {type(fig).__name__}")
print(f"   ax:  {type(ax).__name__}")

print("\n4. Кастомные цвета:")
fig2, ax2 = eplt.gradient_subplots(
    gradient_colors=("#1a0033", "#330066"),
    figsize=(8, 5)
)
ax2.plot(x, y, linewidth=2, color='#FF6B9D')
ax2.set_title('Demo: Custom Colors (Purple)')
print("   ✓ Фиолетовый градиент создан")

print("\n" + "=" * 50)
print("✨ Демонстрация завершена успешно!")
print("\nДля просмотра всех примеров:")
print("  python examples/gradient_background_example.py")
print("  python examples/gradient_background_combo_example.py")

