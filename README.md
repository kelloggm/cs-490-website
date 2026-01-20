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

The course meets on Mondays and Wednesdays at 11:30am. The course is open to students at all levels:
bachelor's, master's, and PhD. Graduate students will be expected to engage with current research in the
topic; see [this description](https://kelloggm.github.io//martinjkellogg.com/teaching/cs485-sp26/about/#bs-vs-msphd-students) in the syllabus for the specific requirements for graduate students.

On this website, you can find:
- the [syllabus](about.md),
- a [course calendar](calendar.md) (which includes links to the required readings and all assignment due dates),
- links to assignment descriptions for the [course project](./projects) and [individual reflection essays](./assignments),
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
