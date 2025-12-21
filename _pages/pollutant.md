---
title: "Transport of Coastal Pollutants and Larvae"
layout: single
permalink: /research/pollutant/
author_profile: false
toc: true
---

## Overview
The release of coastal pollutants—including excessive nutrients, microplastics, petrochemical compounds, and heavy metals like mercury—poses significant threats to water quality and marine ecosystems. The transport and ultimate fate of these substances are primarily governed by fundamental physical dynamics (currents, waves, and turbulence) and specific biogeochemical properties (degradation, buoyancy, and settling).

To simulate these processes, we treat pollutants as discrete particles and model their trajectories by coupling a Lagrangian particle-tracking framework with a high-resolution hydrodynamic driver. Our team is actively developing **ptrack-schism**, an open-source particle-tracking model designed for diverse applications, ranging from pollutant dispersion to the movement of harmful algal blooms (HABs) and fish larvae.

The source code is publicly available here: [https://github.com/JiabiDu/ptrack_schism](https://github.com/JiabiDu/ptrack_schism).



![harvey_pollutant](/images/particle_tracking_harvey.gif)
*Figure 1: Simulation of particle transport during Hurricane Harvey, showing the rapid export of coastal materials to the shelf.*

## Study 01: Microplastic Transport and Accumulation
Microplastics are an emerging environmental threat. Unlike dissolved pollutants, their transport is influenced by particle size, shape, and density, which determine their vertical position in the water column. Our research focuses on identifying accumulation "hotspots" in Galveston Bay and understanding how extreme weather events, such as flooding, flush accumulated plastics from estuaries into the open ocean.

## Study 02: Oyster Larvae Connectivity
The sustainability of oyster reefs depends on the successful transport of larvae from spawning sites to suitable settlement habitats. We use our particle-tracking model to simulate the "biological connectivity" between reefs. By incorporating larval behavior (such as vertical migration) and local circulation patterns, we help resource managers identify critical reefs that act as primary sources of larvae for the rest of the bay system.
