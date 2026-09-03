---
layout: page
title: Office Hours
permalink: /office-hours/
nav_order: 8
description: A weekly calendar of course staff office hours.
---

<!--
  This page is generated from the `office_hours:` front matter in _staffers/*.md.
  Do not type times or locations here: edit the staffer's file and both this page
  and the staff page update together.
-->

# Weekly Office Hours

Sections are coordinated, so **you may attend any staff member's office
hours regardless of which section you are enrolled in** --- go to whichever slot below fits
your schedule. Office hours are the fastest way to get in-person help, and we expect you to have tried
them (and Discord) before asking for an appointment.

The three instructors are also available by appointment; see the
[staff page]({{ site.baseurl }}{% link staff.md %}) for how to schedule one.

{% assign week = 'Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday' | split: ',' %}
{% for day in week %}
{%- assign encoded = '' -%}
{%- for staffer in site.staffers -%}
{%- for oh in staffer.office_hours -%}
{%- if oh.day == day -%}
{%- capture start_minutes %}{% include minutes.liquid time=oh.start %}{% endcapture -%}
{%- capture sort_key %}000{{ start_minutes | strip }}{% endcapture -%}
{%- assign sort_key = sort_key | slice: -4, 4 -%}
{%- capture entry -%}
{{ sort_key }}~{{ oh.start }}~{{ oh.end }}~{{ staffer.name }}~{{ staffer.role }}~{{ oh.location | default: 'TBD' }}
{%- endcapture -%}
{%- assign encoded = encoded | append: entry | append: '|' -%}
{%- endif -%}
{%- endfor -%}
{%- endfor -%}
{%- if encoded != '' -%}
{%- assign slots = encoded | split: '|' | sort -%}
## {{ day }}

| Time | Staff member | Role | Location |
|:-----|:-------------|:-----|:---------|
{% for slot in slots -%}
{%- assign f = slot | split: '~' -%}
| {{ f[1] }}&ndash;{{ f[2] }} | {{ f[3] }} | {{ f[4] }} | {% if f[5] == 'TBD' %}TBD{% else %}{{ f[5] }}{% endif %} |
{% endfor %}
{% endif -%}
{%- endfor %}

Times are Eastern. Locations marked TBD have not been assigned yet; they will be filled in
here as soon as we have them.
