# 🔍 Case File: Operation Beetcoin Network 🔍

**FROM:** Special Agent Dwight K. Schrute III  

**TITLE:** Assistant Regional Manager / Volunteer Deputy Sheriff

**TO:** Assistant to the Special Agent (YOU)  

**RE:** URGENT - Criminal Network Investigation  

**CONFIDENTIAL**

![Special Agent Dwight K. Schrute](img/dw.jpg)

---

**Listen up, Assistant.**

I have uncovered a sophisticated criminal network operating right under our noses. This is not a drill. I'm talking about organized financial crime, money laundering, the whole nine yards. Do I know who's behind it? Not yet. Do I have all the answers? No. But that's where YOU come in.

I've obtained critical evidence – a folder containing transaction records and member information. The folder will be in your possession soon. I haven't had time to analyze it myself because I'm busy with approximately 47 other cases, plus my duties at the beet farm. Your job is to open those files, examine them closely, and understand what format the data is in.  

Here's what I know about this criminal network: they're operating through some kind of "premium elite" financial service – the kind that only allows exactly **100 members**, with exclusive IDs ranging from **0 to 99**. Very fancy. Very exclusive. Very illegal.

This is basic detective work, people.

---

## 🎯 THE EVIDENCE

The evidence folder contains everything you need. I guarantee it. Do I need to hold your hand and tell you the exact file names? No. You're a detective now. You'll find transaction records and member information.
Everything is there. All you have to do is open your eyes and look. If I can find evidence while simultaneously managing a beet farm, you can find a few files.

---

## 🔐 PHASE ONE: FIND THE COLLECTOR

Pay attention, Assistant. I've already done some preliminary work on this case. Through my extensive network of informants and superior detective skills, I've identified one of the associates – a "collector." I'm talking about the person who's receiving money from multiple sources to consolidate funds. But I can't just tell you the collector's name directly. This is classified information. If this memo falls into the wrong hands, the entire operation could be compromised.  

I've hidden the collector's name deep inside a **classified file** within your evidence folder. It's not labeled obviously. It's buried. Hidden in plain sight. Only those with a true Schrute-level eye for detail will find it. Trust no one. Treat this file as if it were radioactive.  

The collector is one of the associates – a member of the gang. But they're special. They're our way in. They're the crack in the operation that's going to bring the whole thing down.

---

## 🎯 PHASE TWO: IDENTIFY THE BOSS

Now here's where the real work begins. Collectors don't keep the money – they're middle management at best. They funnel it upward to someone more important. I need you to go through the transactions and find out where the collector is sending THEIR money. 

Specifically, find which person received the largest **total** amount of money from the collector. And when I say **total**, I mean add up ALL the money the collector sent to each person across all transactions. The person who received the most money in total from the collector? That's the boss. Simple math, Assistant. Probably.

---

## 🎯 PHASE THREE: MAP THE NETWORK

Once you've identified the boss, map out the entire criminal network. Who else is sending money to this boss? Every single one of those accounts is an associate – a member of this criminal organization. Your job is to identify ALL of them. Every. Single. One. No excuses.  

Be aware: the database contains countless other transactions. Ordinary rich criminals paying bills, buying beets, living their boring criminal lives. None of them would ever send money to THIS boss - only the associates would. The pattern is clear to those with Schrute-level perception. All transactions in these records are part of confirmed criminal activity, however, we are focusing only on one specific group connected to our active lead.

**CRITICAL DETAIL:** The boss, the collector, and all the associates are part of these 100 members. Anyone who sends money to the boss is in the gang. The rest of the members of this premium elite club are just ordinary criminals - not interested in those for now...

---

## 🎯 PHASE FOUR: GET THE NAMES

But here's the problem: user IDs are just numbers. Numbers don't help me make arrests. I need **names**. The evidence folder contains identity information that links these user IDs to real identities. Once you figure out how this information is organized, look up the **real names** of all these criminals. Then we'll know exactly who we're dealing with.  

---

## 🎯 PHASE FIVE: CALCULATE THE BALANCES

When you're done identifying the network, I need to know how much money each criminal has left in their pocket. A person's balance is simple accounting: take all the money they've received from ANY transaction in the entire database, and subtract all the money they've sent in ANY transaction in the database. What's left is their balance.

Let me be crystal clear: when calculating balances, you count EVERY transaction in the database where that person is involved – whether they're sending or receiving, whether it's to another gang associate or to some random other criminal buying office supplies. All of it counts. 

**Can balances be negative?** Of course they can. If someone spent more than they received, their balance is negative. They're in the red.

---

## 📋 FINAL REPORT FORMAT

When you're done, I need a **final report** that lists every member of this gang – the boss, the collector, and all the other associates. The report must include each criminal's **ID, real name, and balance**. 

**The rows must appear in ascending order of ID.** Lowest ID first, highest ID last. This is non-negotiable. Bureaucrats love sorted lists, and I am many things, but I am not a monster who submits unsorted data. Is this hard to accomplish? Not if you think hard enough! You might be able to mark each member as a person of interest or not.

The report must include ONLY the boss and the associates (which includes the collector, since they're also an associate). Don't clutter my report with other criminals. I don't care about them. They're not under investigation - for now...

---

## ⚠️ CRITICAL: EVIDENCE HANDLING PROTOCOLS ⚠️

**ATTENTION ASSISTANT:** This is a federal investigation. Any evidence you collect must hold up in court. That means your investigation methods must be **BASIC and TRANSPARENT**.

I've seen too many cases thrown out because some rookie used fancy techniques that the jury couldn't understand. Judges don't like it. Defense attorneys will tear it apart. We need methods that a jury of regular citizens can follow.

**YOU ARE RESTRICTED TO BASIC INVESTIGATION TECHNIQUES ONLY:**

- ✓ Lists (basic record keeping)  
- ✓ Loops (going through records one by one)  
- ✓ Strings (for parsing/extracting data)  
- ✓ Basic file operations (opening evidence files)

**DO NOT USE ADVANCED TECHNIQUES:**  
- ✗ Dictionaries (defense will claim data manipulation)  
- ✗ Regular expressions (jury won't understand pattern matching)  
- ✗ List comprehensions (too compact, lacks transparency)  
- ✗ Map functions (not standard procedure)  
- ✗ Exception handling (we don't anticipate errors in clean evidence)  
- ✗ Pandas, CSV, NumPy, or any other data-processing libraries (too powerful, screams "tampering" to the jury)  

Keep it simple. Keep it clear. Keep it admissible.  

If you use unauthorized techniques, the entire case gets thrown out and these criminals walk free. **Don't be the reason we lose this case, Assistant.**

---

## 📝 YOUR DELIVERABLES

For your final report – and I expect this to be thorough – you will write your investigation code in a file called **investigate.py**.  

Your code must generate an evidence file with your findings: **analysis.txt**

### Required Output Format for analysis.txt:

```
id	name	balance
0	Jane Smith	15000
5	John Doe	-2000
12	Michael Scott	50000
...
```

**CRITICAL FORMATTING REQUIREMENTS:**
- Line 1: Header row with the text `id	name	balance` (using TAB characters between columns)
- Remaining lines: One row per criminal, sorted by ID in ascending order
- Use a **tab character (`\t`)** to separate columns – not spaces, not commas, TABS
- Include all identified criminals: the boss, the collector, and all other associates
- If your formatting is off by even one space, I'll know. And I'll be disappointed.

---

## ⚡ YOUR ASSIGNMENT - NON-NEGOTIABLE ⚡

You will solve this case by analyzing the data, identifying the criminal network, and generating the final report. Failure is not an option.

**Deliverables (due immediately):**  
1. Create the file `investigate.py` containing your investigation code  
2. Your code must generate `analysis.txt` with the **exact** format shown above  

Use it wisely. Study it. Learn from it. Then replicate it with the actual criminal data.

---

## 📊 CASE EVALUATION CRITERIA 📊

**Your performance will be measured in Schrute Bucks.**  
These are the official currency of merit in this task force.

Either you solve the case or you fail.  
No gray area. No "partial credit."  
You earn **100 Schrute Bucks** for success or **zero** for failure.  
Think of it as a pass/fail system – because in law enforcement, "almost catching" a criminal means you didn't.

**Total Possible: 100 Schrute Bucks**

---

Do not disappoint me, Assistant.

**Dwight K. Schrute III**  
Special Agent / Assistant Regional Manager  
Volunteer Sheriff Deputy  
Scranton Crime Task Force  

P.S. Schrute Bucks are redeemable for one extra five-minute break or one beet from my farm per 100 earned. Use them wisely.

---

## ⚠️ WHERE ARE THE CASE FILES? ⚠️

I can’t just hand over classified data to anyone with a keyboard and Wi-Fi. This is top-level material. You want access? You’ll follow protocol.

You must create a new file called **ACCESS_REQUEST.txt**.
Inside it, write your Cougarnet ID. That’s it - no names, no emails, no jokes, no emojis.
Save it, commit it, and push it to your repo.

Only then will I consider authorizing your data access.
Once authorized, **YOU CANNOT MAKE ANY CHANGES TO THIS FILE OR MOVE/DELETE IT**.
No file, no data. That’s how the Schrute Bureau of Investigation operates.

---
