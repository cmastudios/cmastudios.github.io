---
id: 443
title: Strange delays running zsh
date: 2014-09-21T00:04:26+00:00
author: Connor Monahan
layout: post
guid: https://cmastudios.me/?p=443
permalink: /2014/09/21/strange-delays-running-zsh/
dsq_thread_id:
  - "3042449117"
categories:
  - Uncategorized
---
As a lot of fellow users of the Z-shell, I have oh-my-zsh installed to make installing plugins and themes easier. One issue I was having earlier today was every time I typed a command or pressed return, it would delay for a couple seconds while displaying &#8216;xcodebuild&#8217; and then &#8216;git&#8217; in the title bar. This was very frustrating, as it made quick work more difficult.

After a while, I thought manually updating the repository would be helpful. I went into ~/.oh-my-zsh and ran \`git pull\`. I then received a message saying similar to You must run as root to agree to the license. It hit me that I did an update of the Xcode command line tools earlier in the day. I ran \`sudo xcodebuild\` and followed the prompts to accept the license. This caused the delays to vanish. Thought I would share if anyone else had a similar problem.