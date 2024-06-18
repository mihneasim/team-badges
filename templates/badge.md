{% macro badge_row(badge_left, badge_right) %}
| ![{{ badge_left.name }}](badges-img/{{ badge_left.img }} "{{ badge_left.shortDesc }}")  | **{{ badge_left.name }}** <br> {{ badge_left.desc }} | {% if badge_right %}![{{ badge_right.name }}](badges-img/{{ badge_right.img }} "{{ badge_left.shortDesc }}") | **{{ badge_right.name }}** {{ badge_right.desc }}  |{% else %} | |{% endif %}
{%- endmacro -%}
|  Badge | Description |  Badge | Description |
|---|----|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|{% for (badge_left, badge_right) in badge_tuples %}{{ badge_row(badge_left, badge_right) }}{% endfor %}
