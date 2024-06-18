### {{ user.name }}
{% for badge in user.badges %}
<img src="badges-img/{{ badges[badge.name].img }}" title="Earned {{ badge.earned_at }}: {{ badge.desc or badges[badge.name].shortDesc }}" width="80">{% endfor %}

