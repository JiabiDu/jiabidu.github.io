---
permalink: /
title: "Welcome to the Coastal Ocean & Robotics Lab"
author_profile: false
---

<div style="display: flex; flex-wrap: wrap; gap: 30px; align-items: flex-start; margin-bottom: 40px;">

  <div style="flex: 2; min-width: 300px;">
    <h2>We develop and use advanced technologies to explore the frontiers of ocean science!</h2>
    <p>We study the physical and biogeochemical processes in coastal, shelf, and deep oceans. Our work integrates long-term monitoring data with multi-scale modeling systems to capture critical interactions between the climate and the ocean.</p>
    <p>As the climate changes and extreme weather events become more frequent, the resiliency of coastal ecosystems and communities is increasingly threatened. Our lab investigates how these climate events reshape coastal ocean dynamics, linking physical processes to pressing environmental issues.</p>
  </div>

  <div style="flex: 1; min-width: 250px; background-color: #f8f9fa; border-radius: 12px; padding: 20px; border-left: 4px solid #004a99;">
    <h3 style="margin-top: 0; border-bottom: 2px solid #004a99; padding-bottom: 5px;">
      <i class="fas fa-rss"></i> Latest News
    </h3>
    <ul style="list-style-type: none; padding-left: 0; font-size: 0.9rem;">
      {% for item in site.data.news limit:5 %}
      <li style="margin-bottom: 12px; border-bottom: 1px solid #eee; padding-bottom: 8px;">
        <strong style="color: #004a99; font-size: 0.8rem;">{{ item.date }}</strong><br>
        {{ item.text }}
      </li>
      {% endfor %}
    </ul>
  </div>
</div>

<hr>

## Why Numerical Modeling? 
![particle tracking simulations](/images/ptrack_galveston_d31.gif)
Numerical models are the most effective tools for providing a synoptic, three-dimensional view of oceanographic processes. They allow us to integrate sparse in-situ measurements and satellite data into a mathematically consistent 3D environment. Furthermore, numerical models are the only means by which we can predict future conditions and conduct large-scale "what-if" experiments to understand our changing planet.

## Why Marine Robots?
![robot deployment](/movies/robot01.mp4)
Reliable scientific discovery depends on consistent observation. Marine robots are becoming essential for exploring our oceans, particularly during extreme weather events like hurricanes when conditions are too dangerous for traditional research vessels. Our lab is engineering cost-efficient, versatile autonomous vehicles designed to transform the future of coastal water surveys and ensure data continuity in the harshest environments.