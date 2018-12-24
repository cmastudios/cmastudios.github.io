---
id: 329
title: Debugging plugins on a live Bukkit server
date: 2013-11-17T22:55:32+00:00
author: Connor Monahan
layout: post
guid: http://cmastudios.me/?p=329
permalink: /2013/11/17/debugging-plugins-on-a-live-bukkit-server/
---
>&lt;tommytony&gt; java -Xms2048M -Xmx2048M -Xdebug -Xrunjdwp:transport=dt_socket,address=8787,server=y,suspend=y -jar craftbukkit-1.6.4-R2.0.jar   
>&lt;tommytony&gt; then create a new Debug Configuration in eclipse   
>&lt;tommytony&gt; choose Remote Java Application   
>&lt;tommytony&gt; set port 8787   
>&lt;tommytony&gt; run that debug profile from eclipse   
>&lt;tommytony&gt; your server should start   
>&lt;tommytony&gt; and you can breakpoint   
