---
id: 296
title: Progress bar code I found
date: 2013-10-23T19:56:48+00:00
author: Connor Monahan
layout: post
guid: http://cmastudios.me/?p=296
permalink: /2013/10/23/progress-bar-code-i-found/
---
```java
public String generateProgressBar() {
  int total = getSizeX() * getSizeY() * getSizeZ(); // Area
  double percentage = this.visitedBlocks / total;
  StringBuilder progBar = new StringBuilder();
  progBar.append(Math.round(percentage * 100)).append("% ["); // 0.1 becomes 10
  int bars = (int) percentage * 10; // 0.1 becomes 1
  for (int bar = 1; bar &lt;= 10; bar++) {
    if (bars &gt;= bar) {
      progBar.append('#');
    } else {
      progBar.append('_');
    }
  }
  progBar.append(']');
  return progBar.toString();
}
```
