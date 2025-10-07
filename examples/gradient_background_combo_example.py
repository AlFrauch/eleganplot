"""
Пример комбинирования gradient_subplots с другими методами EleganPlot.
"""

import numpy as np
import eleganplot as eplt

# Генерируем данные
x = np.linspace(0, 10, 100)
y1 = np.sin(x) * np.exp(-x/10)
y2 = np.cos(x) * np.exp(-x/10)

# Пример 1: Градиентный фон + gradient_fill
print("Создание графика: Градиентный фон + gradient_fill...")
fig, ax = eplt.gradient_subplots(
    figsize=(10, 6),
    dpi=200,
    gradient_colors=("#001020", "#002040"),
)

ax.gradient_fill(x, y1, fill_color='#00aaff', linewidth=2, label='sin(x) * exp(-x/10)')
ax.set_xlabel('X', fontsize=12)
ax.set_ylabel('Y', fontsize=12)
ax.set_title('Gradient Background + Gradient Fill', fontsize=14, pad=20)
ax.legend(fontsize=11)
ax.grid(True, alpha=0.2, linestyle='--')

eplt.savefig('examples/gradient_bg_with_fill.png', dpi=200, bbox_inches='tight')
print("✓ Сохранено: gradient_bg_with_fill.png")

# Пример 2: Градиентный фон + glow_line
print("Создание графика: Градиентный фон + glow_line...")
fig, ax = eplt.gradient_subplots(
    figsize=(10, 6),
    dpi=200,
    gradient_colors=("#0a0015", "#150030"),
)

main_line1, glow_lines1 = ax.glow_line(
    x, y1, 
    glow_color='cyan', 
    glow_width=6.0,
    glow_alpha=0.8,
    linewidth=2,
    label='sin(x) * exp(-x/10)'
)

main_line2, glow_lines2 = ax.glow_line(
    x, y2, 
    glow_color='magenta', 
    glow_width=6.0,
    glow_alpha=0.8,
    linewidth=2,
    label='cos(x) * exp(-x/10)'
)

ax.set_xlabel('X', fontsize=12)
ax.set_ylabel('Y', fontsize=12)
ax.set_title('Gradient Background + Glow Lines', fontsize=14, pad=20)
ax.legend(fontsize=11)
ax.grid(True, alpha=0.2, linestyle='--')

eplt.savefig('examples/gradient_bg_with_glow.png', dpi=200, bbox_inches='tight')
print("✓ Сохранено: gradient_bg_with_glow.png")

# Пример 3: Градиентный фон + confidence_band
print("Создание графика: Градиентный фон + confidence_band...")
y_mean = np.sin(x)
y_std = 0.15 * np.ones_like(x)

fig, ax = eplt.gradient_subplots(
    figsize=(10, 6),
    dpi=200,
    gradient_colors=("#001a00", "#003300"),
)

ax.confidence_band(x, y_mean, y_std, confidence=0.95, alpha=0.3, color='#00ff88')
ax.plot(x, y_mean, color='#00ff88', linewidth=2, label='Mean with 95% confidence')

ax.set_xlabel('X', fontsize=12)
ax.set_ylabel('Y', fontsize=12)
ax.set_title('Gradient Background + Confidence Band', fontsize=14, pad=20)
ax.legend(fontsize=11)
ax.grid(True, alpha=0.2, linestyle='--')

eplt.savefig('examples/gradient_bg_with_confidence.png', dpi=200, bbox_inches='tight')
print("✓ Сохранено: gradient_bg_with_confidence.png")

# Пример 4: Комбо всех эффектов
print("Создание графика: Комбинация всех эффектов...")
fig, ax = eplt.gradient_subplots(
    figsize=(12, 7),
    dpi=200,
    gradient_colors=("#0d001a", "#1a0033"),
)

# Доверительный интервал для фона
y_bg_mean = np.sin(x/2) * 0.5
y_bg_std = 0.1 * np.ones_like(x)
ax.confidence_band(x, y_bg_mean, y_bg_std, confidence=0.95, alpha=0.2, color='#666666')

# Основная линия с градиентной заливкой
ax.gradient_fill(x, y1, fill_color='#ff6b9d', linewidth=2, alpha_coef=0.6)

# Вторая линия с эффектом свечения
main_line, glow_lines = ax.glow_line(
    x, y2, 
    glow_color='#00ffff', 
    glow_width=5.0,
    glow_alpha=0.7,
    linewidth=2
)

ax.set_xlabel('X', fontsize=13)
ax.set_ylabel('Y', fontsize=13)
ax.set_title('Ultimate Combo: Gradient BG + Fill + Glow + Confidence', fontsize=15, pad=20)
ax.grid(True, alpha=0.15, linestyle='--')

eplt.savefig('examples/gradient_bg_ultimate_combo.png', dpi=200, bbox_inches='tight')
print("✓ Сохранено: gradient_bg_ultimate_combo.png")

print("\n✨ Все примеры комбинаций созданы успешно!")

