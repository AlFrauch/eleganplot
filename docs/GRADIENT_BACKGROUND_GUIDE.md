# Руководство по использованию gradient_subplots

![Пример градиентного фона](images/test_gradient_bg.png)

## Описание

`gradient_subplots` - это функция для создания графиков с красивым градиентным фоном. Она создает фигуру с градиентом и возвращает ось с прозрачным фоном для построения графиков поверх градиента.

## Основное использование

```python
import eleganplot as eplt
import numpy as np

# Простое использование
fig, ax = eplt.gradient_subplots(dpi=200)
x = np.linspace(0, 10, 100)
y = np.sin(x)
ax.plot(x, y)
eplt.show()
```

## Параметры

### `figsize`
- **Тип:** `tuple[float, float]`
- **По умолчанию:** `(8, 5)`
- **Описание:** Размер фигуры (ширина, высота) в дюймах

```python
fig, ax = eplt.gradient_subplots(figsize=(10, 6))
```

### `dpi`
- **Тип:** `int | None`
- **По умолчанию:** `None`
- **Описание:** Разрешение фигуры в точках на дюйм

```python
fig, ax = eplt.gradient_subplots(dpi=200)
```

### `gradient_colors`
- **Тип:** `tuple[str, str]`
- **По умолчанию:** `("#00080a", "#042628")` - тёмный сине-зелёный градиент
- **Описание:** Цвета для градиента (начальный, конечный)

```python
# Фиолетовый градиент
fig, ax = eplt.gradient_subplots(gradient_colors=("#1a0033", "#330066"))

# Зелёный градиент
fig, ax = eplt.gradient_subplots(gradient_colors=("#002200", "#004400"))

# Синий градиент
fig, ax = eplt.gradient_subplots(gradient_colors=("#000033", "#001166"))
```

### `axes_position`
- **Тип:** `tuple[float, float, float, float]`
- **По умолчанию:** `(0.12, 0.12, 0.75, 0.75)`
- **Описание:** Позиция осей в формате `[left, bottom, width, height]` в относительных координатах от 0 до 1

```python
# Больше места для заголовка
fig, ax = eplt.gradient_subplots(axes_position=(0.15, 0.15, 0.7, 0.7))
```

### `nx` и `ny`
- **Тип:** `int`
- **По умолчанию:** `nx=512`, `ny=64`
- **Описание:** Разрешение градиента по горизонтали и вертикали

```python
# Более высокое разрешение градиента
fig, ax = eplt.gradient_subplots(nx=1024, ny=128)
```

## Примеры использования

### Пример 1: Базовый график

```python
import numpy as np
import eleganplot as eplt

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = eplt.gradient_subplots(dpi=200)
ax.plot(x, y, linewidth=2, label='sin(x)')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('График с градиентным фоном')
ax.legend()
ax.grid(True, alpha=0.3)
eplt.show()
```

### Пример 2: Несколько кривых с кастомными цветами

```python
import numpy as np
import eleganplot as eplt

x = np.linspace(0, 10, 100)

fig, ax = eplt.gradient_subplots(
    figsize=(10, 6),
    dpi=200,
    gradient_colors=("#1a0033", "#330066"),
)

ax.plot(x, np.sin(x), linewidth=2, label='sin(x)', color='#FF6B9D')
ax.plot(x, np.cos(x), linewidth=2, label='cos(x)', color='#FFA07A')
ax.plot(x, np.sin(x)*np.cos(x), linewidth=2, label='sin(x)*cos(x)', color='#98FB98')

ax.set_xlabel('X', fontsize=12)
ax.set_ylabel('Y', fontsize=12)
ax.set_title('Триганометрические функции', fontsize=14)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)
eplt.show()
```

![Пример с несколькими кривыми](images/gradien_bar.png)

### Пример 3: Затухающая синусоида с заливкой

```python
import numpy as np
import eleganplot as eplt

x = np.linspace(0, 10, 100)
y = np.exp(-x/5) * np.sin(2*x)

fig, ax = eplt.gradient_subplots(
    figsize=(8, 5),
    dpi=200,
    gradient_colors=("#002200", "#004400"),
)

ax.plot(x, y, linewidth=3, color='#00FF88', label='Затухающая синусоида')
ax.fill_between(x, y, alpha=0.3, color='#00FF88')

ax.set_xlabel('Время', fontsize=12)
ax.set_ylabel('Амплитуда', fontsize=12)
ax.set_title('Затухающая синусоида', fontsize=14)
ax.legend(fontsize=11)
ax.grid(True, alpha=0.2, linestyle='--')
eplt.show()
```

## Советы по выбору цветов

### Тёмные темы
Рекомендуется использовать два тёмных цвета для создания тонкого градиента:

- **Тёмный сине-зелёный:** `("#00080a", "#042628")` (по умолчанию)
- **Тёмный фиолетовый:** `("#1a0033", "#330066")`
- **Тёмный зелёный:** `("#002200", "#004400")`
- **Тёмный синий:** `("#000033", "#001166")`
- **Чёрно-серый:** `("#0a0a0a", "#1a1a1a")`

### Светлые темы
Также можно создавать светлые градиенты:

- **Светло-голубой:** `("#e6f2ff", "#b3d9ff")`
- **Светло-розовый:** `("#ffe6f0", "#ffb3d9")`
- **Светло-зелёный:** `("#e6ffe6", "#b3ffb3")`

## Комбинирование с другими методами EleganPlot

`gradient_subplots` хорошо сочетается с другими методами библиотеки:

```python
import eleganplot as eplt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

# Градиентный фон + метод gradient_fill
fig, ax = eplt.gradient_subplots(dpi=200, gradient_colors=("#001a33", "#003366"))
ax.gradient_fill(x, y, fill_color='#00aaff', linewidth=2)
ax.set_title('Комбинация gradient_subplots и gradient_fill')
eplt.show()
```

## Возвращаемые значения

Функция возвращает кортеж `(fig, ax)`:
- `fig` - объект `Figure` для управления фигурой
- `ax` - объект `EleganAxes` для построения графиков

```python
fig, ax = eplt.gradient_subplots()

# Работа с фигурой
fig.suptitle('Общий заголовок')

# Работа с осями
ax.plot([1, 2, 3], [1, 4, 2])
```

## Сохранение графиков

```python
fig, ax = eplt.gradient_subplots(dpi=200)
ax.plot(x, y)

# Сохранение с высоким качеством
eplt.savefig('my_plot.png', dpi=300, bbox_inches='tight')

# Или через объект фигуры
fig.savefig('my_plot.pdf', bbox_inches='tight')
```

