**Incident report analysis**

**Instructions**

As you continue through this course, you may use this template to record your findings after completing an activity or to take notes on what you've learned about a specific tool or concept. You can also use this chart as a way to practice applying the NIST framework to different situations you encounter.

| Summary | During the development phase of my Student E-commerce Platform, a critical security misconfiguration was identified involving the backend database credentials. An API key with administrative access to the Supabase instance was hardcoded into the application source code and pushed to a public GitHub repository. The exposure was detected by an external secret scanning tool (GitGuardian). This vulnerability potentially allowed unauthorized actors to read, modify, or delete student and product data stored in the database. The incident was contained by revoking the compromised key and refactoring the code to use environment variables. |  |  |
| :---- | :---- | ----- | ----- |
| Identify | **Assets Affected:** The Supabase database (containing user PII and transaction data) and the GitHub repository. **Risk:** Unrestricted access to the backend database. Anyone with the key could bypass authentication. **Audit Findings:** A code review confirmed that the API key was stored in cleartext within a configuration file that was not excluded by `.gitignore`. |  |  |
| Protect | **Secret Management:** The codebase was refactored to remove hardcoded credentials. We implemented a `.env` file to store sensitive keys locally. **Access Control:** The `.env` file was immediately added to `.gitignore` to ensure it is never committed to the remote repository. **Key Rotation:** The exposed API key was permanently revoked in the Supabase dashboard and replaced with a new, secure key. |  |  |
| Detect | **Tools Used:** The incident was detected via an alert from **GitGuardian**, an automated secret scanning tool. **Future Detection:** To improve detection speed and prevent recurrence, I have installed a **pre-commit hook** (using tools like `gitleaks` or `husky`) that scans the code for potential secrets *before* a commit can be finalized. |  |  |
| Respond | **Containment:** Upon receiving the alert, the repository history was scrubbed (using `git filter-repo`), and the compromised key was revoked within 15 minutes. **Investigation:** I audited the Supabase authentication logs for the duration the key was exposed to verify if any unauthorized IP addresses accessed the database. (No suspicious activity was found). |  |  |
| Recover | **Restoration:** The application was redeployed with the new secure API keys injected via the hosting platform’s environment variable settings. **Validation:** Verified that the application could connect to the database using the new secure method and that the public GitHub repository no longer contained traces of the key in the commit history. |  |  |

---

| Reflections/Notes:  This incident highlighted the importance of "Shifting Left" in security—handling security earlier in the development lifecycle. Secret Management: I learned that even for student projects, `.env` files are mandatory. Hardcoding is never an option. Automated Safety Nets: Relying on manual checks isn't enough. Automated tools like GitGuardian are essential "safety nets" for developers. Portfolio Value: This incident demonstrates my ability to manage Cloud Security and Application Security (AppSec), specifically regarding API protection and secret management. |
| :---- |

