---
title: "Marine Robot Development"
layout: single
permalink: /research/marine_robot/
author_profile: false
toc: true
---

## Overview
![robot deployment](/movies/robot01.mp4)
**What happens in the water during a storm?**

Traditional research vessels are often restricted by dangerous conditions during extreme weather events. To address this gap in observational data, our lab is developing autonomous marine robots designed to operate in harsh coastal environments. These vehicles serve as versatile platforms, carrying scientific instruments to conduct high-resolution surveys along predefined paths.

## 01. Design & Engineering
Our primary focus is the development of an **Autonomous Surface Vehicle (ASV)**. The design prioritizes durability and precision navigation.


**Key Design Features:**
* **High Buoyancy:** Optimized hull design for stability at the air-sea interface.
* **Redundant Waterproofing:** Robust enclosures to protect the onboard control systems and electronics.
* **Dual-Thruster Propulsion:** Differential steering using two underwater thrusters for precise maneuvering, including forward, reverse, and rapid turns.
* **Autonomous Navigation:** Integrated GPS and flight-controller systems for waypoint-based missions.

## 02. Development and Testing
The development process follows a rigorous "step-by-step" testing protocol, moving from small controlled tanks to large-scale facilities and, finally, open-water environments. The following video provides a look at our prototyping and testing phases:

<div style="text-align: center; margin: 20px 0;">
  <iframe width="560" height="315" 
    src="https://www.youtube.com/embed/RhGe6vg3lM4"
    frameborder="0" 
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
    allowfullscreen style="border-radius: 12px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
  </iframe>
  <p><i>Caption: Laboratory testing and field trials of our autonomous surface vehicle.</i></p>
</div>

## 03. Field Deployments
### Galveston Channel (December 12, 2025)
Following a period of heavy rain, we successfully deployed the robot in the Galveston Channel. Despite challenging current conditions, the robot autonomously navigated a cross-channel path of approximately 800 meters, demonstrating its reliability in high-traffic, high-energy environments.
![](/movies/test_20251212.mp4)

### Shell Beach (November 06, 2025)
Our first near-shore beach test focused on path-following precision. The robot was tasked with following a complex multi-waypoint trajectory to evaluate its response to wave action and shallow-water bathymetry.

![](/images/robot_20251106_shell_beach.png)
*Figure 1: (a) Distance to next stop; (b) yaw error between robot's yaw and target yaw; (c) current yaw; (d) yaw correction based on GPS reading.*