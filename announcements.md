---
layout: page
title: Announcements
description: A feed containing all of the class announcements.
---

# Announcements

Announcements will be posted here and on CampusWire.

{% assign announcements = site.announcements | reverse %}
{% for announcement in announcements %}
{{ announcement }}
{% endfor %}
