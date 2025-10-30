---
layout: home
title: CS 485/698 AI-Assisted Software Engineering (Sp26)
nav_exclude: true
permalink: /:path/
seo:
  type: Course
  name: CS 485/698 AI-Assisted Software Engineering (sp26)
---

<img id="course-banner" src="" alt="Course Banner" style="width:100%;" />

# CS 485: AI-Assisted Software Engineering

Modern generative artificial intelligence tools are astonishingly effective at generating code, given natural language specifications. The software engineering industry is rapidly adopting these tools to improve engineers’ productivity: instead of writing all of their code themselves, many engineers are now effectively “team leaders”, managing a “team” of artificial intelligence tools. In this course, students will get hands-on experience in using such artificial intelligence tools for software engineering in a semester-long course project. Topics will include agents, requirements elicitation and specification in the AI era, AI code generation and how to ensure that AI-generated code is correct, and discussions of how other traditional software engineering practices like code review and static analysis can help with AI-assisted software engineering.

<span style="color: red; font-size: 2em;"><strong>This website is under construction!</strong></span>

Any and all of its contents may change before the start of the spring semester.

The registrar is still working on scheduling this course. However, they have indicated to me
that it will _probably_ be scheduled Monday/Wednesday 11:30am-12:50pm.

When it is complete, the course website will consist of:
- the [syllabus](about.md),
- a [course calendar](calendar.md) (which includes links to the required readings),
- links to  [assignment descriptions](./projects),
- a [staff](staff.md) page, and
- useful [tutorials](tutorials.md).

{% raw %}
<script>
  document.addEventListener("DOMContentLoaded", function() {
    var bannerCount = 4;
    var randomIndex = Math.floor(Math.random() * bannerCount);
    var bannerImage = "assets/images/banner" + randomIndex + ".png";
    document.getElementById("course-banner").src = bannerImage;
  });
</script>
{% endraw %}
