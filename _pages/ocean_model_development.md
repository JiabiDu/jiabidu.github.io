---
title: "Ocean Model Development"
layout: single
permalink: /research/ocean_model_development/
author_profile: false
toc: true
---

## Overview
Our lab develops and applies diverse oceanographic models across multiple scales, specializing in:
* **Regional Coastal Modeling** based on the SCHISM framework.
* **Large-scale Regional Modeling** utilizing MOM6.
* **Lagrangian Particle Tracking** coupled with high-resolution hydrodynamic drivers.

## 01: Regional Coastal Ocean Model
We have been actively developing this regional model since 2017. Built on [SCHISM](https://ccrm.vims.edu/schismweb/), the model employs a hybrid unstructured grid (quadrangles and triangles) to precisely resolve the complex geometry and bathymetry of coastal environments. 

The system has been rigorously validated against water levels, current velocities, temperature, and salinity within bays, as well as stratification and offshore currents on the continental shelf ([Du et al. 2019](https://os.copernicus.org/articles/15/951/2019/); [Du and Park, 2024](https://www.twdb.texas.gov/publications/reports/contracted_reports/doc/2300012715.pdf); [Summers et al. 2024](https://pubs.acs.org/doi/abs/10.1021/acsestwater.3c00839); [Hua et al., 2025](https://www.sciencedirect.com/science/article/pii/S1463500325001064); [Du et al., 2026](https://link.springer.com/article/10.1007/s12237-025-01648-4)). Notably, the model was used to simulate hydrodynamic responses during Hurricane Harvey, successfully reproducing long-lasting elevated water levels, intense along-channel velocities, sharp salinity drops with slow recovery, and massive freshwater plumes on the shelf (Du and Park, 2019). 



Currently, this framework has been officially adopted by the **Texas Water Development Board (TWDB)** as their operational model, providing short-term forecasts for the entire Texas coast. These operational products are accessible at [https://midgewater.twdb.texas.gov](https://midgewater.twdb.texas.gov). 

![Study Plot](/images/highlight_study01/figure01.jpg)
*Figure 1: (a) Numerical model domain in the northern Gulf of Mexico covering 13 major coastal bays; (b) high-resolution model grid within Galveston Bay; (c) detailed grid and bathymetry at the Galveston Bay mouth. TWDB salinity monitoring stations are marked in panel (b).*

![SSS Animation](/images/run19q3_SSS2.gif)
*Animation 1: Sea surface salinity over the entire year 2018. The time series plot shows the observed and modelled salinity at a middle bay station MIDG in Galveston Bay*

## 02: Large-scale Ocean Model
Utilizing [MOM6](https://mom6.readthedocs.io/en/main/), PhD student Junwei Hua is applying this regional model to fundamental research regarding the impact of mesoscale ocean eddies on heat content and the development of marine heatwaves in shelf waters. 

![mom6](/images/mom6.png)
*Figure 2: Snapshot of modelled sea surface temperature on 1993-01-01*

## 03: Particle-tracking Model
A primary application of our hydrodynamic models is understanding the transport and dispersion of coastal materials, such as microplastics, fish larvae, and harmful algal blooms. We are actively enhancing the Lagrangian module in SCHISM by developing custom functions for behavior and fate. The source code is publicly available at [https://github.com/JiabiDu/ptrack_schism](https://github.com/JiabiDu/ptrack_schism).



Key applications include:
* **Microplastic Transport:** Modeling plastic movement in Galveston Bay ([Summers et al. 2023](https://www.sciencedirect.com/science/article/abs/pii/S0048969723043103)).
* **Connectivity & Flushing:** Calculating flushing times across 13 major coastal bays in the Northern Gulf of Mexico ([Du et al. 2026](https://link.springer.com/article/10.1007/s12237-025-01648-4)).

![ptrack](/images/ptrack_galveston_d31.gif)
*Animation 2: movement of particles released in Galveston Bay*