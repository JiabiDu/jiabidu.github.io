---
title: "Research"
layout: single
permalink: /research/
author_profile: false
sidebar:
  nav: "toc"
toc: true
toc_label: "Research Projects"
toc_icon: "flask"
toc_sticky: true
---

## Coastal and estuarine dynamics
The physical dynamics is the fundamental process for sediment transport, pollutant dispersion, and ecosystem. Coastal and estuarine dynamics involve a variety of processes as the coastal ocean is impacted by tides, freshwater input, and atmospheric forcings. Because of notable freshwater input, coastal and estuarine waters are typically characterized by a strong salinity gradient that drives bottom water to move from high salinity to low salinity. 
![coastal dynamics](/images/CoastalDynamics.jpeg)
(Figure source: Danial Khojasteh et al. 2021)

In this lab, we tried to understand how the coastal and estuarine processes respond to different forcings, changing climates, sea-level rise, and extreme weather events.

## Interaction between deep, shelf, and coastal oceans 
Because of different densities, different parts of the ocean are dynamically separated. However, cross-exchange between shelf and deep ocean and between estuaries and shelf ocean occurs all the time and could be strongly intensified under certain conditions. For instance, upwelling could happen in the western Gulf of Mexico during summer when the wind blows to the upcoast (from Mexico to the Texas coast). When Loop Current Eddies (shed from Loop Current, part of Gulf Stream) pinches onto the shelf break, it will shed out warm water and impact the baroclinic stability at the shelf break, leading to acute cross-shelf exchange. Moving to the inner shelf, the cross-shelf exchange is even more dynamic because of the velocity shear between the inner and outer shelf current. 

How does a warming climate impact the cross-shelf exchange?

How does such change impact the coastal materials, such as nutrients, pollutants, and sediments? 

## Coastal pollutant dispersion
The release of coastal pollutants such as excessive nutrients, microplastic, petrochemical compounds, and mercury affects the water quality and ecosystem. Their transport and fate are largely controlled by fundamental physical dynamics and biogeochemical properties. Pollutants are typically treated as particles and their transports is simulated by coupling a particle tracking model with a hydrodynamics model. Our team is actively developing the particle tracking model (available at https://github.com/JiabiDu/ptrack_schism), which can be used for not only pollutants but also harmful algal bloom and fish larvae. 
![harvey_pollutant](/images/particle_tracking_harvey.gif)


## Coastal flooding 
Flooding is a major concern for coastal communities. Flooding risk is elevated with sea level rise and more intense precipitation events. Flooding can be induced by multiple processes, including tide, storm surge, freshwater runoff, and precipitation. We refer the flooding induced by multiple processes as compound flooding. Simulating compound flooding in a numerical model faces a number of challenges including 1) computational efficiency when adding a lot of grid cell on low-lying land; 2) blockage of small river/creek channels with traditional mesh that use a constant resolution on the land; 3) the interaction between tide and river runoff; and 4) the baroclinic impact from deep ocean dynamics.  
![flooding](/images/flooding.jpg)
(Figure source: Huang et al. 2024)

## Biogeochemical processes and water quality
Biogeochemical modeling for coastal waters involves the use of mathematical and computational tools to simulate the interactions between biological, chemical, and physical processes in coastal ecosystems. These models help scientists understand and predict how nutrients, organic matter, and pollutants cycle through coastal environments, which can include estuaries, lagoons, and coastal shelves.
![bgc](/images/biogeochemical.jpg)

The primary components of biogeochemical models include:
* **Biological Processes**: These include the growth and decay of phytoplankton, zooplankton, and other organisms, as well as their interactions with each other and their environments.
* **Chemical Processes**: This covers the transformation and movement of nutrients (like nitrogen and phosphorus), oxygen, and other chemical substances within the water and sediments.
* **Physical Processes**: This involves the movement of water (e.g., currents, tides) and its effects on the distribution and mixing of biological and chemical components.
By integrating these processes, biogeochemical models can provide insights into phenomena such as algal blooms, oxygen depletion, and the impacts of human activities (like agriculture and pollution) on coastal health. They are valuable tools for managing coastal resources, predicting environmental changes, and supporting sustainable development in these critical areas. 
