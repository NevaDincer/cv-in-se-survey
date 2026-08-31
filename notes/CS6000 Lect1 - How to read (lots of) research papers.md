 [video](http://youtube.com/watch?v=3hnFxCEkcME)**

---

## Why Read

Reading trains you to think critically about research quality  because ==eventually someone will think critically about yours.== You need to understand how people tell their story and what makes work good.

Two goals that persist even after you've learned critical reading:

- Gain perspective and knowledge about other problems
- Keep up with the state of the art (==“research is advancing the state of the art== —> if you don't know the state of the art, you can't do good research")

As you read more, you get better at identifying which questions are worth asking and which are worth answering.

---

## Research Papers

Primary form of disseminating results in CS.

**Conference papers** — shorter (4–8 pages), most up to date.

**Journal papers** — longer (10–20 pages), often the complete version of a conference paper, sometimes a combination of multiple ones. May come out several years after the conference. Useful for getting a broader picture when entering a field.

Peer review is the cornerstone — it's what determines quality and impact. Look for venues with strong peer review.

---

## Five Pass Method

Based on Keshav's work, with variations. 
We use the first four.

==**Pass 1: Browse**
**Pass 2: Skim** (browse + skim together = scan) 
**Pass 3: Critical Read**
**Pass 4: Creative Read**
**Pass 5: In-depth** (unbounded — for when you're actually implementing)

---

## Why Not Just Search

Keyword search only finds what you already know to look for. You won't find things you don't have the vocabulary for yet, and you won't stumble onto things you didn't know you needed. ==You have to browse to keep up.==

Volume reality: big conferences have 200–700 papers, top journals publish ~400/year. At 10 papers/week that's 30 weeks just for one conference. You need to browse fast and browse a lot.

*Keep a reading list — Google Scholar or similar.* Add to it frequently.

---

## Pass 1: Browse

**Goal:** be efficient and stay aware.

**How:**

- Read abstract, scan figures and captions
- 1–2 minute gut check
- If you can't tell it's good or relevant after that, move on

**Also useful:** check who cited it and who wrote it. Papers by people or citing work you already know are more likely to be relevant.

**Key habit:** err on the positive side — if you're unsure, add it to the reading list rather than risk missing something. Do not get sucked into reading further. Practice timing yourself. At 2 min/paper you can do 30 papers in an hour.

---

## Pass 2: Skim

Do this after you've built a reading list from browsing — not immediately after.

**Rule:** believe everything, assume it's all true. Given that, is the paper actually interesting?

Many papers fail here — you believe everything and still say "who cares."

Read through each section quickly. Then try to summarize in 2–3 sentences:

- What problem does it address?
- What is new about the solution?
- How significant was the experiment/theory?

If you can't do it in 2–3 sentences → you skimmed too lightly. If you have too many ideas → you went too deep. Target: 5–10 minutes.

**After the scan, answer the Six Cs:**

1. **Category** — what type of paper is it?
2. **Context** — what other papers is it related to? How does it relate to your work?
3. **Contributions** — what are the main contributions?
4. **Credible** — does it appear to have any credibility?
5. **Care** — given it's valid, will anyone care? Will it change anything?
6. **Cost** — how much time and effort will it take to read carefully?

Then decide: does it go on the "read more" list or the "done" list?

---

## Pass 3: Critical Read

About an hour. Read carefully but ignore fine details — don't check proofs line by line. Focus on assumptions and methodology.

**Core questions to ask:**

**On the problem:**

- Is the problem clearly and formally stated, or just vaguely described?
- Is it a meaningful, realistic problem — if it were solved, would it matter?
- Is it the _right_ problem, or has the formalization simplified reality too much ("assume a spherical chicken")?
- What are the explicit and implicit assumptions about the problem itself?
- Are there simple existing solutions the authors seem unaware of?

**On the technique:**

- What are the implicit assumptions? Check edge cases: divide by zero? Singular matrices? Does a minimum actually exist?
- Is the logic of the paper sound given its assumptions?
- Has the right theorem been proven — is it actually applicable here?

**On the experiments:**

- Was the right data collected to support the claims?
- Was training and test data kept separate? Were hyperparameters tuned on test data? (Both are big no-nos.)
- Did they compare against the actual current state of the art, or something outdated?
- Do the numbers in different parts of the paper actually add up?
- Are generalizations valid — did they test on a narrow population but claim broadly?
- Are claims modest enough to match the evidence?

**On reproducibility:**

- Could you implement this from what's given? Missing parameters or data = lower value.
- Are there confounding factors or prohibitively expensive experimental setups?

**Credibility checks:**

- Watch for sweeping generalizations, biased language, or dismissive phrases ("laughably inept" etc.) - these signal unscientific thinking.
- Check what they cite and whether those citations are used correctly.

**At the end you should be able to answer:** on what dimension(s) did this paper advance the state of the art?

Highlight things that bother you as you go - don't get bogged down mid-read. Come back to them. Your first gut instinct is usually right, it just takes time to pin down why.

---

## Pass 4: Creative Read

Also about an hour. Only do this after the critical read passes — no point building on a shaky foundation.

Harder than critical reading. Tearing down is easier than building up.

**Questions to ask:**

- What is the novelty, and what new directions does it open up that didn't exist before?
- Are there good ideas in the paper beyond what the authors claim as the contribution — techniques that could apply elsewhere?
- Could these ideas combine with your own work?
- What if different assumptions were made — could you do better?
- Are there better numerical methods than what they used?
- What would be the next thing you'd do if you were going to extend this paper?

**Key habit:** actually write this down. Spend a few minutes staring at a blank page asking "what could I do with this that I couldn't do before?" It's not quick. It might result in nothing. It might result in a lot.

---

## Pass 5: In-depth

Unbounded — could be a week. For papers you're actually going to implement or build on directly. Not covered in detail in this course except for one paper.

If going this deep: look for a thesis version, check if code is on GitHub, consider reaching out to the authors.