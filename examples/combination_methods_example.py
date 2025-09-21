"""
Примеры комбинирования методов EleganPlot.

Демонстрирует, как одновременно использовать glow_line, gradient_plot 
и другие эффекты для создания сложных и красивых визуализаций.
"""

import numpy as np
import matplotlib.pyplot as plt
import eleganplot as eplt

def basic_combination():
    """Базовый пример комбинирования glow_line и gradient_plot."""
    print("🎨 Базовое комбинирование методов...")
    
    # Создаём данные
    x = np.linspace(0, 4*np.pi, 200)
    y1 = np.sin(x) * np.exp(-x/10)
    y2 = np.cos(x) * np.exp(-x/10) + 0.5
    
    fig, ax = eplt.subplots(figsize=(12, 8))
    ax.set_facecolor('black')
    ax.set_title('Комбинирование Glow Line + Gradient Plot', 
                fontsize=16, fontweight='bold', color='white')
    
    # Сначала gradient_plot для создания заливки
    line1, gradient1 = ax.gradient_plot(
        x, y1, 
        fill_color='cyan', 
        alpha_coef=0.3,
        gradient_steps=150,
        linewidth=0  # Скрываем основную линию gradient_plot
    )
    
    # Затем glow_line поверх для эффекта свечения
    main_line1, glow_lines1 = ax.glow_line(
        x, y1,
        glow_color='cyan',
        glow_width=3.0,
        glow_alpha=0.8,
        glow_layers=12,
        alpha_mode='gradient',
        linewidth=2
    )
    
    # Вторая линия с другими параметрами
    line2, gradient2 = ax.gradient_plot(
        x, y2,
        fill_color='orange',
        alpha_coef=0.4,
        gradient_steps=150,
        linewidth=0
    )
    
    main_line2, glow_lines2 = ax.glow_line(
        x, y2,
        glow_color='orange',
        colormap='plasma',
        glow_width=4.0,
        glow_alpha=0.7,
        glow_layers=15,
        alpha_mode='pulse',
        linewidth=2
    )
    
    ax.set_xlabel('X', color='white')
    ax.set_ylabel('Y', color='white')
    ax.grid(True, alpha=0.2)
    
    plt.tight_layout()
    plt.show()


def advanced_combination():
    """Продвинутый пример с несколькими эффектами."""
    print("🚀 Продвинутое комбинирование...")
    
    # Создаём более сложные данные
    x = np.linspace(0, 6*np.pi, 300)
    
    # Основная синусоида
    y_main = np.sin(x)
    
    # Высокочастотные колебания
    y_high = y_main + 0.2 * np.sin(10*x)
    
    # Огибающая
    y_envelope_upper = y_main + 0.5
    y_envelope_lower = y_main - 0.5
    
    fig, ax = eplt.subplots(figsize=(14, 10))
    ax.set_facecolor('#0a0a0a')
    ax.set_title('Сложная композиция эффектов', 
                fontsize=18, fontweight='bold', color='white')
    
    # 1. Градиентная заливка для области между огибающими
    ax.fill_between(x, y_envelope_lower, y_envelope_upper, 
                   alpha=0.1, color='purple')
    
    # 2. Gradient plot для основной функции
    line_main, gradient_main = ax.gradient_plot(
        x, y_main,
        fill_color='blue',
        alpha_coef=0.4,
        gradient_steps=200,
        linewidth=0
    )
    
    # 3. Glow line для основной функции с мягким свечением
    main_line, glow_lines = ax.glow_line(
        x, y_main,
        glow_color='blue',
        glow_width=2.5,
        glow_alpha=0.6,
        glow_layers=10,
        alpha_mode='uniform',
        linewidth=1.5
    )
    
    # 4. Glow line для высокочастотной составляющей
    high_main, high_glow = ax.glow_line(
        x, y_high,
        glow_color='cyan',
        colormap='plasma',
        glow_width=1.5,
        glow_alpha=0.8,
        glow_layers=8,
        alpha_mode='gradient',
        linewidth=1
    )
    
    # 5. Тонкие светящиеся линии для огибающих
    upper_line, upper_glow = ax.glow_line(
        x, y_envelope_upper,
        glow_color='yellow',
        glow_width=1.0,
        glow_alpha=0.4,
        glow_layers=6,
        linewidth=0.8,
        linestyle='--'
    )
    
    lower_line, lower_glow = ax.glow_line(
        x, y_envelope_lower,
        glow_color='yellow',
        glow_width=1.0,
        glow_alpha=0.4,
        glow_layers=6,
        linewidth=0.8,
        linestyle='--'
    )
    
    ax.set_xlabel('X', color='white', fontsize=14)
    ax.set_ylabel('Y', color='white', fontsize=14)
    ax.grid(True, alpha=0.2, color='gray')
    
    plt.tight_layout()
    plt.show()


def interactive_combination():
    """Пример с разными настройками для экспериментов."""
    print("🎛️ Интерактивный пример...")
    
    x = np.linspace(0, 3*np.pi, 150)
    
    # Создаём сетку субплотов для сравнения
    fig, axes = eplt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle('Различные комбинации эффектов', fontsize=16, fontweight='bold')
    
    # Настройки для каждого субплота
    configs = [
        {
            'title': 'Glow + Gradient (мягкий)',
            'y_func': lambda x: np.sin(x),
            'gradient_alpha': 0.3,
            'glow_alpha': 0.5,
            'glow_width': 2.0,
            'color': 'cyan'
        },
        {
            'title': 'Glow + Gradient (яркий)',
            'y_func': lambda x: np.cos(x) + 0.5,
            'gradient_alpha': 0.6,
            'glow_alpha': 0.9,
            'glow_width': 4.0,
            'color': 'orange'
        },
        {
            'title': 'Многослойное свечение',
            'y_func': lambda x: np.sin(2*x) * 0.8,
            'gradient_alpha': 0.2,
            'glow_alpha': 0.7,
            'glow_width': 3.5,
            'color': 'magenta'
        },
        {
            'title': 'Цветовая схема',
            'y_func': lambda x: np.cos(3*x) * 0.6 - 0.5,
            'gradient_alpha': 0.4,
            'glow_alpha': 0.8,
            'glow_width': 3.0,
            'color': 'green'
        }
    ]
    
    for i, config in enumerate(configs):
        ax = axes[i // 2, i % 2]
        ax.set_facecolor('#1a1a1a')
        
        y = config['y_func'](x)
        
        # Gradient plot
        line, gradient = ax.gradient_plot(
            x, y,
            fill_color=config['color'],
            alpha_coef=config['gradient_alpha'],
            gradient_steps=100,
            linewidth=0
        )
        
        # Glow line
        main_line, glow_lines = ax.glow_line(
            x, y,
            glow_color=config['color'],
            glow_width=config['glow_width'],
            glow_alpha=config['glow_alpha'],
            glow_layers=12,
            alpha_mode='gradient' if i % 2 == 0 else 'pulse',
            colormap='viridis' if i == 3 else None,
            linewidth=2
        )
        
        ax.set_title(config['title'], fontsize=12, fontweight='bold')
        ax.grid(True, alpha=0.2)
    
    plt.tight_layout()
    plt.show()


def create_custom_combined_method():
    """Создаём собственный метод, комбинирующий эффекты."""
    print("🛠️ Создание кастомного комбинированного метода...")
    
    @eplt.custom_axes_method("glow_gradient_plot")
    def glow_gradient_plot(ax, x, y, 
                          color='cyan',
                          gradient_alpha=0.4,
                          glow_alpha=0.7,
                          glow_width=3.0,
                          glow_layers=12,
                          **kwargs):
        """
        Комбинированный метод: gradient_plot + glow_line в одном вызове.
        
        Parameters
        ----------
        ax : EleganAxes
            Оси для построения
        x, y : array-like
            Координаты данных
        color : str
            Основной цвет эффектов
        gradient_alpha : float
            Прозрачность градиентной заливки
        glow_alpha : float
            Прозрачность свечения
        glow_width : float
            Ширина свечения
        glow_layers : int
            Количество слоев свечения
        **kwargs
            Дополнительные параметры для основной линии
        """
        # Сначала gradient_plot
        line, gradient = ax.gradient_plot(
            x, y,
            fill_color=color,
            alpha_coef=gradient_alpha,
            gradient_steps=150,
            linewidth=0
        )
        
        # Затем glow_line
        main_line, glow_lines = ax.glow_line(
            x, y,
            glow_color=color,
            glow_width=glow_width,
            glow_alpha=glow_alpha,
            glow_layers=glow_layers,
            alpha_mode='gradient',
            **kwargs
        )
        
        return {
            'gradient_line': line,
            'gradient_fill': gradient,
            'main_line': main_line,
            'glow_lines': glow_lines
        }
    
    # Применяем метод к классу
    from eleganplot.utils.decorators import apply_custom_methods
    apply_custom_methods(eplt.axes().__class__)
    
    # Используем новый метод
    fig, ax = eplt.subplots(figsize=(12, 8))
    ax.set_facecolor('black')
    ax.set_title('Кастомный комбинированный метод', 
                fontsize=16, fontweight='bold', color='white')
    
    x = np.linspace(0, 4*np.pi, 200)
    y1 = np.sin(x) * np.exp(-x/8)
    y2 = np.cos(x) * np.exp(-x/8) + 1
    
    # Используем наш новый метод!
    result1 = ax.glow_gradient_plot(
        x, y1, 
        color='cyan',
        gradient_alpha=0.3,
        glow_alpha=0.8,
        glow_width=3.5,
        linewidth=2
    )
    
    result2 = ax.glow_gradient_plot(
        x, y2,
        color='orange', 
        gradient_alpha=0.4,
        glow_alpha=0.6,
        glow_width=2.5,
        linewidth=1.5
    )
    
    ax.set_xlabel('X', color='white')
    ax.set_ylabel('Y', color='white')
    ax.grid(True, alpha=0.2)
    
    plt.tight_layout()
    plt.show()
    
    print("✅ Кастомный метод 'glow_gradient_plot' создан и применён!")


def main():
    """Запуск всех примеров."""
    print("🎨 Демонстрация комбинирования методов EleganPlot\n")
    
    try:
        basic_combination()
        print()
        
        advanced_combination()
        print()
        
        interactive_combination()
        print()
        
        create_custom_combined_method()
        print()
        
        print("🎉 Все примеры выполнены успешно!")
        print("\n📝 Ключевые принципы комбинирования:")
        print("  1. gradient_plot создаёт заливку (linewidth=0 чтобы скрыть линию)")
        print("  2. glow_line добавляет эффект свечения поверх")
        print("  3. Можно комбинировать любые методы на одних осях")
        print("  4. Порядок вызовов влияет на z-order (что поверх чего)")
        print("  5. Создавайте кастомные методы для часто используемых комбинаций")
        
    except Exception as e:
        print(f"❌ Ошибка при выполнении примеров: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
