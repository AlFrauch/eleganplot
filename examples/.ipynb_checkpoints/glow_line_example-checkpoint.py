"""
Примеры использования функции свечения линии в EleganPlot.

Этот скрипт демонстрирует различные возможности функции glow_line:
- Базовое свечение
- Настройка цвета и ширины свечения
- Различные функции затухания
- Режимы изменения прозрачности
- Цветовые схемы
"""

import numpy as np
import matplotlib.pyplot as plt
import sys
import os

# Добавляем путь к пакету eleganplot
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import eleganplot
from eleganplot.utils import get_decay_functions


def basic_glow_example():
    """Базовый пример свечения линии."""
    fig, axes = eleganplot.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('Базовые примеры свечения линии', fontsize=16, fontweight='bold')
    
    x = np.linspace(0, 4*np.pi, 200)
    y = np.sin(x) * np.exp(-x/10)
    
    # Простое свечение
    axes[0, 0].glow_line(x, y, glow_color='cyan', glow_width=3.0, glow_alpha=0.6)
    axes[0, 0].set_title('Простое свечение')
    axes[0, 0].set_facecolor('black')
    
    # Широкое свечение
    axes[0, 1].glow_line(x, y, glow_color='orange', glow_width=8.0, glow_alpha=0.4, glow_layers=15)
    axes[0, 1].set_title('Широкое свечение')
    axes[0, 1].set_facecolor('black')
    
    # Яркое свечение
    axes[1, 0].glow_line(x, y, glow_color='lime', glow_width=4.0, glow_alpha=0.8, glow_layers=20)
    axes[1, 0].set_title('Яркое свечение')
    axes[1, 0].set_facecolor('black')
    
    # Мягкое свечение
    axes[1, 1].glow_line(x, y, glow_color='magenta', glow_width=6.0, glow_alpha=0.3, glow_layers=25)
    axes[1, 1].set_title('Мягкое свечение')
    axes[1, 1].set_facecolor('black')
    
    plt.tight_layout()
    plt.show()


def decay_functions_example():
    """Пример различных функций затухания."""
    fig, axes = eleganplot.subplots(2, 3, figsize=(15, 10))
    fig.suptitle('Функции затухания свечения', fontsize=16, fontweight='bold')
    
    x = np.linspace(0, 2*np.pi, 150)
    y = np.sin(2*x) * np.cos(x)
    
    # Получаем доступные функции затухания
    decay_funcs = get_decay_functions()
    
    func_names = ['linear', 'exponential', 'gaussian', 'quadratic', 'cubic', 'sine']
    
    for i, func_name in enumerate(func_names):
        row, col = i // 3, i % 3
        axes[row, col].glow_line(
            x, y, 
            glow_color='cyan',
            glow_width=5.0,
            glow_alpha=0.6,
            decay_function=decay_funcs[func_name],
            glow_layers=15
        )
        axes[row, col].set_title(f'Затухание: {func_name}')
        axes[row, col].set_facecolor('black')
    
    plt.tight_layout()
    plt.show()


def alpha_modes_example():
    """Пример различных режимов изменения прозрачности."""
    fig, axes = eleganplot.subplots(1, 3, figsize=(15, 5))
    fig.suptitle('Режимы изменения прозрачности', fontsize=16, fontweight='bold')
    
    x = np.linspace(0, 3*np.pi, 200)
    y = np.sin(x) + 0.3*np.sin(5*x)
    
    modes = ['uniform', 'gradient', 'pulse']
    colors = ['red', 'green', 'blue']
    
    for i, (mode, color) in enumerate(zip(modes, colors)):
        axes[i].glow_line(
            x, y,
            glow_color=color,
            glow_width=4.0,
            glow_alpha=0.7,
            alpha_mode=mode,
            glow_layers=12
        )
        axes[i].set_title(f'Режим: {mode}')
        axes[i].set_facecolor('black')
    
    plt.tight_layout()
    plt.show()


def colormap_example():
    """Пример использования цветовых схем."""
    fig, axes = eleganplot.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('Цветовые схемы свечения', fontsize=16, fontweight='bold')
    
    x = np.linspace(0, 4*np.pi, 250)
    y = np.sin(x) * np.exp(-x/15)
    
    colormaps = ['plasma', 'viridis', 'inferno', 'magma']
    
    for i, cmap in enumerate(colormaps):
        row, col = i // 2, i % 2
        axes[row, col].glow_line(
            x, y,
            colormap=cmap,
            glow_width=6.0,
            glow_alpha=0.8,
            glow_layers=20
        )
        axes[row, col].set_title(f'Цветовая схема: {cmap}')
        axes[row, col].set_facecolor('black')
    
    plt.tight_layout()
    plt.show()


def custom_decay_example():
    """Пример пользовательской функции затухания."""
    fig, axes = eleganplot.subplots(1, 3, figsize=(15, 5))
    fig.suptitle('Пользовательские функции затухания', fontsize=16, fontweight='bold')
    
    x = np.linspace(0, 2*np.pi, 150)
    y = np.sin(3*x) * np.cos(x/2)
    
    # Различные пользовательские функции затухания
    custom_functions = [
        lambda r: np.exp(-10 * r**4),  # Очень резкое затухание
        lambda r: 1 / (1 + 5*r**2),   # Лоренцевское затухание
        lambda r: np.cos(np.pi * r / 2)**2  # Косинусоидальное затухание
    ]
    
    names = ['Резкое', 'Лоренцевское', 'Косинусоидальное']
    colors = ['yellow', 'orange', 'red']
    
    for i, (func, name, color) in enumerate(zip(custom_functions, names, colors)):
        axes[i].glow_line(
            x, y,
            glow_color=color,
            glow_width=5.0,
            glow_alpha=0.7,
            decay_function=func,
            glow_layers=15
        )
        axes[i].set_title(f'{name} затухание')
        axes[i].set_facecolor('black')
    
    plt.tight_layout()
    plt.show()


def complex_example():
    """Комплексный пример с несколькими линиями."""
    fig, ax = eleganplot.subplots(figsize=(12, 8))
    ax.set_title('Комплексный пример свечения', fontsize=16, fontweight='bold')
    ax.set_facecolor('black')
    
    x = np.linspace(0, 4*np.pi, 300)
    
    # Несколько функций с разными параметрами свечения
    functions = [
        (np.sin(x), 'cyan', 'plasma', 'exponential'),
        (np.cos(x) + 0.5, 'orange', 'viridis', 'gaussian'),
        (np.sin(2*x) * 0.5 - 1, 'magenta', 'inferno', 'linear'),
    ]
    
    decay_funcs = get_decay_functions()
    
    for i, (y, color, cmap, decay_name) in enumerate(functions):
        ax.glow_line(
            x, y,
            glow_color=color,
            colormap=cmap,
            glow_width=4.0 + i,
            glow_alpha=0.6,
            decay_function=decay_funcs[decay_name],
            glow_layers=15,
            alpha_mode='gradient'
        )
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    print("Запуск примеров свечения линии...")
    print("Закройте каждое окно, чтобы перейти к следующему примеру.")
    
    basic_glow_example()
    decay_functions_example()
    alpha_modes_example()
    colormap_example()
    custom_decay_example()
    complex_example()
    
    print("Все примеры завершены!")
