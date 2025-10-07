# Быстрый старт: gradient_subplots

![Примеры gradient_subplots](images/Simple.png)

## Базовое использование

```python
import eleganplot as eplt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

# Создание фигуры с градиентным фоном
fig, ax = eplt.gradient_subplots(dpi=200)
ax.plot(x, y)
eplt.show()
```

## Кастомизация цветов

```python
# Фиолетовый градиент
fig, ax = eplt.gradient_subplots(
    gradient_colors=("#1a0033", "#330066")
)

# Зелёный градиент
fig, ax = eplt.gradient_subplots(
    gradient_colors=("#002200", "#004400")
)

# Синий градиент
fig, ax = eplt.gradient_subplots(
    gradient_colors=("#000033", "#001166")
)
```

## Все параметры

```python
fig, ax = eplt.gradient_subplots(
    figsize=(10, 6),           # Размер фигуры
    dpi=200,                   # Разрешение
    gradient_colors=(...),     # Цвета градиента
    axes_position=(0.12, 0.12, 0.75, 0.75),  # Позиция осей
    nx=512,                    # Разрешение градиента по X
    ny=64,                     # Разрешение градиента по Y
)
```

## Комбинация с другими методами

```python
# С gradient_fill
fig, ax = eplt.gradient_subplots(gradient_colors=("#001020", "#002040"))
ax.gradient_fill(x, y, fill_color='#00aaff')

# С glow_line
fig, ax = eplt.gradient_subplots(gradient_colors=("#0a0015", "#150030"))
ax.glow_line(x, y, glow_color='cyan', glow_width=6.0)

# С confidence_band
fig, ax = eplt.gradient_subplots(gradient_colors=("#001a00", "#003300"))
ax.confidence_band(x, y, y_std, confidence=0.95)
```

## Готовые цветовые схемы

| Название | Цвета | Описание |
|----------|-------|----------|
| **Тёмный сине-зелёный** | `("#00080a", "#042628")` | По умолчанию |
| **Фиолетовый** | `("#1a0033", "#330066")` | Для презентаций |
| **Зелёный** | `("#002200", "#004400")` | Природная тема |
| **Синий** | `("#000033", "#001166")` | Классический |
| **Чёрно-серый** | `("#0a0a0a", "#1a1a1a")` | Минималистичный |

