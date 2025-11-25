### **Incident Handler's Journal**

---

#### **Date: October 26, 2025 | Entry: \#1**

**Description:** Analysis of the recent AWS US-EAST-1 Disruption **Tool(s) used:** AWS Health Dashboard, Dig (DNS lookup tool), Twitter (X) for real-time user reports.

**The 5 W's**

* **Who caused the incident?** AWS Internal Systems (Automated process failure).  
* **What happened?** A cascading failure in the `us-east-1` region that took down major services (EC2, Lambda) and external apps like Snapchat. It was caused by a "race condition" in the DynamoDB DNS management system.  
* **When did the incident occur?** October 20, 2025 (Just prior to starting this module).  
* **Where did the incident happen?** US-EAST-1 Region (Northern Virginia), with global ripple effects.  
* **Why did the incident happen?** A race condition occurred where a slower worker process overwrote a newer configuration with an older one. The cleanup automation then deleted valid DNS records, making the database invisible to the network.

**Additional notes:** This was a great example of how "Region Isolation" isn't always perfect. Even if you have backups in `us-west-2`, if the control plane for DNS fails, the impact can still be felt globally.

---

#### **Date: October 31, 2025 | Entry: \#2**

**Description:** Case Study: The "Great Global Outage" (CrowdStrike) **Tool(s) used:** Virtual Machine (for safe mode simulation), Researching Incident Reports.

**The 5 W's**

* **Who caused the incident?** CrowdStrike (Cybersecurity Vendor).  
* **What happened?** A faulty configuration update (Channel File 291\) caused a logic error in the sensor software, leading to a boot loop (BSOD) on 8.5 million Windows devices.  
* **When did the incident occur?** July 19, 2024 (Historical Analysis).  
* **Where did the incident happen?** Global impact on critical infrastructure (airlines, 911, healthcare).  
* **Why did the incident happen?** A failure in the Quality Control (QC) process. The file wasn't properly validated before being pushed to the "Kernel" level of the OS. Because it ran in the Kernel (Ring 0), the crash took down the whole system, not just the app.

**Additional notes:** I learned about the difference between User Mode and Kernel Mode today. This incident proves why security vendors ideally shouldn't have deep kernel access if it can be avoided.

---

#### **Date: November 8, 2025 | Entry: \#3**

**Description:** Case Study: XZ Utils Supply Chain Attack **Tool(s) used:** GitHub History Viewer, Valgrind (conceptually).

**The 5 W's**

* **Who caused the incident?** "Jia Tan" (A likely state-sponsored actor infiltrating open source).  
* **What happened?** Malicious code was inserted into `xz-utils`, a compression tool used by Linux. It modified the SSH daemon to create a "master key" backdoor for attackers to log into Linux servers.  
* **When did the incident occur?** March 2024 (Historical Analysis).  
* **Where did the incident happen?** The open-source GitHub repository for XZ Utils.  
* **Why did the incident happen?** **Social Engineering.** The attacker spent years building trust with the overworked maintainer to gain write access. They then hid the backdoor in complex build files that didn't look like normal code.

**Additional notes:** This is terrifying because it wasn't a "hack" in the traditional sense; it was a "long con" human manipulation. It shows that we need to verify the *people* behind the code, not just the code itself.

---

#### **Date: November 15, 2025 | Entry: \#4**

**Description:** Case Study: Snowflake Identity Attacks (UNC5537) **Tool(s) used:** HaveIBeenPwned (to check for leaked creds), MFA configuration tools.

**The 5 W's**

* **Who caused the incident?** A financially motivated group tracked as UNC5537.  
* **What happened?** Massive data theft from companies like Ticketmaster and Santander. Attackers used valid credentials (username/password) stolen from malware logs to log into Snowflake cloud instances.  
* **When did the incident occur?** May–June 2024 (Historical Analysis).  
* **Where did the incident happen?** Cloud customer accounts hosted on Snowflake.  
* **Why did the incident happen?** **Lack of MFA.** The victims did not have Multi-Factor Authentication enabled on their admin or service accounts. The attackers simply "logged in" rather than "breaking in."

**Additional notes:** Key takeaway: The Cloud Provider secures the *cloud* (infrastructure), but the Customer must secure *what is in the cloud* (identity). MFA is non-negotiable.

---

#### **Date: November 19, 2025 | Entry: \#5**

**Description:** Breaking News: Cloudflare Global Control Plane Outage **Tool(s) used:** Downdetector, Cloudflare Status Page.

**The 5 W's**

* **Who caused the incident?** Internal Cloudflare Engineering (Operational Error).  
* **What happened?** A massive outage (HTTP 5xx errors) affecting analytics and bot management. A configuration file ballooned in size, causing the proxy software to crash when it tried to load it.  
* **When did the incident occur?** November 18, 2025 (Yesterday).  
* **Where did the incident happen?** Global impact triggered by a database update.  
* **Why did the incident happen?** A database query returned duplicate rows, causing a config file to exceed a hard-coded limit (200 features). The software didn't have enough pre-allocated memory to handle the larger file and crashed.

**Additional notes:** This happened while I was studying\! It emphasizes the danger of "magic numbers" (hard limits) in code and why input validation is needed even for internal configuration files.

---

#### **Date: November 22, 2025 | Entry: \#6**

**Description:** Analysis of "Banana Squad" Malicious Repos **Tool(s) used:** Python Sandbox, VirusTotal.

**The 5 W's**

* **Who caused the incident?** "Banana Squad" / "Water Curse" threat actors.  
* **What happened?** Fake GitHub repositories (posing as Discord tools or game cheats) are spreading malware.  
* **When did the incident occur?** Ongoing (Investigated this week).  
* **Where did the incident happen?** GitHub Public Repositories.  
* **Why did the incident happen?** Attackers used "Star Jacking" (fake stars) to make repos look legitimate. They hid payloads in Visual Studio `PreBuild` events so code runs as soon as a developer opens the project, before they even click "Run."

**Additional notes:** I need to be careful when cloning repos for my own projects. Always check the commit history and user activity, not just the star count.

