## {{ user.name }}
{% for badge in user.badges %}
![alt text](badges-img/{{ badges[badge.name].img }} "Earned {{ badge.earned_at }}: {{ badge.desc or badges[badge.name].shortDesc }}"){% endfor %}

