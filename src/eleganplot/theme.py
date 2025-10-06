from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Mapping

import matplotlib as mpl
from matplotlib import cycler


@dataclass
class Theme:
    """Описывает визуальную тему EleganPlot.

    Параметры задают цвета и базовые параметры Matplotlib для единого стиля.
    """

    name: str
    background_color: str
    axes_facecolor: str
    grid_color: str
    text_color: str
    palette: List[str] = field(default_factory=list)
    font_family: str = "DejaVu Sans"
    grid_alpha: float = 0.25
    # Дополнительные rcParams для тонкой настройки темы
    extra_rc: Dict[str, object] = field(default_factory=dict)

    def rcparams(self) -> Dict[str, object]:
        """Возвращает словарь rcParams для применения темы."""
        params = {
            "figure.facecolor": self.background_color,
            "axes.facecolor": self.axes_facecolor,
            "savefig.facecolor": self.background_color,
            "axes.edgecolor": self.text_color,
            "axes.labelcolor": self.text_color,
            "axes.titlecolor": self.text_color,
            "xtick.color": self.text_color,
            "ytick.color": self.text_color,
            "text.color": self.text_color,
            "grid.color": self.grid_color,
            "grid.alpha": self.grid_alpha,
            "axes.grid": True,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "font.family": self.font_family,
        }
        if self.palette:
            params["axes.prop_cycle"] = cycler(color=self.palette)
        # Переопределения специфичных rc-параметров темы
        if self.extra_rc:
            params.update(self.extra_rc)
        return params


ELEGAN_DARK = Theme(
    name="EleganDark",
    background_color="#1b1f24",
    axes_facecolor="#242a31",
    grid_color="#3e4c59",
    text_color="#e6edf3",
    palette=["#8fd3f4", "#f78fb3", "#a8e6cf", "#ffd3b6", "#c4a7e7"],
)

ELEGAN_LIGHT = Theme(
    name="EleganLight",
    background_color="#ffffff",
    axes_facecolor="#f7f7f9",
    grid_color="#c7c9d1",
    text_color="#1f2328",
    palette=["#005f73", "#ae2012", "#0a9396", "#ee9b00", "#6a4c93"],
)


MIDNIGHT = Theme(
    name="Midnight",
    background_color="#0e1116",
    axes_facecolor="#151a21",
    grid_color="#2b3440",
    text_color="#e6edf3",
    palette=["#64b5f6", "#ff8a65", "#81c784", "#ffd54f", "#ba68c8"],
)


FRAUCH = Theme(
    name="Frauch",
    background_color="#2a2d31",
    axes_facecolor="#2a2d31",
    grid_color="#3e4c59",
    text_color="#787878",
    palette=[],
    extra_rc={"text.usetex": True},
)


FRAUCH_NEW = Theme(
    name="Frauch",
    background_color="#000c16",
    axes_facecolor="#000c16",
    grid_color="#a9bac9",
    text_color="#787878",
    palette=[],
    extra_rc={"text.usetex": True},
)


THEMES: Mapping[str, Theme] = {
    "dark": ELEGAN_DARK,
    "light": ELEGAN_LIGHT,
    "midnight": MIDNIGHT,
    "frauch": FRAUCH,
    # Пользовательские и дополнительные темы
}


_CURRENT_THEME: Theme = FRAUCH_NEW


def set_current_theme(theme: Theme | str) -> Theme:
    """Устанавливает текущую тему.

    Принимает инстанс `Theme` или строку: ключ из `list_themes()`.
    Возвращает применённую тему.
    """

    global _CURRENT_THEME
    if isinstance(theme, str):
        lower = theme.lower()
        if lower in {"elegandark", "default"}:
            lower = "dark"
        if lower in THEMES:
            _CURRENT_THEME = THEMES[lower]
        else:
            raise ValueError(f"Неизвестная тема: {theme}")
    else:
        _CURRENT_THEME = theme
    apply_theme(_CURRENT_THEME)
    return _CURRENT_THEME


def get_current_theme() -> Theme:
    return _CURRENT_THEME


def apply_theme(theme: Theme | None = None) -> Theme:
    """Применяет `rcParams` выбранной темы."""
    selected = theme or _CURRENT_THEME
    mpl.rcParams.update(selected.rcparams())
    return selected


def list_themes() -> List[str]:
    """Возвращает список ключей доступных тем."""
    return list(THEMES.keys())


