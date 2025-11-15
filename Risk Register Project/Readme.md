GRC Risk Register Project — Law Firm Simulation

Project Overview



This project simulates a full Governance, Risk, and Compliance (GRC) assessment for a fictional mid-sized law firm. The purpose is to identify, assess, and treat cybersecurity risks using industry-standard frameworks, including:



NIST SP 800-30 (Risk Assessment Guide)



NIST SP 800-53 (Security and Privacy Controls)



Qualitative Risk Scoring (Likelihood × Impact)



Best practices for governance and security documentation



The deliverables include a fully formatted Excel risk register, a risk heatmap, and supporting documentation suitable for real-world GRC work or portfolio demonstration.



Organization Profile (Simulated)



Name: Hamilton \& Cole LLP

Industry: Legal Services

Employees: ~120

Environment: Microsoft 365, internal document management, HR database, laptops, VPN

Security Drivers:



ABA Cybersecurity Rules



State \& Federal Privacy Laws



GDPR (International Clients)



&nbsp;1. Asset Inventory



A complete inventory was created to classify critical assets based on confidentiality, integrity, and availability (CIA).

Key assets include:



Client case files



Billing system



Document Management System (DMS)



HR employee records



Email system (Microsoft 365)



Attorney laptops



VPN remote access



See Excel → Sheet 1: Asset Inventory



&nbsp;2. Risk Identification



Risks were identified by mapping assets to threats and vulnerabilities such as:



Risk ID	Asset			Threat			Vulnerability

R1	Client Case Files	Ransomware		No offline backups

R2	Email System		Phishing		No MFA, weak training

R3	Attorney Laptops	Device Theft		No disk encryption

R4	DMS			Insider Threat		Excessive privileges

R5	VPN			Brute-force Attack	Weak password policy

R6	HR Records		Data Breach		Misconfigured permissions

R7	Billing System		Downtime		No redundancy



See Excel → Sheet 2: Risk Identification



3\. Risk Assessment (Likelihood × Impact)



Risks were assessed using a 1–5 qualitative scale:



Likelihood: 1 (Rare) → 5 (Almost Certain)



Impact: 1 (Low) → 5 (Severe)



Risk Score = Likelihood × Impact



Conditional formatting automatically classifies risk:



Critical



High



Medium



Low



See Excel → Sheet 3: Risk Assessment



4\. Risk Treatment Plan



Each risk was assigned a mitigation strategy mapped to NIST 800-53 controls, including:



AT-2: Security Awareness \& Phishing Training



IA-2 / IA-5: MFA \& Strong Authentication



MP-5: Device Encryption



CP-9 / CP-10: Backups \& Disaster Recovery



AC-2 / AC-6: Access Management \& Least Privilege



SI-3: Malware \& Endpoint Detection



Each risk includes:

✔ Mitigation strategy

✔ Control type

✔ NIST mapping

✔ Risk owner

✔ Status (Planned, In Progress, Complete)



See Excel → Sheet 4: Risk Treatment



5\. Executive Summary



The assessment identified three primary risks:



Ransomware targeting client case files (Critical)



Phishing attacks via email (High)



Device theft causing potential client data exposure (High)



Recommended actions:



Enforce MFA firm-wide



Deploy EDR and encryption



Establish offline backup strategy



Conduct quarterly access reviews



Strengthen password \& VPN security



Improve system redundancy



See Excel → Sheet 5: Executive Summary



📈 6. Risk Heatmap



A visual risk heatmap was generated using Python (matplotlib) to plot Likelihood × Impact values.



Example snippet:



plt.imshow(matrix, cmap="YlOrRd", origin="lower")

plt.scatter(impact-1, likelihood-1)





The heatmap helps prioritize risks during governance and leadership meetings.



See file → Risk\_Heatmap.png



Project Deliverables



This project includes:



File	Description

Risk\_Register\_LawFirm\_Professional.xlsx	Complete risk register with formulas, dropdowns, formatting

Risk\_Heatmap.png	Visual risk map of all threats

README.md	Full project documentation

Skills Demonstrated



Risk assessment (qualitative scoring)



GRC documentation \& reporting



NIST SP 800-30 \& NIST SP 800-53 frameworks



Control mapping \& governance planning



Excel automation (validation, formulas, conditional formatting)



Python visualization (heatmaps)



Security analysis \& prioritization



About This Project



This project was created as part of a personal GRC and cybersecurity portfolio to demonstrate hands-on experience in:



Governance



Risk Management



Compliance



Security program development



If you'd like to review or collaborate on additional GRC or cybersecurity projects, feel free to connect!

